import grpc
from fastapi import Request
from config import AUTH_GRPC_SERVER_ADDR
from protos import auth_pb2_grpc
from utils import KeyAuthClientInterceptor


async def grpc_auth_client(request: Request):
    print("create auth_client")
    auth = request.headers.get("rpc-auth-key")
    print(f"auth {auth}")
    channel = grpc.aio.insecure_channel(
        str(AUTH_GRPC_SERVER_ADDR),
        interceptors=[
            KeyAuthClientInterceptor(auth),
        ],
    )
    client = auth_pb2_grpc.AuthServiceStub(channel)
    return client
