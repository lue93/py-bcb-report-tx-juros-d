# Nome do interpretador Python
PYTHON=python3

.PHONY: scrapper

# Alvo principal
run: scrapper fastapi

# Executa o scrapper primeiro
scrapper:
    PYTHONPATH=. $(PYTHON) /app/json_scrapper.py

# Depois sobe o servidor FastAPI
fastapi:
	uvicorn app.main:app --reload
