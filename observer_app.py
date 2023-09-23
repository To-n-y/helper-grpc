import asyncio

from config import JAEGER_GRPC_SERVER_ADDR, OBSERVER_GRPC_SERVER_ADDR
from service import observer_service

if __name__ == '__main__':
    asyncio.run(
        observer_service.start(
            addr=OBSERVER_GRPC_SERVER_ADDR, jaeger_addr=JAEGER_GRPC_SERVER_ADDR
        )
    )