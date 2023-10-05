.PHONY: dev
dev:
	poetry run streamlit run streamlit_app.py

requirements.txt: pyproject.toml
	poetry export -f requirements.txt --output requirements.txt
