# Email a PDF certificate for each new Google Sheets row (n8n workflow)

Import `n8n-sheets-certificate-email.json` into n8n (Workflows, Import from file). It uses plain HTTP Request nodes, so it runs on n8n Cloud and self-hosted n8n. It holds no credentials and no template ID; you add your own.

When a learner is added to your sheet, this workflow fills a certificate design with their name, course and date, turns it into a PDF and emails it to them. No HTML to write.

How it works
1. New learner row watches your sheet for new rows.
2. Make certificate PDF sends the row to a saved certificate design on thirds.ai and waits for the PDF.
3. PDF ready? checks the status. If the file is still being made, Still rendering? sends it to Wait 3s and Check PDF status, which loop until it is done. A failed or cancelled PDF goes to Stop: PDF failed instead of looping.
4. Download PDF fetches the finished file.
5. Email certificate sends it as an attachment.

Set up
1. Sheet columns: learner, email, course, date.
2. On thirds.ai, open the Portrait course certificate in the gallery, click Use this template, put your logo on it, and copy the Template ID (starts with tpl_).
3. Make an API key on thirds.ai and add it in n8n as a Header Auth credential: name Authorization, value Bearer YOUR_KEY.
4. Paste your Template ID into Make certificate PDF and set your issuer name.
5. Connect Google Sheets and Gmail.

Each finished PDF uses one credit; a failed one costs nothing. A free account gets 50 credits a month. Self-hosted? You can use the thirds.ai community node instead of the HTTP Request node.

Guide: https://thirds.ai/integrations/n8n?utm_source=n8n&utm_medium=community&utm_campaign=own-content&utm_content=n8n-certificate-template

(Disclosure: I'm connected to thirds.ai.)
