#!/usr/bin/env python3
import argparse
from pathlib import Path

def read(path, default=""):
    return path.read_text(encoding="utf-8") if path.exists() else default

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def refine_requirements(root):
    prompt = """# Codex Task: Refine Novel Requirements

## Read
- AGENTS.md
- TASKS.md
- requirements/novel-requirements.md
- shared/templates/novel-requirements.template.md

## Goal
Rewrite `requirements/novel-requirements.md` into a professional creative requirements document.

## Must Include
1. 项目基本信息
2. 题材与定位
3. 一句话卖点
4. 核心爽点设计
5. 主角设计
6. 外挂 / 金手指设计
7. 世界观与修行体系
8. 人物关系设计
9. 文风要求
10. 大纲生成要求
11. 正文生成要求
12. 审核标准
13. 第一卷目标
14. 禁止事项总表

## Done
Run:
```bash
make check-requirements
```
"""
    out = root / ".webnovel" / "reports" / "refine-requirements-task.md"
    write(out, prompt)
    print(out)

def route(root, request):
    out = root / ".codex" / "TASK.md"
    if any(k in request for k in ["优化", "完善", "整理", "需求"]):
        body = "# Current Codex Task\n\n## Matched Intent\nrefine_requirements\n\n```bash\nmake refine-requirements\nmake check-requirements\n```\n"
    else:
        body = "# Current Codex Task\n\n## Matched Intent\ncheck_requirements\n\n```bash\nmake check-requirements\n```\n"
    write(out, body)
    print(out)

def show_task(root):
    print(read(root / ".codex" / "TASK.md"))

def doctor(root):
    files = ["AGENTS.md","TASKS.md","requirements/novel-requirements.md","shared/templates/novel-requirements.template.md","shared/scripts/check_requirements.py"]
    ok = True
    for f in files:
        exists = (root / f).exists()
        print(("OK   " if exists else "MISS ") + f)
        ok = ok and exists
    raise SystemExit(0 if ok else 1)

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    for c in ["refine-requirements","requirements-task","doctor","task"]:
        a = sub.add_parser(c); a.add_argument("project")
    a = sub.add_parser("route"); a.add_argument("project"); a.add_argument("request")
    args = p.parse_args()
    root = Path(args.project)
    if args.cmd in ["refine-requirements", "requirements-task"]:
        refine_requirements(root)
    elif args.cmd == "route":
        route(root, args.request)
    elif args.cmd == "task":
        show_task(root)
    elif args.cmd == "doctor":
        doctor(root)

if __name__ == "__main__":
    main()
