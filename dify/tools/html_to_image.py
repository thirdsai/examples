from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from utils.thirds_client import ThirdsError, check_html, file_name, render

FORMATS = {"png": "image/png", "jpeg": "image/jpeg", "webp": "image/webp"}


def _size(value: Any, default: int, low: int, high: int, label: str) -> int:
    if value in (None, ""):
        return default
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ThirdsError(f"{label} must be a whole number of pixels.") from None
    if not number.is_integer() or not low <= number <= high:
        raise ThirdsError(f"{label} must be a whole number from {low} to {high}.")
    return int(number)


class HtmlToImageTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        try:
            html = check_html(tool_parameters.get("html"))
            image_format = tool_parameters.get("format") or "png"
            if image_format not in FORMATS:
                raise ThirdsError("Format must be png, jpeg or webp.")
            width = _size(tool_parameters.get("width"), 1200, 320, 7680, "Width")
            height = _size(tool_parameters.get("height"), 630, 200, 4320, "Height")
            image: dict[str, Any] = {"format": image_format, "width": width, "height": height}
            if tool_parameters.get("transparent"):
                if image_format == "jpeg":
                    raise ThirdsError("JPEG has no transparency. Choose PNG for a transparent background.")
                image["transparent"] = True
            body: dict[str, Any] = {"html": html, "image": image}
            if tool_parameters.get("run_javascript"):
                body["javascript"] = {"mode": "enabled"}
            job, data = render("image", self.runtime.credentials.get("api_key", ""), body)
        except ThirdsError as e:
            raise ValueError(str(e)) from None

        extension = "jpg" if image_format == "jpeg" else image_format
        name = file_name(tool_parameters.get("file_name"), "image", extension)
        yield self.create_blob_message(blob=data, meta={"mime_type": FORMATS[image_format], "filename": name})
        yield self.create_json_message(
            {"job_id": job.get("id"), "file_name": name, "bytes": len(data), "width": width, "height": height}
        )
