from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Optional

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
