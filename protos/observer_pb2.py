# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/observer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15protos/observer.proto\x12\x08observer"V\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x18\n\x10\x61ge_restrictions\x18\x04 \x01(\x04\x12\x0b\n\x03\x64\x61y\x18\x05 \x01(\x04"W\n\x12\x43reateEventRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x18\n\x10\x61ge_restrictions\x18\x03 \x01(\x04\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x04"5\n\x13\x43reateEventResponse\x12\x1e\n\x05\x45vent\x18\x01 \x01(\x0b\x32\x0f.observer.Event""\n\x14ReadEventByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x04"3\n\x11ReadEventResponse\x12\x1e\n\x05\x45vent\x18\x01 \x01(\x0b\x32\x0f.observer.Event"g\n\x16UpdateEventByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x18\n\x10\x61ge_restrictions\x18\x04 \x01(\x04\x12\x0b\n\x03\x64\x61y\x18\x05 \x01(\x04"5\n\x13UpdateEventResponse\x12\x1e\n\x05\x45vent\x18\x01 \x01(\x0b\x32\x0f.observer.Event"$\n\x16\x44\x65leteEventByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x04"&\n\x13\x44\x65leteEventResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08"\x12\n\x10ListEventRequest"4\n\x11ListEventResponse\x12\x1f\n\x06\x45vents\x18\x01 \x03(\x0b\x32\x0f.observer.Event2\x99\x03\n\x0fObserverService\x12J\n\x0b\x43reateEvent\x12\x1c.observer.CreateEventRequest\x1a\x1d.observer.CreateEventResponse\x12L\n\rReadEventById\x12\x1e.observer.ReadEventByIdRequest\x1a\x1b.observer.ReadEventResponse\x12R\n\x0fUpdateEventById\x12 .observer.UpdateEventByIdRequest\x1a\x1d.observer.UpdateEventResponse\x12R\n\x0f\x44\x65leteEventById\x12 .observer.DeleteEventByIdRequest\x1a\x1d.observer.DeleteEventResponse\x12\x44\n\tListEvent\x12\x1a.observer.ListEventRequest\x1a\x1b.observer.ListEventResponseb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "protos.observer_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_EVENT"]._serialized_start = 35
    _globals["_EVENT"]._serialized_end = 121
    _globals["_CREATEEVENTREQUEST"]._serialized_start = 123
    _globals["_CREATEEVENTREQUEST"]._serialized_end = 210
    _globals["_CREATEEVENTRESPONSE"]._serialized_start = 212
    _globals["_CREATEEVENTRESPONSE"]._serialized_end = 265
    _globals["_READEVENTBYIDREQUEST"]._serialized_start = 267
    _globals["_READEVENTBYIDREQUEST"]._serialized_end = 301
    _globals["_READEVENTRESPONSE"]._serialized_start = 303
    _globals["_READEVENTRESPONSE"]._serialized_end = 354
    _globals["_UPDATEEVENTBYIDREQUEST"]._serialized_start = 356
    _globals["_UPDATEEVENTBYIDREQUEST"]._serialized_end = 459
    _globals["_UPDATEEVENTRESPONSE"]._serialized_start = 461
    _globals["_UPDATEEVENTRESPONSE"]._serialized_end = 514
    _globals["_DELETEEVENTBYIDREQUEST"]._serialized_start = 516
    _globals["_DELETEEVENTBYIDREQUEST"]._serialized_end = 552
    _globals["_DELETEEVENTRESPONSE"]._serialized_start = 554
    _globals["_DELETEEVENTRESPONSE"]._serialized_end = 592
    _globals["_LISTEVENTREQUEST"]._serialized_start = 594
    _globals["_LISTEVENTREQUEST"]._serialized_end = 612
    _globals["_LISTEVENTRESPONSE"]._serialized_start = 614
    _globals["_LISTEVENTRESPONSE"]._serialized_end = 666
    _globals["_OBSERVERSERVICE"]._serialized_start = 669
    _globals["_OBSERVERSERVICE"]._serialized_end = 1078
# @@protoc_insertion_point(module_scope)
