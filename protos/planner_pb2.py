# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/planner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14protos/planner.proto\x12\x07planner\"A\n\x05\x45vent\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x04\x12\x12\n\nevent_name\x18\x02 \x01(\t\x12\x12\n\nevent_type\x18\x03 \x01(\t\"8\n\x04Plan\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x1d\n\x05\x65vent\x18\x02 \x01(\x0b\x32\x0e.planner.Event\"&\n\x13ReadUserPlanRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\"5\n\x14ReadUserPlanResponse\x12\x1d\n\x05\x65vent\x18\x01 \x03(\x0b\x32\x0e.planner.Event\"<\n\x15\x43reateUserPlanRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x12\n\nevent_name\x18\x02 \x01(\t\"5\n\x16\x43reateUserPlanResponse\x12\x1b\n\x04plan\x18\x01 \x01(\x0b\x32\r.planner.Plan2\xa9\x01\n\x0ePlannerService\x12H\n\tReadPlans\x12\x1c.planner.ReadUserPlanRequest\x1a\x1d.planner.ReadUserPlanResponse\x12M\n\nCreatePlan\x12\x1e.planner.CreateUserPlanRequest\x1a\x1f.planner.CreateUserPlanResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.planner_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EVENT']._serialized_start=33
  _globals['_EVENT']._serialized_end=98
  _globals['_PLAN']._serialized_start=100
  _globals['_PLAN']._serialized_end=156
  _globals['_READUSERPLANREQUEST']._serialized_start=158
  _globals['_READUSERPLANREQUEST']._serialized_end=196
  _globals['_READUSERPLANRESPONSE']._serialized_start=198
  _globals['_READUSERPLANRESPONSE']._serialized_end=251
  _globals['_CREATEUSERPLANREQUEST']._serialized_start=253
  _globals['_CREATEUSERPLANREQUEST']._serialized_end=313
  _globals['_CREATEUSERPLANRESPONSE']._serialized_start=315
  _globals['_CREATEUSERPLANRESPONSE']._serialized_end=368
  _globals['_PLANNERSERVICE']._serialized_start=371
  _globals['_PLANNERSERVICE']._serialized_end=540
# @@protoc_insertion_point(module_scope)
