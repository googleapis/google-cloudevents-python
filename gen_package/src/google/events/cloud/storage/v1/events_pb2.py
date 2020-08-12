# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/events/cloud/storage/v1/events.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.events.cloud.storage.v1 import data_pb2 as google_dot_events_dot_cloud_dot_storage_dot_v1_dot_data__pb2
from google.events import cloudevent_pb2 as google_dot_events_dot_cloudevent__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/events/cloud/storage/v1/events.proto',
  package='google.events.cloud.storage.v1',
  syntax='proto3',
  serialized_options=b'\252\002\'Google.Events.Protobuf.Cloud.Storage.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+google/events/cloud/storage/v1/events.proto\x12\x1egoogle.events.cloud.storage.v1\x1a)google/events/cloud/storage/v1/data.proto\x1a\x1egoogle/events/cloudevent.proto\"\x86\x01\n\x14ObjectFinalizedEvent\x12?\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x31.google.events.cloud.storage.v1.StorageObjectData:-\xb2\xf8\xd8,(google.cloud.storage.object.v1.finalized\"\x84\x01\n\x13ObjectArchivedEvent\x12?\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x31.google.events.cloud.storage.v1.StorageObjectData:,\xb2\xf8\xd8,\'google.cloud.storage.object.v1.archived\"\x82\x01\n\x12ObjectDeletedEvent\x12?\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x31.google.events.cloud.storage.v1.StorageObjectData:+\xb2\xf8\xd8,&google.cloud.storage.object.v1.deleted\"\x92\x01\n\x1aObjectMetadataUpdatedEvent\x12?\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x31.google.events.cloud.storage.v1.StorageObjectData:3\xb2\xf8\xd8,.google.cloud.storage.object.v1.metadataUpdatedB*\xaa\x02\'Google.Events.Protobuf.Cloud.Storage.V1b\x06proto3'
  ,
  dependencies=[google_dot_events_dot_cloud_dot_storage_dot_v1_dot_data__pb2.DESCRIPTOR,google_dot_events_dot_cloudevent__pb2.DESCRIPTOR,])




_OBJECTFINALIZEDEVENT = _descriptor.Descriptor(
  name='ObjectFinalizedEvent',
  full_name='google.events.cloud.storage.v1.ObjectFinalizedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.events.cloud.storage.v1.ObjectFinalizedEvent.data', index=0,
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
  serialized_options=b'\262\370\330,(google.cloud.storage.object.v1.finalized',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=289,
)


_OBJECTARCHIVEDEVENT = _descriptor.Descriptor(
  name='ObjectArchivedEvent',
  full_name='google.events.cloud.storage.v1.ObjectArchivedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.events.cloud.storage.v1.ObjectArchivedEvent.data', index=0,
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
  serialized_options=b'\262\370\330,\'google.cloud.storage.object.v1.archived',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=424,
)


_OBJECTDELETEDEVENT = _descriptor.Descriptor(
  name='ObjectDeletedEvent',
  full_name='google.events.cloud.storage.v1.ObjectDeletedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.events.cloud.storage.v1.ObjectDeletedEvent.data', index=0,
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
  serialized_options=b'\262\370\330,&google.cloud.storage.object.v1.deleted',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=427,
  serialized_end=557,
)


_OBJECTMETADATAUPDATEDEVENT = _descriptor.Descriptor(
  name='ObjectMetadataUpdatedEvent',
  full_name='google.events.cloud.storage.v1.ObjectMetadataUpdatedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.events.cloud.storage.v1.ObjectMetadataUpdatedEvent.data', index=0,
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
  serialized_options=b'\262\370\330,.google.cloud.storage.object.v1.metadataUpdated',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=560,
  serialized_end=706,
)

_OBJECTFINALIZEDEVENT.fields_by_name['data'].message_type = google_dot_events_dot_cloud_dot_storage_dot_v1_dot_data__pb2._STORAGEOBJECTDATA
_OBJECTARCHIVEDEVENT.fields_by_name['data'].message_type = google_dot_events_dot_cloud_dot_storage_dot_v1_dot_data__pb2._STORAGEOBJECTDATA
_OBJECTDELETEDEVENT.fields_by_name['data'].message_type = google_dot_events_dot_cloud_dot_storage_dot_v1_dot_data__pb2._STORAGEOBJECTDATA
_OBJECTMETADATAUPDATEDEVENT.fields_by_name['data'].message_type = google_dot_events_dot_cloud_dot_storage_dot_v1_dot_data__pb2._STORAGEOBJECTDATA
DESCRIPTOR.message_types_by_name['ObjectFinalizedEvent'] = _OBJECTFINALIZEDEVENT
DESCRIPTOR.message_types_by_name['ObjectArchivedEvent'] = _OBJECTARCHIVEDEVENT
DESCRIPTOR.message_types_by_name['ObjectDeletedEvent'] = _OBJECTDELETEDEVENT
DESCRIPTOR.message_types_by_name['ObjectMetadataUpdatedEvent'] = _OBJECTMETADATAUPDATEDEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectFinalizedEvent = _reflection.GeneratedProtocolMessageType('ObjectFinalizedEvent', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTFINALIZEDEVENT,
  '__module__' : 'google.events.cloud.storage.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:google.events.cloud.storage.v1.ObjectFinalizedEvent)
  })
_sym_db.RegisterMessage(ObjectFinalizedEvent)

ObjectArchivedEvent = _reflection.GeneratedProtocolMessageType('ObjectArchivedEvent', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTARCHIVEDEVENT,
  '__module__' : 'google.events.cloud.storage.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:google.events.cloud.storage.v1.ObjectArchivedEvent)
  })
_sym_db.RegisterMessage(ObjectArchivedEvent)

ObjectDeletedEvent = _reflection.GeneratedProtocolMessageType('ObjectDeletedEvent', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDELETEDEVENT,
  '__module__' : 'google.events.cloud.storage.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:google.events.cloud.storage.v1.ObjectDeletedEvent)
  })
_sym_db.RegisterMessage(ObjectDeletedEvent)

ObjectMetadataUpdatedEvent = _reflection.GeneratedProtocolMessageType('ObjectMetadataUpdatedEvent', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTMETADATAUPDATEDEVENT,
  '__module__' : 'google.events.cloud.storage.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:google.events.cloud.storage.v1.ObjectMetadataUpdatedEvent)
  })
_sym_db.RegisterMessage(ObjectMetadataUpdatedEvent)


DESCRIPTOR._options = None
_OBJECTFINALIZEDEVENT._options = None
_OBJECTARCHIVEDEVENT._options = None
_OBJECTDELETEDEVENT._options = None
_OBJECTMETADATAUPDATEDEVENT._options = None
# @@protoc_insertion_point(module_scope)
