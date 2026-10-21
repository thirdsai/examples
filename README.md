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
| [`dify/`](dify/) | Dify tool plugin: HTML to PDF and HTML to image tools for workflows and agents | Dify 1.0+ (Marketplace or .difypkg upload) |

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
- [HTML to PDF on AWS Lambda in Python with only the standard library: no Chromium layer, optional S3 output for big files](https://gist.github.com/thirdsai/1e8750fa4e1ebe2024b75018130b284d)
- [Supabase Edge Function: a PDF for every new invoice row, saved to a private Storage bucket. No Puppeteer, no npm packages, safe on webhook retries](https://gist.github.com/thirdsai/496b5a9a7d4300bbd58c4f8753bb29a6)
- [Shopify products to ad PNGs in every size (1080 square, 4:5, story, 1200x628) from the public products.json. Node 18, no packages](https://gist.github.com/thirdsai/d14b676543815819a181658989013c7e)
- [HTML string to PNG in Python with only the standard library, plus a 1200x630 Open Graph image for every page that skips unchanged pages](https://gist.github.com/thirdsai/82130c379f5c894d55123622229f001d)
- [Google Sheets to a branded weekly PDF report with totals, an SVG bar chart and a clean table, emailed every Monday by Apps Script](https://gist.github.com/thirdsai/b1c49051c623ac423b642dc921f72586)
- [Invoice PDFs from an Express route in Node 18, no Puppeteer or Chromium: cents totals, escaped data, repeating table header, Page X of Y, safe retries](https://gist.github.com/thirdsai/fe2d23f091208baaa162d4da9d70eba9)
- [Bubble API Connector recipe: multi page quote PDFs where repeating group rows never split, saved as a Bubble file, key kept server side](https://gist.github.com/thirdsai/0ee495b1ad0d94f7584f3c1b07bc7122)
- [Invoice PDFs from an async FastAPI route, no WeasyPrint or wkhtmltopdf: cents totals, escaped data, repeating table header, Page X of Y, safe retries](https://gist.github.com/thirdsai/d560689abac2d46ca46009d7194e6729)
- [Airtable scripting extension: a 1200x630 social card PNG for every record, saved to an attachment field, only changed records rendered again](https://gist.github.com/thirdsai/49b32c331a6b533864199e7cf0b232c7)
- [Puppeteer in Docker: fix "No usable sandbox!" without --no-sandbox, using a seccomp profile and a non-root user, or ship no browser at all](https://gist.github.com/thirdsai/fdf7a8eb2d305772bfe8389fcb9dd73c)
- [Puppeteer: wait until a page that loads its data after the load event is really finished before page.pdf(), plus the same page as a PDF from an API](https://gist.github.com/thirdsai/d6613eb3603275b041b9cb3e4ccc13bc)
- [Puppeteer headerTemplate and footerTemplate: seven traps measured (scripts, missing header, tiny text, page CSS, zero margins, flexbox, images) and a helper that avoids them](https://gist.github.com/thirdsai/d7340585ce2697430d54510d51c709e2)
- [A weekly PDF report from Grafana OSS without Enterprise reporting or the image renderer: dashboard queries over the HTTP API, drawn as HTML and SVG. Tested on a local Grafana with test data](https://gist.github.com/thirdsai/e7a660fe87ed3c752f7fc7f4c77ea024)
- [Capture a handwritten signature on a canvas in the browser and place it in a PDF agreement with an audit block. Node, no libraries. Not a sealed digital signature](https://gist.github.com/thirdsai/4c13e51a4748c8922d2e4c67475e142c)
- [Remove the date, title, URL and page count Chrome prints on every page, from the page's own CSS: zero @page margins plus repeating padding, measured](https://gist.github.com/thirdsai/be42af132ea72ad12fbdd600f749eaf9)
- [Get a PDF from your API into the browser without corrupting it: fetch, axios and base64 traps, popup blocking and UTF-8 file names, measured in Chrome](https://gist.github.com/thirdsai/1bb161aeccdf052886e22263c7528d24)
- [Print only one element of a page: why the popular print CSS gives blank pages or clipped rows, and a small helper that does not](https://gist.github.com/thirdsai/5799d2c1a240c006b01614aca1a74ab5)
- [A4 pages in HTML that print 1:1: @page size, zero margins, border-box and screen-only gaps, measured with a marker, plus a check for overflowing sheets](https://gist.github.com/thirdsai/26b24a717cb86812cb63228414cb0345)
- [FPDF and UTF-8 in PHP: what utf8_decode, iconv, mb_convert_encoding and tFPDF actually print, measured, plus a helper that never prints an empty line](https://gist.github.com/thirdsai/18c1903a04a5cc36bbcd6cebb091cf27)
- [Serving a PDF from PHP: correct headers, inline or download, stray BOM and whitespace bytes, path traversal and Laravel, measured, plus a send_pdf helper](https://gist.github.com/thirdsai/682089dbd0149e22e88a23fb8ebd5815)
- [Text to image in C# on Linux: why System.Drawing fails, SkiaSharp's font and native asset traps, measured, plus a wrapping helper with font fallback](https://gist.github.com/thirdsai/7d589e9efb1fe17d4b42fc71c67d3c29)
- [Returning a PDF from ASP.NET Core on .NET 10: the answers that return JSON, empty files or 500s, measured, plus a PdfResults helper for inline or download](https://gist.github.com/thirdsai/1a620193e5831861b1d33d5599f4aba2)
- [Many matplotlib figures in one PDF with PdfPages: page sizes, Type 3 fonts, memory, missing glyphs and reproducible bytes, measured, plus a helper](https://gist.github.com/thirdsai/a20ffdf50d2e67ece53324e1b0e6a768)
- [Returning a generated image from FastAPI or Flask: empty bodies, JSON errors, RGBA to JPEG and a blocked event loop, measured, plus an ETag helper](https://gist.github.com/thirdsai/4f2860236f636e2e3dafab0943531f95)
- [XLSX to PDF with headless LibreOffice: parallel runs, silent failures, a running instance, CSV delimiters and cut up sheets, measured, plus a Python wrapper](https://gist.github.com/thirdsai/ffa285aabba9a43b3ede75b3fdf7efc2)
- [Fonts in Chrome PDFs on Linux and in containers: which font packages cover which scripts, lang and Han glyphs, line breaks, measured, plus a fontconfig preflight](https://gist.github.com/thirdsai/35072ca775127b143e083efe9f6c776f)
- [Resize photos into social cards with sharp in Node: EXIF rotation, GPS leaks, lost subjects, black bars and transparency, measured, plus a helper](https://gist.github.com/thirdsai/e3918e662f37ce8f81138db1c784bb18)
- [Google Forms Apps Script: a tidy PDF of every response, saved to Drive and emailed to you or the respondent, every question type handled](https://gist.github.com/thirdsai/877f157e6528cddca6ea16415013dd9f)
- [Merge PNG, JPEG, WebP or GIF images into one PDF, one image per page, large ones scaled down to fit, in Python with only the standard library (no Pillow or ImageMagick)](https://gist.github.com/thirdsai/7335ce60b0e06e29b4b42f357f035703)
- [Power Automate custom connector plus cloud flow: SharePoint or Dataverse rows to a PDF from one HTML template, with images, a repeating header, rows that never split and Page X of Y, saved to OneDrive or SharePoint](https://gist.github.com/thirdsai/14639aa030ad1e8a60cf61716994a876)
- [Webflow CMS Open Graph images: one Node script with no packages that renders a 1200x630 share card for every collection item from one HTML design, skips unchanged items and writes the Image field through the Data API v2](https://gist.github.com/thirdsai/1fb6851e0633651d767804881c56b37a)
- [Microsoft Forms response to PDF in Power Automate, without the file that won't open](https://gist.github.com/thirdsai/057cf63096921cc34e24abc57edffedd)
- [Outlook email to PDF in SharePoint with Power Automate, inline images included](https://gist.github.com/thirdsai/43079ea2b671c1e46c66f5e486a735bf)
- [PDF file content in Power Automate: base64, base64ToBinary, and why the attachment is corrupt or blank](https://gist.github.com/thirdsai/bf68e8e1b45ed859b381a4342806b3dc)
- [50 statements in one PDF from a SQL stored procedure, without merging PDFs in Power Automate](https://gist.github.com/thirdsai/c8980a480c336363287eefb2cdc94cd6)
- [One Excel worksheet to PDF from Power Automate, with dates as shown and links that still click](https://gist.github.com/thirdsai/2e575e0bcdd20f1a251701586231c8b7)
- [Power Apps to PDF with every gallery row and the signature, through one flow](https://gist.github.com/thirdsai/f96e7f066e90bb987cc7aca9d8681554)
- [wkhtmltopdf 0.12.6 "Warning: Blocked access to file": the flag, where it goes, and the safer --allow, measured](https://gist.github.com/thirdsai/172afdaa5fbd99482dab9e7af790094b)
- [Google Fonts in wkhtmltopdf: which ways of loading the font work, and the silent woff2 fallback, measured](https://gist.github.com/thirdsai/e4b70049feafabe9956a384446e28724)
- [WeasyPrint on Windows: "OSError: cannot load library 'gobject-2.0': error 0x7e", what it means and how to check before you import](https://gist.github.com/thirdsai/fc34f22d7f12e3a3ea9cc1b41a8ed5e2)
- [html2canvas: leave elements out of the screenshot, four ways measured, and why the cloned element came out blank](https://gist.github.com/thirdsai/1125e1241e32917fd58bf21625978741)
- [Chrome's PDF viewer: where the tab title and the Save file name come from, measured](https://gist.github.com/thirdsai/c2ae83f90b9f33d46162cb1dc694db73)
- [Rails ActionMailer: attach a generated invoice PDF, and the four ways it goes wrong, measured](https://gist.github.com/thirdsai/70d886efc19cab9fa7e8fc36be349036)
- [pdfMake from HTML and from data: "Unrecognized document structure", the dynamic table that will not build, and the fix (pdfmake 0.3.12, tested)](https://gist.github.com/thirdsai/19298786c8e31a69dfe8feda006aa560)
- [pdfMake "Roboto-Regular.ttf not found in virtual file system": script order, bundles, and the 0.3 call that replaces pdfMake.vfs (tested)](https://gist.github.com/thirdsai/d6268cfdac74911a0a6cf3c339302151)
- [Convert SVG to PNG in Python: CairoSVG, svglib, Wand, pyvips and headless Chrome on one test SVG (tested 2026)](https://gist.github.com/thirdsai/9e9ce19f6a6fac4a2b02cb5848b631ca)
- [Plotly and folium to HTML and PNG in 2026: Kaleido 1.x needs Chrome, folium's _to_png downloads Firefox, and OpenStreetMap blocks its tiles (tested)](https://gist.github.com/thirdsai/b74119d1b61dcfd67db07c7ca93b4448)
- [Nodemailer PDF attachment arrives damaged or empty: the six ways it goes wrong, measured against a local SMTP server](https://gist.github.com/thirdsai/fa73dd8457415cdf2539a5d07eebdd23)
- [Fill an existing PDF form in Node.js with pdf-lib: wrong field names, "WinAnsi cannot encode", invisible values and a flatten bug (tested 2026)](https://gist.github.com/thirdsai/75dd204149144fbe7fee5b9e2424e012)
- [Name badges from a CSV or Excel export as one print ready A4 or Letter PDF: auto grid, names that shrink or wrap, ribbons, cut marks, Python standard library only](https://gist.github.com/thirdsai/41a8a30ec9396812d54fc7eaf9597c63)
- [Google Sheets Apps Script: a PDF receipt for every paid row, totals in pence, saved to Drive and emailed, never double sent on rerun](https://gist.github.com/thirdsai/328237e68b1d991188150978b54b922b)
- [mPDF: why a header image covers the body and why a footer shows only on the last page, measured on mPDF 8.3 with the fixes](https://gist.github.com/thirdsai/5f594545da50b78ce977001a7385ab72)
- [TCPDF writeHTML on 6.11 and 7.0: rows split across pages, nobr on tr vs table, and 11 ways of placing an image, measured](https://gist.github.com/thirdsai/dfa8a454563f0200978b5f0b2878f782)
- [wkhtmltopdf page-break-after doing nothing: 22 break placements on 0.12.6 and which parents swallow the break](https://gist.github.com/thirdsai/745f26573cb667161de172c2435d2e8d)
- [docx to PDF from Node: LibreOffice vs mammoth vs docx-preview on one Word file, headers, page numbers, images and page breaks checked](https://gist.github.com/thirdsai/be16152afa19878556a561edc4a2f680)
- [A custom header and footer on every printed page in Chrome: thead and tfoot, position fixed, @page margin boxes, running elements, measured](https://gist.github.com/thirdsai/eef1d8ede816380e91dd5839050b652f)
- [Puppeteer PDF that opens blank or corrupt: page.pdf() now returns a Uint8Array, Express 4 res.send turns it into JSON, and res.text() on the client, measured](https://gist.github.com/thirdsai/bd154bae4f2fcf0e469a9021bea71d20)
- [wkhtmltopdf repeated thead overlapping rows: it happens when one row is taller than the page; 10 cases on 0.12.6.1 and the fixes that work](https://gist.github.com/thirdsai/47df8988d393a250ccdf454b303acd9c)
- [WeasyPrint 70: headers and footers on every page (margin boxes, running elements, page N of M) and @font-face that loads, 18 cases checked](https://gist.github.com/thirdsai/a449561c124c4817a8e05f078d420b76)
- [Puppeteer on Vercel, Could not find Chrome: why the cache misses the bundle, 701 MB vs 250 MB, and @sparticuz/chromium cold start, measured](https://gist.github.com/thirdsai/edbcba1f62c616f65a0e36038fdbf4f9)
- [wkhtmltopdf from C# with an HTML string: the stdout deadlock, UTF-8 mojibake and relative images with stdin, 12 cases on .NET 10](https://gist.github.com/thirdsai/de6bdebf2a532b45440a3e7434b81b7d)
- [PDFKit or wicked_pdf hanging in development: wkhtmltopdf calls back into a one request at a time server; reproduced in Ruby with the fixes](https://gist.github.com/thirdsai/7903231b5a194650e0f050e62e700465)
- [Shopify orders export CSV to one PDF of packing slips, one per order, line items grouped, tick boxes for the packer, Python standard library only.](https://gist.github.com/thirdsai/ee92adbbc7e109e563ff8f99eb38c7c8)
- [Zapier recipe: a landscape PDF certificate for every new Sheets row or form response, emailed automatically, safe on Zapier replays.](https://gist.github.com/thirdsai/eec0abe0807e251766bd726f596798a9)
- [Google Sheets Apps Script: a PDF payslip for every employee row, any number of earnings and deductions, totals in whole cents, saved to Drive and emailed, safe to rerun.](https://gist.github.com/thirdsai/57e7894c14acb7951affc5202ffe4a60)
- [Bubble recipe: a 1200x630 Open Graph share image for every Thing on a dynamic page, made in a backend workflow, stored in Bubble, safe on retries.](https://gist.github.com/thirdsai/ccd52db9ab1bfb3eb417330e7b14f96f)
- [Google Sheets Apps Script: 4x6 shipping labels for every new order row in one PDF, one per page, saved to Drive, safe to rerun.](https://gist.github.com/thirdsai/2c5c6558a54adeb2ecab7e5cf3231805)
- [Airtable automation script: a certificate of completion PDF attached to the record when it matches a condition, with a printed certificate ID, safe on retries.](https://gist.github.com/thirdsai/aa43352d70e89edf76731acae3e34f43)
- [n8n workflow: a 1200x630 Open Graph share image for every new blog post from any RSS feed, cleaned and escaped titles, safe to rerun.](https://gist.github.com/thirdsai/6121bd5440422fd3a032dc03fc45787f)

(Disclosure: I'm connected to thirds.ai.)
