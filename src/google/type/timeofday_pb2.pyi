from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TimeOfDay(_message.Message):
    __slots__ = ["hours", "minutes", "nanos", "seconds"]
    HOURS_FIELD_NUMBER: ClassVar[int]
    MINUTES_FIELD_NUMBER: ClassVar[int]
    NANOS_FIELD_NUMBER: ClassVar[int]
    SECONDS_FIELD_NUMBER: ClassVar[int]
    hours: int
    minutes: int
    nanos: int
    seconds: int
    def __init__(
        self,
        hours: Optional[int] = ...,
        minutes: Optional[int] = ...,
        seconds: Optional[int] = ...,
        nanos: Optional[int] = ...,
    ) -> None: ...
