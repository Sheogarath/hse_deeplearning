#!/usr/bin/env python3
"""Inventory and summarize all course files, with notebook cell contents."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
out=root/"COURSE_CODE_REVIEW"
out.mkdir(exist_ok=True)
skip={".git","lecture_text","lecture_visuals","lecture_image_data","lecture_diagrams","lecture_diagram_maps","COURSE_CODE_REVIEW"}
files=sorted(p for p in root.rglob("*") if p.is_file() and not any(part in skip for part in p.relative_to(root).parts))
lines=["# Repository inventory","",f"Files: {len(files)}",""]
for p in files:
    rel=p.relative_to(root)
    lines.append(f"- `{rel}` ({p.stat().st_size} bytes)")
(out/"INVENTORY.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
notebooks=["# Notebook contents",""]
texts=["# Other text files",""]
for p in files:
    rel=p.relative_to(root)
    if p.suffix==".ipynb":
        try:
            data=json.loads(p.read_text(encoding="utf-8"))
            notebooks.extend([f"## {rel}",""])
            for i,c in enumerate(data.get("cells",[]),1):
                source="".join(c.get("source",[]))
                # Remove embedded image base64 data URIs and notebook output blobs
                import re
                source=re.sub(r"data:image/[^;]+;base64,[A-Za-z0-9+/=]+","[embedded image]",source)
                notebooks.extend([f"### Cell {i}: {c.get('cell_type')}","",source[:20000],""])
        except Exception as e:notebooks.append(f"ERROR {rel}: {e}")
    elif p.suffix.lower() in {".py",".md",".txt",".yml",".yaml",".toml",".json",".csv",".sh"} and not rel.as_posix().startswith(".github/"):
        try:
            s=p.read_text(encoding="utf-8")
            if len(s)>300000:s=s[:300000]+"\n[TRUNCATED]"
            texts.extend([f"## {rel}","",s,""])
        except Exception:pass
(out/"NOTEBOOKS.md").write_text("\n".join(notebooks),encoding="utf-8")
(out/"TEXT_FILES.md").write_text("\n".join(texts),encoding="utf-8")
