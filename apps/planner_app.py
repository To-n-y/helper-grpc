import asyncio
import os
import sys

parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(1, parent)
from config import JAEGER_SERVER_ADDR, PLANNER_GRPC_SERVER_ADDR
from service import planner_service

if __name__ == "__main__":
    asyncio.run(
        planner_service.start(
            addr=str(PLANNER_GRPC_SERVER_ADDR),
            jaeger_addr=str(JAEGER_SERVER_ADDR),
        )
    )
