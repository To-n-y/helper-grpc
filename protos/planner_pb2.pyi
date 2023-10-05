from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ["event_id", "event_name", "event_type"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    event_name: str
    event_type: str
    def __init__(self, event_id: _Optional[int] = ..., event_name: _Optional[str] = ..., event_type: _Optional[str] = ...) -> None: ...

class Plan(_message.Message):
    __slots__ = ["user_name", "event"]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    event: Event
    def __init__(self, user_name: _Optional[str] = ..., event: _Optional[_Union[Event, _Mapping]] = ...) -> None: ...

class ReadUserPlanRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class ReadUserPlanResponse(_message.Message):
    __slots__ = ["event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, event: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class CreateUserPlanRequest(_message.Message):
    __slots__ = ["user_id", "event_name"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    event_name: str
    def __init__(self, user_id: _Optional[int] = ..., event_name: _Optional[str] = ...) -> None: ...

class CreateUserPlanResponse(_message.Message):
    __slots__ = ["plan"]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    plan: Plan
    def __init__(self, plan: _Optional[_Union[Plan, _Mapping]] = ...) -> None: ...
