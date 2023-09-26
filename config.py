import os

from starlette.config import Config
from starlette.datastructures import Secret

dir_path = os.path.dirname(os.path.realpath(__file__))

root_dir = dir_path + "\\db\\"
config = Config(f"{dir_path}\\.env")

OBSERVER_GRPC_SERVER_ADDR = config(
    "OBSERVER_GRPC_SERVER_ADDR", cast=Secret, default="secret1"
)
JAEGER_GRPC_SERVER_ADDR = config(
    "JAEGER_GRPC_SERVER_ADDR", cast=Secret, default="secret2"
)
POSTGRES_URL = config(
    "POSTGRES_URL", cast=Secret, default="secret3"
)
AUTH_GRPC_SERVER_ADDR = config(
    "AUTH_GRPC_SERVER_ADDR", cast=Secret, default="secret4"
)
SECRET_KEY = config(
    "SECRET_KEY", cast=Secret, default="secret5"
)
