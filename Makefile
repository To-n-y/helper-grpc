run:
	poetry run uvicorn api:app --reload

migrate:
	poetry run alembic upgrade head

lint:
	poetry run isort .
	poetry run flake8 service clients api.py
	poetry run mypy --install-types
	poetry run mypy --explicit-package-bases clients api.py
	poetry run black --check --line-length 79 --skip-string-normalization --extend-exclude="protos" .

test:
	poetry run pytest