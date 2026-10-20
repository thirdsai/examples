"""Small client for the documented thirds.ai render API (https://thirds.ai/v1/openapi.json).

Only https://thirds.ai is contacted. The API key is sent in the Authorization header
and never appears in error messages.
"""

import hashlib
import json
import time
from typing import Any
from urllib.parse import urljoin

import httpx

API_BASE = "https://thirds.ai"
MAX_HTML_BYTES = 5 * 1024 * 1024  # the API limit for the html field
REQUEST_TIMEOUT = httpx.Timeout(60.0, connect=10.0)
OVERALL_DEADLINE_SECONDS = 100  # stop polling an unfinished job after this; below MAX_REQUEST_TIMEOUT=120 set in main.py
POLL_INTERVAL_SECONDS = 1.5


class ThirdsError(Exception):
    """An error with a message that is safe to show to the Dify user."""


USER_AGENT = {"User-Agent": "thirds-dify-plugin/0.0.1"}


class _BearerAuth(httpx.Auth):
    """Adds the API key to thirds.ai API requests only, never to the signed download link."""

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def auth_flow(self, request: httpx.Request):
        path = request.url.path
        if request.url.host == "thirds.ai" and path.startswith("/v1/") and not path.startswith("/v1/downloads/"):
            request.headers["Authorization"] = "Bearer " + self._api_key
        yield request


def _error_from_response(res: httpx.Response) -> ThirdsError:
    try:
        error = res.json().get("error") or {}
    except ValueError:
        error = {}
    code = error.get("code") or "unknown_error"
    detail = error.get("message") or ""
    request_id = error.get("request_id")
    suffix = f" (request {request_id})" if request_id else ""
    if res.status_code == 401:
        return ThirdsError("thirds.ai rejected the API key. Check the key in the thirds.ai plugin settings.")
    if res.status_code == 402:
        return ThirdsError(f"The thirds.ai account has no credits left for this file.{suffix}")
    if res.status_code == 403:
        return ThirdsError(f"The thirds.ai account cannot make files yet: {detail or code}.{suffix}")
    if res.status_code == 409:
        return ThirdsError(f"thirds.ai reported a conflict: {detail or code}.{suffix}")
    if res.status_code == 413:
        return ThirdsError("The HTML is too large for thirds.ai. Keep it under 5 MB.")
    if res.status_code in (400, 422):
        return ThirdsError(f"thirds.ai could not accept these options: {detail or code}.{suffix}")
    if res.status_code == 429:
        return ThirdsError(f"thirds.ai is rate limiting this key. Try again shortly.{suffix}")
    return ThirdsError(f"thirds.ai answered HTTP {res.status_code} ({code}). Try again.{suffix}")


def check_api_key(api_key: str) -> None:
    """Validate a key by listing the newest PDF job. This uses no credits."""
    if not api_key or not api_key.strip():
        raise ThirdsError("Enter your thirds.ai API key.")
    try:
        res = httpx.get(
            f"{API_BASE}/v1/pdf",
            params={"limit": 1},
            headers=USER_AGENT,
            auth=_BearerAuth(api_key.strip()),
            timeout=REQUEST_TIMEOUT,
        )
    except httpx.HTTPError as e:
        raise ThirdsError(f"Could not reach thirds.ai: {type(e).__name__}.") from None
    if res.status_code != 200:
        raise _error_from_response(res)


def check_html(html: Any) -> str:
    if not isinstance(html, str) or not html.strip():
        raise ThirdsError("The html input is empty. Pass the HTML document to render.")
    if len(html.encode("utf-8")) > MAX_HTML_BYTES:
        raise ThirdsError("The HTML is too large for thirds.ai. Keep it under 5 MB.")
    return html


def idempotency_key(kind: str, body: dict[str, Any]) -> str:
    # The same request sent twice (a retry, or a workflow run again) returns the first job
    # instead of making a second file and using a second credit.
    digest = hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
    return f"dify-{kind}-{digest[:48]}"


def render(kind: str, api_key: str, body: dict[str, Any]) -> tuple[dict[str, Any], bytes]:
    """Create a PDF or image job, wait for it, and return (job, file bytes)."""
    if kind not in ("pdf", "image"):
        raise ValueError(kind)
    api_key = (api_key or "").strip()
    if not api_key:
        raise ThirdsError("The thirds.ai API key is missing. Add it in the plugin settings.")
    deadline = time.monotonic() + OVERALL_DEADLINE_SECONDS
    with httpx.Client(
        timeout=REQUEST_TIMEOUT, follow_redirects=False, headers=USER_AGENT, auth=_BearerAuth(api_key)
    ) as client:
        try:
            res = client.post(
                f"{API_BASE}/v1/{kind}",
                json=body,
                headers={"Idempotency-Key": idempotency_key(kind, body)},
            )
            if res.status_code not in (200, 201, 202):
                raise _error_from_response(res)
            job = res.json()
            while job.get("status") in ("queued", "running"):
                if time.monotonic() > deadline:
                    raise ThirdsError(
                        f"thirds.ai is still working on job {job.get('id')}. Run the tool again with the same "
                        "input to pick up the same job without using a second credit."
                    )
                time.sleep(POLL_INTERVAL_SECONDS)
                res = client.get(f"{API_BASE}/v1/{kind}/{job['id']}")
                if res.status_code != 200:
                    raise _error_from_response(res)
                job = res.json()
            if job.get("status") != "succeeded":
                error = job.get("error") or {}
                reason = error.get("message") or error.get("code") or job.get("status")
                raise ThirdsError(f"thirds.ai could not make the file (job {job.get('id')}): {reason}. No credit is used.")
            url = urljoin(API_BASE, (job.get("download") or {}).get("url") or "")
            if not url.startswith(API_BASE + "/"):
                raise ThirdsError(f"thirds.ai returned no download link for job {job.get('id')}.")
            # The signed download link carries its own short-lived token, so no API key is sent.
            file_res = client.get(url)
            if file_res.status_code != 200:
                raise ThirdsError(f"Downloading the file for job {job.get('id')} failed with HTTP {file_res.status_code}.")
        except httpx.HTTPError as e:
            raise ThirdsError(f"Could not reach thirds.ai: {type(e).__name__}. Try again.") from None
    return job, file_res.content


def file_name(value: Any, default: str, extension: str) -> str:
    name = str(value or "").strip() or default
    name = "".join(c for c in name if c not in '\\/:*?"<>|\r\n\t').strip(" .") or default
    if not name.lower().endswith(f".{extension}"):
        name = f"{name}.{extension}"
    return name[:120]
