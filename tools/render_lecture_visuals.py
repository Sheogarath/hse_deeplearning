#!/usr/bin/env python3
"""Render PPTX slides and extract text visible in images with OCR.

Creates per-slide OCR transcripts and compact visual contact sheets.
Original PowerPoint files remain unchanged.
"""
from pathlib import Path
import subprocess
import tempfile
import re
import xml.etree.ElementTree as ET
import zipfile
import shutil
from urllib.parse import quote
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "lecture_visuals"
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}

def run(args):
    return subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def extract(pptx):
    rel = pptx.relative_to(ROOT)
    target = OUT / rel.with_suffix("")
    target.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temp:
        temp = Path(temp)
        run(["libreoffice", "-env:UserInstallation=file:///tmp/lo_lecture_visual", "--headless", "--convert-to", "pdf", "--outdir", str(temp), str(pptx)])
        pdf = temp / (pptx.stem + ".pdf")
        if not pdf.exists():
            raise RuntimeError("LibreOffice did not produce PDF")
        run(["pdftoppm", "-f", "1", "-l", "1000", "-r", "95", "-png", str(pdf), str(temp / "slide")])
        pngs = sorted(temp.glob("slide-*.png"))
        transcript = [f"# Visual review: {rel.as_posix()}", "", "OCR of fully rendered slides; also includes image-only labels. OCR may contain mistakes.", ""]
        thumbs = []
        for n, png in enumerate(pngs, 1):
            txt = run(["tesseract", str(png), "stdout", "-l", "rus+eng"]).stdout.strip()
            transcript += [f"## Slide {n}", "", txt or "[No text detected in rendered slide]", ""]
            with Image.open(png) as original:
                im = original.convert("RGB")
                im.thumbnail((650, 400))
                tile = Image.new("RGB", (680, 430), "white")
                tile.paste(im, ((680-im.width)//2, 8))
                ImageDraw.Draw(tile).text((12, 407), f"Slide {n}", fill="black")
                thumbs.append(tile)
        for offset in range(0, len(thumbs), 12):
            batch = thumbs[offset:offset+12]
            sheet = Image.new("RGB", (680*3, 430*4), "#dddddd")
            for j, im in enumerate(batch):
                sheet.paste(im, ((j%3)*680, (j//3)*430))
            sheet.save(target / f"contact_{offset//12+1:02d}.jpg", quality=70, optimize=True)
        (target / "OCR.md").write_text("\n".join(transcript), encoding="utf-8")
        return len(pngs), len(thumbs)

def main():
    OUT.mkdir(exist_ok=True)
    index = ["# Visual lecture index", "", "Rendered slide contact sheets and OCR of text embedded in diagrams, screenshots and pictures.", ""]
    for pptx in sorted(ROOT.rglob("*.pptx")):
        if ".git" in pptx.parts:
            continue
        try:
            count, _ = extract(pptx)
            rel = pptx.relative_to(ROOT)
            folder = rel.with_suffix("").as_posix()
            index.append(f"- [{rel.as_posix()}]({folder}/OCR.md): {count} rendered slides; contact sheets in adjacent folder")
        except Exception as exc:
            index.append(f"- {pptx.relative_to(ROOT)}: ERROR {exc}")
    (OUT / "INDEX.md").write_text("\n".join(index)+"\n", encoding="utf-8")

if __name__ == "__main__":
    main()
