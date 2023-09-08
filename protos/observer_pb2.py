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


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15protos/observer.proto\x12\x08observer\x1a\x1egoogle/protobuf/wrappers.proto\"\x80\x01\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x34\n\x10\x61ge_restrictions\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x0b\n\x03\x64\x61y\x18\x05 \x01(\x04\x12\x0c\n\x04time\x18\x06 \x01(\t\"\x81\x01\n\x12\x43reateEventRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x34\n\x10\x61ge_restrictions\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x04\x12\x0c\n\x04time\x18\x05 \x01(\t\"5\n\x13\x43reateEventResponse\x12\x1e\n\x05\x45vent\x18\x01 \x01(\x0b\x32\x0f.observer.Event\"\x1e\n\x10ReadEventRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"3\n\x11ReadEventResponse\x12\x1e\n\x05\x45vent\x18\x01 \x01(\x0b\x32\x0f.observer.Event\"\x81\x01\n\x12UpdateEventRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x34\n\x10\x61ge_restrictions\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x04\x12\x0c\n\x04time\x18\x05 \x01(\t\"5\n\x13UpdateEventResponse\x12\x1e\n\x05\x45vent\x18\x01 \x01(\x0b\x32\x0f.observer.Event\" \n\x12\x44\x65leteEventRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"&\n\x13\x44\x65leteEventResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x13\n\x11ListEventsRequest\"5\n\x12ListEventsResponse\x12\x1f\n\x06\x45vents\x18\x01 \x03(\x0b\x32\x0f.observer.Event2\x81\x03\n\x0c\x45ventService\x12J\n\x0b\x43reateEvent\x12\x1c.observer.CreateEventRequest\x1a\x1d.observer.CreateEventResponse\x12\x44\n\tReadEvent\x12\x1a.observer.ReadEventRequest\x1a\x1b.observer.ReadEventResponse\x12J\n\x0bUpdateEvent\x12\x1c.observer.UpdateEventRequest\x1a\x1d.observer.UpdateEventResponse\x12J\n\x0b\x44\x65leteEvent\x12\x1c.observer.DeleteEventRequest\x1a\x1d.observer.DeleteEventResponse\x12G\n\nListEvents\x12\x1b.observer.ListEventsRequest\x1a\x1c.observer.ListEventsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.observer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_EVENT']._serialized_start=68
  _globals['_EVENT']._serialized_end=196
  _globals['_CREATEEVENTREQUEST']._serialized_start=199
  _globals['_CREATEEVENTREQUEST']._serialized_end=328
  _globals['_CREATEEVENTRESPONSE']._serialized_start=330
  _globals['_CREATEEVENTRESPONSE']._serialized_end=383
  _globals['_READEVENTREQUEST']._serialized_start=385
  _globals['_READEVENTREQUEST']._serialized_end=415
  _globals['_READEVENTRESPONSE']._serialized_start=417
  _globals['_READEVENTRESPONSE']._serialized_end=468
  _globals['_UPDATEEVENTREQUEST']._serialized_start=471
  _globals['_UPDATEEVENTREQUEST']._serialized_end=600
  _globals['_UPDATEEVENTRESPONSE']._serialized_start=602
  _globals['_UPDATEEVENTRESPONSE']._serialized_end=655
  _globals['_DELETEEVENTREQUEST']._serialized_start=657
  _globals['_DELETEEVENTREQUEST']._serialized_end=689
  _globals['_DELETEEVENTRESPONSE']._serialized_start=691
  _globals['_DELETEEVENTRESPONSE']._serialized_end=729
  _globals['_LISTEVENTSREQUEST']._serialized_start=731
  _globals['_LISTEVENTSREQUEST']._serialized_end=750
  _globals['_LISTEVENTSRESPONSE']._serialized_start=752
  _globals['_LISTEVENTSRESPONSE']._serialized_end=805
  _globals['_EVENTSERVICE']._serialized_start=808
  _globals['_EVENTSERVICE']._serialized_end=1193
# @@protoc_insertion_point(module_scope)
