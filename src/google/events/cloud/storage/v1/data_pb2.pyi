from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class StorageObjectData(_message.Message):
    __slots__ = [
        "bucket",
        "cache_control",
        "component_count",
        "content_disposition",
        "content_encoding",
        "content_language",
        "content_type",
        "crc32c",
        "customer_encryption",
        "etag",
        "event_based_hold",
        "generation",
        "id",
        "kind",
        "kms_key_name",
        "md5_hash",
        "media_link",
        "metadata",
        "metageneration",
        "name",
        "retention_expiration_time",
        "self_link",
        "size",
        "storage_class",
        "temporary_hold",
        "time_created",
        "time_deleted",
        "time_storage_class_updated",
        "updated",
    ]

    class CustomerEncryption(_message.Message):
        __slots__ = ["encryption_algorithm", "key_sha256"]
        ENCRYPTION_ALGORITHM_FIELD_NUMBER: ClassVar[int]
        KEY_SHA256_FIELD_NUMBER: ClassVar[int]
        encryption_algorithm: str
        key_sha256: str
        def __init__(
            self,
            encryption_algorithm: Optional[str] = ...,
            key_sha256: Optional[str] = ...,
        ) -> None: ...

    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: Optional[str] = ..., value: Optional[str] = ...
        ) -> None: ...
    BUCKET_FIELD_NUMBER: ClassVar[int]
    CACHE_CONTROL_FIELD_NUMBER: ClassVar[int]
    COMPONENT_COUNT_FIELD_NUMBER: ClassVar[int]
    CONTENT_DISPOSITION_FIELD_NUMBER: ClassVar[int]
    CONTENT_ENCODING_FIELD_NUMBER: ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: ClassVar[int]
    CRC32C_FIELD_NUMBER: ClassVar[int]
    CUSTOMER_ENCRYPTION_FIELD_NUMBER: ClassVar[int]
    ETAG_FIELD_NUMBER: ClassVar[int]
    EVENT_BASED_HOLD_FIELD_NUMBER: ClassVar[int]
    GENERATION_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    KIND_FIELD_NUMBER: ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: ClassVar[int]
    MD5_HASH_FIELD_NUMBER: ClassVar[int]
    MEDIA_LINK_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    METAGENERATION_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    RETENTION_EXPIRATION_TIME_FIELD_NUMBER: ClassVar[int]
    SELF_LINK_FIELD_NUMBER: ClassVar[int]
    SIZE_FIELD_NUMBER: ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: ClassVar[int]
    TEMPORARY_HOLD_FIELD_NUMBER: ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: ClassVar[int]
    TIME_DELETED_FIELD_NUMBER: ClassVar[int]
    TIME_STORAGE_CLASS_UPDATED_FIELD_NUMBER: ClassVar[int]
    UPDATED_FIELD_NUMBER: ClassVar[int]
    bucket: str
    cache_control: str
    component_count: int
    content_disposition: str
    content_encoding: str
    content_language: str
    content_type: str
    crc32c: str
    customer_encryption: StorageObjectData.CustomerEncryption
    etag: str
    event_based_hold: bool
    generation: int
    id: str
    kind: str
    kms_key_name: str
    md5_hash: str
    media_link: str
    metadata: _containers.ScalarMap[str, str]
    metageneration: int
    name: str
    retention_expiration_time: _timestamp_pb2.Timestamp
    self_link: str
    size: int
    storage_class: str
    temporary_hold: bool
    time_created: _timestamp_pb2.Timestamp
    time_deleted: _timestamp_pb2.Timestamp
    time_storage_class_updated: _timestamp_pb2.Timestamp
    updated: _timestamp_pb2.Timestamp
    def __init__(
        self,
        content_encoding: Optional[str] = ...,
        content_disposition: Optional[str] = ...,
        cache_control: Optional[str] = ...,
        content_language: Optional[str] = ...,
        metageneration: Optional[int] = ...,
        time_deleted: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        content_type: Optional[str] = ...,
        size: Optional[int] = ...,
        time_created: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        crc32c: Optional[str] = ...,
        component_count: Optional[int] = ...,
        md5_hash: Optional[str] = ...,
        etag: Optional[str] = ...,
        updated: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        storage_class: Optional[str] = ...,
        kms_key_name: Optional[str] = ...,
        time_storage_class_updated: Optional[
            Union[_timestamp_pb2.Timestamp, Mapping]
        ] = ...,
        temporary_hold: bool = ...,
        retention_expiration_time: Optional[
            Union[_timestamp_pb2.Timestamp, Mapping]
        ] = ...,
        metadata: Optional[Mapping[str, str]] = ...,
        event_based_hold: bool = ...,
        name: Optional[str] = ...,
        id: Optional[str] = ...,
        bucket: Optional[str] = ...,
        generation: Optional[int] = ...,
        customer_encryption: Optional[
            Union[StorageObjectData.CustomerEncryption, Mapping]
        ] = ...,
        media_link: Optional[str] = ...,
        self_link: Optional[str] = ...,
        kind: Optional[str] = ...,
    ) -> None: ...
