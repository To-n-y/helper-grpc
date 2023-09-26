run_gateway:
	poetry run uvicorn api:app --reload

run_observer:
	python observer_app.py

run_auth:
	python auth_app.py

make_migrate:
	poetry run alembic revision --autogenerate

migrate_head:
	poetry run alembic upgrade head

lint:
	poetry run isort service clients api.py
	poetry run flake8 service clients api.py
	poetry run black --check --line-length 79 --skip-string-normalization --extend-exclude="protos" service models clients api.py
	poetry run mypy --install-types
	poetry run mypy --pretty --config-file pyproject.toml .

test:
	poetry run pytest

update_proto:
	python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. protos/*.proto
