# Privacy policy: thirds.ai plugin for Dify

Last updated: 20 October 2026

This plugin turns HTML into PDF files and images by calling the thirds.ai API. This page explains what data the plugin handles, where it goes and what is kept.

## What the plugin collects and stores

The plugin itself collects, stores and logs no user data. It has no database, no analytics and no tracking. It does not use Dify plugin storage.

## What is sent to a third party

Each tool call sends the following to [thirds.ai](https://thirds.ai) over HTTPS:

* **The HTML you pass to the tool**, and the options you choose (page size, margin, image size, format, transparency, JavaScript on or off). The HTML can contain personal data if you or your workflow put it there, for example a name and address on an invoice. The plugin does not inspect or filter it.
* **Your thirds.ai API key**, in the Authorization header, so thirds.ai knows which account to use.
* **An idempotency key**, a hash of the request, so a retry returns the same job.

The plugin then downloads the finished file from thirds.ai and hands it to Dify. Dify stores the file like any other tool output, under Dify's own policies.

## What thirds.ai keeps

According to the [thirds.ai privacy policy](https://thirds.ai/privacy):

* The HTML and assets you send exist on its servers only to make the file, and the input of a job is deleted when the job ends.
* The finished PDF or image is kept for the account's retention period and then deleted. You can choose a shorter period or delete a file earlier.
* Document content is not written into its logs, and no person looks at documents unless you ask for help with them.
* The account keeps a record of renders and credit use. The live service and file storage are hosted by Hetzner Online GmbH in Finland.

Read the full policy at [thirds.ai/privacy](https://thirds.ai/privacy). For data requests, such as a copy or deletion of your data, write to support@thirds.ai.

## Sensitive data

The plugin is not designed for health, financial, biometric or children's data. If your HTML contains such data, you are responsible for having a legal basis to send it to thirds.ai.

## Contact

Questions about this policy: support@thirds.ai, or an issue in [github.com/thirdsai/examples](https://github.com/thirdsai/examples/issues).
