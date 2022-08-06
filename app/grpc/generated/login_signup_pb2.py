# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/grpc/generated/login_signup.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%app/grpc/generated/login_signup.proto\x12\x04user\"_\n\rCreateRequest\x12\x14\n\x05\x65mail\x18\x01 \x01(\tR\x05\x65mail\x12\x1c\n\tfull_name\x18\x02 \x01(\tR\tfull_name\x12\x1a\n\x08password\x18\x03 \x01(\tR\x08password\"\x80\x01\n\x0f\x46indUserRequest\x12\x1f\n\x08username\x18\x01 \x01(\tH\x00R\x08username\x88\x01\x01\x12\x19\n\x05\x65mail\x18\x02 \x01(\tH\x01R\x05\x65mail\x88\x01\x01\x12\x1a\n\x08password\x18\x03 \x01(\tR\x08passwordB\x0b\n\t_usernameB\x08\n\x06_email\"a\n\x0bUserAddress\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x10\n\x08\x64istrict\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\x0b\n\x03lat\x18\x04 \x01(\t\x12\x0b\n\x03lng\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\"Q\n\x0cUserProvider\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x1a\n\x12\x64isplay_on_profile\x18\x04 \x01(\x08\"\xa6\x02\n\x0cUserResponse\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x11\n\tfull_name\x18\x04 \x01(\t\x12\x0b\n\x03\x62io\x18\x05 \x01(\t\x12\r\n\x05phone\x18\x06 \x01(\t\x12\x0e\n\x06gender\x18\x07 \x01(\t\x12\x0b\n\x03\x64ob\x18\x08 \x01(\t\x12\x12\n\nlast_login\x18\t \x01(\t\x12$\n\taddresses\x18\n \x03(\x0b\x32\x11.user.UserAddress\x12%\n\tproviders\x18\x0b \x03(\x0b\x32\x12.user.UserProvider\x12\x19\n\x11prefer_categories\x18\x0c \x03(\t\x12\x11\n\tis_active\x18\r \x01(\x08\x12\x0e\n\x06is_kol\x18\x0e \x01(\x08\x32\x92\x01\n\x12LoginSignupService\x12\x43\n\x14\x46indUserByCredential\x12\x15.user.FindUserRequest\x1a\x12.user.UserResponse\"\x00\x12\x37\n\nCreateUser\x12\x13.user.CreateRequest\x1a\x12.user.UserResponse\"\x00\x42\x13Z\x11./app/grpc/rpc_pbb\x06proto3')



_CREATEREQUEST = DESCRIPTOR.message_types_by_name['CreateRequest']
_FINDUSERREQUEST = DESCRIPTOR.message_types_by_name['FindUserRequest']
_USERADDRESS = DESCRIPTOR.message_types_by_name['UserAddress']
_USERPROVIDER = DESCRIPTOR.message_types_by_name['UserProvider']
_USERRESPONSE = DESCRIPTOR.message_types_by_name['UserResponse']
CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREQUEST,
  '__module__' : 'app.grpc.generated.login_signup_pb2'
  # @@protoc_insertion_point(class_scope:user.CreateRequest)
  })
_sym_db.RegisterMessage(CreateRequest)

FindUserRequest = _reflection.GeneratedProtocolMessageType('FindUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERREQUEST,
  '__module__' : 'app.grpc.generated.login_signup_pb2'
  # @@protoc_insertion_point(class_scope:user.FindUserRequest)
  })
_sym_db.RegisterMessage(FindUserRequest)

UserAddress = _reflection.GeneratedProtocolMessageType('UserAddress', (_message.Message,), {
  'DESCRIPTOR' : _USERADDRESS,
  '__module__' : 'app.grpc.generated.login_signup_pb2'
  # @@protoc_insertion_point(class_scope:user.UserAddress)
  })
_sym_db.RegisterMessage(UserAddress)

UserProvider = _reflection.GeneratedProtocolMessageType('UserProvider', (_message.Message,), {
  'DESCRIPTOR' : _USERPROVIDER,
  '__module__' : 'app.grpc.generated.login_signup_pb2'
  # @@protoc_insertion_point(class_scope:user.UserProvider)
  })
_sym_db.RegisterMessage(UserProvider)

UserResponse = _reflection.GeneratedProtocolMessageType('UserResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERRESPONSE,
  '__module__' : 'app.grpc.generated.login_signup_pb2'
  # @@protoc_insertion_point(class_scope:user.UserResponse)
  })
_sym_db.RegisterMessage(UserResponse)

_LOGINSIGNUPSERVICE = DESCRIPTOR.services_by_name['LoginSignupService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\021./app/grpc/rpc_pb'
  _CREATEREQUEST._serialized_start=47
  _CREATEREQUEST._serialized_end=142
  _FINDUSERREQUEST._serialized_start=145
  _FINDUSERREQUEST._serialized_end=273
  _USERADDRESS._serialized_start=275
  _USERADDRESS._serialized_end=372
  _USERPROVIDER._serialized_start=374
  _USERPROVIDER._serialized_end=455
  _USERRESPONSE._serialized_start=458
  _USERRESPONSE._serialized_end=752
  _LOGINSIGNUPSERVICE._serialized_start=755
  _LOGINSIGNUPSERVICE._serialized_end=901
# @@protoc_insertion_point(module_scope)
