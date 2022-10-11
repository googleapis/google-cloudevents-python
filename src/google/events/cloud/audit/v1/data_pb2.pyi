from typing import ClassVar, Iterable, Mapping, Optional, Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from google.api import monitored_resource_pb2 as _monitored_resource_pb2
from google.rpc import status_pb2 as _status_pb2
from google.rpc.context import attribute_context_pb2 as _attribute_context_pb2

ALERT: LogSeverity
CRITICAL: LogSeverity
DEBUG: LogSeverity
DEFAULT: LogSeverity
DESCRIPTOR: _descriptor.FileDescriptor
EMERGENCY: LogSeverity
ERROR: LogSeverity
INFO: LogSeverity
NOTICE: LogSeverity
WARNING: LogSeverity

class AuditLog(_message.Message):
    __slots__ = [
        "authentication_info",
        "authorization_info",
        "metadata",
        "method_name",
        "num_response_items",
        "request",
        "request_metadata",
        "resource_location",
        "resource_name",
        "resource_original_state",
        "response",
        "service_data",
        "service_name",
        "status",
    ]
    AUTHENTICATION_INFO_FIELD_NUMBER: ClassVar[int]
    AUTHORIZATION_INFO_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: ClassVar[int]
    NUM_RESPONSE_ITEMS_FIELD_NUMBER: ClassVar[int]
    REQUEST_FIELD_NUMBER: ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: ClassVar[int]
    RESOURCE_LOCATION_FIELD_NUMBER: ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: ClassVar[int]
    RESOURCE_ORIGINAL_STATE_FIELD_NUMBER: ClassVar[int]
    RESPONSE_FIELD_NUMBER: ClassVar[int]
    SERVICE_DATA_FIELD_NUMBER: ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    authentication_info: AuthenticationInfo
    authorization_info: _containers.RepeatedCompositeFieldContainer[AuthorizationInfo]
    metadata: _struct_pb2.Struct
    method_name: str
    num_response_items: int
    request: _struct_pb2.Struct
    request_metadata: RequestMetadata
    resource_location: ResourceLocation
    resource_name: str
    resource_original_state: _struct_pb2.Struct
    response: _struct_pb2.Struct
    service_data: _struct_pb2.Struct
    service_name: str
    status: _status_pb2.Status
    def __init__(
        self,
        service_name: Optional[str] = ...,
        method_name: Optional[str] = ...,
        resource_name: Optional[str] = ...,
        resource_location: Optional[Union[ResourceLocation, Mapping]] = ...,
        resource_original_state: Optional[Union[_struct_pb2.Struct, Mapping]] = ...,
        num_response_items: Optional[int] = ...,
        status: Optional[Union[_status_pb2.Status, Mapping]] = ...,
        authentication_info: Optional[Union[AuthenticationInfo, Mapping]] = ...,
        authorization_info: Optional[Iterable[Union[AuthorizationInfo, Mapping]]] = ...,
        request_metadata: Optional[Union[RequestMetadata, Mapping]] = ...,
        request: Optional[Union[_struct_pb2.Struct, Mapping]] = ...,
        response: Optional[Union[_struct_pb2.Struct, Mapping]] = ...,
        metadata: Optional[Union[_struct_pb2.Struct, Mapping]] = ...,
        service_data: Optional[Union[_struct_pb2.Struct, Mapping]] = ...,
    ) -> None: ...

