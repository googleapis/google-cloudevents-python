from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessagePublishedData(_message.Message):
    __slots__ = ["message", "subscription"]
    MESSAGE_FIELD_NUMBER: ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: ClassVar[int]
    message: PubsubMessage
    subscription: str
    def __init__(
        self,
        message: Optional[Union[PubsubMessage, Mapping]] = ...,
        subscription: Optional[str] = ...,
    ) -> None: ...

class PubsubMessage(_message.Message):
    __slots__ = ["attributes", "data", "message_id", "ordering_key", "publish_time"]

    class AttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: Optional[str] = ..., value: Optional[str] = ...
        ) -> None: ...
    ATTRIBUTES_FIELD_NUMBER: ClassVar[int]
    DATA_FIELD_NUMBER: ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: ClassVar[int]
    ORDERING_KEY_FIELD_NUMBER: ClassVar[int]
    PUBLISH_TIME_FIELD_NUMBER: ClassVar[int]
    attributes: _containers.ScalarMap[str, str]
    data: bytes
    message_id: str
    ordering_key: str
    publish_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        data: Optional[bytes] = ...,
        attributes: Optional[Mapping[str, str]] = ...,
        message_id: Optional[str] = ...,
        publish_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        ordering_key: Optional[str] = ...,
    ) -> None: ...
