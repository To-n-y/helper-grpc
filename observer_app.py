import asyncio
from service import observer_service
from config import OBSERVER_GRPC_SERVER_ADDR, JAEGER_GRPC_SERVER_ADDR

if __name__ == '__main__':
    asyncio.run(observer_service.start(addr=OBSERVER_GRPC_SERVER_ADDR, jaeger_addr=JAEGER_GRPC_SERVER_ADDR))
