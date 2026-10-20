# thirds.ai for Dify

Turn HTML into PDF files and PNG, JPEG or WebP images inside Dify workflows, chatflows and agents. The plugin sends your HTML to the [thirds.ai](https://thirds.ai/?utm_source=dify&utm_medium=community&utm_campaign=own-content&utm_content=dify-plugin) render API, waits for the file and returns it as a Dify file.

**Source repository:** https://github.com/thirdsai/examples/tree/main/dify

## Tools

| Tool | What it returns |
|---|---|
| **HTML to PDF** | A PDF file. Options: page size (A4, Letter, Legal, A3, A5), landscape, margin, run JavaScript. |
| **HTML to image** | A PNG, JPEG or WebP file. Options: width (320 to 7680 px), height (200 to 4320 px), transparent background (PNG), run JavaScript. |

Each tool also returns a small JSON object with the job ID, file name and size.

## Setup

1. **Get an API key.** Sign in at [thirds.ai](https://thirds.ai/?utm_source=dify&utm_medium=community&utm_campaign=own-content&utm_content=dify-plugin) with an email link, GitHub or Google, and verify your email address. Open **API keys**, create a named key and copy it. The full key is shown once. The [authentication guide](https://thirds.ai/docs/api?utm_source=dify&utm_medium=community&utm_campaign=own-content&utm_content=dify-plugin#authentication) has the details.
2. **Install the plugin.** In Dify, open **Plugins**, search the Marketplace for **thirds.ai** and click **Install**.
3. **Configure the credential.** Open the plugin from **Plugins** (or from the tool picker in a workflow), choose to authorize it, paste the key into **API key** and save. Dify checks the key right away with a read-only call that uses no credits.

### Credentials and account

* **Required credential:** one thirds.ai API key, stored by Dify as a secret. The plugin sends it only to thirds.ai in the `Authorization: Bearer` header.
* **External paid service:** thirds.ai is a paid API with a free plan. The free plan includes a monthly allowance of credits and needs no card; paid plans add more. Each finished PDF or image uses one credit, and a failed render uses none.

## Usage

### In a workflow or chatflow

1. Add an **LLM** node (or a **Template** node) that writes a complete HTML document, with inline CSS.
2. Add **thirds.ai, HTML to PDF** or **thirds.ai, HTML to image** and set **HTML** to that output.
3. Pick the page size or image size in the node settings.
4. Use the tool's `files` output in the next node, for example an **Answer** node or an upload step.

### In an agent

Add the tools to an **Agent** node or an agent app. The model writes the HTML and calls the tool when the user asks for a PDF or an image, for example "Make a one page PDF invoice for order 1042".

### Example HTML

```html
<!doctype html>
<html>
<head>
<style>
  @page { size: A4; margin: 18mm; }
  body { font-family: Helvetica, Arial, sans-serif; color: #1f2937; }
  h1 { margin: 0 0 12px; }
  table { width: 100%; border-collapse: collapse; }
  td, th { padding: 6px; border-bottom: 1px solid #e5e7eb; text-align: left; }
  thead { display: table-header-group; }
  tr { break-inside: avoid; }
</style>
</head>
<body>
  <h1>Invoice 1042</h1>
  <table>
    <thead><tr><th>Item</th><th>Qty</th></tr></thead>
    <tbody><tr><td>Consulting</td><td>3</td></tr></tbody>
  </table>
</body>
</html>
```

### Tips

* **Images and fonts** must load from public HTTPS URLs or be inlined as data URLs. The file is made on thirds.ai's servers, so `localhost` or private network addresses do not load.
* **Page breaks:** CSS such as `break-inside: avoid` and `thead { display: table-header-group; }` keeps table rows whole and repeats the header on each page.
* **Web fonts in images:** turn on **Run JavaScript** and set `data-thirds-render-ready="true"` on the `<html>` element after `document.fonts.ready`, so the capture waits for the font.
* **Retries are safe.** The plugin sends an idempotency key made from the request, so a retry or a re-run with the same input returns the first file instead of making a second one and using another credit.

## Connection requirements

* **Outbound HTTPS** from the Dify plugin runtime to `https://thirds.ai` (port 443). This is the only host the plugin contacts, and it is declared in `manifest.yaml`. Self-hosted Dify behind a firewall or proxy must allow it.
* **Endpoints used:** `POST /v1/pdf`, `POST /v1/image`, `GET /v1/pdf/{id}`, `GET /v1/image/{id}`, `GET /v1/pdf?limit=1` (credential check) and the short-lived signed download link returned by the job. See the [API reference](https://thirds.ai/docs/api?utm_source=dify&utm_medium=community&utm_campaign=own-content&utm_content=dify-plugin).
* **Timeouts:** each request times out after 60 seconds, and a tool call gives up after 100 seconds. A job that is still running can be picked up by running the tool again with the same input.
* **Limits:** HTML up to 5 MB. A PDF can hold up to 100 pages.

## Errors

| Message starts with | What to do |
|---|---|
| The html input is empty | Pass the HTML document to the **HTML** input. |
| thirds.ai rejected the API key | Check or replace the key in the plugin settings. |
| The thirds.ai account has no credits left | Wait for the monthly allowance or add credits in thirds.ai. |
| thirds.ai could not accept these options | Check the margin, size or format value shown in the message. |
| thirds.ai could not make the file | Fix the HTML named in the message. A failed render uses no credit. |
| Could not reach thirds.ai | Check the outbound HTTPS rule above, then try again. |

The API key never appears in error messages or logs.

## Privacy

See [PRIVACY.md](PRIVACY.md). In short: the plugin stores nothing itself. The HTML you render and your API key go to thirds.ai, which deletes the input when the job ends and keeps the finished file for your account's retention period.

## Maintainer and support

This plugin is made and maintained by thirds.ai. For help, open an issue in the [source repository](https://github.com/thirdsai/examples/issues) or write to support@thirds.ai.

## License

MIT, as in the source repository.
