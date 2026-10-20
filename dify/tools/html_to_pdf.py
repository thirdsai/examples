import re
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from utils.thirds_client import ThirdsError, check_html, file_name, render

PAGE_SIZES = {"A4", "Letter", "Legal", "A3", "A5"}
LENGTH_RE = re.compile(r"^(?:0|[1-9][0-9]*)(?:\.[0-9]{1,4})?(?:px|in|cm|mm)$")


class HtmlToPdfTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        try:
            html = check_html(tool_parameters.get("html"))
            page_size = tool_parameters.get("page_size") or "A4"
            if page_size not in PAGE_SIZES:
                raise ThirdsError(f"Page size must be one of {', '.join(sorted(PAGE_SIZES))}.")
            margin = str(tool_parameters.get("margin") or "0mm").strip()
            if not LENGTH_RE.match(margin):
                raise ThirdsError("Margin needs a number and a unit, such as 12mm, 0.5in or 20px.")
            body: dict[str, Any] = {
                "html": html,
                "pdf": {
                    "format": page_size,
                    "landscape": bool(tool_parameters.get("landscape")),
                    "margins": {"top": margin, "right": margin, "bottom": margin, "left": margin},
                },
            }
            if tool_parameters.get("run_javascript"):
                body["javascript"] = {"mode": "enabled"}
            job, pdf = render("pdf", self.runtime.credentials.get("api_key", ""), body)
        except ThirdsError as e:
            raise ValueError(str(e)) from None

        name = file_name(tool_parameters.get("file_name"), "document", "pdf")
        yield self.create_blob_message(blob=pdf, meta={"mime_type": "application/pdf", "filename": name})
        yield self.create_json_message({"job_id": job.get("id"), "file_name": name, "bytes": len(pdf)})
