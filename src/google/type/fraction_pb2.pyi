from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Fraction(_message.Message):
    __slots__ = ["denominator", "numerator"]
    DENOMINATOR_FIELD_NUMBER: ClassVar[int]
    NUMERATOR_FIELD_NUMBER: ClassVar[int]
    denominator: int
    numerator: int
    def __init__(
        self, numerator: Optional[int] = ..., denominator: Optional[int] = ...
    ) -> None: ...