class AuthenticationInfo(_message.Message):
    __slots__ = [
        "authority_selector",
        "principal_email",
        "principal_subject",
        "service_account_delegation_info",
        "service_account_key_name",
        "third_party_principal",
    ]
    AUTHORITY_SELECTOR_FIELD_NUMBER: ClassVar[int]
    PRINCIPAL_EMAIL_FIELD_NUMBER: ClassVar[int]
    PRINCIPAL_SUBJECT_FIELD_NUMBER: ClassVar[int]
    SERVICE_ACCOUNT_DELEGATION_INFO_FIELD_NUMBER: ClassVar[int]
    SERVICE_ACCOUNT_KEY_NAME_FIELD_NUMBER: ClassVar[int]
    THIRD_PARTY_PRINCIPAL_FIELD_NUMBER: ClassVar[int]
    authority_selector: str
    principal_email: str
    principal_subject: str
    service_account_delegation_info: _containers.RepeatedCompositeFieldContainer[
        ServiceAccountDelegationInfo
    ]
    service_account_key_name: str
    third_party_principal: _struct_pb2.Struct
    def __init__(
        self,
        principal_email: Optional[str] = ...,
        authority_selector: Optional[str] = ...,
        third_party_principal: Optional[Union[_struct_pb2.Struct, Mapping]] = ...,
        service_account_key_name: Optional[str] = ...,
        service_account_delegation_info: Optional[
            Iterable[Union[ServiceAccountDelegationInfo, Mapping]]
        ] = ...,
        principal_subject: Optional[str] = ...,
    ) -> None: ...

class AuthorizationInfo(_message.Message):
    __slots__ = ["granted", "permission", "resource", "resource_attributes"]
    GRANTED_FIELD_NUMBER: ClassVar[int]
    PERMISSION_FIELD_NUMBER: ClassVar[int]
    RESOURCE_ATTRIBUTES_FIELD_NUMBER: ClassVar[int]
    RESOURCE_FIELD_NUMBER: ClassVar[int]
    granted: bool
    permission: str
    resource: str
    resource_attributes: _attribute_context_pb2.AttributeContext.Resource
    def __init__(
        self,
        resource: Optional[str] = ...,
        permission: Optional[str] = ...,
        granted: bool = ...,
        resource_attributes: Optional[
            Union[_attribute_context_pb2.AttributeContext.Resource, Mapping]
        ] = ...,
    ) -> None: ...

class LogEntryData(_message.Message):
    __slots__ = [
        "insert_id",
        "labels",
        "log_name",
        "operation",
        "proto_payload",
        "receive_timestamp",
        "resource",
        "severity",
        "span_id",
        "split",
        "timestamp",
        "trace",
    ]

    class LabelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: Optional[str] = ..., value: Optional[str] = ...
        ) -> None: ...
    INSERT_ID_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    LOG_NAME_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    PROTO_PAYLOAD_FIELD_NUMBER: ClassVar[int]
    RECEIVE_TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    RESOURCE_FIELD_NUMBER: ClassVar[int]
    SEVERITY_FIELD_NUMBER: ClassVar[int]
    SPAN_ID_FIELD_NUMBER: ClassVar[int]
    SPLIT_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    TRACE_FIELD_NUMBER: ClassVar[int]
    insert_id: str
    labels: _containers.ScalarMap[str, str]
    log_name: str
    operation: LogEntryOperation
    proto_payload: AuditLog
    receive_timestamp: _timestamp_pb2.Timestamp
    resource: _monitored_resource_pb2.MonitoredResource
    severity: LogSeverity
    span_id: str
    split: LogSplit
    timestamp: _timestamp_pb2.Timestamp
    trace: str
    def __init__(
        self,
        log_name: Optional[str] = ...,
        resource: Optional[
            Union[_monitored_resource_pb2.MonitoredResource, Mapping]
        ] = ...,
        proto_payload: Optional[Union[AuditLog, Mapping]] = ...,
        insert_id: Optional[str] = ...,
        labels: Optional[Mapping[str, str]] = ...,
        operation: Optional[Union[LogEntryOperation, Mapping]] = ...,
        timestamp: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        receive_timestamp: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        severity: Optional[Union[LogSeverity, str]] = ...,
        trace: Optional[str] = ...,
        span_id: Optional[str] = ...,
        split: Optional[Union[LogSplit, Mapping]] = ...,
    ) -> None: ...

class LogEntryOperation(_message.Message):
    __slots__ = ["first", "id", "last", "producer"]
    FIRST_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    LAST_FIELD_NUMBER: ClassVar[int]
    PRODUCER_FIELD_NUMBER: ClassVar[int]
    first: bool
    id: str
    last: bool
    producer: str
    def __init__(
        self,
        id: Optional[str] = ...,
        producer: Optional[str] = ...,
        first: bool = ...,
        last: bool = ...,
    ) -> None: ...

