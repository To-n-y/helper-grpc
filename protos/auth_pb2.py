# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11protos/auth.proto\x12\x04\x61uth\".\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\t\" \n\x0fReadUserRequest\x12\r\n\x05token\x18\x01 \x01(\t\",\n\x10ReadUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.auth.User\".\n\x0cLoginRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1e\n\rLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t\"R\n\x11\x43reateUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0e\n\x06gender\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\".\n\x12\x43reateUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.auth.User2\xbb\x01\n\x0b\x41uthService\x12\x39\n\x08ReadUser\x12\x15.auth.ReadUserRequest\x1a\x16.auth.ReadUserResponse\x12\x30\n\x05Login\x12\x12.auth.LoginRequest\x1a\x13.auth.LoginResponse\x12?\n\nCreateUser\x12\x17.auth.CreateUserRequest\x1a\x18.auth.CreateUserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.auth_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=27
  _globals['_USER']._serialized_end=73
  _globals['_READUSERREQUEST']._serialized_start=75
  _globals['_READUSERREQUEST']._serialized_end=107
  _globals['_READUSERRESPONSE']._serialized_start=109
  _globals['_READUSERRESPONSE']._serialized_end=153
  _globals['_LOGINREQUEST']._serialized_start=155
  _globals['_LOGINREQUEST']._serialized_end=201
  _globals['_LOGINRESPONSE']._serialized_start=203
  _globals['_LOGINRESPONSE']._serialized_end=233
  _globals['_CREATEUSERREQUEST']._serialized_start=235
  _globals['_CREATEUSERREQUEST']._serialized_end=317
  _globals['_CREATEUSERRESPONSE']._serialized_start=319
  _globals['_CREATEUSERRESPONSE']._serialized_end=365
  _globals['_AUTHSERVICE']._serialized_start=368
  _globals['_AUTHSERVICE']._serialized_end=555
# @@protoc_insertion_point(module_scope)
