import os

from starlette.config import Config
from starlette.datastructures import Secret

dir_path = os.path.dirname(os.path.realpath(__file__))

root_dir = dir_path + "\\db\\"
print("ROOT", root_dir)
print("DIR", dir_path)
config = Config(f"{dir_path}\\.env")
# DATABASE_URL = f"sqlite:///{root_dir}" + config(
#     "DB_NAME", cast=str, default=os.getenv("DB_NAME", "db.sqlite")
# )
# print(DATABASE_URL)

OBSERVER_GRPC_SERVER_ADDR = config(
    "OBSERVER_GRPC_SERVER_ADDR", cast=Secret, default="secret"
)
JAEGER_GRPC_SERVER_ADDR = config(
    "JAEGER_GRPC_SERVER_ADDR", cast=Secret, default="secret"
)
