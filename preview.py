#!/usr/bin/env python3
"""Serve the project folder on http://127.0.0.1:8000 for local previews."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HOST, PORT = "127.0.0.1", 8000

if __name__ == "__main__":
    httpd = ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Serving at http://{HOST}:{PORT}/")
    print("Open that URL in a browser (index.html loads by default). Ctrl+C to stop.")
    httpd.serve_forever()
