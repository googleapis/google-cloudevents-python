from typing import ClassVar, Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class LatLng(_message.Message):
    __slots__ = ["latitude", "longitude"]
    LATITUDE_FIELD_NUMBER: ClassVar[int]
    LONGITUDE_FIELD_NUMBER: ClassVar[int]
    latitude: float
    longitude: float
    def __init__(
        self, latitude: Optional[float] = ..., longitude: Optional[float] = ...
    ) -> None: ...
