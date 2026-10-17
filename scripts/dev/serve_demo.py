"""Serve the UK Baseline data catalogue demo on this computer and open it in the browser.

Input/output CRS: n/a. Data layer: catalogue site (local demo).

Serves the ``site`` folder next to this script on http://localhost:8010/, or the
next free port up to 8030, and opens the default browser once the server is
listening. Press Ctrl+C in this window, or close it, to stop.

Standard library only, so it runs on any Python 3.9 or later.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import os
import socket
import socketserver
import sys
import threading
import webbrowser
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE / "site"
FIRST_PORT, LAST_PORT = 8010, 8030


class DemoHandler(http.server.SimpleHTTPRequestHandler):
    """Static files with fixed types (the Windows registry can misreport .js)."""

    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".html": "text/html; charset=utf-8",
        ".js": "text/javascript; charset=utf-8",
        ".css": "text/css; charset=utf-8",
        ".json": "application/json",
        ".svg": "image/svg+xml",
        ".png": "image/png",
        ".woff2": "font/woff2",
        ".pdf": "application/pdf",
        ".xml": "application/xml",
        ".gz": "application/gzip",
    }

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002 - stdlib signature
        """Keep the window quiet: one line per page is noise here."""


class DemoServer(http.server.ThreadingHTTPServer):
    """Refuses a port another program already holds (no address reuse)."""

    allow_reuse_address = False
    daemon_threads = True

    def server_bind(self) -> None:
        if hasattr(socket, "SO_EXCLUSIVEADDRUSE"):          # Windows: no shared ports
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        socketserver.TCPServer.server_bind(self)            # skip the slow host-name lookup
        self.server_name, self.server_port = "localhost", self.server_address[1]


def bind(first: int = FIRST_PORT, last: int = LAST_PORT) -> DemoServer:
    """The server on the first free port from ``first`` to ``last``."""
    handler = functools.partial(DemoHandler, directory=str(SITE))
    for port in range(first, last + 1):
        try:
            return DemoServer(("127.0.0.1", port), handler)
        except OSError:
            continue
    raise SystemExit(f"No free port between {first} and {last}. Close another local server and try again.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Serve the catalogue demo and open it in the browser.")
    parser.add_argument("--no-browser", action="store_true", help="serve only; do not open a browser")
    args = parser.parse_args(argv)
    if not (SITE / "index.html").is_file():
        print(f"The demo site is missing: {SITE}")
        return 1
    server = bind()
    url = f"http://localhost:{server.server_address[1]}/"
    print(f"UK Baseline data catalogue demo: {url}", flush=True)
    print("Close this window (or press Ctrl+C) to stop it.", flush=True)
    # DEMO_NO_BROWSER=1 lets a test run start_demo.bat without opening a window.
    if not (args.no_browser or os.environ.get("DEMO_NO_BROWSER") == "1"):
        threading.Timer(0.6, webbrowser.open, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
