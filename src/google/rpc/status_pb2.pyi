from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(_message.Message):
    __slots__ = ["code", "details", "message"]
    CODE_FIELD_NUMBER: ClassVar[int]
    DETAILS_FIELD_NUMBER: ClassVar[int]
    MESSAGE_FIELD_NUMBER: ClassVar[int]
    code: int
    details: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    message: str
    def __init__(
        self,
        code: Optional[int] = ...,
        message: Optional[str] = ...,
        details: Optional[Iterable[Union[_any_pb2.Any, Mapping]]] = ...,
    ) -> None: ...
