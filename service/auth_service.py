from grpc import aio
from grpc_health.v1 import health_pb2, health_pb2_grpc
from grpc_reflection.v1alpha import reflection
from opentelemetry import trace
from opentelemetry.instrumentation.grpc import GrpcAioInstrumentorServer
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider

from models.models import User, connect_db
from protos import auth_pb2, auth_pb2_grpc
from utils.interceptors import AuthInterceptor
from utils.jwt_utils import (
    create_access_token,
    get_current_user_email,
    get_hashed_password,
    verify_password,
)


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    async def ReadUser(self, request, context):
        session = connect_db()

        user_email = get_current_user_email(request.token)
        if user_email is None:
            return auth_pb2.ReadUserResponse(
                user={
                    "id": 1,
                    "name": "inspired",
                    "role": "user",
                }
            )
        cur_user = session.query(User).filter(User.email == user_email).first()
        print("ReadUserByToken", cur_user.id)
        return auth_pb2.ReadUserResponse(
            user={
                "id": cur_user.id,
                "name": cur_user.username,
                "role": cur_user.role,
            }
        )

    async def Login(self, request, context):
        session = connect_db()

        cur_user = (
            session.query(User).filter(User.username == request.name).first()
        )

        if cur_user is None:
            return auth_pb2.LoginResponse(token='does not exist')
        print("FIR")
        print(request.password, cur_user.password)
        if not verify_password(request.password, cur_user.password):
            return auth_pb2.LoginResponse(token='incorrect password')
        print("SEC")
        print("Create new token")
        print(create_access_token(cur_user.email))
        return auth_pb2.LoginResponse(
            token=create_access_token(cur_user.email)
        )

    async def CreateUser(self, request, context):
        session = connect_db()
        hashed_password = get_hashed_password(request.password)
        new_user = User(
            username=request.name,
            email=request.email,
            gender=request.gender,
            password=hashed_password,
        )
        session.add(new_user)
        session.commit()
        print("Create new user")
        return auth_pb2.CreateUserResponse(
            user={
                "id": new_user.id,
                "name": new_user.username,
                "role": new_user.role,
            }
        )

    async def Check(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.SERVING
        )

    async def Watch(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.UNIMPLEMENTED
        )


async def start(addr, jaeger_addr):
    trace.set_tracer_provider(
        TracerProvider(resource=Resource.create({SERVICE_NAME: "Auth"}))
    )
    grpc_server_instrumentor = GrpcAioInstrumentorServer()
    grpc_server_instrumentor.instrument()

    server = aio.server(
        interceptors=[
            AuthInterceptor(),
        ]
    )
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    SERVICE_NAMES = (
        auth_pb2.DESCRIPTOR.services_by_name["AuthService"].full_name,
        reflection.SERVICE_NAME,
    )
    service = AuthService()
    health_pb2_grpc.add_HealthServicer_to_server(service, server)
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port(addr)
    print(f"AuthService {addr}")
    await server.start()
    await server.wait_for_termination()


# TODO: checks and try-excepts
