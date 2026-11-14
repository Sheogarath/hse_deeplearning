#!/usr/bin/env python3
"""Extract slide text and speaker notes from PowerPoint files using Python stdlib."""
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "lecture_text"
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
SLIDE = re.compile(r"ppt/slides/slide(\d+)\.xml$")
NOTES = re.compile(r"ppt/notesSlides/notesSlide(\d+)\.xml$")


def extract(xml):
    root = ET.fromstring(xml)
    paragraphs = []
    for p in root.findall(".//a:p", NS):
        parts = [t.text or "" for t in p.findall(".//a:t", NS)]
        line = "".join(parts).strip()
        if line:
            paragraphs.append(line)
    return paragraphs


def process(src):
    relative = src.relative_to(ROOT)
    dest = OUT / relative.with_suffix(".md")
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = "https://github.com/Sheogarath/hse_deeplearning/blob/main/" + quote(relative.as_posix(), safe="/")
    lines = [f"# {relative.name}", "", f"Source: {url}", ""]
    with zipfile.ZipFile(src) as archive:
        names = archive.namelist()
        slides = sorted(((int(m.group(1)), name) for name in names if (m := SLIDE.fullmatch(name))))
        notes = {int(m.group(1)): name for name in names if (m := NOTES.fullmatch(name))}
        for num, name in slides:
            lines.extend([f"## Slide {num}", ""])
            lines.extend(extract(archive.read(name)) or ["[No extractable text]"])
            lines.append("")
            if num in notes:
                note_text = extract(archive.read(notes[num]))
                if note_text:
                    lines.extend(["### Speaker notes", "", *note_text, ""])
    dest.write_text("\n".join(lines), encoding="utf-8")
    return relative.as_posix(), dest.relative_to(ROOT).as_posix(), len(slides)


def main():
    OUT.mkdir(exist_ok=True)
    presentations = sorted(p for p in ROOT.rglob("*.pptx") if ".git" not in p.parts and "lecture_text" not in p.parts)
    index = ["# Lecture presentations", "", "Automatically extracted slide text. Images, equations stored as images, and charts may require viewing the original PPTX.", ""]
    for src in presentations:
        try:
            original, output, count = process(src)
            index.append(f"- [{original}]({output.removeprefix('lecture_text/')}) — {count} slides")
        except Exception as exc:
            index.append(f"- {src.relative_to(ROOT)} — extraction error: {exc}")
    (OUT / "INDEX.md").write_text("\n".join(index) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
