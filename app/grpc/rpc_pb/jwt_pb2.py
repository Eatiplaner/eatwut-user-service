# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jwt.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tjwt.proto\x12\x04\x61uth\"\x1d\n\x0cValidRequest\x12\r\n\x05token\x18\x01 \x01(\t\"\x1e\n\rValidResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x32\x45\n\nJwtService\x12\x37\n\nValidToken\x12\x12.auth.ValidRequest\x1a\x13.auth.ValidResponse\"\x00\x42\x13Z\x11./app/grpc/rpc_pbb\x06proto3')



_VALIDREQUEST = DESCRIPTOR.message_types_by_name['ValidRequest']
_VALIDRESPONSE = DESCRIPTOR.message_types_by_name['ValidResponse']
ValidRequest = _reflection.GeneratedProtocolMessageType('ValidRequest', (_message.Message,), {
  'DESCRIPTOR' : _VALIDREQUEST,
  '__module__' : 'jwt_pb2'
  # @@protoc_insertion_point(class_scope:auth.ValidRequest)
  })
_sym_db.RegisterMessage(ValidRequest)

ValidResponse = _reflection.GeneratedProtocolMessageType('ValidResponse', (_message.Message,), {
  'DESCRIPTOR' : _VALIDRESPONSE,
  '__module__' : 'jwt_pb2'
  # @@protoc_insertion_point(class_scope:auth.ValidResponse)
  })
_sym_db.RegisterMessage(ValidResponse)

_JWTSERVICE = DESCRIPTOR.services_by_name['JwtService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\021./app/grpc/rpc_pb'
  _VALIDREQUEST._serialized_start=19
  _VALIDREQUEST._serialized_end=48
  _VALIDRESPONSE._serialized_start=50
  _VALIDRESPONSE._serialized_end=80
  _JWTSERVICE._serialized_start=82
  _JWTSERVICE._serialized_end=151
# @@protoc_insertion_point(module_scope)
