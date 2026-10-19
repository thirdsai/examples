#!/usr/bin/env python3
"""One ad design, every product, three sizes: a ZIP of PNGs per CSV row via thirds.ai image packs.

CSV columns must match your template's fields, for example: headline,price,photo
Usage: THIRDS_API_KEY=... TEMPLATE_ID=tpl_... VERSION=1 python3 ad-sizes-from-csv.py products.csv
Each finished image costs one credit, so 20 products x 3 sizes = 60 credits.
"""
import csv, hashlib, json, os, sys, time, urllib.request

API = "https://thirds.ai"
KEY = os.environ["THIRDS_API_KEY"]
# Square design: original is the square, then a 4:5 portrait and a 9:16 story.
# ("square-post" would repeat a square original and cost a credit for a copy.)
SIZES = ["original", "1080x1350", "story"]


def call(method, path, body=None, key=None):
    headers = {"Authorization": f"Bearer {KEY}"}
    data = None
    if body is not None:
        headers.update({"Content-Type": "application/json", "Idempotency-Key": key})
        data = json.dumps(body).encode()
    req = urllib.request.Request(API + path, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


os.makedirs("ads", exist_ok=True)
with open(sys.argv[1], newline="", encoding="utf-8") as f:
    for n, row in enumerate(csv.DictReader(f), start=1):
        key = "pack-" + hashlib.sha256(json.dumps(row, sort_keys=True).encode()).hexdigest()[:32]
        job = call("POST", "/v1/image-packs", {
            "template_id": os.environ["TEMPLATE_ID"], "version": int(os.environ.get("VERSION", "1")),
            "data": row, "format": "png", "sizes": SIZES}, key)
        deadline = time.time() + 300
        while job["state"] in ("queued", "running"):
            if time.time() > deadline:
                sys.exit(f"row {n} still running; re-run, the same key picks it up")
            time.sleep(3)
            job = call("GET", f"/v1/image-packs/{job['id']}")
        print(n, job["state"], [m["state"] for m in job["members"]])
        if job.get("archive_url"):
            with urllib.request.urlopen(API + job["archive_url"], timeout=120) as r, open(f"ads/{n:03d}.zip", "wb") as out:
                out.write(r.read())
