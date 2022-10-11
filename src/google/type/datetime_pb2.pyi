from typing import ClassVar, Mapping, Optional, Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DateTime(_message.Message):
    __slots__ = [
        "day",
        "hours",
        "minutes",
        "month",
        "nanos",
        "seconds",
        "time_zone",
        "utc_offset",
        "year",
    ]
    DAY_FIELD_NUMBER: ClassVar[int]
    HOURS_FIELD_NUMBER: ClassVar[int]
    MINUTES_FIELD_NUMBER: ClassVar[int]
    MONTH_FIELD_NUMBER: ClassVar[int]
    NANOS_FIELD_NUMBER: ClassVar[int]
    SECONDS_FIELD_NUMBER: ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: ClassVar[int]
    UTC_OFFSET_FIELD_NUMBER: ClassVar[int]
    YEAR_FIELD_NUMBER: ClassVar[int]
    day: int
    hours: int
    minutes: int
    month: int
    nanos: int
    seconds: int
    time_zone: TimeZone
    utc_offset: _duration_pb2.Duration
    year: int
    def __init__(
        self,
        year: Optional[int] = ...,
        month: Optional[int] = ...,
        day: Optional[int] = ...,
        hours: Optional[int] = ...,
        minutes: Optional[int] = ...,
        seconds: Optional[int] = ...,
        nanos: Optional[int] = ...,
        utc_offset: Optional[Union[_duration_pb2.Duration, Mapping]] = ...,
        time_zone: Optional[Union[TimeZone, Mapping]] = ...,
    ) -> None: ...

class TimeZone(_message.Message):
    __slots__ = ["id", "version"]
    ID_FIELD_NUMBER: ClassVar[int]
    VERSION_FIELD_NUMBER: ClassVar[int]
    id: str
    version: str
    def __init__(
        self, id: Optional[str] = ..., version: Optional[str] = ...
    ) -> None: ...
