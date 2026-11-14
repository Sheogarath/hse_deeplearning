#!/usr/bin/env python3
"""Build compact per-slide diagram maps from PowerPoint native shapes.

Outputs spatial reading order, labelled objects, and connector endpoint candidates.
Endpoint associations are heuristic; they are explicitly marked as such.
"""
from pathlib import Path
import zipfile, re, math, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"lecture_diagram_maps"
NS={"p":"http://schemas.openxmlformats.org/presentationml/2006/main","a":"http://schemas.openxmlformats.org/drawingml/2006/main"}
SLIDE=re.compile(r"ppt/slides/slide(\d+)\.xml$")
def pos(e):
    t=e.find(".//a:xfrm",NS)
    if t is None:return None
    o=t.find("a:off",NS);s=t.find("a:ext",NS)
    if o is None or s is None:return None
    return tuple(int(x) for x in (o.get("x","0"),o.get("y","0"),s.get("cx","0"),s.get("cy","0")))
def label(e):
    return " ".join((x.text or "").strip() for x in e.findall(".//a:t",NS)).strip()
def midpoint(p):return (p[0]+p[2]/2,p[1]+p[3]/2)
def process(pptx):
    rel=pptx.relative_to(ROOT);out=OUT/rel.with_suffix(".md")
    out.parent.mkdir(parents=True,exist_ok=True)
    lines=[f"# {rel.as_posix()}","","Automatically inferred reading order and possible connections. **Connections are heuristic**, not verified semantic claims.",""]
    with zipfile.ZipFile(pptx) as z:
        slides=sorted((int(m.group(1)),name) for name in z.namelist() if (m:=SLIDE.fullmatch(name)))
        for number,name in slides:
            root=ET.fromstring(z.read(name));tree=root.find(".//p:spTree",NS)
            lines.extend([f"## Slide {number}",""])
            if tree is None:continue
            shapes=[];links=[];pictures=0
            for e in tree.iter():
                tag=e.tag.rsplit("}",1)[-1]
                if tag=="pic":pictures+=1
                if tag not in ("sp","cxnSp"):continue
                p=pos(e)
                if not p:continue
                if tag=="cxnSp":links.append(p)
                elif label(e):shapes.append((p,label(e).replace("\n"," ")[:160]))
            shapes.sort(key=lambda x:(round(x[0][1]/300000),x[0][0]))
            lines.append(f"Native text objects: {len(shapes)}; connectors: {len(links)}; embedded pictures: {pictures}")
            lines.append("")
            for p,s in shapes[:100]:
                lines.append(f"- ({round(p[0]/914400,1)}in, {round(p[1]/914400,1)}in) {s}")
            if len(shapes)>100:lines.append(f"- ... {len(shapes)-100} more labelled objects")
            if links and shapes:
                lines.extend(["","### Possible connector endpoints (spatial inference)",""])
                for p in links[:80]:
                    a=(p[0],p[1]);b=(p[0]+p[2],p[1]+p[3])
                    near=lambda point:min(shapes,key=lambda s:math.dist(point,midpoint(s[0])))[1]
                    start,end=near(a),near(b)
                    if start!=end:lines.append(f"- {start[:70]} -> {end[:70]} (unverified)")
            lines.append("")
    out.write_text("\n".join(lines),encoding="utf-8")
    return rel,out.relative_to(ROOT),len(slides)
def main():
    OUT.mkdir(exist_ok=True)
    index=["# Spatial diagram maps","","Heuristic maps generated from editable PowerPoint shapes. Raster graphics still require direct visual inspection.",""]
    for p in sorted(ROOT.rglob("*.pptx")):
        if ".git" in p.parts:continue
        try:
            rel,out,n=process(p)
            index.append(f"- [{rel}]({out.relative_to(OUT) if out.is_absolute() else out.relative_to(Path('lecture_diagram_maps'))}): {n} slides")
        except Exception as e:index.append(f"- {p.relative_to(ROOT)}: ERROR {e}")
    (OUT/"INDEX.md").write_text("\n".join(index)+"\n",encoding="utf-8")
if __name__=="__main__":main()
