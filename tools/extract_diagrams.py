#!/usr/bin/env python3
"""Describe native PowerPoint drawing geometry and relationships as searchable text.

This complements rendered contact sheets and OCR. It does not claim to interpret
raster pictures or guarantee semantic understanding of diagrams.
"""
from pathlib import Path
import re, zipfile, xml.etree.ElementTree as ET
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"lecture_diagrams"
NS={"p":"http://schemas.openxmlformats.org/presentationml/2006/main",
    "a":"http://schemas.openxmlformats.org/drawingml/2006/main"}
SLIDE=re.compile(r"ppt/slides/slide(\d+)\.xml$")
def attr(node, path, name, default=""):
    child=node.find(path,NS)
    return child.get(name,default) if child is not None else default
def desc(shape):
    text=" ".join((x.text or "") for x in shape.findall(".//a:t",NS)).strip()
    xfrm=shape.find(".//a:xfrm",NS)
    x=y=w=h=""
    if xfrm is not None:
        off=xfrm.find("a:off",NS);ext=xfrm.find("a:ext",NS)
        if off is not None:x,y=off.get("x",""),off.get("y","")
        if ext is not None:w,h=ext.get("cx",""),ext.get("cy","")
    tag=shape.tag.rsplit("}",1)[-1]
    kind=attr(shape,".//a:prstGeom","prst")
    name=attr(shape,".//p:cNvPr","name")
    rot=xfrm.get("rot","") if xfrm is not None else ""
    return f"- {tag} {name!r} type={kind or 'custom'} pos=({x},{y}) size=({w},{h}) rotation={rot} text={text[:350]!r}"
def main():
    OUT.mkdir(exist_ok=True)
    index=["# Native PowerPoint diagram structure","","Coordinates are EMUs. Shapes and connectors are recorded in drawing order. This is structural evidence, not a substitute for inspecting the rendered slide.",""]
    for src in sorted(ROOT.rglob("*.pptx")):
        if ".git" in src.parts:continue
        rel=src.relative_to(ROOT); dest=OUT/rel.with_suffix(".md")
        dest.parent.mkdir(parents=True,exist_ok=True)
        lines=[f"# {rel.as_posix()}","","Native shapes, connectors and images in the original slide XML.",""]
        try:
            with zipfile.ZipFile(src) as z:
                slides=sorted((int(m.group(1)),n) for n in z.namelist() if (m:=SLIDE.fullmatch(n)))
                for number,name in slides:
                    root=ET.fromstring(z.read(name))
                    shapes=root.find(".//p:spTree",NS)
                    lines.extend([f"## Slide {number}",""])
                    if shapes is None:continue
                    for el in shapes:
                        kind=el.tag.rsplit("}",1)[-1]
                        if kind in ("sp","cxnSp","pic","graphicFrame","grpSp"):
                            lines.append(desc(el))
                    lines.append("")
            dest.write_text("\n".join(lines),encoding="utf-8")
            index.append(f"- [{rel.as_posix()}]({rel.with_suffix('.md').as_posix()})")
        except Exception as exc:index.append(f"- {rel}: ERROR {exc}")
    (OUT/"INDEX.md").write_text("\n".join(index)+"\n",encoding="utf-8")
if __name__=="__main__":main()
