import os

from starlette.config import Config
from starlette.datastructures import Secret

dir_path = os.path.dirname(os.path.realpath(__file__))

root_dir = dir_path + "\\db\\"
config = Config(f"{dir_path}\\.env")
# DATABASE_URL = f"sqlite:///{root_dir}" + config(
#     "DB_NAME", cast=str, default=os.getenv("DB_NAME", "db.sqlite")
# )
# print(DATABASE_URL)

OBSERVER_GRPC_SERVER_ADDR = config(
    "OBSERVER_GRPC_SERVER_ADDR", cast=Secret, default="secret1"
)
JAEGER_GRPC_SERVER_ADDR = config(
    "JAEGER_GRPC_SERVER_ADDR", cast=Secret, default="secret2"
)
POSTGRES_URL = config(
    "POSTGRES_URL", cast=Secret, default="secret3"
)
