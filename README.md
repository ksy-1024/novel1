# v3.19 Requirements Pro

这版专门优化 `requirements/novel-requirements.md`，让它从“创意说明”升级为“专业创作需求书”。

## 新增能力

```text
1. 专业 novel-requirements.md 模板
2. check_requirements.py 完整性检查
3. refine-requirements 任务生成
4. requirements-task 任务生成
5. TASKS.md 增加需求检查和需求优化工作流
```

## 常用命令

```bash
make check-requirements
make refine-requirements
make requirements-task
```

## 推荐 Codex 提示

```text
读取 AGENTS.md、TASKS.md 和 shared/templates/novel-requirements.template.md。
请把 requirements/novel-requirements.md 优化成专业创作需求书。
完成后运行 make check-requirements。
```
