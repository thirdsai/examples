# thirds.ai examples

Working examples for making PDFs and images from HTML or from saved designs with the [thirds.ai API](https://thirds.ai/?utm_source=github&utm_medium=community&utm_campaign=own-content&utm_content=examples-readme). Each folder has the code or workflow file, a README with setup steps, and (for most) a sample of the output it produced when it was run against the live API in October 2026.

Every example needs a thirds.ai API key (`THIRDS_API_KEY`). Most also need the ID of a saved design (`TEMPLATE_ID`, starts with `tpl_`). Each finished file uses one credit, a failed one costs nothing, and a free account gets 50 credits a month. No key or template ID is stored in this repo.

## Start here: page numbers, headers and clean page breaks in HTML to PDF

[`html-to-pdf-page-numbers/`](html-to-pdf-page-numbers/)

If an invoice or report looks right in the browser but splits a table row across two pages, or has no page numbers, the fix is a few lines of print CSS plus the right PDF options. The guide covers `break-inside`, `break-before`, orphans and widows, fonts on a server, and a header plus a `1 / N` footer in one request. `example-request.json` is a full request body; `sample-output.pdf` is the 4 page A4 file it produced, with the header on every page, the table head repeated and no split rows.

## All examples

| Folder | What it does | Runs on |
|--------|--------------|---------|
| [`html-to-pdf-page-numbers/`](html-to-pdf-page-numbers/) | Print CSS and one request for page numbers, a header and clean breaks | any HTTP client |
| [`certificates-from-csv/`](certificates-from-csv/) | One certificate PDF per row of a class list, safe to re-run | Python 3, standard library |
| [`og-image-per-post/`](og-image-per-post/) | A 1200x630 Open Graph PNG for each blog post at build time, skipping existing ones | Node 20+, no dependencies |
| [`ad-sizes-from-csv/`](ad-sizes-from-csv/) | One ad design, one row per product, a ZIP of PNGs in three sizes each | Python 3, standard library |
| [`n8n/sheets-certificate-email/`](n8n/sheets-certificate-email/) | New Google Sheets row to certificate PDF to Gmail | n8n Cloud or self-hosted (HTTP Request nodes) |
| [`make/donation-receipt/`](make/donation-receipt/) | Stripe gift to branded donation receipt PDF | Make (HTTP app) |

## Notes

* Every request sends an `Idempotency-Key`, so a retry or a re-run never makes or charges for a second file.
* Finished files come back as a signed `download.url`. Add `https://thirds.ai` in front; the link lasts 15 minutes and needs no key.
* The n8n and Make files were exported with credentials removed. Add your own key and template ID after import.

Questions or a broken example? Open an issue on this repo.

(Disclosure: I'm connected to thirds.ai.)
