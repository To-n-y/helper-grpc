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

from models.models import Event, connect_db
from protos import observer_pb2, observer_pb2_grpc


class ObserverService(observer_pb2_grpc.ObserverServiceServicer):
    # all events
    async def ListEvent(self, request, context):
        session = connect_db()
        events = session.query(Event).all()
        events_response = [
            observer_pb2.Event(
                id=x.id,
                name=x.name,
                type=x.type,
                age_restrictions=x.age_restrictions,
                day=x.day,
            )
            for x in events
        ]
        print("GetEventList")
        return observer_pb2.ListEventResponse(Events=events_response)

    # single event
    async def ReadEventById(self, request, context):
        session = connect_db()
        event = session.query(Event).filter(Event.id == request.id).first()
        event_response = observer_pb2.Event(
            id=event.id,
            name=event.name,
            type=event.type,
            age_restrictions=event.age_restrictions,
            day=event.day,
        )
        print("GetEventById")
        return observer_pb2.ReadEventResponse(Event=event_response)

    # create event
    async def CreateEvent(self, request, context):
        if not (0 <= request.day <= 7):
            context.set_code(StatusCode.INVALID_ARGUMENT)
            context.set_details('0<= day <=7')
            return observer_pb2.CreateEventResponse()
        event = Event(
            name=request.name,
            type=request.type,
            age_restrictions=request.age_restrictions,
            day=request.day,
        )
        session = connect_db()
        session.add(event)
        session.commit()
        print("CreateEvent")
        new_event = observer_pb2.Event(
            id=event.id,
            name=request.name,
            type=request.type,
            age_restrictions=request.age_restrictions,
            day=request.day,
        )
        return observer_pb2.CreateEventResponse(Event=new_event)

    # update event
    async def UpdateEventById(self, request, context):
        session = connect_db()
        event = session.query(Event).filter(Event.id == request.id).first()
        if event is not None:
            event.name = request.name
            event.type = request.type
            event.age_restrictions = request.age_restrictions
            event.day = request.day
            session.add(event)
            session.commit()
        print("UpdateEvent")
        upd_event = observer_pb2.Event(
            id=request.id,
            name=request.name,
            type=request.type,
            age_restrictions=request.age_restrictions,
            day=request.day,
        )
        return observer_pb2.UpdateEventResponse(Event=upd_event)

    # delete event
    async def DeleteEventById(self, request, context):
        session = connect_db()
        event = session.query(Event).filter(Event.id == request.id).first()
        if event is not None:
            session.delete(event)
            session.commit()
        print("DeleteEventById")
        return observer_pb2.DeleteEventResponse(success=True)

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
        TracerProvider(resource=Resource.create({SERVICE_NAME: "Observer"}))
    )

    grpc_server_instrumentor = GrpcAioInstrumentorServer()
    grpc_server_instrumentor.instrument()
    grpc_client_instrumentor = GrpcAioInstrumentorClient()
    grpc_client_instrumentor.instrument()

    server = aio.server()
    observer_pb2_grpc.add_ObserverServiceServicer_to_server(
        ObserverService(), server
    )
    service = ObserverService()
    health_pb2_grpc.add_HealthServicer_to_server(service, server)
    server.add_insecure_port(addr)
    SERVICE_NAMES = (
        observer_pb2.DESCRIPTOR.services_by_name["ObserverService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    print(f"ObserverService {addr}")

    await server.start()
    await server.wait_for_termination()
