from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Money(_message.Message):
    __slots__ = ["currency_code", "nanos", "units"]
    CURRENCY_CODE_FIELD_NUMBER: ClassVar[int]
    NANOS_FIELD_NUMBER: ClassVar[int]
    UNITS_FIELD_NUMBER: ClassVar[int]
    currency_code: str
    nanos: int
    units: int
    def __init__(
        self,
        currency_code: Optional[str] = ...,
        units: Optional[int] = ...,
        nanos: Optional[int] = ...,
    ) -> None: ...
