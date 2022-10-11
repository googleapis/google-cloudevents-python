from typing import ClassVar, Mapping, Optional, Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class AlertData(_message.Message):
    __slots__ = ["create_time", "end_time", "payload"]
    CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    END_TIME_FIELD_NUMBER: ClassVar[int]
    PAYLOAD_FIELD_NUMBER: ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    payload: _struct_pb2.Struct
    def __init__(
        self,
        create_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        end_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        payload: Optional[Union[_struct_pb2.Struct, Mapping]] = ...,
    ) -> None: ...
