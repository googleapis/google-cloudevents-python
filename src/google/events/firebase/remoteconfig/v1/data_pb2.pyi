from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

ADMIN_SDK_NODE: RemoteConfigUpdateOrigin
CONSOLE: RemoteConfigUpdateOrigin
DESCRIPTOR: _descriptor.FileDescriptor
FORCED_UPDATE: RemoteConfigUpdateType
INCREMENTAL_UPDATE: RemoteConfigUpdateType
REMOTE_CONFIG_UPDATE_ORIGIN_UNSPECIFIED: RemoteConfigUpdateOrigin
REMOTE_CONFIG_UPDATE_TYPE_UNSPECIFIED: RemoteConfigUpdateType
REST_API: RemoteConfigUpdateOrigin
ROLLBACK: RemoteConfigUpdateType

class RemoteConfigEventData(_message.Message):
    __slots__ = [
        "description",
        "rollback_source",
        "update_origin",
        "update_time",
        "update_type",
        "update_user",
        "version_number",
    ]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    ROLLBACK_SOURCE_FIELD_NUMBER: ClassVar[int]
    UPDATE_ORIGIN_FIELD_NUMBER: ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: ClassVar[int]
    UPDATE_TYPE_FIELD_NUMBER: ClassVar[int]
    UPDATE_USER_FIELD_NUMBER: ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: ClassVar[int]
    description: str
    rollback_source: int
    update_origin: RemoteConfigUpdateOrigin
    update_time: _timestamp_pb2.Timestamp
    update_type: RemoteConfigUpdateType
    update_user: RemoteConfigUser
    version_number: int
    def __init__(
        self,
        version_number: Optional[int] = ...,
        update_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        update_user: Optional[Union[RemoteConfigUser, Mapping]] = ...,
        description: Optional[str] = ...,
        update_origin: Optional[Union[RemoteConfigUpdateOrigin, str]] = ...,
        update_type: Optional[Union[RemoteConfigUpdateType, str]] = ...,
        rollback_source: Optional[int] = ...,
    ) -> None: ...

class RemoteConfigUser(_message.Message):
    __slots__ = ["email", "image_url", "name"]
    EMAIL_FIELD_NUMBER: ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    email: str
    image_url: str
    name: str
    def __init__(
        self,
        name: Optional[str] = ...,
        email: Optional[str] = ...,
        image_url: Optional[str] = ...,
    ) -> None: ...

class RemoteConfigUpdateOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class RemoteConfigUpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
