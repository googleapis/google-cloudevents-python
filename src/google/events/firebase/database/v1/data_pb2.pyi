from typing import ClassVar, Mapping, Optional, Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ReferenceEventData(_message.Message):
    __slots__ = ["data", "delta"]
    DATA_FIELD_NUMBER: ClassVar[int]
    DELTA_FIELD_NUMBER: ClassVar[int]
    data: _struct_pb2.Value
    delta: _struct_pb2.Value
    def __init__(
        self,
        data: Optional[Union[_struct_pb2.Value, Mapping]] = ...,
        delta: Optional[Union[_struct_pb2.Value, Mapping]] = ...,
    ) -> None: ...
