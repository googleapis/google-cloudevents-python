from typing import ClassVar, Iterable, Mapping, Optional, Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class BadRequest(_message.Message):
    __slots__ = ["field_violations"]

    class FieldViolation(_message.Message):
        __slots__ = ["description", "field"]
        DESCRIPTION_FIELD_NUMBER: ClassVar[int]
        FIELD_FIELD_NUMBER: ClassVar[int]
        description: str
        field: str
        def __init__(
            self, field: Optional[str] = ..., description: Optional[str] = ...
        ) -> None: ...
    FIELD_VIOLATIONS_FIELD_NUMBER: ClassVar[int]
    field_violations: _containers.RepeatedCompositeFieldContainer[
        BadRequest.FieldViolation
    ]
    def __init__(
        self,
        field_violations: Optional[
            Iterable[Union[BadRequest.FieldViolation, Mapping]]
        ] = ...,
    ) -> None: ...

class DebugInfo(_message.Message):
    __slots__ = ["detail", "stack_entries"]
    DETAIL_FIELD_NUMBER: ClassVar[int]
    STACK_ENTRIES_FIELD_NUMBER: ClassVar[int]
    detail: str
    stack_entries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self, stack_entries: Optional[Iterable[str]] = ..., detail: Optional[str] = ...
    ) -> None: ...

class ErrorInfo(_message.Message):
    __slots__ = ["domain", "metadata", "reason"]

    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: Optional[str] = ..., value: Optional[str] = ...
        ) -> None: ...
    DOMAIN_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    REASON_FIELD_NUMBER: ClassVar[int]
    domain: str
    metadata: _containers.ScalarMap[str, str]
    reason: str
    def __init__(
        self,
        reason: Optional[str] = ...,
        domain: Optional[str] = ...,
        metadata: Optional[Mapping[str, str]] = ...,
    ) -> None: ...

class Help(_message.Message):
    __slots__ = ["links"]

    class Link(_message.Message):
        __slots__ = ["description", "url"]
        DESCRIPTION_FIELD_NUMBER: ClassVar[int]
        URL_FIELD_NUMBER: ClassVar[int]
        description: str
        url: str
        def __init__(
            self, description: Optional[str] = ..., url: Optional[str] = ...
        ) -> None: ...
    LINKS_FIELD_NUMBER: ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[Help.Link]
    def __init__(
        self, links: Optional[Iterable[Union[Help.Link, Mapping]]] = ...
    ) -> None: ...

class LocalizedMessage(_message.Message):
    __slots__ = ["locale", "message"]
    LOCALE_FIELD_NUMBER: ClassVar[int]
    MESSAGE_FIELD_NUMBER: ClassVar[int]
    locale: str
    message: str
    def __init__(
        self, locale: Optional[str] = ..., message: Optional[str] = ...
    ) -> None: ...

class PreconditionFailure(_message.Message):
    __slots__ = ["violations"]

    class Violation(_message.Message):
        __slots__ = ["description", "subject", "type"]
        DESCRIPTION_FIELD_NUMBER: ClassVar[int]
        SUBJECT_FIELD_NUMBER: ClassVar[int]
        TYPE_FIELD_NUMBER: ClassVar[int]
        description: str
        subject: str
        type: str
        def __init__(
            self,
            type: Optional[str] = ...,
            subject: Optional[str] = ...,
            description: Optional[str] = ...,
        ) -> None: ...
    VIOLATIONS_FIELD_NUMBER: ClassVar[int]
    violations: _containers.RepeatedCompositeFieldContainer[
        PreconditionFailure.Violation
    ]
    def __init__(
        self,
        violations: Optional[
            Iterable[Union[PreconditionFailure.Violation, Mapping]]
        ] = ...,
    ) -> None: ...

class QuotaFailure(_message.Message):
    __slots__ = ["violations"]

    class Violation(_message.Message):
        __slots__ = ["description", "subject"]
        DESCRIPTION_FIELD_NUMBER: ClassVar[int]
        SUBJECT_FIELD_NUMBER: ClassVar[int]
        description: str
        subject: str
        def __init__(
            self, subject: Optional[str] = ..., description: Optional[str] = ...
        ) -> None: ...
    VIOLATIONS_FIELD_NUMBER: ClassVar[int]
    violations: _containers.RepeatedCompositeFieldContainer[QuotaFailure.Violation]
    def __init__(
        self,
        violations: Optional[Iterable[Union[QuotaFailure.Violation, Mapping]]] = ...,
    ) -> None: ...

class RequestInfo(_message.Message):
    __slots__ = ["request_id", "serving_data"]
    REQUEST_ID_FIELD_NUMBER: ClassVar[int]
    SERVING_DATA_FIELD_NUMBER: ClassVar[int]
    request_id: str
    serving_data: str
    def __init__(
        self, request_id: Optional[str] = ..., serving_data: Optional[str] = ...
    ) -> None: ...

class ResourceInfo(_message.Message):
    __slots__ = ["description", "owner", "resource_name", "resource_type"]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    OWNER_FIELD_NUMBER: ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: ClassVar[int]
    description: str
    owner: str
    resource_name: str
    resource_type: str
    def __init__(
        self,
        resource_type: Optional[str] = ...,
        resource_name: Optional[str] = ...,
        owner: Optional[str] = ...,
        description: Optional[str] = ...,
    ) -> None: ...

class RetryInfo(_message.Message):
    __slots__ = ["retry_delay"]
    RETRY_DELAY_FIELD_NUMBER: ClassVar[int]
    retry_delay: _duration_pb2.Duration
    def __init__(
        self, retry_delay: Optional[Union[_duration_pb2.Duration, Mapping]] = ...
    ) -> None: ...
