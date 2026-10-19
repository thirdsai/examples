# certificates_from_csv.py

Make one certificate PDF per row of a CSV (learner, course, date) with the thirds.ai API. Python standard library only, safe to re-run.

Give every learner in a class list their own certificate PDF.

1. On thirds.ai, open the [Portrait course certificate](https://thirds.ai/gallery/completion-certificate?utm_source=github&utm_medium=community&utm_campaign=own-content&utm_content=gist-certificates), click Use this template, put your logo on it, and copy its Template ID.
2. Save your list as `learners.csv` with the columns `learner,course,date`.
3. Run `THIRDS_API_KEY=... TEMPLATE_ID=tpl_... ISSUER="Your school" python3 certificates_from_csv.py learners.csv`.

You get `certificates/001-alex-morgan.pdf` and so on. Each row sends an idempotency key built from the row number and name, so if the script stops halfway you can run it again and it will not pay twice for the rows that already worked. Rows that fail are skipped and printed, and a failed file costs nothing.

No code at all? The free [certificate generator](https://thirds.ai/tools/certificate-generator?utm_source=github&utm_medium=community&utm_campaign=own-content&utm_content=gist-certificates) makes single certificates in the browser, and a free account fills the design from a CSV and gives you a ZIP.

(Disclosure: I'm connected to thirds.ai.)
