from typing import ClassVar, Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SchedulerJobData(_message.Message):
    __slots__ = ["custom_data"]
    CUSTOM_DATA_FIELD_NUMBER: ClassVar[int]
    custom_data: bytes
    def __init__(self, custom_data: Optional[bytes] = ...) -> None: ...
