import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".emnv")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

OBSERVER_GRPC_SERVER_ADDR = os.environ.get(
    "OBSERVER_GRPC_SERVER_ADDR", "localhost:5053"
)

PLANNER_GRPC_SERVER_ADDR = os.environ.get("PLANNER_GRPC_SERVER_ADDR", "localhost:5051")

JAEGER_SERVER_ADDR = os.environ.get("JAEGER_SERVER_ADDR", "localhost:50053")

KAFKA_SERVER_ADDR = os.environ.get("JAEGER_SERVER_ADDR", "localhost:9094")

REDIS_SERVER_ADDR = os.environ.get("REDIS_SERVER_ADDR", "localhost:6379")

POSTGRES_URL = os.environ.get(
    "POSTGRES_URL", "postgresql://postgres:qwerty@localhost:5432/mydb"
)

TEST_POSTGRES_URL = os.environ.get(
    "TEST_POSTGRES_URL", "postgresql://postgres:qwerty@localhost:5432/mytestdb"
)

AUTH_GRPC_SERVER_ADDR = os.environ.get("AUTH_GRPC_SERVER_ADDR", "localhost:5052")

SECRET_KEY = os.environ.get("SECRET_KEY", "secret1")

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "secret2")

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

ALGORITHM = os.environ.get("ALGORITHM", "HS256")
