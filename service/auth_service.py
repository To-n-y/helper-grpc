import datetime
import uuid

from grpc import aio
from grpc_health.v1 import health_pb2, health_pb2_grpc
from grpc_reflection.v1alpha import reflection
from opentelemetry import trace
from opentelemetry.instrumentation.grpc import GrpcAioInstrumentorServer
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider

from models.models import AuthToken, User, connect_db
from protos import auth_pb2, auth_pb2_grpc
from utils import AuthInterceptor, get_hash_password


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    async def ReadUser(self, request, context):
        session = connect_db()
        entered_token = (
            session.query(AuthToken)
            .filter(AuthToken.token == request.token)
            .first()
        )

        if entered_token is None:
            return auth_pb2.ReadUserResponse(
                user={"id": 1, "name": "no such token", "role": "user"}
            )
        # TODO: inspiration time
        # if datetime.datetime.utcnow > entered_token.created_at:
        #    pass
        cur_user = session.query(User).get(entered_token.user_id)
        print("ReadUserByToken")
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
        if cur_user.password != get_hash_password(request.password):
            return auth_pb2.LoginResponse(token='incorrect password')
        new_token = AuthToken(user_id=cur_user.id, token=uuid.uuid4().hex)
        session.add(new_token)
        session.commit()
        print("Create new token")
        return auth_pb2.LoginResponse(token=new_token.token)

    async def CreateUser(self, request, context):
        session = connect_db()
        hashed_password = get_hash_password(request.password)
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
