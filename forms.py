from pydantic import BaseModel


class UserLoginForm(BaseModel):
    username: str
    password: str


class UserCreateForm(BaseModel):
    email: str
    password: str
    username: str
    gender: str


class TokenSchema(BaseModel):
    access_token: str


class TokenPayload(BaseModel):
    sub: str | None = None
    exp: int | None = None
