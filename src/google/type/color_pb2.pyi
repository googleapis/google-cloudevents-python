from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Color(_message.Message):
    __slots__ = ["alpha", "blue", "green", "red"]
    ALPHA_FIELD_NUMBER: ClassVar[int]
    BLUE_FIELD_NUMBER: ClassVar[int]
    GREEN_FIELD_NUMBER: ClassVar[int]
    RED_FIELD_NUMBER: ClassVar[int]
    alpha: _wrappers_pb2.FloatValue
    blue: float
    green: float
    red: float
    def __init__(
        self,
        red: Optional[float] = ...,
        green: Optional[float] = ...,
        blue: Optional[float] = ...,
        alpha: Optional[Union[_wrappers_pb2.FloatValue, Mapping]] = ...,
    ) -> None: ...
