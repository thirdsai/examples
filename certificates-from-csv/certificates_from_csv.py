#!/usr/bin/env python3
"""Make one certificate PDF per row of a CSV with the thirds.ai API.

CSV columns: learner,course,date
Usage: THIRDS_API_KEY=... TEMPLATE_ID=tpl_... python3 certificates_from_csv.py learners.csv
Each finished PDF costs one credit; a failed one costs nothing.
"""
import csv, json, os, re, sys, time, urllib.request, urllib.error

API = "https://thirds.ai"
KEY = os.environ["THIRDS_API_KEY"]
TEMPLATE_ID = os.environ["TEMPLATE_ID"]
ISSUER = os.environ.get("ISSUER", "Your organisation")


def call(method, path, body=None, key=None):
    headers = {"Authorization": f"Bearer {KEY}"}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        headers["Idempotency-Key"] = key
        data = json.dumps(body).encode()
    req = urllib.request.Request(API + path, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def make_pdf(row, n):
    # Same row and same data gives the same key, so a re-run never pays twice.
    key = f"cert-{n}-{re.sub(r'[^a-z0-9]+', '-', row['learner'].lower())}"
    job = call("POST", "/v1/pdf", {
        "template_id": TEMPLATE_ID,
        "data": {"issuer": ISSUER, "learner": row["learner"],
                 "course": row["course"], "date": row["date"]},
    }, key)
    deadline = time.time() + 120
    while job["status"] in ("queued", "running"):
        if time.time() > deadline:
            raise TimeoutError(f"row {n} still {job['status']}; re-run to pick it up")
        time.sleep(2)
        job = call("GET", f"/v1/pdf/{job['id']}")
    if job["status"] != "succeeded":
        raise RuntimeError(f"row {n}: {job['status']} {job.get('error')}")
    out = f"certificates/{n:03d}-{key[len(f'cert-{n}-'):]}.pdf"
    # The signed link does not need the API key and lasts 15 minutes.
    with urllib.request.urlopen(API + job["download"]["url"], timeout=60) as r, open(out, "wb") as f:
        f.write(r.read())
    return out


if __name__ == "__main__":
    os.makedirs("certificates", exist_ok=True)
    with open(sys.argv[1], newline="", encoding="utf-8") as f:
        for n, row in enumerate(csv.DictReader(f), start=1):
            try:
                print("saved", make_pdf(row, n))
            except (urllib.error.HTTPError, RuntimeError, TimeoutError) as e:
                print("skipped row", n, e, file=sys.stderr)
