# Batch image generation for ads: one design, 20 products, three sizes each

`ad-sizes-from-csv.py` makes a ZIP of PNGs per CSV row, in three sizes each, via thirds.ai image packs. Python standard library only.

Testing ads means a lot of near-identical images: the same layout with a different product, price or headline, in square, portrait and story sizes. Making them one by one in a design tool is where the afternoon goes. Here is a way to make the whole set from a spreadsheet with the layout locked.

**1. Make one good design.** Start from a square ad layout you like (the thirds.ai gallery has static ad designs, or rebuild one of your own from a screenshot). Mark the parts that change as fields: `headline`, `price`, `photo`.

**2. Add the sizes once.** Smart resize lays the design out again for each shape instead of cropping it. Check each size, fix any by hand, then save.

**3. One row per product.** A CSV with the same column names as your fields:

```
headline,price,photo
Autumn coat,£79,https://example.com/coat.jpg
Wool scarf,£25,https://example.com/scarf.jpg
```

**4. Run it.** `THIRDS_API_KEY=... TEMPLATE_ID=tpl_... python3 ad-sizes-from-csv.py products.csv` asks for an image pack per row (`original` for the square, `1080x1350` for portrait, `story`) and saves a ZIP per product in `ads/`. Set `VERSION` if your template has more than one saved version (it defaults to 1). Each key is a hash of the row, so you can stop and re-run safely.

**5. Test with the layout fixed.** Because only the fields change, a winning ad tells you something about the headline or the offer, not about a random new layout.

Cost check: 20 products times 3 sizes is 60 images, one credit each; a free account has 50 a month, and a pack of 500 credits costs $10. In the editor, the same thing is Export pack for one design, or a CSV upload for many rows.

Guide: [static ad variations from one design](https://thirds.ai/use-cases/static-ads?utm_source=github&utm_medium=community&utm_campaign=own-content&utm_content=batch-ad-images)

Drafted with AI help.

(Disclosure: I'm connected to thirds.ai.)
