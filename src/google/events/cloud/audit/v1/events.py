# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = events_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Dict, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class ServiceAccountDelegationInfo:
    principal_email: Optional[str] = None
    service_metadata: Optional[Dict[str, Any]] = None
    third_party_claims: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ServiceAccountDelegationInfo':
        assert isinstance(obj, dict)
        principal_email = from_union([from_str, from_none], obj.get("principalEmail"))
        service_metadata = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("serviceMetadata"))
        third_party_claims = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("thirdPartyClaims"))
        return ServiceAccountDelegationInfo(principal_email, service_metadata, third_party_claims)

    def to_dict(self) -> dict:
        result: dict = {}
        result["principalEmail"] = from_union([from_str, from_none], self.principal_email)
        result["serviceMetadata"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.service_metadata)
        result["thirdPartyClaims"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.third_party_claims)
        return result


@dataclass
class AuthenticationInfo:
    authority_selector: Optional[str] = None
    principal_subject: Optional[str] = None
    principle_email: Optional[str] = None
    service_account_delegation_info: Optional[List[ServiceAccountDelegationInfo]] = None
    service_account_key_name: Optional[str] = None
    third_party_principal: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthenticationInfo':
        assert isinstance(obj, dict)
        authority_selector = from_union([from_str, from_none], obj.get("authoritySelector"))
        principal_subject = from_union([from_str, from_none], obj.get("principalSubject"))
        principle_email = from_union([from_str, from_none], obj.get("principleEmail"))
        service_account_delegation_info = from_union([lambda x: from_list(ServiceAccountDelegationInfo.from_dict, x), from_none], obj.get("serviceAccountDelegationInfo"))
        service_account_key_name = from_union([from_str, from_none], obj.get("serviceAccountKeyName"))
        third_party_principal = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("thirdPartyPrincipal"))
        return AuthenticationInfo(authority_selector, principal_subject, principle_email, service_account_delegation_info, service_account_key_name, third_party_principal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authoritySelector"] = from_union([from_str, from_none], self.authority_selector)
        result["principalSubject"] = from_union([from_str, from_none], self.principal_subject)
        result["principleEmail"] = from_union([from_str, from_none], self.principle_email)
        result["serviceAccountDelegationInfo"] = from_union([lambda x: from_list(lambda x: to_class(ServiceAccountDelegationInfo, x), x), from_none], self.service_account_delegation_info)
        result["serviceAccountKeyName"] = from_union([from_str, from_none], self.service_account_key_name)
        result["thirdPartyPrincipal"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.third_party_principal)
        return result


@dataclass
class ResourceAttributes:
    labels: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    service: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResourceAttributes':
        assert isinstance(obj, dict)
        labels = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("labels"))
        name = from_union([from_str, from_none], obj.get("name"))
        service = from_union([from_str, from_none], obj.get("service"))
        type = from_union([from_str, from_none], obj.get("type"))
        return ResourceAttributes(labels, name, service, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["labels"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.labels)
        result["name"] = from_union([from_str, from_none], self.name)
        result["service"] = from_union([from_str, from_none], self.service)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class AuthorizationInfo:
    granted: Optional[bool] = None
    permission: Optional[str] = None
    resource_attributes: Optional[ResourceAttributes] = None
    response: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthorizationInfo':
        assert isinstance(obj, dict)
        granted = from_union([from_bool, from_none], obj.get("granted"))
        permission = from_union([from_str, from_none], obj.get("permission"))
        resource_attributes = from_union([ResourceAttributes.from_dict, from_none], obj.get("resourceAttributes"))
        response = from_union([from_str, from_none], obj.get("response"))
        return AuthorizationInfo(granted, permission, resource_attributes, response)

    def to_dict(self) -> dict:
        result: dict = {}
        result["granted"] = from_union([from_bool, from_none], self.granted)
        result["permission"] = from_union([from_str, from_none], self.permission)
        result["resourceAttributes"] = from_union([lambda x: to_class(ResourceAttributes, x), from_none], self.resource_attributes)
        result["response"] = from_union([from_str, from_none], self.response)
        return result


@dataclass
class Peer:
    ip: Optional[str] = None
    labels: Optional[Dict[str, Any]] = None
    port: Optional[int] = None
    principal: Optional[str] = None
    region_code: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Peer':
        assert isinstance(obj, dict)
        ip = from_union([from_str, from_none], obj.get("ip"))
        labels = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("labels"))
        port = from_union([from_int, from_none], obj.get("port"))
        principal = from_union([from_str, from_none], obj.get("principal"))
        region_code = from_union([from_str, from_none], obj.get("regionCode"))
        return Peer(ip, labels, port, principal, region_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ip"] = from_union([from_str, from_none], self.ip)
        result["labels"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.labels)
        result["port"] = from_union([from_int, from_none], self.port)
        result["principal"] = from_union([from_str, from_none], self.principal)
        result["regionCode"] = from_union([from_str, from_none], self.region_code)
        return result


@dataclass
class Auth:
    access_levels: Optional[List[str]] = None
    audiences: Optional[List[str]] = None
    claims: Optional[Dict[str, Any]] = None
    presenter: Optional[str] = None
    principal: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Auth':
        assert isinstance(obj, dict)
        access_levels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("accessLevels"))
        audiences = from_union([lambda x: from_list(from_str, x), from_none], obj.get("audiences"))
        claims = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("claims"))
        presenter = from_union([from_str, from_none], obj.get("presenter"))
        principal = from_union([from_str, from_none], obj.get("principal"))
        return Auth(access_levels, audiences, claims, presenter, principal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["accessLevels"] = from_union([lambda x: from_list(from_str, x), from_none], self.access_levels)
        result["audiences"] = from_union([lambda x: from_list(from_str, x), from_none], self.audiences)
        result["claims"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.claims)
        result["presenter"] = from_union([from_str, from_none], self.presenter)
        result["principal"] = from_union([from_str, from_none], self.principal)
        return result


@dataclass
class Request:
    protocol: Optional[str] = None
    auth: Optional[Auth] = None
    host: Optional[str] = None
    id: Optional[str] = None
    method: Optional[str] = None
    path: Optional[str] = None
    headers: Optional[Dict[str, Any]] = None
    query: Optional[str] = None
    reason: Optional[str] = None
    scheme: Optional[str] = None
    size: Optional[int] = None
    time: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Request':
        assert isinstance(obj, dict)
        protocol = from_union([from_str, from_none], obj.get("protocol"))
        auth = from_union([Auth.from_dict, from_none], obj.get("auth"))
        host = from_union([from_str, from_none], obj.get("host"))
        id = from_union([from_str, from_none], obj.get("id"))
        method = from_union([from_str, from_none], obj.get("method"))
        path = from_union([from_str, from_none], obj.get("path"))
        headers = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("headers"))
        query = from_union([from_str, from_none], obj.get("query"))
        reason = from_union([from_str, from_none], obj.get("reason"))
        scheme = from_union([from_str, from_none], obj.get("scheme"))
        size = from_union([from_int, from_none], obj.get("size"))
        time = from_union([from_str, from_none], obj.get("time"))
        return Request(protocol, auth, host, id, method, path, headers, query, reason, scheme, size, time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["protocol"] = from_union([from_str, from_none], self.protocol)
        result["auth"] = from_union([lambda x: to_class(Auth, x), from_none], self.auth)
        result["host"] = from_union([from_str, from_none], self.host)
        result["id"] = from_union([from_str, from_none], self.id)
        result["method"] = from_union([from_str, from_none], self.method)
        result["path"] = from_union([from_str, from_none], self.path)
        result["headers"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.headers)
        result["query"] = from_union([from_str, from_none], self.query)
        result["reason"] = from_union([from_str, from_none], self.reason)
        result["scheme"] = from_union([from_str, from_none], self.scheme)
        result["size"] = from_union([from_int, from_none], self.size)
        result["time"] = from_union([from_str, from_none], self.time)
        return result


@dataclass
class RequestMetadata:
    caller_ip: Optional[str] = None
    caller_network: Optional[str] = None
    caller_supplied_user_agent: Optional[str] = None
    destination_attributes: Optional[Peer] = None
    request_attributes: Optional[Request] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RequestMetadata':
        assert isinstance(obj, dict)
        caller_ip = from_union([from_str, from_none], obj.get("callerIp"))
        caller_network = from_union([from_str, from_none], obj.get("callerNetwork"))
        caller_supplied_user_agent = from_union([from_str, from_none], obj.get("callerSuppliedUserAgent"))
        destination_attributes = from_union([Peer.from_dict, from_none], obj.get("destinationAttributes"))
        request_attributes = from_union([Request.from_dict, from_none], obj.get("requestAttributes"))
        return RequestMetadata(caller_ip, caller_network, caller_supplied_user_agent, destination_attributes, request_attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["callerIp"] = from_union([from_str, from_none], self.caller_ip)
        result["callerNetwork"] = from_union([from_str, from_none], self.caller_network)
        result["callerSuppliedUserAgent"] = from_union([from_str, from_none], self.caller_supplied_user_agent)
        result["destinationAttributes"] = from_union([lambda x: to_class(Peer, x), from_none], self.destination_attributes)
        result["requestAttributes"] = from_union([lambda x: to_class(Request, x), from_none], self.request_attributes)
        return result


@dataclass
class ResourceLocation:
    current_locations: Optional[List[str]] = None
    original_locations: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResourceLocation':
        assert isinstance(obj, dict)
        current_locations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("currentLocations"))
        original_locations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("originalLocations"))
        return ResourceLocation(current_locations, original_locations)

    def to_dict(self) -> dict:
        result: dict = {}
        result["currentLocations"] = from_union([lambda x: from_list(from_str, x), from_none], self.current_locations)
        result["originalLocations"] = from_union([lambda x: from_list(from_str, x), from_none], self.original_locations)
        return result


