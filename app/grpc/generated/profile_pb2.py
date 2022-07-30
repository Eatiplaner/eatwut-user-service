# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/grpc/generated/profile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n app/grpc/generated/profile.proto\x12\x04user\"y\n\x0fUserAddressData\x12\x1a\n\x08\x64istrict\x18\x01 \x01(\tR\x08\x64istrict\x12\x12\n\x04\x63ity\x18\x02 \x01(\tR\x04\x63ity\x12\x10\n\x03lat\x18\x03 \x01(\tR\x03lat\x12\x10\n\x03lng\x18\x04 \x01(\tR\x03lng\x12\x12\n\x04type\x18\x05 \x01(\tR\x04type\"h\n\x10UserProviderData\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12.\n\x12\x64isplay_on_profile\x18\x03 \x01(\x08R\x12\x64isplay_on_profile\"\xe6\x03\n\x11UpdateProfileData\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\x12\x14\n\x05\x65mail\x18\x02 \x01(\tR\x05\x65mail\x12\x1c\n\tfull_name\x18\x03 \x01(\tR\tfull_name\x12\x12\n\x03\x62io\x18\x04 \x01(\tH\x00R\x03\x62io\x12\x16\n\x05phone\x18\x05 \x01(\tH\x01R\x05phone\x12\x16\n\x06gender\x18\x06 \x01(\tR\x06gender\x12\x12\n\x03\x64ob\x18\x07 \x01(\tH\x02R\x03\x64ob\x12 \n\nlast_login\x18\x08 \x01(\tH\x03R\nlast_login\x12\x33\n\taddresses\x18\t \x03(\x0b\x32\x15.user.UserAddressDataR\taddresses\x12\x34\n\tproviders\x18\n \x03(\x0b\x32\x16.user.UserProviderDataR\tproviders\x12,\n\x11prefer_categories\x18\x0b \x03(\tR\x11prefer_categories\x12\x1e\n\tis_active\x18\x0c \x01(\x08H\x04R\tis_activeB\x0b\n\tbio_oneofB\r\n\x0bphone_oneofB\x0b\n\tdob_oneofB\x12\n\x10last_login_oneofB\x11\n\x0fis_active_oneof\"C\n\x14UpdateProfileRequest\x12+\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.user.UpdateProfileDataR\x04\x64\x61ta\"h\n\x12ProfileUserAddress\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x10\n\x08\x64istrict\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\x0b\n\x03lat\x18\x04 \x01(\t\x12\x0b\n\x03lng\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\"X\n\x13ProfileUserProvider\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x1a\n\x12\x64isplay_on_profile\x18\x04 \x01(\x08\"\xf2\x02\n\x15UpdateProfileResponse\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x11\n\tfull_name\x18\x04 \x01(\t\x12\r\n\x03\x62io\x18\x05 \x01(\tH\x00\x12\x0f\n\x05phone\x18\x06 \x01(\tH\x01\x12\x0e\n\x06gender\x18\x07 \x01(\t\x12\r\n\x03\x64ob\x18\x08 \x01(\tH\x02\x12\x14\n\nlast_login\x18\t \x01(\tH\x03\x12+\n\taddresses\x18\n \x03(\x0b\x32\x18.user.ProfileUserAddress\x12,\n\tproviders\x18\x0b \x03(\x0b\x32\x19.user.ProfileUserProvider\x12\x19\n\x11prefer_categories\x18\x0c \x03(\t\x12\x11\n\tis_active\x18\r \x01(\x08\x42\x0b\n\tbio_oneofB\r\n\x0bphone_oneofB\x0b\n\tdob_oneofB\x12\n\x10last_login_oneof2\\\n\x0eProfileService\x12J\n\rUpdateProfile\x12\x1a.user.UpdateProfileRequest\x1a\x1b.user.UpdateProfileResponse\"\x00\x42\x13Z\x11./app/grpc/rpc_pbb\x06proto3')



