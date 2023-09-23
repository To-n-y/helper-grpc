import typing as t

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKeyHeader
from google.protobuf.json_format import MessageToDict
from grpc.aio import AioRpcError

from clients.observer_client import grpc_observer_client
from protos import observer_pb2

api_key_header = APIKeyHeader(name="rpc-auth-key")

app = FastAPI()


@app.get("/")
async def ping():
    return {"ping": True}


@app.get("/event")
async def get_events_list(
    client: t.Any = Depends(grpc_observer_client),
) -> JSONResponse:
    try:
        events = await client.ListEvents(observer_pb2.ListEventsRequest())
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(events))


@app.get("/event/{id:int}")
async def get_event(
    id: int, client: t.Any = Depends(grpc_observer_client)
) -> JSONResponse:
    try:
        event = await client.ReadEvent(observer_pb2.ReadEventRequest(id=id))
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(event))


@app.post("/event", status_code=status.HTTP_201_CREATED)
async def create_event(
    name: str,
    type: str,
    age_rest: bool,
    day: int,
    client: t.Any = Depends(grpc_observer_client),
) -> JSONResponse:
    try:
        event = await client.CreateEvent(
            observer_pb2.CreateEventRequest(
                name=name, type=type, age_restrictions=age_rest, day=day
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
    age_rest: bool,
    day: int,
    client: t.Any = Depends(grpc_observer_client),
) -> JSONResponse:
    try:
        event = await client.UpdateEvent(
            observer_pb2.UpdateEventRequest(
                id=id, name=name, type=type, age_restrictions=age_rest, day=day
            )
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(event))


@app.delete("/event/{id:int}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(
    id: int, client: t.Any = Depends(grpc_observer_client)
) -> JSONResponse:
    try:
        event = await client.DeleteEvent(
            observer_pb2.DeleteEventRequest(id=id)
        )
    except AioRpcError as e:
        raise HTTPException(status_code=400, detail=e.details())

    return JSONResponse(MessageToDict(event))
