# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/events/firebase/auth/v1/events.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.events.firebase.auth.v1 import data_pb2 as google_dot_events_dot_firebase_dot_auth_dot_v1_dot_data__pb2
from google.events import cloudevent_pb2 as google_dot_events_dot_cloudevent__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/events/firebase/auth/v1/events.proto',
  package='google.events.firebase.auth.v1',
  syntax='proto3',
  serialized_options=b'\252\002\'Google.Events.Protobuf.Firebase.Auth.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+google/events/firebase/auth/v1/events.proto\x12\x1egoogle.events.firebase.auth.v1\x1a)google/events/firebase/auth/v1/data.proto\x1a\x1egoogle/events/cloudevent.proto\"z\n\x10UserCreatedEvent\x12;\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32-.google.events.firebase.auth.v1.AuthEventData:)\xb2\xf8\xd8,$google.firebase.auth.user.v1.updated\"z\n\x10UserDeletedEvent\x12;\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32-.google.events.firebase.auth.v1.AuthEventData:)\xb2\xf8\xd8,$google.firebase.auth.user.v1.deletedB*\xaa\x02\'Google.Events.Protobuf.Firebase.Auth.V1b\x06proto3'
  ,
  dependencies=[google_dot_events_dot_firebase_dot_auth_dot_v1_dot_data__pb2.DESCRIPTOR,google_dot_events_dot_cloudevent__pb2.DESCRIPTOR,])




_USERCREATEDEVENT = _descriptor.Descriptor(
  name='UserCreatedEvent',
  full_name='google.events.firebase.auth.v1.UserCreatedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.events.firebase.auth.v1.UserCreatedEvent.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\262\370\330,$google.firebase.auth.user.v1.updated',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=276,
)


_USERDELETEDEVENT = _descriptor.Descriptor(
  name='UserDeletedEvent',
  full_name='google.events.firebase.auth.v1.UserDeletedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.events.firebase.auth.v1.UserDeletedEvent.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\262\370\330,$google.firebase.auth.user.v1.deleted',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=400,
)

_USERCREATEDEVENT.fields_by_name['data'].message_type = google_dot_events_dot_firebase_dot_auth_dot_v1_dot_data__pb2._AUTHEVENTDATA
_USERDELETEDEVENT.fields_by_name['data'].message_type = google_dot_events_dot_firebase_dot_auth_dot_v1_dot_data__pb2._AUTHEVENTDATA
DESCRIPTOR.message_types_by_name['UserCreatedEvent'] = _USERCREATEDEVENT
DESCRIPTOR.message_types_by_name['UserDeletedEvent'] = _USERDELETEDEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserCreatedEvent = _reflection.GeneratedProtocolMessageType('UserCreatedEvent', (_message.Message,), {
  'DESCRIPTOR' : _USERCREATEDEVENT,
  '__module__' : 'google.events.firebase.auth.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:google.events.firebase.auth.v1.UserCreatedEvent)
  })
_sym_db.RegisterMessage(UserCreatedEvent)

UserDeletedEvent = _reflection.GeneratedProtocolMessageType('UserDeletedEvent', (_message.Message,), {
  'DESCRIPTOR' : _USERDELETEDEVENT,
  '__module__' : 'google.events.firebase.auth.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:google.events.firebase.auth.v1.UserDeletedEvent)
  })
_sym_db.RegisterMessage(UserDeletedEvent)


DESCRIPTOR._options = None
_USERCREATEDEVENT._options = None
_USERDELETEDEVENT._options = None
# @@protoc_insertion_point(module_scope)
