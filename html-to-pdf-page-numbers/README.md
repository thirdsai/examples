# How to add page numbers, a header and clean page breaks to an HTML to PDF export

Files in this Gist:
* `print.css`: the print rules from step 1.
* `example-request.json`: a full request body for `POST https://thirds.ai/v1/pdf` with a long invoice style table, a header, a `1 / N` footer and a forced page break. It was run against the live API on 17 Oct 2026 and gave a 4 page A4 PDF with the header on every page, the table head repeated and no split rows.

If your invoice or report looks right in the browser but splits a table row across two pages, or comes out with no page numbers, the fix is a few lines of print CSS plus the right PDF options. This guide covers both, then shows the one API request that does it on a server with no headless browser to run.

**1. Control where pages break**

```css
h1, h2 { break-after: avoid; }          /* keep a heading with its text */
tr, .total { break-inside: avoid; }     /* never split a row or the total */
.new-page { break-before: page; }       /* force a break */
p { orphans: 3; widows: 3; }
```

`break-inside: avoid` only works if the block fits on one page, so let rows grow with their text. A fixed row height or `overflow: hidden` will hide values instead.

**2. Test the awkward cases.** Make the same document with no items, one item, many items and one very long item name. Most broken PDFs only break on one of these.

**3. Use a real table.** Put invoice lines in a `table` with `thead` and `tbody`, and compute totals in your app before you render, not in the template.

**4. Fonts.** A font that is only installed on your laptop will not load on a server. Load a licensed web font with `@font-face`, or use a generic family, and add `<meta charset="utf-8">` so currency symbols and accented names come out right.

**5. Page numbers and a header.** Headers and footers sit outside the page body, so they need their own margin and their own inline styles. With the thirds.ai API it is one request:

```json
POST https://thirds.ai/v1/pdf
{
  "html": "<!doctype html><html><head><meta charset='utf-8'></head><body>...</body></html>",
  "pdf": {
    "format": "A4",
    "margins": { "top": "20mm", "right": "12mm", "bottom": "20mm", "left": "12mm" },
    "display_header_footer": true,
    "header_template": "<span style='font-size:9px;width:100%;text-align:center'>Quarterly report</span>",
    "footer_template": "<span style='font-size:9px;width:100%;text-align:center'><span class='pageNumber'></span> / <span class='totalPages'></span></span>"
  }
}
```

Send it with `Authorization: Bearer YOUR_API_KEY` and an `Idempotency-Key` header so a retry never makes a second file. The answer has an `id` and a `status`; when it is `succeeded`, download the file from `download.url` (add `https://thirds.ai` in front; the signed link lasts 15 minutes). A CSS `@page` size does not override `pdf.format`, so keep the two in agreement.

If you are moving off wkhtmltopdf, which is archived, the thirds.ai migration guide (https://thirds.ai/docs/wkhtmltopdf?utm_source=github&utm_medium=community&utm_campaign=own-content&utm_content=html-to-pdf-wkhtmltopdf) maps its options to one request.

Try it: [HTML to PDF API with page numbers](https://thirds.ai/html-to-pdf?utm_source=github&utm_medium=community&utm_campaign=own-content&utm_content=html-to-pdf-page-numbers). A free account gets 50 PDFs a month, one credit per finished file, and a failed file costs nothing.

Drafted with AI help.

(Disclosure: I'm connected to thirds.ai.)
