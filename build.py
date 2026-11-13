# -*- coding: utf-8 -*-
"""把题库 JSON 内联进单文件网页，输出 index.html（唯一产物，可直接双击/部署）。"""
import json, pathlib, re

ROOT = pathlib.Path(r"D:\workspace\proj_006_longmarch_quiz")
data = json.loads((ROOT / "src" / "questions.json").read_text(encoding="utf-8"))
tpl = (ROOT / "src" / "template.html").read_text(encoding="utf-8")

payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
assert "</script" not in payload.lower()
html = tpl.replace("/*__DATA__*/", payload)

out = ROOT / "index.html"
out.write_text(html, encoding="utf-8")

n = len(data["single"]) + len(data["judge"])
print(f"题目 {n} 道；输出 index.html {out.stat().st_size/1024:.1f} KB")
print("答案缺失：", [q["id"] for q in data["judge"] if q["answer"] is None])
