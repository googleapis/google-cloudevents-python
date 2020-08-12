# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/events/firebase/auth/v1/data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/events/firebase/auth/v1/data.proto',
  package='google.events.firebase.auth.v1',
  syntax='proto3',
  serialized_options=b'\252\002\'Google.Events.Protobuf.Firebase.Auth.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)google/events/firebase/auth/v1/data.proto\x12\x1egoogle.events.firebase.auth.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xac\x01\n\rAuthEventData\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12>\n\x08metadata\x18\x07 \x01(\x0b\x32,.google.events.firebase.auth.v1.UserMetadata\x12?\n\rprovider_data\x18\x08 \x03(\x0b\x32(.google.events.firebase.auth.v1.UserInfo\"u\n\x0cUserMetadata\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x11last_signed_in_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\";\n\x08UserInfo\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x13\n\x0bprovider_id\x18\x05 \x01(\tB*\xaa\x02\'Google.Events.Protobuf.Firebase.Auth.V1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_AUTHEVENTDATA = _descriptor.Descriptor(
  name='AuthEventData',
  full_name='google.events.firebase.auth.v1.AuthEventData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='google.events.firebase.auth.v1.AuthEventData.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='google.events.firebase.auth.v1.AuthEventData.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='google.events.firebase.auth.v1.AuthEventData.metadata', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider_data', full_name='google.events.firebase.auth.v1.AuthEventData.provider_data', index=3,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=283,
)


_USERMETADATA = _descriptor.Descriptor(
  name='UserMetadata',
  full_name='google.events.firebase.auth.v1.UserMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='created_at', full_name='google.events.firebase.auth.v1.UserMetadata.created_at', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_signed_in_at', full_name='google.events.firebase.auth.v1.UserMetadata.last_signed_in_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=402,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='google.events.firebase.auth.v1.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='google.events.firebase.auth.v1.UserInfo.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='google.events.firebase.auth.v1.UserInfo.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider_id', full_name='google.events.firebase.auth.v1.UserInfo.provider_id', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=404,
  serialized_end=463,
)

_AUTHEVENTDATA.fields_by_name['metadata'].message_type = _USERMETADATA
_AUTHEVENTDATA.fields_by_name['provider_data'].message_type = _USERINFO
_USERMETADATA.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_USERMETADATA.fields_by_name['last_signed_in_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['AuthEventData'] = _AUTHEVENTDATA
DESCRIPTOR.message_types_by_name['UserMetadata'] = _USERMETADATA
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthEventData = _reflection.GeneratedProtocolMessageType('AuthEventData', (_message.Message,), {
  'DESCRIPTOR' : _AUTHEVENTDATA,
  '__module__' : 'google.events.firebase.auth.v1.data_pb2'
  # @@protoc_insertion_point(class_scope:google.events.firebase.auth.v1.AuthEventData)
  })
_sym_db.RegisterMessage(AuthEventData)

UserMetadata = _reflection.GeneratedProtocolMessageType('UserMetadata', (_message.Message,), {
  'DESCRIPTOR' : _USERMETADATA,
  '__module__' : 'google.events.firebase.auth.v1.data_pb2'
  # @@protoc_insertion_point(class_scope:google.events.firebase.auth.v1.UserMetadata)
  })
_sym_db.RegisterMessage(UserMetadata)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'google.events.firebase.auth.v1.data_pb2'
  # @@protoc_insertion_point(class_scope:google.events.firebase.auth.v1.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
