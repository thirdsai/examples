// Make a 1200x630 Open Graph PNG for every post at build time with thirds.ai.
// posts.json: [{"slug":"grow-tomatoes","title":"...","description":"..."}]
// Usage: THIRDS_API_KEY=... TEMPLATE_ID=tpl_... SITE_NAME="My blog" SITE_URL=example.com node og-image-per-post.mjs
// Node 20+. Each finished image costs one credit; posts with an existing PNG are skipped.
import { readFile, writeFile, mkdir, access } from "node:fs/promises";
import { createHash } from "node:crypto";

const API = "https://thirds.ai";
const auth = { Authorization: `Bearer ${process.env.THIRDS_API_KEY}` };
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function call(method, path, body, key) {
  const res = await fetch(API + path, {
    method,
    headers: body ? { ...auth, "Content-Type": "application/json", "Idempotency-Key": key } : auth,
    body: body ? JSON.stringify(body) : undefined,
    signal: AbortSignal.timeout(60000),
  });
  if (!res.ok) throw new Error(`${path}: HTTP ${res.status} ${await res.text()}`);
  return res.json();
}

const posts = JSON.parse(await readFile("posts.json", "utf8"));
await mkdir("public/og", { recursive: true });

for (const post of posts) {
  const out = `public/og/${post.slug}.png`;
  try { await access(out); continue; } catch {}
  const data = {
    site_name: process.env.SITE_NAME,
    page_title: post.title,
    description: post.description,
    site_url: `${process.env.SITE_URL}/${post.slug}`,
  };
  // The key changes when the title changes, so an edited post gets a new card.
  const key = "og-" + createHash("sha256").update(JSON.stringify(data)).digest("hex").slice(0, 32);
  let job = await call("POST", "/v1/image", { template_id: process.env.TEMPLATE_ID, data, image: { format: "png" } }, key);
  const deadline = Date.now() + 120000;
  while (job.status === "queued" || job.status === "running") {
    if (Date.now() > deadline) throw new Error(`${post.slug}: still ${job.status}`);
    await sleep(2000);
    job = await call("GET", `/v1/image/${job.id}`);
  }
  if (job.status !== "succeeded") { console.error(post.slug, job.status); continue; }
  const file = await fetch(API + job.download.url);
  await writeFile(out, Buffer.from(await file.arrayBuffer()));
  console.log("saved", out);
}
