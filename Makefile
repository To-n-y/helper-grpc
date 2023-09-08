install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

db_up:
	python scripts/create_db.py
run:
	uvicorn api:app --reload
