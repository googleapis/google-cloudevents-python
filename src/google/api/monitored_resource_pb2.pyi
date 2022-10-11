from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MonitoredResource(_message.Message):
    __slots__ = ["labels", "type"]

    class LabelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: Optional[str] = ..., value: Optional[str] = ...
        ) -> None: ...
    LABELS_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    labels: _containers.ScalarMap[str, str]
    type: str
    def __init__(
        self, type: Optional[str] = ..., labels: Optional[Mapping[str, str]] = ...
    ) -> None: ...
