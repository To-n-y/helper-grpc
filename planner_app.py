import asyncio

from config import JAEGER_GRPC_SERVER_ADDR, PLANNER_GRPC_SERVER_ADDR
from service import planner_service

if __name__ == '__main__':
    asyncio.run(
        planner_service.start(
            addr=str(PLANNER_GRPC_SERVER_ADDR), jaeger_addr=str(JAEGER_GRPC_SERVER_ADDR)
        )
    )
