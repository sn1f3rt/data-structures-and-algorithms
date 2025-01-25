env:
	uv venv

rmenv:
	rm -rf .venv

install:
	uv sync

export:
	uv export --format requirements-txt --no-hashes > requirements.txt

format:
	ruff check --select I --fix .
	ruff format .

.PHONY: env rmenv install export format
.DEFAULT_GOAL := format
