# og-image-per-post.mjs

Build-time Open Graph images: one 1200x630 PNG per blog post from a single design, skipped when the PNG already exists. Node 20+, no dependencies.

Every post on your site gets its own link-preview card with its title on it, made at build time.

1. On thirds.ai, open the [Open Graph card](https://thirds.ai/gallery/open-graph-card?utm_source=github&utm_medium=community&utm_campaign=own-content&utm_content=gist-og-images) design, click Use this template and put your logo and colours on it. Its fields are `site_name`, `page_title`, `description` and `site_url`.
2. Write `posts.json` as a list of `{slug, title, description}` (most static site generators can print this).
3. Run `THIRDS_API_KEY=... TEMPLATE_ID=tpl_... SITE_NAME="My blog" SITE_URL=example.com node og-image-per-post.mjs` before your build. Images are written to `public/og/<slug>.png`.
4. Point each page at it: `<meta property="og:image" content="https://example.com/og/<slug>.png">` plus `og:image:width` 1200 and `og:image:height` 630.

Posts that already have a PNG are skipped, so only new posts spend a credit. The idempotency key is a hash of the card's text, so an edited title gets a new card. Platforms cache previews: after you change an image, give it a new file name and re-scrape it in the Facebook Sharing Debugger or LinkedIn Post Inspector. Keep the title away from the edges, since some apps crop the card.

One-off card with no code: the free [Open Graph image generator](https://thirds.ai/tools/open-graph-image-generator?utm_source=github&utm_medium=community&utm_campaign=own-content&utm_content=gist-og-images).

(Disclosure: I'm connected to thirds.ai.)
