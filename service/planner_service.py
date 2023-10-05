from grpc import StatusCode, aio
from grpc_health.v1 import health_pb2, health_pb2_grpc
from grpc_reflection.v1alpha import reflection
from opentelemetry import trace
from opentelemetry.instrumentation.grpc import (
    GrpcAioInstrumentorClient,
    GrpcAioInstrumentorServer,
)
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider

from models.models import User, Event, Plan, connect_db
from protos import planner_pb2, planner_pb2_grpc


class PlannerService(planner_pb2_grpc.PlannerServiceServicer):
    # all plans
    async def ReadPlans(self, request, context):
        session = connect_db()
        user = session.query(User).filter(User.id == request.user_id).first()
        print("QAZWSX")
        events = session.query(Plan).filter(Plan.user_id == user.id).all()
        print("QWERTY")
        events_response = [
            planner_pb2.Event(
                event_id=x.id,
                event_name=x.name,
                event_type=x.event_type,
            )
            for x in events
        ]

        print("ReadPlans")
        return planner_pb2.ReadUserPlanResponse(event=events_response)

    # create plan
    async def CreatePlan(self, request, context):
        session = connect_db()
        print("ER")
        user = session.query(User).filter(User.id == request.user_id).first()
        print('ioj')
        event = session.query(Event).filter(Event.name == request.event_name).first()
        new_plan = Plan(user_id=request.user_id, event_id=event.id, event_type=event.type, name=event.name)
        print("WERR")
        session.add(new_plan)
        session.commit()
        print("CreatePlan")
        plan = planner_pb2.Plan(user_name=user.username,
                                event=planner_pb2.Event(event_id=event.id, event_name=event.name,
                                                        event_type=event.type))
        return planner_pb2.CreateUserPlanResponse(plan=plan)

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
        TracerProvider(resource=Resource.create({SERVICE_NAME: "Planner"}))
    )

    grpc_server_instrumentor = GrpcAioInstrumentorServer()
    grpc_server_instrumentor.instrument()
    grpc_client_instrumentor = GrpcAioInstrumentorClient()
    grpc_client_instrumentor.instrument()

    server = aio.server()
    planner_pb2_grpc.add_PlannerServiceServicer_to_server(
        PlannerService(), server
    )
    service = PlannerService()
    health_pb2_grpc.add_HealthServicer_to_server(service, server)
    server.add_insecure_port(addr)
    SERVICE_NAMES = (
        planner_pb2.DESCRIPTOR.services_by_name["PlannerService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    print(f"PlannerService {addr}")

    await server.start()
    await server.wait_for_termination()
