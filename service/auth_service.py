from grpc import aio
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from grpc_reflection.v1alpha import reflection
from opentelemetry import trace
from opentelemetry.instrumentation.grpc import GrpcAioInstrumentorServer
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider

from protos import auth_pb2
from protos import auth_pb2_grpc
from utils import AuthInterceptor


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    async def ReadUser(self, request, context):
        print("ReadUserByToken")
        print(request.token)
        # TODO: get name, id from request.token
        return auth_pb2.ReadUserResponse(user={"id": 1, "name": "name", "role": "user"})

    async def Login(self, request, context):
        pass

    async def Check(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.SERVING
        )

    async def Watch(self, request, context):
        return health_pb2.HealthCheckResponse(
            status=health_pb2.HealthCheckResponse.UNIMPLEMENTED
        )


async def start(
        addr,
        jaeger_addr
):
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
