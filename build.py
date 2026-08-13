#!/usr/bin/env python3
"""Inline the subset fonts into index.html.

The display face is JetBrains Mono (SIL OFL 1.1), subset to the Latin range plus the
symbols this page uses, converted to woff2 and base64'd into the stylesheet. That keeps
the page a single file with zero external requests, and makes the typography identical
on every OS instead of resolving to SF Mono / Consolas / DejaVu per platform.

Regenerate the .woff2 files with:
  pyftsubset JetBrainsMonoNerdFont-Regular.ttf --unicodes=... --flavor=woff2
"""
import base64, pathlib, sys

root = pathlib.Path(__file__).parent
tpl  = (root / "src" / "index.template.html").read_text()

for token, name in (("__FONT_R__", "jbm-Regular.woff2"), ("__FONT_B__", "jbm-Bold.woff2")):
    f = root / "src" / name
    if not f.exists():
        sys.exit(f"missing {f}")
    tpl = tpl.replace(token, base64.b64encode(f.read_bytes()).decode())

out = root / "index.html"
out.write_text(tpl)
kb = len(out.read_bytes()) / 1024
print(f"built index.html — {kb:.0f}KB")
if "__FONT_" in tpl:
    sys.exit("ERROR: unsubstituted font token remains")
