import grpc

from config import PLANNER_GRPC_SERVER_ADDR
from protos import planner_pb2_grpc


async def grpc_planner_client():
    channel = grpc.aio.insecure_channel(str(PLANNER_GRPC_SERVER_ADDR))
    client = planner_pb2_grpc.PlannerServiceStub(channel)
    return client
