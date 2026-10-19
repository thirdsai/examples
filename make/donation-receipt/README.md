# Branded donation receipt PDF for every Stripe gift (Make blueprint)

Import `make-donation-receipt.blueprint.json` into Make (open a new scenario and use Import Blueprint). It uses Make's HTTP app, so no private app is needed.

What the blueprint does
1. Custom webhook receives a Stripe `checkout.session.completed` event. Add your own webhook in Make and point a Stripe webhook endpoint at its URL.
2. Set multiple variables turns the event into `donor_name`, `donor_email`, `amount` (Stripe's `amount_total / 100`, since Stripe sends the smallest unit), `received_on` (formatted as YYYY-MM-DD, which the design requires) and `receipt_number` (`GIFT-` plus the payment intent id).
3. HTTP POST to `https://thirds.ai/v1/pdf` with your Template ID, the donor data and an `Idempotency-Key` of `receipt-<receipt number>`, so a re-run never makes or charges for a second receipt.
4. Router: if the PDF is `succeeded`, Get a file downloads it. If not, a Repeater waits 3 seconds, checks the status again and downloads the file once it is ready.

What you add
* Your thirds.ai API key, in a Make keychain on both HTTP modules (the export holds no key).
* Your Template ID in place of `tpl_PASTE_YOUR_TEMPLATE_ID`. On thirds.ai, open the Donation receipt design in the gallery, click Use this template, add your logo and charity details, and copy the ID.
* Your charity's details in the request body. Replace the YOUR CHARITY NAME, YOUR CHARITY ADDRESS, YOUR CONTACT EMAIL and YOUR CHARITY REGISTRATION LINE placeholders, and edit `amount_note`, `designation`, `message` and `tax_statement` to suit.
* An email step after Get a file (Gmail or Microsoft 365 Send an email to `donor_email` with the file attached). The blueprint stops at the downloaded PDF because email modules need your own login.

Using Tally instead of Stripe? Swap the webhook for Tally Watch new responses and map the form fields into the same five variables.

Each finished PDF uses one credit and a failed one costs nothing; a free thirds.ai account gets 50 a month.

Check what your country asks a receipt to say. In the US, a single gift of $250 or more needs a written acknowledgment that states whether the donor got any goods or services in return; in the UK, say if a Gift Aid declaration applies.

Guide: https://thirds.ai/use-cases/quotes-and-receipts?utm_source=make&utm_medium=community&utm_campaign=own-content&utm_content=make-donation-receipt

(Disclosure: I'm connected to thirds.ai.)
