import json
import os

import aioredis
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
from sqlalchemy.orm import Session

from db.base import engine
from db.events import EventsRepo
from db.models import Event
from protos import observer_pb2, observer_pb2_grpc

redis = None


class ObserverService(observer_pb2_grpc.ObserverServiceServicer):
    # all events
    async def ListEvent(self, request, context):
        with Session(bind=engine.connect()) as session:
            events = EventsRepo(session).get_event_list()
            events_list = [
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
        return observer_pb2.ListEventResponse(events=events_list)

    # single event
    async def ReadEventById(self, request, context):
        if os.getenv('IN_CONTAINER') is not None:
            cache = await redis.get(str(request.id))
            if cache is not None:
                print("GET FROM CACHE")
                cache_event = observer_pb2.Event(
                    **(json.loads(cache.decode('utf-8')))
                )
                return observer_pb2.ReadEventResponse(event=cache_event)
        # session = connect_db()
        with Session(bind=engine.connect()) as session:
            event = EventsRepo(session).get_event(request.id)
            event_response = observer_pb2.Event(
                id=event.id,
                name=event.name,
                type=event.type,
                age_restrictions=event.age_restrictions,
                day=event.day,
            )
            print("GetEventById")
        if os.getenv('IN_CONTAINER') is not None:
            await redis.set(
                str(request.id),
                json.dumps(
                    {
                        "id": event.id,
                        "name": event.name,
                        "type": event.type,
                        "age_restrictions": event.age_restrictions,
                        "day": event.day,
                    }
                ),
                expire=3600,
            )
            print('CACHED')
        return observer_pb2.ReadEventResponse(event=event_response)

    # create event
    async def CreateEvent(self, request, context):
        if not (0 <= request.day <= 7):
            context.set_code(StatusCode.INVALID_ARGUMENT)
            context.set_details("0 <= day <= 7")
            return observer_pb2.CreateEventResponse()
        event = Event(
            name=request.name,
            type=request.type,
            age_restrictions=request.age_restrictions,
            day=request.day,
        )
        # session = connect_db()
        with Session(bind=engine.connect()) as session:
            created_event = EventsRepo(session).create_event(event=event)
            new_event = observer_pb2.Event(
                id=created_event.id,
                name=created_event.name,
                type=created_event.type,
                age_restrictions=created_event.age_restrictions,
                day=created_event.day,
            )
        print("CreateEvent")
        return observer_pb2.CreateEventResponse(event=new_event)

    # update event
    async def UpdateEventById(self, request, context):
        # session = connect_db()
        event = Event(
            name=request.name,
            type=request.type,
            age_restrictions=request.age_restrictions,
            day=request.day,
        )
        with Session(bind=engine.connect()) as session:
            EventsRepo(session).update_event(
                event_id=request.id, new_event=event
            )
        # event = session.query(Event).filter(Event.id == request.id).first()

        if os.getenv('IN_CONTAINER') is not None:
            exist_cache = await redis.get(str(request.id))
            if exist_cache is not None:
                await redis.set(
                    str(request.id),
                    json.dumps(
                        {
                            "id": event.id,
                            "name": event.name,
                            "type": event.type,
                            "age_restrictions": event.age_restrictions,
                            "day": event.day,
                        }
                    ),
                    expire=3600,
                )
                print('UPDATE CACHE')
        print("UpdateEvent")
        upd_event = observer_pb2.Event(
            id=request.id,
            name=request.name,
            type=request.type,
            age_restrictions=request.age_restrictions,
            day=request.day,
        )
        return observer_pb2.UpdateEventResponse(event=upd_event)

    # delete event
    async def DeleteEventById(self, request, context):
        # session = connect_db()
        with Session(bind=engine.connect()) as session:
            EventsRepo(session).delete_event(request.id)

        if os.getenv('IN_CONTAINER') is not None:
            exist_cache = await redis.get(str(request.id))
            if exist_cache is not None:
                await redis.delete(request.id)
                print("DELETE FROM CACHE")
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
    if os.getenv('IN_CONTAINER') is not None:
        global redis
        redis = await aioredis.create_redis(address=('localhost', 6379))
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