_USERADDRESSDATA = DESCRIPTOR.message_types_by_name['UserAddressData']
_USERPROVIDERDATA = DESCRIPTOR.message_types_by_name['UserProviderData']
_UPDATEPROFILEDATA = DESCRIPTOR.message_types_by_name['UpdateProfileData']
_UPDATEPROFILEREQUEST = DESCRIPTOR.message_types_by_name['UpdateProfileRequest']
_PROFILEUSERADDRESS = DESCRIPTOR.message_types_by_name['ProfileUserAddress']
_PROFILEUSERPROVIDER = DESCRIPTOR.message_types_by_name['ProfileUserProvider']
_UPDATEPROFILERESPONSE = DESCRIPTOR.message_types_by_name['UpdateProfileResponse']
UserAddressData = _reflection.GeneratedProtocolMessageType('UserAddressData', (_message.Message,), {
  'DESCRIPTOR' : _USERADDRESSDATA,
  '__module__' : 'app.grpc.generated.profile_pb2'
  # @@protoc_insertion_point(class_scope:user.UserAddressData)
  })
_sym_db.RegisterMessage(UserAddressData)

UserProviderData = _reflection.GeneratedProtocolMessageType('UserProviderData', (_message.Message,), {
  'DESCRIPTOR' : _USERPROVIDERDATA,
  '__module__' : 'app.grpc.generated.profile_pb2'
  # @@protoc_insertion_point(class_scope:user.UserProviderData)
  })
_sym_db.RegisterMessage(UserProviderData)

UpdateProfileData = _reflection.GeneratedProtocolMessageType('UpdateProfileData', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROFILEDATA,
  '__module__' : 'app.grpc.generated.profile_pb2'
  # @@protoc_insertion_point(class_scope:user.UpdateProfileData)
  })
_sym_db.RegisterMessage(UpdateProfileData)

UpdateProfileRequest = _reflection.GeneratedProtocolMessageType('UpdateProfileRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROFILEREQUEST,
  '__module__' : 'app.grpc.generated.profile_pb2'
  # @@protoc_insertion_point(class_scope:user.UpdateProfileRequest)
  })
_sym_db.RegisterMessage(UpdateProfileRequest)

ProfileUserAddress = _reflection.GeneratedProtocolMessageType('ProfileUserAddress', (_message.Message,), {
  'DESCRIPTOR' : _PROFILEUSERADDRESS,
  '__module__' : 'app.grpc.generated.profile_pb2'
  # @@protoc_insertion_point(class_scope:user.ProfileUserAddress)
  })
_sym_db.RegisterMessage(ProfileUserAddress)

ProfileUserProvider = _reflection.GeneratedProtocolMessageType('ProfileUserProvider', (_message.Message,), {
  'DESCRIPTOR' : _PROFILEUSERPROVIDER,
  '__module__' : 'app.grpc.generated.profile_pb2'
  # @@protoc_insertion_point(class_scope:user.ProfileUserProvider)
  })
_sym_db.RegisterMessage(ProfileUserProvider)

UpdateProfileResponse = _reflection.GeneratedProtocolMessageType('UpdateProfileResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROFILERESPONSE,
  '__module__' : 'app.grpc.generated.profile_pb2'
  # @@protoc_insertion_point(class_scope:user.UpdateProfileResponse)
  })
_sym_db.RegisterMessage(UpdateProfileResponse)

_PROFILESERVICE = DESCRIPTOR.services_by_name['ProfileService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\021./app/grpc/rpc_pb'
  _USERADDRESSDATA._serialized_start=42
  _USERADDRESSDATA._serialized_end=163
  _USERPROVIDERDATA._serialized_start=165
  _USERPROVIDERDATA._serialized_end=269
  _UPDATEPROFILEDATA._serialized_start=272
  _UPDATEPROFILEDATA._serialized_end=758
  _UPDATEPROFILEREQUEST._serialized_start=760
  _UPDATEPROFILEREQUEST._serialized_end=827
  _PROFILEUSERADDRESS._serialized_start=829
  _PROFILEUSERADDRESS._serialized_end=933
  _PROFILEUSERPROVIDER._serialized_start=935
  _PROFILEUSERPROVIDER._serialized_end=1023
  _UPDATEPROFILERESPONSE._serialized_start=1026
  _UPDATEPROFILERESPONSE._serialized_end=1396
  _PROFILESERVICE._serialized_start=1398
  _PROFILESERVICE._serialized_end=1490
# @@protoc_insertion_point(module_scope)
