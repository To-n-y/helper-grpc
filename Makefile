CODE_FOLDERS := apps service clients db
TEST_FOLDERS := tests


.PHONY: format test lint run migration migrate update_proto db_up docker_up docker_build docker_run run_bandit

format:
	poetry run black --line-length 79 --skip-string-normalization --extend-exclude="protos" $(CODE_FOLDERS) $(TEST_FOLDERS)
	isort $(CODE_FOLDERS) $(TEST_FOLDERS)

run:
ifeq ($(x),gateway)
	poetry run uvicorn apps.api:app --reload
else
	poetry run python apps/$(x)_app.py
endif

test:
	poetry run pytest --slow -cov=service --cov-report xml

lint:
	poetry run isort $(CODE_FOLDERS) $(TEST_FOLDERS)
	poetry run flake8 $(CODE_FOLDERS) $(TEST_FOLDERS)
	poetry run black --check --line-length 79 --skip-string-normalization --extend-exclude="protos" $(CODE_FOLDERS) $(TEST_FOLDERS)

migration:
	poetry run alembic revision --autogenerate -m"$(x)"

migrate:
	poetry run alembic upgrade head

update_proto:
	poetry run python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. protos/*.proto

db_up:
	docker run --name postgres_container -d -e POSTGRES_PASSWORD=qwerty --network mynetwork postgres

docker_up:
	docker-compose -f docker/docker-compose.yml up --build

docker_build:
	docker build -t $(x)_image -f docker/Dockerfile.$(x) .

docker_run:
ifeq ($(x),gateway)
	docker run --name gateway_container -d -p 127.0.0.1:8000:8000 --env-file .env --network mynetwork gateway_image
else
	docker run --name $(x)_container -d --env-file .env --network mynetwork $(x)_image
endif

run_bandit:
	poetry run bandit -r apps/ -f csv -o out.csv