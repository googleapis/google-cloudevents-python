# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/events/cloudevent.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/events/cloudevent.proto',
  package='google.events',
  syntax='proto3',
  serialized_options=b'\252\002\026Google.Events.Protobuf',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1egoogle/events/cloudevent.proto\x12\rgoogle.events\x1a google/protobuf/descriptor.proto:<\n\x10\x63loud_event_type\x12\x1f.google.protobuf.MessageOptions\x18\x86\x8f\xcb\x05 \x01(\tB\x19\xaa\x02\x16Google.Events.Protobufb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


CLOUD_EVENT_TYPE_FIELD_NUMBER = 11716486
cloud_event_type = _descriptor.FieldDescriptor(
  name='cloud_event_type', full_name='google.events.cloud_event_type', index=0,
  number=11716486, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

DESCRIPTOR.extensions_by_name['cloud_event_type'] = cloud_event_type
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(cloud_event_type)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
