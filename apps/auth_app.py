import os
import sys

parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(1, parent)
print("PATH", sys.path, os.getcwd())
import asyncio

from config import AUTH_GRPC_SERVER_ADDR, JAEGER_GRPC_SERVER_ADDR
from service import auth_service

if __name__ == "__main__":
    asyncio.run(
        auth_service.start(
            addr=str(AUTH_GRPC_SERVER_ADDR),
            jaeger_addr=str(JAEGER_GRPC_SERVER_ADDR),
        )
    )
