.PHONY: dev
dev:
	poetry run uvicorn app.main:app --reload

.PHONY: build
build:
	docker compose build

requirements.txt: pyproject.toml
	poetry export -f requirements.txt --output requirements.txt
