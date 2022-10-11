from typing import ClassVar, Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

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
