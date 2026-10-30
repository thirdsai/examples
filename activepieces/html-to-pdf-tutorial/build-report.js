// Activepieces Code step "Build report": turns a list of rows into print ready HTML for the HTTP step.
// Inputs: title, company, currency (3 letter code), notes, rows (a list or JSON text of
//   { order, date, customer, item, qty, price } objects, for example from Google Sheets "Get Rows").
// Output: body (the JSON body for POST /v1/pdf), idempotency_key, file_name.
export const code = async (inputs) => {
  const clean = (v) => String(v == null ? '' : v).trim();
  const esc = (v) => clean(v).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const rows = typeof inputs.rows === 'string' ? JSON.parse(inputs.rows || '[]') : (inputs.rows || []);
  if (!Array.isArray(rows) || !rows.length) throw new Error('rows is empty: map a list of rows into this step');
  const cur = (clean(inputs.currency) || 'GBP').toUpperCase();
  const money = (n) => { try { return new Intl.NumberFormat('en-GB', { style: 'currency', currency: cur }).format(n); } catch (e) { return `${Number(n).toFixed(2)} ${cur}`; } };
  const lines = rows.map((r, i) => {
    const qty = Number(r.qty), price = Number(r.price);
    if (!(qty > 0) || !isFinite(price)) throw new Error(`row ${i + 1} (${clean(r.order)}): qty and price must be numbers`);
    return { ...r, qty, price, amount: Math.round(qty * price * 100) / 100 };
  });
  const total = Math.round(lines.reduce((s, r) => s + r.amount, 0) * 100) / 100;
  const title = clean(inputs.title) || 'Report';

  const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>${esc(title)}</title><style>
/* Page size and margins come from the request (pdf.format and pdf.margins), so they are not repeated here. */
* { box-sizing: border-box; }
body { margin: 0; font: 10pt/1.45 "Liberation Sans", Arial, sans-serif; color: #1d2433; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1 { font-size: 20pt; margin: 0 0 2mm; color: #1f4e79; }
h2 { font-size: 13pt; margin: 8mm 0 3mm; color: #1f4e79; break-after: avoid; }
.muted { color: #57606a; }
.cards { display: flex; gap: 4mm; margin: 6mm 0; }
.card { flex: 1; border: 1px solid #d0d7de; border-radius: 2mm; padding: 3mm 4mm; break-inside: avoid; }
.card b { display: block; font-size: 15pt; }
table { width: 100%; border-collapse: collapse; }
thead { display: table-header-group; }   /* repeat the header row on every page */
tfoot { display: table-row-group; }      /* print the total once, at the end */
tr { break-inside: avoid; }              /* never split a row across two pages */
th { text-align: left; font-size: 8pt; letter-spacing: .06em; text-transform: uppercase; color: #fff; background: #1f4e79; padding: 2mm 2.5mm; }
td { padding: 2mm 2.5mm; border-bottom: 1px solid #d0d7de; vertical-align: top; overflow-wrap: anywhere; }
.r { text-align: right; white-space: nowrap; }
.total td { font-weight: 700; font-size: 11pt; background: #eef3f9; }
.new-page { break-before: page; }        /* start this section on a fresh page */
.keep { break-inside: avoid; }
</style></head><body>
<h1>${esc(title)}</h1>
<div class="muted">${esc(inputs.company)} &middot; ${lines.length} orders</div>
<div class="cards"><div class="card">Orders<b>${lines.length}</b></div><div class="card">Items<b>${lines.reduce((s, r) => s + r.qty, 0)}</b></div><div class="card">Total<b>${esc(money(total))}</b></div></div>
<h2>All orders</h2>
<table><thead><tr><th>Order</th><th>Date</th><th>Customer</th><th>Item</th><th class="r">Qty</th><th class="r">Price</th><th class="r">Amount</th></tr></thead>
<tbody>${lines.map((r) => `<tr><td>${esc(r.order)}</td><td class="r">${esc(r.date)}</td><td>${esc(r.customer)}</td><td>${esc(r.item)}</td><td class="r">${r.qty}</td><td class="r">${esc(money(r.price))}</td><td class="r">${esc(money(r.amount))}</td></tr>`).join('')}</tbody>
<tfoot><tr class="total"><td colspan="6">Total</td><td class="r">${esc(money(total))}</td></tr></tfoot></table>
<section class="new-page"><h2>Notes</h2><div class="keep"><p>${esc(inputs.notes)}</p></div></section>
</body></html>`;

  const hash = (s) => { let h = 2166136261; for (const ch of s) { h ^= ch.codePointAt(0); h = Math.imul(h, 16777619) >>> 0; } return h.toString(36); };
  const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'report';
  return {
    file_name: `${slug}.pdf`,
    idempotency_key: `ap-report-${slug}-${hash(html)}`,
    body: {
      html,
      wait: true,
      pdf: {
        format: 'A4',
        margins: { top: '16mm', right: '14mm', bottom: '20mm', left: '14mm' },
        display_header_footer: true,
        header_template: '<span></span>',
        footer_template: `<div style="width:100%;font-size:8px;color:#57606a;padding:0 14mm;display:flex;justify-content:space-between"><span>${esc(title)}</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`,
        title,
      },
    },
  };
};
