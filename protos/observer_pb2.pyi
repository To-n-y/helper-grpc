from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ["id", "name", "type", "age_restrictions", "day"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AGE_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: str
    age_restrictions: int
    day: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., age_restrictions: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...

class CreateEventRequest(_message.Message):
    __slots__ = ["name", "type", "age_restrictions", "day"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AGE_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    age_restrictions: int
    day: int
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., age_restrictions: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...

class CreateEventResponse(_message.Message):
    __slots__ = ["Event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    Event: Event
    def __init__(self, Event: _Optional[_Union[Event, _Mapping]] = ...) -> None: ...

class ReadEventByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ReadEventResponse(_message.Message):
    __slots__ = ["Event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    Event: Event
    def __init__(self, Event: _Optional[_Union[Event, _Mapping]] = ...) -> None: ...

class UpdateEventByIdRequest(_message.Message):
    __slots__ = ["id", "name", "type", "age_restrictions", "day"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AGE_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: str
    age_restrictions: int
    day: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., age_restrictions: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...

class UpdateEventResponse(_message.Message):
    __slots__ = ["Event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    Event: Event
    def __init__(self, Event: _Optional[_Union[Event, _Mapping]] = ...) -> None: ...

class DeleteEventByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteEventResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ListEventRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListEventResponse(_message.Message):
    __slots__ = ["Events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    Events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, Events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...