class LogSplit(_message.Message):
    __slots__ = ["index", "total_splits", "uid"]
    INDEX_FIELD_NUMBER: ClassVar[int]
    TOTAL_SPLITS_FIELD_NUMBER: ClassVar[int]
    UID_FIELD_NUMBER: ClassVar[int]
    index: int
    total_splits: int
    uid: str
    def __init__(
        self,
        uid: Optional[str] = ...,
        index: Optional[int] = ...,
        total_splits: Optional[int] = ...,
    ) -> None: ...

class RequestMetadata(_message.Message):
    __slots__ = [
        "caller_ip",
        "caller_network",
        "caller_supplied_user_agent",
        "destination_attributes",
        "request_attributes",
    ]
    CALLER_IP_FIELD_NUMBER: ClassVar[int]
    CALLER_NETWORK_FIELD_NUMBER: ClassVar[int]
    CALLER_SUPPLIED_USER_AGENT_FIELD_NUMBER: ClassVar[int]
    DESTINATION_ATTRIBUTES_FIELD_NUMBER: ClassVar[int]
    REQUEST_ATTRIBUTES_FIELD_NUMBER: ClassVar[int]
    caller_ip: str
    caller_network: str
    caller_supplied_user_agent: str
    destination_attributes: _attribute_context_pb2.AttributeContext.Peer
    request_attributes: _attribute_context_pb2.AttributeContext.Request
    def __init__(
        self,
        caller_ip: Optional[str] = ...,
        caller_supplied_user_agent: Optional[str] = ...,
        caller_network: Optional[str] = ...,
        request_attributes: Optional[
            Union[_attribute_context_pb2.AttributeContext.Request, Mapping]
        ] = ...,
        destination_attributes: Optional[
            Union[_attribute_context_pb2.AttributeContext.Peer, Mapping]
        ] = ...,
    ) -> None: ...

class ResourceLocation(_message.Message):
    __slots__ = ["current_locations", "original_locations"]
    CURRENT_LOCATIONS_FIELD_NUMBER: ClassVar[int]
    ORIGINAL_LOCATIONS_FIELD_NUMBER: ClassVar[int]
    current_locations: _containers.RepeatedScalarFieldContainer[str]
    original_locations: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        current_locations: Optional[Iterable[str]] = ...,
        original_locations: Optional[Iterable[str]] = ...,
    ) -> None: ...

class ServiceAccountDelegationInfo(_message.Message):
    __slots__ = ["first_party_principal", "third_party_principal"]

    class FirstPartyPrincipal(_message.Message):
        __slots__ = ["principal_email", "service_metadata"]
        PRINCIPAL_EMAIL_FIELD_NUMBER: ClassVar[int]
        SERVICE_METADATA_FIELD_NUMBER: ClassVar[int]
        principal_email: str
        service_metadata: _struct_pb2.Struct
        def __init__(
            self,
            principal_email: Optional[str] = ...,
            service_metadata: Optional[Union[_struct_pb2.Struct, Mapping]] = ...,
        ) -> None: ...

    class ThirdPartyPrincipal(_message.Message):
        __slots__ = ["third_party_claims"]
        THIRD_PARTY_CLAIMS_FIELD_NUMBER: ClassVar[int]
        third_party_claims: _struct_pb2.Struct
        def __init__(
            self, third_party_claims: Optional[Union[_struct_pb2.Struct, Mapping]] = ...
        ) -> None: ...
    FIRST_PARTY_PRINCIPAL_FIELD_NUMBER: ClassVar[int]
    THIRD_PARTY_PRINCIPAL_FIELD_NUMBER: ClassVar[int]
    first_party_principal: ServiceAccountDelegationInfo.FirstPartyPrincipal
    third_party_principal: ServiceAccountDelegationInfo.ThirdPartyPrincipal
    def __init__(
        self,
        first_party_principal: Optional[
            Union[ServiceAccountDelegationInfo.FirstPartyPrincipal, Mapping]
        ] = ...,
        third_party_principal: Optional[
            Union[ServiceAccountDelegationInfo.ThirdPartyPrincipal, Mapping]
        ] = ...,
    ) -> None: ...

class LogSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
