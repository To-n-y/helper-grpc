import asyncio
import sys
import os
parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent)

from config import JAEGER_GRPC_SERVER_ADDR, OBSERVER_GRPC_SERVER_ADDR
from service import observer_service

if __name__ == '__main__':
    asyncio.run(
        observer_service.start(
            addr=str(OBSERVER_GRPC_SERVER_ADDR), jaeger_addr=str(JAEGER_GRPC_SERVER_ADDR)
        )
    )