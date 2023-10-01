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
	poetry run isort service clients utils api.py
	poetry run flake8 service clients utils api.py
	poetry run black --check --line-length 79 --skip-string-normalization --extend-exclude="protos" service models clients utils api.py
	poetry run mypy --install-types
	poetry run mypy --pretty --config-file pyproject.toml .

test:
	poetry run pytest

update_proto:
	python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. protos/*.proto

docker_up_postgres:
	docker run --name postgres_container -d -e POSTGRES_PASSWORD=qwerty --network mynetwork postgres

docker_build_gateway:
	docker build -t gateway_image -f docker/Dockerfile.gateway .

docker_run_gateway:
	docker run --name gateway_container -d -p 127.0.0.1:8000:8000 --env-file .env --network mynetwork gateway_image

docker_build_observer:
	docker build -t observer_image -f docker/Dockerfile.observer .

docker_run_observer:
	docker run --name observer_container -d -p 127.0.0.1:8888:8888 --env-file .env --network mynetwork observer_image

docker_build_auth:
	docker build -t auth_image -f docker/Dockerfile.auth .

docker_run_auth:
	docker run --name auth_container -d -p 127.0.0.1:5053:5053 --env-file .env --network mynetwork auth_image

docker_rm:
	docker container prune