from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class ArrayValue(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Value]
    def __init__(
        self, values: Optional[Iterable[Union[Value, Mapping]]] = ...
    ) -> None: ...

class Document(_message.Message):
    __slots__ = ["create_time", "fields", "name", "update_time"]

    class FieldsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: Value
        def __init__(
            self, key: Optional[str] = ..., value: Optional[Union[Value, Mapping]] = ...
        ) -> None: ...
    CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    FIELDS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    fields: _containers.MessageMap[str, Value]
    name: str
    update_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        name: Optional[str] = ...,
        fields: Optional[Mapping[str, Value]] = ...,
        create_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        update_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
    ) -> None: ...

class DocumentEventData(_message.Message):
    __slots__ = ["old_value", "update_mask", "value"]
    OLD_VALUE_FIELD_NUMBER: ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    old_value: Document
    update_mask: DocumentMask
    value: Document
    def __init__(
        self,
        value: Optional[Union[Document, Mapping]] = ...,
        old_value: Optional[Union[Document, Mapping]] = ...,
        update_mask: Optional[Union[DocumentMask, Mapping]] = ...,
    ) -> None: ...

class DocumentMask(_message.Message):
    __slots__ = ["field_paths"]
    FIELD_PATHS_FIELD_NUMBER: ClassVar[int]
    field_paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, field_paths: Optional[Iterable[str]] = ...) -> None: ...

class MapValue(_message.Message):
    __slots__ = ["fields"]

    class FieldsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: Value
        def __init__(
            self, key: Optional[str] = ..., value: Optional[Union[Value, Mapping]] = ...
        ) -> None: ...
    FIELDS_FIELD_NUMBER: ClassVar[int]
    fields: _containers.MessageMap[str, Value]
    def __init__(self, fields: Optional[Mapping[str, Value]] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = [
        "array_value",
        "boolean_value",
        "bytes_value",
        "double_value",
        "geo_point_value",
        "integer_value",
        "map_value",
        "null_value",
        "reference_value",
        "string_value",
        "timestamp_value",
    ]
    ARRAY_VALUE_FIELD_NUMBER: ClassVar[int]
    BOOLEAN_VALUE_FIELD_NUMBER: ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: ClassVar[int]
    GEO_POINT_VALUE_FIELD_NUMBER: ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: ClassVar[int]
    MAP_VALUE_FIELD_NUMBER: ClassVar[int]
    NULL_VALUE_FIELD_NUMBER: ClassVar[int]
    REFERENCE_VALUE_FIELD_NUMBER: ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: ClassVar[int]
    array_value: ArrayValue
    boolean_value: bool
    bytes_value: bytes
    double_value: float
    geo_point_value: _latlng_pb2.LatLng
    integer_value: int
    map_value: MapValue
    null_value: _struct_pb2.NullValue
    reference_value: str
    string_value: str
    timestamp_value: _timestamp_pb2.Timestamp
    def __init__(
        self,
        null_value: Optional[Union[_struct_pb2.NullValue, str]] = ...,
        boolean_value: bool = ...,
        integer_value: Optional[int] = ...,
        double_value: Optional[float] = ...,
        timestamp_value: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        string_value: Optional[str] = ...,
        bytes_value: Optional[bytes] = ...,
        reference_value: Optional[str] = ...,
        geo_point_value: Optional[Union[_latlng_pb2.LatLng, Mapping]] = ...,
        array_value: Optional[Union[ArrayValue, Mapping]] = ...,
        map_value: Optional[Union[MapValue, Mapping]] = ...,
    ) -> None: ...
