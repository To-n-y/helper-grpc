import typing as t

from fastapi import Depends, FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKeyHeader

api_key_header = APIKeyHeader(name="rpc-auth-key")

app = FastAPI()


@app.get("/")
async def ping():
    return {"ping": True}


@app.get("/event")
async def get_events_list(client: t.Any = Depends()) -> JSONResponse:
    pass


@app.get("/event/{id:int}")
async def get_event(id: int, client: t.Any = Depends()) -> JSONResponse:
    pass


@app.post("/event", status_code=status.HTTP_201_CREATED)
async def create_event(client: t.Any = Depends()) -> JSONResponse:
    pass


@app.patch("/event/{id:int}")
async def update_event(client: t.Any = Depends()) -> JSONResponse:
    pass


@app.delete("/event/{id:int}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(id: int, client: t.Any = Depends()) -> JSONResponse:
    pass
