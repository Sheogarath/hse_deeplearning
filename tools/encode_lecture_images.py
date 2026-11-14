#!/usr/bin/env python3
"""Encode existing lecture contact sheets as text for GitHub text-only readers."""
from pathlib import Path
import base64
root=Path(__file__).resolve().parents[1]
source=root/"lecture_visuals"
out=root/"lecture_image_data"
index=["# Encoded lecture slide contact sheets","","Base64 JPEG files mirror the contact sheets for text-only GitHub API clients.",""]
for f in sorted(source.rglob("contact_*.jpg")):
    rel=f.relative_to(source)
    dest=out/rel.with_suffix(".b64")
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(base64.b64encode(f.read_bytes()).decode("ascii"),encoding="ascii")
    index.append(f"- [{rel}]({rel.with_suffix('.b64').as_posix()})")
out.mkdir(exist_ok=True)
(out/"INDEX.md").write_text("\n".join(index)+"\n",encoding="utf-8")