@dataclass
class Status:
    code: Optional[int] = None
    details: Optional[List[Any]] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Status':
        assert isinstance(obj, dict)
        code = from_union([from_int, from_none], obj.get("code"))
        details = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("details"))
        message = from_union([from_str, from_none], obj.get("message"))
        return Status(code, details, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_union([from_int, from_none], self.code)
        result["details"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.details)
        result["message"] = from_union([from_str, from_none], self.message)
        return result


@dataclass
class AuditLogWrittenEvent:
    """The event is triggered when a new Cloud Audit Log entry is written."""
    resource_location: Optional[ResourceLocation] = None
    authentication_info: Optional[AuthenticationInfo] = None
    metadata: Optional[Dict[str, Any]] = None
    method_name: Optional[str] = None
    num_response_items: Optional[int] = None
    request: Optional[Dict[str, Any]] = None
    request_metadata: Optional[RequestMetadata] = None
    authorization_info: Optional[List[AuthorizationInfo]] = None
    resource_name: Optional[str] = None
    resource_original_state: Optional[Dict[str, Any]] = None
    response: Optional[Dict[str, Any]] = None
    service_data: Optional[Dict[str, Any]] = None
    service_name: Optional[str] = None
    status: Optional[Status] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuditLogWrittenEvent':
        assert isinstance(obj, dict)
        resource_location = from_union([ResourceLocation.from_dict, from_none], obj.get("resourceLocation"))
        authentication_info = from_union([AuthenticationInfo.from_dict, from_none], obj.get("authenticationInfo"))
        metadata = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("metadata"))
        method_name = from_union([from_str, from_none], obj.get("methodName"))
        num_response_items = from_union([from_int, from_none], obj.get("numResponseItems"))
        request = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("request"))
        request_metadata = from_union([RequestMetadata.from_dict, from_none], obj.get("requestMetadata"))
        authorization_info = from_union([lambda x: from_list(AuthorizationInfo.from_dict, x), from_none], obj.get("authorizationInfo"))
        resource_name = from_union([from_str, from_none], obj.get("resourceName"))
        resource_original_state = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("resourceOriginalState"))
        response = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("response"))
        service_data = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("serviceData"))
        service_name = from_union([from_str, from_none], obj.get("serviceName"))
        status = from_union([Status.from_dict, from_none], obj.get("status"))
        return AuditLogWrittenEvent(resource_location, authentication_info, metadata, method_name, num_response_items, request, request_metadata, authorization_info, resource_name, resource_original_state, response, service_data, service_name, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["resourceLocation"] = from_union([lambda x: to_class(ResourceLocation, x), from_none], self.resource_location)
        result["authenticationInfo"] = from_union([lambda x: to_class(AuthenticationInfo, x), from_none], self.authentication_info)
        result["metadata"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.metadata)
        result["methodName"] = from_union([from_str, from_none], self.method_name)
        result["numResponseItems"] = from_union([from_int, from_none], self.num_response_items)
        result["request"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.request)
        result["requestMetadata"] = from_union([lambda x: to_class(RequestMetadata, x), from_none], self.request_metadata)
        result["authorizationInfo"] = from_union([lambda x: from_list(lambda x: to_class(AuthorizationInfo, x), x), from_none], self.authorization_info)
        result["resourceName"] = from_union([from_str, from_none], self.resource_name)
        result["resourceOriginalState"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.resource_original_state)
        result["response"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.response)
        result["serviceData"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.service_data)
        result["serviceName"] = from_union([from_str, from_none], self.service_name)
        result["status"] = from_union([lambda x: to_class(Status, x), from_none], self.status)
        return result


@dataclass
class Events:
    """The event is triggered when a new Cloud Audit Log entry is written."""
    audit_log_written_event: Optional[AuditLogWrittenEvent] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Events':
        assert isinstance(obj, dict)
        audit_log_written_event = from_union([AuditLogWrittenEvent.from_dict, from_none], obj.get("AuditLogWrittenEvent"))
        return Events(audit_log_written_event)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AuditLogWrittenEvent"] = from_union([lambda x: to_class(AuditLogWrittenEvent, x), from_none], self.audit_log_written_event)
        return result


def events_from_dict(s: Any) -> Events:
    return Events.from_dict(s)


def events_to_dict(x: Events) -> Any:
    return to_class(Events, x)
