import os
import sys
import typing as t

parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(1, parent)

from aiokafka import AIOKafkaProducer
from fastapi import Body, Depends, FastAPI, HTTPException, Security, status
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKeyHeader
from google.protobuf.json_format import MessageToDict
from grpc.aio import AioRpcError
from prometheus_fastapi_instrumentator import Instrumentator
from sqlalchemy.orm import Session

from clients.auth_client import grpc_auth_client
from clients.observer_client import grpc_observer_client
from clients.planner_client import grpc_planner_client
from db.base import connect_db
from forms import UserCreateForm, UserLoginForm
from protos import auth_pb2, observer_pb2, planner_pb2

api_key_header = APIKeyHeader(name="rpc-auth-key")

app = FastAPI()


async def send_one(key, value):
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9094'
    )  # TODO config(URL)
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait(
            topic="my_topic", key=str(key).encode(), value=str(value).encode()
        )  # TODO config(topic)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()


@app.get("/")
async def ping():
    return {"message": f"Hello, {os.getenv('MY_BACKEND_NAME')}"}


@app.get("/event")
async def get_events_list(
    client: t.Any = Depends(grpc_observer_client),
    session: Session = Depends(connect_db),
) -> JSONResponse:
    try:
        events = await client.ListEvent(observer_pb2.ListEventRequest())
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(events))


@app.get("/event/{id:int}")
async def get_event(
    id: int,
    client: t.Any = Depends(grpc_observer_client),
) -> JSONResponse:
    try:
        event = await client.ReadEventById(
            observer_pb2.ReadEventByIdRequest(id=id)
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(event))


@app.post("/event", status_code=status.HTTP_201_CREATED)
async def create_event(
    name: str,
    typ: str,
    age_rest: int,
    day: int,
    client: t.Any = Depends(grpc_observer_client),
) -> JSONResponse:
    try:
        event = await client.CreateEvent(
            observer_pb2.CreateEventRequest(
                name=name, type=typ, age_restrictions=age_rest, day=day
            )
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(event))


@app.patch("/event/{id:int}")
async def update_event(
    id: int,
    name: str,
    type: str,
    age_rest: int,
    day: int,
    client: t.Any = Depends(grpc_observer_client),
) -> JSONResponse:
    try:
        event = await client.UpdateEventById(
            observer_pb2.UpdateEventByIdRequest(
                id=id, name=name, type=type, age_restrictions=age_rest, day=day
            )
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(event))


@app.delete("/event/{id:int}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(
    id: int,
    client: t.Any = Depends(grpc_observer_client),
) -> JSONResponse:
    try:
        event = await client.DeleteEventById(
            observer_pb2.DeleteEventByIdRequest(id=id)
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(event))


@app.get("/user")
async def get_user(
    api_key: str = Security(api_key_header),
    client: t.Any = Depends(grpc_auth_client),
) -> JSONResponse:
    print(f"api_key_header {api_key}")
    try:
        curr_user = await client.ReadUser(
            auth_pb2.ReadUserRequest(token=api_key)
        )
        await send_one(key='get_user_call', value=curr_user.user.id)
    except AioRpcError as e:
        import traceback

        traceback.print_exc()
        raise HTTPException(status_code=400, detail=e.details())
    return JSONResponse(MessageToDict(curr_user))


@app.post("/login")
async def get_token(
    user_form: UserLoginForm = Body(..., embed=True),
    client: t.Any = Depends(grpc_auth_client),
) -> JSONResponse:
    try:
        token = await client.Login(
            auth_pb2.LoginRequest(
                name=user_form.username, password=user_form.password
            )
        )
    except AioRpcError as e:
        import traceback

        traceback.print_exc()
        raise HTTPException(status_code=400, detail=e.details())
    return JSONResponse(MessageToDict(token))


@app.post("/user")
async def create_user(
    user: UserCreateForm = Body(..., embed=True),
    client: t.Any = Depends(grpc_auth_client),
) -> JSONResponse:
    try:
        user = await client.CreateUser(
            auth_pb2.CreateUserRequest(
                name=user.username,
                email=user.email,
                gender=user.gender,
                password=user.password,
            )
        )
    except AioRpcError as e:
        import traceback

        traceback.print_exc()
        raise HTTPException(status_code=400, detail=e.details())
    return JSONResponse(MessageToDict(user))


@app.get("/plan")
async def get_plans(
    api_key: str = Security(api_key_header),
    auth_client: t.Any = Depends(grpc_auth_client),
    planner_client: t.Any = Depends(grpc_planner_client),
) -> JSONResponse:
    print(f"api_key_header {api_key}")
    try:
        curr_user = await auth_client.ReadUser(
            auth_pb2.ReadUserRequest(token=api_key)
        )
        plans = await planner_client.ReadPlans(
            planner_pb2.ReadUserPlanRequest(user_id=curr_user.user.id)
        )
    except AioRpcError as e:
        import traceback

        traceback.print_exc()
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(plans))


@app.post("/plan")
async def create_plan(
    event_name: str,
    api_key: str = Security(api_key_header),
    auth_client: t.Any = Depends(grpc_auth_client),
    planner_client: t.Any = Depends(grpc_planner_client),
) -> JSONResponse:
    print(f"api_key_header {api_key}")
    curr_user = None
    plan = None
    try:
        curr_user = await auth_client.ReadUser(
            auth_pb2.ReadUserRequest(token=api_key)
        )
        plan = await planner_client.CreatePlan(
            planner_pb2.CreateUserPlanRequest(
                user_id=curr_user.user.id, event_name=event_name
            )
        )
    except AioRpcError as e:
        import traceback

        traceback.print_exc()
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(plan))


Instrumentator().instrument(app).expose(app)
