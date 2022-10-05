from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthEventData(_message.Message):
    __slots__ = ["custom_claims", "disabled", "display_name", "email", "email_verified", "metadata", "phone_number", "photo_URL", "provider_data", "uid"]
    CUSTOM_CLAIMS_FIELD_NUMBER: ClassVar[int]
    DISABLED_FIELD_NUMBER: ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: ClassVar[int]
    EMAIL_FIELD_NUMBER: ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: ClassVar[int]
    PHOTO_URL_FIELD_NUMBER: ClassVar[int]
    PROVIDER_DATA_FIELD_NUMBER: ClassVar[int]
    UID_FIELD_NUMBER: ClassVar[int]
    custom_claims: _struct_pb2.Struct
    disabled: bool
    display_name: str
    email: str
    email_verified: bool
    metadata: UserMetadata
    phone_number: str
    photo_URL: str
    provider_data: _containers.RepeatedCompositeFieldContainer[UserInfo]
    uid: str
    def __init__(self, uid: Optional[str] = ..., email: Optional[str] = ..., email_verified: bool = ..., display_name: Optional[str] = ..., photo_URL: Optional[str] = ..., disabled: bool = ..., metadata: Optional[Union[UserMetadata, Mapping]] = ..., provider_data: Optional[Iterable[Union[UserInfo, Mapping]]] = ..., phone_number: Optional[str] = ..., custom_claims: Optional[Union[_struct_pb2.Struct, Mapping]] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ["display_name", "email", "photo_URL", "provider_id", "uid"]
    DISPLAY_NAME_FIELD_NUMBER: ClassVar[int]
    EMAIL_FIELD_NUMBER: ClassVar[int]
    PHOTO_URL_FIELD_NUMBER: ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: ClassVar[int]
    UID_FIELD_NUMBER: ClassVar[int]
    display_name: str
    email: str
    photo_URL: str
    provider_id: str
    uid: str
    def __init__(self, uid: Optional[str] = ..., email: Optional[str] = ..., display_name: Optional[str] = ..., photo_URL: Optional[str] = ..., provider_id: Optional[str] = ...) -> None: ...

class UserMetadata(_message.Message):
    __slots__ = ["create_time", "last_sign_in_time"]
    CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    LAST_SIGN_IN_TIME_FIELD_NUMBER: ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    last_sign_in_time: _timestamp_pb2.Timestamp
    def __init__(self, create_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., last_sign_in_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...
