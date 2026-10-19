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

## More examples

- [Page numbers, a header and clean page breaks in an HTML to PDF export: print CSS plus one thirds.ai API request](https://gist.github.com/thirdsai/621b60696b517bc0ef1baf8fb2c1a2db)
- [Make one certificate PDF per row of a CSV (learner, course, date) with the thirds.ai API. Python standard library only, safe to re-run](https://gist.github.com/thirdsai/8d625784ed204b719c0c856221788a2e)
- [n8n workflow: email a PDF certificate for each new Google Sheets row, using HTTP Request nodes and the thirds.ai API](https://gist.github.com/thirdsai/fc75c468233df20ad1bee3d6966bd016)
- [Build-time Open Graph images: one 1200x630 PNG per blog post from a single design, skipped when the PNG already exists. Node 20+, no dependencies](https://gist.github.com/thirdsai/2ac4be0f25843f341dcedd442b9b474d)
- [Make blueprint: a branded donation receipt PDF for every Stripe gift, via the HTTP app and the thirds.ai API](https://gist.github.com/thirdsai/249ba8d95ce76be8eb256a2f4dada28d)
- [Batch ad images: one design, one row per product, a ZIP of PNGs in three sizes each, via thirds.ai image packs](https://gist.github.com/thirdsai/b3227e494d2fbbd53a017ca35703d527)
- [Airtable scripting extension: turn each invoice record into a branded PDF and attach it to the record](https://gist.github.com/thirdsai/a282f61b85f1067f6b6aa70db825df0a)
- [Google Sheets + Apps Script: make a PDF certificate for each learner row, save it to Drive and email it](https://gist.github.com/thirdsai/13d3b5f3a19bd6c375518c378461ac39)
- [Zapier recipe: turn an order-paid webhook into a PDF receipt with line items, tax and a Paid stamp. Includes a curl test with a mocked payload](https://gist.github.com/thirdsai/ac3d5053c1c02c0adfb8afe183824c8c)
- [Next.js App Router: an API route that turns server-built invoice HTML into a PDF with thirds.ai, plus a download button component](https://gist.github.com/thirdsai/3172d9f83bd21bdf29f89d298567c7b0)
- [QR code labels for every row of a CSV, as a print ready A4 PDF (21 per sheet). Node 18+, QR codes drawn locally as SVG](https://gist.github.com/thirdsai/3a85e2063cf79d936aee67bdf07017b9)
- [HTML to PDF in C# with HttpClient: A4, header, Page X of Y footer, CSS page breaks. No NuGet packages](https://gist.github.com/thirdsai/f8a22f7fc3161fb9f1740c8affcd119a)
- [HTML to PDF from Ruby or Rails with only Net::HTTP. A wkhtmltopdf replacement with page numbers and safe retries](https://gist.github.com/thirdsai/a027969ec1e31fe05709a30937e69701)
- [Save a copied or exported ChatGPT conversation as a clean PDF: tables, lists and code blocks intact](https://gist.github.com/thirdsai/df091fb7dc57c5717e79d4a6ccb0e18f)
- [SVG to PNG at any size with a transparent background, rendered by a browser engine (fonts, CSS, foreignObject)](https://gist.github.com/thirdsai/b13895495eed3c5bcebae91ee58f25e8)
- [Node-RED flow: chart data to a PNG with core nodes only, no Chromium on the device](https://gist.github.com/thirdsai/2c322f663b57c244c28770baa231ca22)
- [Django: render a template to HTML and get a PDF back from an API, no wkhtmltopdf or WeasyPrint install](https://gist.github.com/thirdsai/7b1689b9c3539504ef60572ab67dd4dd)
- [Google Sheets Apps Script: one row of ad copy becomes PNGs in every ad size](https://gist.github.com/thirdsai/96e929c00d9b4b280fe5b10f5227045a)
- [HTML to PDF from PHP or Laravel with only ext-curl: page numbers, header and footer, no dompdf or wkhtmltopdf](https://gist.github.com/thirdsai/974a8bce5b106563cfad5b881261f0c2)
- [Invoice PDFs in Go with html/template and only the standard library: no cgo, no Chrome, safe to re-run](https://gist.github.com/thirdsai/d9f1d502a94719d1aff086488454f570)
- [HTML to PDF in Java or Spring Boot with only java.net.http: page numbers, header and footer, no iText or Flying Saucer](https://gist.github.com/thirdsai/f13477de72a37c79ef27080498624437)
- [Stripe Checkout receipt PDFs from a verified webhook in Node, no npm packages, safe on Stripe retries](https://gist.github.com/thirdsai/106f2ef1536c82a3e3b2a5e97d6b9be6)
- [HTML to PDF on Cloudflare Workers, free plan, no Puppeteer or Browser Rendering binding: page numbers, token guard, safe retries](https://gist.github.com/thirdsai/2ca82d80b57fd3867072ede26e282adc)

(Disclosure: I'm connected to thirds.ai.)
