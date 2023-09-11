import grpc

from protos import observer_pb2_grpc
from settings import OBSERVER_GRPC_SERVER_ADDR


async def grpc_observer_client():
    channel = grpc.aio.insecure_channel(OBSERVER_GRPC_SERVER_ADDR)
    client = observer_pb2_grpc.ObserverServiceStub(channel)
    return client
