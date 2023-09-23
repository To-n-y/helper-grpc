install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

db_up:
	poetry run python scripts/create_db.py
run:
	poetry run uvicorn api:app --reload
