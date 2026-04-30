#!/usr/bin/env python3
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
"## 0. 项目基本信息","## 1. 题材与定位","## 2. 一句话卖点","## 3. 核心爽点设计",
"## 4. 主角设计","## 5. 外挂 / 金手指设计","## 6. 世界观与修行体系","## 7. 人物关系设计",
"## 8. 文风要求","## 9. 大纲生成要求","## 10. 正文生成要求","## 11. 审核标准",
"## 12. 第一卷目标","## 13. 禁止事项总表"
]
REQUIRED_KEYWORDS = [
"目标字数","核心读者期待","长期爽点","单章爽点","主角核心驱动力","外挂限制","外挂阶段",
"长篇扩展方向","暧昧/擦边原则","章节级大纲要求","Chapter Commit","第一卷目标"
]

def main():
    if len(sys.argv) < 2:
        print("Usage: check_requirements.py <requirements.md>")
        sys.exit(2)
    path = Path(sys.argv[1])
    if not path.exists():
        print("MISS requirements file:", path)
        sys.exit(1)
    text = path.read_text(encoding="utf-8")
    missing_sections = [s for s in REQUIRED_SECTIONS if s not in text]
    missing_keywords = [k for k in REQUIRED_KEYWORDS if k not in text]
    print("# Requirements Check Report")
    if not missing_sections and not missing_keywords:
        print("OK: requirements are complete enough for setting and outline generation.")
        sys.exit(0)
    if missing_sections:
        print("\nMissing sections:")
        for s in missing_sections:
            print("-", s)
    if missing_keywords:
        print("\nMissing key details:")
        for k in missing_keywords:
            print("-", k)
    print("\nSuggestion: run refine-requirements workflow before generating setting/outline.")
    sys.exit(1)

if __name__ == "__main__":
    main()
