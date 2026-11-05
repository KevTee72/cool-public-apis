#!/usr/bin/env python3
"""Call every "poke it" link in README.md and report which APIs are down.

Usage:
    python ping.py              # check everything
    python ping.py --timeout 10 # custom timeout in seconds

Exits with code 1 if any link fails, so it works in CI.
Standard library only.
"""

import argparse
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

POKE_LINK = re.compile(r"\[poke it\]\((https?://[^)\s]+)\)")
USER_AGENT = "cool-public-apis-ping/1.0 (+https://github.com/KevTee72/cool-public-apis)"


def check(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status
    except urllib.error.HTTPError as err:
        return err.code
    except Exception:
        return 0  # timeout, DNS failure, TLS error and friends


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--readme", default=Path(__file__).with_name("README.md"), type=Path)
    parser.add_argument("--timeout", default=20, type=float)
    parser.add_argument("--workers", default=8, type=int)
    args = parser.parse_args()

    urls = list(dict.fromkeys(POKE_LINK.findall(args.readme.read_text(encoding="utf-8"))))
    if not urls:
        print("No poke it links found. Is this the right README?")
        return 1

    started = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        codes = list(pool.map(lambda u: check(u, args.timeout), urls))

    down = limited = 0
    for url, code in zip(urls, codes):
        if code == 429:  # server is up, we just asked too often
            limited += 1
        elif not 200 <= code < 400:
            down += 1
        label = str(code) if code else "ERR"
        print(f"{label:<4} {urlparse(url).netloc:<32} {url}")

    extra = f", {limited} of them rate limited" if limited else ""
    print(f"\n{len(urls) - down} alive, {down} down{extra} ({time.time() - started:.1f}s)")
    return 1 if down else 0


if __name__ == "__main__":
    sys.exit(main())
