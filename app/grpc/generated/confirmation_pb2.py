# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/grpc/generated/confirmation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%app/grpc/generated/confirmation.proto\x12\x04user\x1a\x1bgoogle/protobuf/empty.proto\",\n\x14\x46indUserIdByEmailReq\x12\x14\n\x05\x65mail\x18\x01 \x01(\tR\x05\x65mail\"#\n\x15\x46indUserIdByEmailResp\x12\n\n\x02id\x18\x01 \x01(\r\"%\n\x12\x43heckActivationReq\x12\x0f\n\x07user_id\x18\x01 \x01(\r\"(\n\x13\x43heckActivationResp\x12\x11\n\tis_active\x18\x01 \x01(\x08\x32\xef\x01\n\x13\x43onfirmationService\x12N\n\x11\x46indUserIdByEmail\x12\x1a.user.FindUserIdByEmailReq\x1a\x1b.user.FindUserIdByEmailResp\"\x00\x12>\n\nActiveUser\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12H\n\x0f\x43heckActivation\x12\x18.user.CheckActivationReq\x1a\x19.user.CheckActivationResp\"\x00\x42\x13Z\x11./app/grpc/rpc_pbb\x06proto3')



_FINDUSERIDBYEMAILREQ = DESCRIPTOR.message_types_by_name['FindUserIdByEmailReq']
_FINDUSERIDBYEMAILRESP = DESCRIPTOR.message_types_by_name['FindUserIdByEmailResp']
_CHECKACTIVATIONREQ = DESCRIPTOR.message_types_by_name['CheckActivationReq']
_CHECKACTIVATIONRESP = DESCRIPTOR.message_types_by_name['CheckActivationResp']
FindUserIdByEmailReq = _reflection.GeneratedProtocolMessageType('FindUserIdByEmailReq', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERIDBYEMAILREQ,
  '__module__' : 'app.grpc.generated.confirmation_pb2'
  # @@protoc_insertion_point(class_scope:user.FindUserIdByEmailReq)
  })
_sym_db.RegisterMessage(FindUserIdByEmailReq)

FindUserIdByEmailResp = _reflection.GeneratedProtocolMessageType('FindUserIdByEmailResp', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERIDBYEMAILRESP,
  '__module__' : 'app.grpc.generated.confirmation_pb2'
  # @@protoc_insertion_point(class_scope:user.FindUserIdByEmailResp)
  })
_sym_db.RegisterMessage(FindUserIdByEmailResp)

CheckActivationReq = _reflection.GeneratedProtocolMessageType('CheckActivationReq', (_message.Message,), {
  'DESCRIPTOR' : _CHECKACTIVATIONREQ,
  '__module__' : 'app.grpc.generated.confirmation_pb2'
  # @@protoc_insertion_point(class_scope:user.CheckActivationReq)
  })
_sym_db.RegisterMessage(CheckActivationReq)

CheckActivationResp = _reflection.GeneratedProtocolMessageType('CheckActivationResp', (_message.Message,), {
  'DESCRIPTOR' : _CHECKACTIVATIONRESP,
  '__module__' : 'app.grpc.generated.confirmation_pb2'
  # @@protoc_insertion_point(class_scope:user.CheckActivationResp)
  })
_sym_db.RegisterMessage(CheckActivationResp)

_CONFIRMATIONSERVICE = DESCRIPTOR.services_by_name['ConfirmationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\021./app/grpc/rpc_pb'
  _FINDUSERIDBYEMAILREQ._serialized_start=76
  _FINDUSERIDBYEMAILREQ._serialized_end=120
  _FINDUSERIDBYEMAILRESP._serialized_start=122
  _FINDUSERIDBYEMAILRESP._serialized_end=157
  _CHECKACTIVATIONREQ._serialized_start=159
  _CHECKACTIVATIONREQ._serialized_end=196
  _CHECKACTIVATIONRESP._serialized_start=198
  _CHECKACTIVATIONRESP._serialized_end=238
  _CONFIRMATIONSERVICE._serialized_start=241
  _CONFIRMATIONSERVICE._serialized_end=480
# @@protoc_insertion_point(module_scope)
