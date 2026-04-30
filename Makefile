PROJECT ?= .
REQUEST ?=

check-requirements:
	python shared/scripts/check_requirements.py $(PROJECT)/requirements/novel-requirements.md

refine-requirements:
	python cli/novel_lite.py refine-requirements $(PROJECT)

requirements-task:
	python cli/novel_lite.py requirements-task $(PROJECT)

route:
	python cli/novel_lite.py route $(PROJECT) "$(REQUEST)"

task:
	python cli/novel_lite.py task $(PROJECT)

doctor:
	python cli/novel_lite.py doctor $(PROJECT)
