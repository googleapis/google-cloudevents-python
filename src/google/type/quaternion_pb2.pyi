from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Quaternion(_message.Message):
    __slots__ = ["w", "x", "y", "z"]
    W_FIELD_NUMBER: ClassVar[int]
    X_FIELD_NUMBER: ClassVar[int]
    Y_FIELD_NUMBER: ClassVar[int]
    Z_FIELD_NUMBER: ClassVar[int]
    w: float
    x: float
    y: float
    z: float
    def __init__(
        self,
        x: Optional[float] = ...,
        y: Optional[float] = ...,
        z: Optional[float] = ...,
        w: Optional[float] = ...,
    ) -> None: ...
