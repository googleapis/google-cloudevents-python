from typing import ClassVar, Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Date(_message.Message):
    __slots__ = ["day", "month", "year"]
    DAY_FIELD_NUMBER: ClassVar[int]
    MONTH_FIELD_NUMBER: ClassVar[int]
    YEAR_FIELD_NUMBER: ClassVar[int]
    day: int
    month: int
    year: int
    def __init__(
        self,
        year: Optional[int] = ...,
        month: Optional[int] = ...,
        day: Optional[int] = ...,
    ) -> None: ...
