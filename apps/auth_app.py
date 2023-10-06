import sys
import os

parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent)
from service import auth_service
import asyncio
from config import AUTH_GRPC_SERVER_ADDR, JAEGER_GRPC_SERVER_ADDR

if __name__ == "__main__":
    asyncio.run(
        auth_service.start(
            addr=str(AUTH_GRPC_SERVER_ADDR), jaeger_addr=str(JAEGER_GRPC_SERVER_ADDR)
        )
    )
