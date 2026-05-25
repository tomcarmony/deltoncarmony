# Delton Carmony — Class of 2026

Static graduation announcement site for **Delton Carmony** (Lincoln High School, Seattle · June 16, 2026). Everything lives in one self-contained **`index.html`**: typography, layout, embedded scripts, and styles—no build step.

## What's on the page

- **Header & copy** celebrating graduation and plans (McGill University, Fall 2026)
- **Photo gallery** (`img/`): on wide layouts a fixed-aspect thumbnail grid crops with `object-fit: cover`; under ~900px width it uses masonry-style columns. Click opens full image in the lightbox.
- **Family announcement** section
- **Share card** with a QR code pointing at the current page URL (`PAGE_URL` in the script—you can pin a canonical URL once the site is live)
- **Venmo / gift** call-to-action (`@tomcarmony`; update handles and links as needed)
- **Family & Friends** comment section ([Cusdis](https://cusdis.com/) embed; `data-app-id` and related attributes in `index.html`)

External assets are loaded from CDNs (Google Fonts, QRCode.js, Cusdis).

## Repo layout

| File        | Purpose                    |
|------------|----------------------------|
| `index.html` | Full page (HTML + CSS + JS) |
| `img/` | Gallery images (`delton-1.jpg` … `delton-7.jpg`; optional) |
| `README.md`  | This file                  |

## Hosting

This repo is GitHub Pages–friendly: enable Pages for the branch that contains `index.html` (typically **root** of the repo, or **`/docs`** if you prefer). The QR code uses `window.location.href` when opened in a browser, so it resolves to whichever URL visitors use once deployed.

Before going live, update:

- Cusdis placeholders / `data-*` attributes on `#cusdis_thread` so comments work on production
- `PAGE_URL` fallback in the QR script if you want a fixed domain when testing from `file://`
- Gallery filenames in `#photo-gallery` / `img/` if you add or rename photos
- Venmo link and any personal copy in the markup

## Preview on localhost

Static pages behave more predictably when served over HTTP than when opened as a `file://` URL (CDN scripts may still load; relative paths and some APIs behave better on a server).

### Option A — one command (recommended)

From the project directory:

```bash
cd /path/to/deltoncarmony

python3 -m http.server 8000
```

Then open **http://localhost:8000/** in your browser. Press **Ctrl+C** in the Terminal to stop the server.

*(If `python3` is unavailable, try `python` on older systems.)*

### Option B — small Python script

Save as `preview.py` next to `index.html` (or paste into Terminal with `python3 -`), then run **`python3 preview.py`**:

```python
#!/usr/bin/env python3
"""Serve the current folder on http://127.0.0.1:8000 for local previews."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HOST, PORT = "127.0.0.1", 8000

if __name__ == "__main__":
    httpd = ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Serving Delton Carmony preview at http://{HOST}:{PORT}/")
    print("Open that URL in a browser (index.html loads by default). Ctrl+C to stop.")
    httpd.serve_forever()
```

---

*Delton — Class of 2026 · Seattle, WA*
