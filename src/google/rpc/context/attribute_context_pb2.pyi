from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttributeContext(_message.Message):
    __slots__ = [
        "api",
        "destination",
        "extensions",
        "origin",
        "request",
        "resource",
        "response",
        "source",
    ]

    class Api(_message.Message):
        __slots__ = ["operation", "protocol", "service", "version"]
        OPERATION_FIELD_NUMBER: ClassVar[int]
        PROTOCOL_FIELD_NUMBER: ClassVar[int]
        SERVICE_FIELD_NUMBER: ClassVar[int]
        VERSION_FIELD_NUMBER: ClassVar[int]
        operation: str
        protocol: str
        service: str
        version: str
        def __init__(
            self,
            service: Optional[str] = ...,
            operation: Optional[str] = ...,
            protocol: Optional[str] = ...,
            version: Optional[str] = ...,
        ) -> None: ...

    class Auth(_message.Message):
        __slots__ = ["access_levels", "audiences", "claims", "presenter", "principal"]
        ACCESS_LEVELS_FIELD_NUMBER: ClassVar[int]
        AUDIENCES_FIELD_NUMBER: ClassVar[int]
        CLAIMS_FIELD_NUMBER: ClassVar[int]
        PRESENTER_FIELD_NUMBER: ClassVar[int]
        PRINCIPAL_FIELD_NUMBER: ClassVar[int]
        access_levels: _containers.RepeatedScalarFieldContainer[str]
        audiences: _containers.RepeatedScalarFieldContainer[str]
        claims: _struct_pb2.Struct
        presenter: str
        principal: str
        def __init__(
            self,
            principal: Optional[str] = ...,
            audiences: Optional[Iterable[str]] = ...,
            presenter: Optional[str] = ...,
            claims: Optional[Union[_struct_pb2.Struct, Mapping]] = ...,
            access_levels: Optional[Iterable[str]] = ...,
        ) -> None: ...

    class Peer(_message.Message):
        __slots__ = ["ip", "labels", "port", "principal", "region_code"]

        class LabelsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: ClassVar[int]
            VALUE_FIELD_NUMBER: ClassVar[int]
            key: str
            value: str
            def __init__(
                self, key: Optional[str] = ..., value: Optional[str] = ...
            ) -> None: ...
        IP_FIELD_NUMBER: ClassVar[int]
        LABELS_FIELD_NUMBER: ClassVar[int]
        PORT_FIELD_NUMBER: ClassVar[int]
        PRINCIPAL_FIELD_NUMBER: ClassVar[int]
        REGION_CODE_FIELD_NUMBER: ClassVar[int]
        ip: str
        labels: _containers.ScalarMap[str, str]
        port: int
        principal: str
        region_code: str
        def __init__(
            self,
            ip: Optional[str] = ...,
            port: Optional[int] = ...,
            labels: Optional[Mapping[str, str]] = ...,
            principal: Optional[str] = ...,
            region_code: Optional[str] = ...,
        ) -> None: ...

    class Request(_message.Message):
        __slots__ = [
            "auth",
            "headers",
            "host",
            "id",
            "method",
            "path",
            "protocol",
            "query",
            "reason",
            "scheme",
            "size",
            "time",
        ]

        class HeadersEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: ClassVar[int]
            VALUE_FIELD_NUMBER: ClassVar[int]
            key: str
            value: str
            def __init__(
                self, key: Optional[str] = ..., value: Optional[str] = ...
            ) -> None: ...
        AUTH_FIELD_NUMBER: ClassVar[int]
        HEADERS_FIELD_NUMBER: ClassVar[int]
        HOST_FIELD_NUMBER: ClassVar[int]
        ID_FIELD_NUMBER: ClassVar[int]
        METHOD_FIELD_NUMBER: ClassVar[int]
        PATH_FIELD_NUMBER: ClassVar[int]
        PROTOCOL_FIELD_NUMBER: ClassVar[int]
        QUERY_FIELD_NUMBER: ClassVar[int]
        REASON_FIELD_NUMBER: ClassVar[int]
        SCHEME_FIELD_NUMBER: ClassVar[int]
        SIZE_FIELD_NUMBER: ClassVar[int]
        TIME_FIELD_NUMBER: ClassVar[int]
        auth: AttributeContext.Auth
        headers: _containers.ScalarMap[str, str]
        host: str
        id: str
        method: str
        path: str
        protocol: str
        query: str
        reason: str
        scheme: str
        size: int
        time: _timestamp_pb2.Timestamp
        def __init__(
            self,
            id: Optional[str] = ...,
            method: Optional[str] = ...,
            headers: Optional[Mapping[str, str]] = ...,
            path: Optional[str] = ...,
            host: Optional[str] = ...,
            scheme: Optional[str] = ...,
            query: Optional[str] = ...,
            time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
            size: Optional[int] = ...,
            protocol: Optional[str] = ...,
            reason: Optional[str] = ...,
            auth: Optional[Union[AttributeContext.Auth, Mapping]] = ...,
        ) -> None: ...

    class Resource(_message.Message):
        __slots__ = [
            "annotations",
            "create_time",
            "delete_time",
            "display_name",
            "etag",
            "labels",
            "location",
            "name",
            "service",
            "type",
            "uid",
            "update_time",
        ]

        class AnnotationsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: ClassVar[int]
            VALUE_FIELD_NUMBER: ClassVar[int]
            key: str
            value: str
            def __init__(
                self, key: Optional[str] = ..., value: Optional[str] = ...
            ) -> None: ...

        class LabelsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: ClassVar[int]
            VALUE_FIELD_NUMBER: ClassVar[int]
            key: str
            value: str
            def __init__(
                self, key: Optional[str] = ..., value: Optional[str] = ...
            ) -> None: ...
        ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
        CREATE_TIME_FIELD_NUMBER: ClassVar[int]
        DELETE_TIME_FIELD_NUMBER: ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: ClassVar[int]
        ETAG_FIELD_NUMBER: ClassVar[int]
        LABELS_FIELD_NUMBER: ClassVar[int]
        LOCATION_FIELD_NUMBER: ClassVar[int]
        NAME_FIELD_NUMBER: ClassVar[int]
        SERVICE_FIELD_NUMBER: ClassVar[int]
        TYPE_FIELD_NUMBER: ClassVar[int]
        UID_FIELD_NUMBER: ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: ClassVar[int]
        annotations: _containers.ScalarMap[str, str]
        create_time: _timestamp_pb2.Timestamp
        delete_time: _timestamp_pb2.Timestamp
        display_name: str
        etag: str
        labels: _containers.ScalarMap[str, str]
        location: str
        name: str
        service: str
        type: str
        uid: str
        update_time: _timestamp_pb2.Timestamp
        def __init__(
            self,
            service: Optional[str] = ...,
            name: Optional[str] = ...,
            type: Optional[str] = ...,
            labels: Optional[Mapping[str, str]] = ...,
            uid: Optional[str] = ...,
            annotations: Optional[Mapping[str, str]] = ...,
            display_name: Optional[str] = ...,
            create_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
            update_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
            delete_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
            etag: Optional[str] = ...,
            location: Optional[str] = ...,
        ) -> None: ...

    class Response(_message.Message):
        __slots__ = ["backend_latency", "code", "headers", "size", "time"]

        class HeadersEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: ClassVar[int]
            VALUE_FIELD_NUMBER: ClassVar[int]
            key: str
            value: str
            def __init__(
                self, key: Optional[str] = ..., value: Optional[str] = ...
            ) -> None: ...
        BACKEND_LATENCY_FIELD_NUMBER: ClassVar[int]
        CODE_FIELD_NUMBER: ClassVar[int]
        HEADERS_FIELD_NUMBER: ClassVar[int]
        SIZE_FIELD_NUMBER: ClassVar[int]
        TIME_FIELD_NUMBER: ClassVar[int]
        backend_latency: _duration_pb2.Duration
        code: int
        headers: _containers.ScalarMap[str, str]
        size: int
        time: _timestamp_pb2.Timestamp
        def __init__(
            self,
            code: Optional[int] = ...,
            size: Optional[int] = ...,
            headers: Optional[Mapping[str, str]] = ...,
            time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
            backend_latency: Optional[Union[_duration_pb2.Duration, Mapping]] = ...,
        ) -> None: ...
    API_FIELD_NUMBER: ClassVar[int]
    DESTINATION_FIELD_NUMBER: ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: ClassVar[int]
    ORIGIN_FIELD_NUMBER: ClassVar[int]
    REQUEST_FIELD_NUMBER: ClassVar[int]
    RESOURCE_FIELD_NUMBER: ClassVar[int]
    RESPONSE_FIELD_NUMBER: ClassVar[int]
    SOURCE_FIELD_NUMBER: ClassVar[int]
    api: AttributeContext.Api
    destination: AttributeContext.Peer
    extensions: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    origin: AttributeContext.Peer
    request: AttributeContext.Request
    resource: AttributeContext.Resource
    response: AttributeContext.Response
    source: AttributeContext.Peer
    def __init__(
        self,
        origin: Optional[Union[AttributeContext.Peer, Mapping]] = ...,
        source: Optional[Union[AttributeContext.Peer, Mapping]] = ...,
        destination: Optional[Union[AttributeContext.Peer, Mapping]] = ...,
        request: Optional[Union[AttributeContext.Request, Mapping]] = ...,
        response: Optional[Union[AttributeContext.Response, Mapping]] = ...,
        resource: Optional[Union[AttributeContext.Resource, Mapping]] = ...,
        api: Optional[Union[AttributeContext.Api, Mapping]] = ...,
        extensions: Optional[Iterable[Union[_any_pb2.Any, Mapping]]] = ...,
    ) -> None: ...
