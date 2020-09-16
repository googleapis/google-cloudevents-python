# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = event_from_dict(json.loads(json_string))

from typing import Optional, Any, Dict, List, Union, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


class LogEntryOperation:
    first: Optional[bool]
    id: Optional[str]
    last: Optional[bool]
    producer: Optional[str]

    def __init__(self, first: Optional[bool], id: Optional[str], last: Optional[bool], producer: Optional[str]) -> None:
        self.first = first
        self.id = id
        self.last = last
        self.producer = producer

    @staticmethod
    def from_dict(obj: Any) -> 'LogEntryOperation':
        assert isinstance(obj, dict)
        first = from_union([from_bool, from_none], obj.get("first"))
        id = from_union([from_str, from_none], obj.get("id"))
        last = from_union([from_bool, from_none], obj.get("last"))
        producer = from_union([from_str, from_none], obj.get("producer"))
        return LogEntryOperation(first, id, last, producer)

    def to_dict(self) -> dict:
        result: dict = {}
        result["first"] = from_union([from_bool, from_none], self.first)
        result["id"] = from_union([from_str, from_none], self.id)
        result["last"] = from_union([from_bool, from_none], self.last)
        result["producer"] = from_union([from_str, from_none], self.producer)
        return result


class ServiceAccountDelegationInfo:
    principal_email: Optional[str]
    service_metadata: Optional[Dict[str, Any]]
    third_party_claims: Optional[Dict[str, Any]]

    def __init__(self, principal_email: Optional[str], service_metadata: Optional[Dict[str, Any]], third_party_claims: Optional[Dict[str, Any]]) -> None:
        self.principal_email = principal_email
        self.service_metadata = service_metadata
        self.third_party_claims = third_party_claims

    @staticmethod
    def from_dict(obj: Any) -> 'ServiceAccountDelegationInfo':
        assert isinstance(obj, dict)
        principal_email = from_union([from_str, from_none], obj.get("principal_email"))
        service_metadata = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("service_metadata"))
        third_party_claims = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("third_party_claims"))
        return ServiceAccountDelegationInfo(principal_email, service_metadata, third_party_claims)

    def to_dict(self) -> dict:
        result: dict = {}
        result["principal_email"] = from_union([from_str, from_none], self.principal_email)
        result["service_metadata"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.service_metadata)
        result["third_party_claims"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.third_party_claims)
        return result


class AuthenticationInfo:
    authority_selector: Optional[str]
    principal_email: Optional[str]
    principal_subject: Optional[str]
    service_account_delegation_info: Optional[List[ServiceAccountDelegationInfo]]
    service_account_key_name: Optional[str]
    third_party_principal: Optional[Dict[str, Any]]

    def __init__(self, authority_selector: Optional[str], principal_email: Optional[str], principal_subject: Optional[str], service_account_delegation_info: Optional[List[ServiceAccountDelegationInfo]], service_account_key_name: Optional[str], third_party_principal: Optional[Dict[str, Any]]) -> None:
        self.authority_selector = authority_selector
        self.principal_email = principal_email
        self.principal_subject = principal_subject
        self.service_account_delegation_info = service_account_delegation_info
        self.service_account_key_name = service_account_key_name
        self.third_party_principal = third_party_principal

    @staticmethod
    def from_dict(obj: Any) -> 'AuthenticationInfo':
        assert isinstance(obj, dict)
        authority_selector = from_union([from_str, from_none], obj.get("authority_selector"))
        principal_email = from_union([from_str, from_none], obj.get("principal_email"))
        principal_subject = from_union([from_str, from_none], obj.get("principal_subject"))
        service_account_delegation_info = from_union([lambda x: from_list(ServiceAccountDelegationInfo.from_dict, x), from_none], obj.get("service_account_delegation_info"))
        service_account_key_name = from_union([from_str, from_none], obj.get("service_account_key_name"))
        third_party_principal = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("third_party_principal"))
        return AuthenticationInfo(authority_selector, principal_email, principal_subject, service_account_delegation_info, service_account_key_name, third_party_principal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authority_selector"] = from_union([from_str, from_none], self.authority_selector)
        result["principal_email"] = from_union([from_str, from_none], self.principal_email)
        result["principal_subject"] = from_union([from_str, from_none], self.principal_subject)
        result["service_account_delegation_info"] = from_union([lambda x: from_list(lambda x: to_class(ServiceAccountDelegationInfo, x), x), from_none], self.service_account_delegation_info)
        result["service_account_key_name"] = from_union([from_str, from_none], self.service_account_key_name)
        result["third_party_principal"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.third_party_principal)
        return result


class Resource:
    labels: Optional[Dict[str, Any]]
    name: Optional[str]
    service: Optional[str]
    type: Optional[str]

    def __init__(self, labels: Optional[Dict[str, Any]], name: Optional[str], service: Optional[str], type: Optional[str]) -> None:
        self.labels = labels
        self.name = name
        self.service = service
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Resource':
        assert isinstance(obj, dict)
        labels = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("labels"))
        name = from_union([from_str, from_none], obj.get("name"))
        service = from_union([from_str, from_none], obj.get("service"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Resource(labels, name, service, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["labels"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.labels)
        result["name"] = from_union([from_str, from_none], self.name)
        result["service"] = from_union([from_str, from_none], self.service)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


class AuthorizationInfo:
    granted: Optional[bool]
    permission: Optional[str]
    resource: Optional[str]
    resource_attributes: Optional[Resource]

    def __init__(self, granted: Optional[bool], permission: Optional[str], resource: Optional[str], resource_attributes: Optional[Resource]) -> None:
        self.granted = granted
        self.permission = permission
        self.resource = resource
        self.resource_attributes = resource_attributes

    @staticmethod
    def from_dict(obj: Any) -> 'AuthorizationInfo':
        assert isinstance(obj, dict)
        granted = from_union([from_bool, from_none], obj.get("granted"))
        permission = from_union([from_str, from_none], obj.get("permission"))
        resource = from_union([from_str, from_none], obj.get("resource"))
        resource_attributes = from_union([Resource.from_dict, from_none], obj.get("resource_attributes"))
        return AuthorizationInfo(granted, permission, resource, resource_attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["granted"] = from_union([from_bool, from_none], self.granted)
        result["permission"] = from_union([from_str, from_none], self.permission)
        result["resource"] = from_union([from_str, from_none], self.resource)
        result["resource_attributes"] = from_union([lambda x: to_class(Resource, x), from_none], self.resource_attributes)
        return result


class Peer:
    ip: Optional[str]
    labels: Optional[Dict[str, Any]]
    port: Optional[int]
    principal: Optional[str]
    region_code: Optional[str]

    def __init__(self, ip: Optional[str], labels: Optional[Dict[str, Any]], port: Optional[int], principal: Optional[str], region_code: Optional[str]) -> None:
        self.ip = ip
        self.labels = labels
        self.port = port
        self.principal = principal
        self.region_code = region_code

    @staticmethod
    def from_dict(obj: Any) -> 'Peer':
        assert isinstance(obj, dict)
        ip = from_union([from_str, from_none], obj.get("ip"))
        labels = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("labels"))
        port = from_union([from_int, from_none], obj.get("port"))
        principal = from_union([from_str, from_none], obj.get("principal"))
        region_code = from_union([from_str, from_none], obj.get("region_code"))
        return Peer(ip, labels, port, principal, region_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ip"] = from_union([from_str, from_none], self.ip)
        result["labels"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.labels)
        result["port"] = from_union([from_int, from_none], self.port)
        result["principal"] = from_union([from_str, from_none], self.principal)
        result["region_code"] = from_union([from_str, from_none], self.region_code)
        return result


class Auth:
    access_levels: Optional[List[str]]
    audiences: Optional[List[str]]
    claims: Optional[Dict[str, Any]]
    presenter: Optional[str]
    principal: Optional[str]

    def __init__(self, access_levels: Optional[List[str]], audiences: Optional[List[str]], claims: Optional[Dict[str, Any]], presenter: Optional[str], principal: Optional[str]) -> None:
        self.access_levels = access_levels
        self.audiences = audiences
        self.claims = claims
        self.presenter = presenter
        self.principal = principal

    @staticmethod
    def from_dict(obj: Any) -> 'Auth':
        assert isinstance(obj, dict)
        access_levels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("access_levels"))
        audiences = from_union([lambda x: from_list(from_str, x), from_none], obj.get("audiences"))
        claims = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("claims"))
        presenter = from_union([from_str, from_none], obj.get("presenter"))
        principal = from_union([from_str, from_none], obj.get("principal"))
        return Auth(access_levels, audiences, claims, presenter, principal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["access_levels"] = from_union([lambda x: from_list(from_str, x), from_none], self.access_levels)
        result["audiences"] = from_union([lambda x: from_list(from_str, x), from_none], self.audiences)
        result["claims"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.claims)
        result["presenter"] = from_union([from_str, from_none], self.presenter)
        result["principal"] = from_union([from_str, from_none], self.principal)
        return result


class Request:
    auth: Optional[Auth]
    headers: Optional[Dict[str, Any]]
    host: Optional[str]
    id: Optional[str]
    method: Optional[str]
    path: Optional[str]
    protocol: Optional[str]
    query: Optional[str]
    reason: Optional[str]
    scheme: Optional[str]
    size: Optional[int]
    time: Optional[str]

    def __init__(self, auth: Optional[Auth], headers: Optional[Dict[str, Any]], host: Optional[str], id: Optional[str], method: Optional[str], path: Optional[str], protocol: Optional[str], query: Optional[str], reason: Optional[str], scheme: Optional[str], size: Optional[int], time: Optional[str]) -> None:
        self.auth = auth
        self.headers = headers
        self.host = host
        self.id = id
        self.method = method
        self.path = path
        self.protocol = protocol
        self.query = query
        self.reason = reason
        self.scheme = scheme
        self.size = size
        self.time = time

    @staticmethod
    def from_dict(obj: Any) -> 'Request':
        assert isinstance(obj, dict)
        auth = from_union([Auth.from_dict, from_none], obj.get("auth"))
        headers = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("headers"))
        host = from_union([from_str, from_none], obj.get("host"))
        id = from_union([from_str, from_none], obj.get("id"))
        method = from_union([from_str, from_none], obj.get("method"))
        path = from_union([from_str, from_none], obj.get("path"))
        protocol = from_union([from_str, from_none], obj.get("protocol"))
        query = from_union([from_str, from_none], obj.get("query"))
        reason = from_union([from_str, from_none], obj.get("reason"))
        scheme = from_union([from_str, from_none], obj.get("scheme"))
        size = from_union([from_int, from_none], obj.get("size"))
        time = from_union([from_str, from_none], obj.get("time"))
        return Request(auth, headers, host, id, method, path, protocol, query, reason, scheme, size, time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["auth"] = from_union([lambda x: to_class(Auth, x), from_none], self.auth)
        result["headers"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.headers)
        result["host"] = from_union([from_str, from_none], self.host)
        result["id"] = from_union([from_str, from_none], self.id)
        result["method"] = from_union([from_str, from_none], self.method)
        result["path"] = from_union([from_str, from_none], self.path)
        result["protocol"] = from_union([from_str, from_none], self.protocol)
        result["query"] = from_union([from_str, from_none], self.query)
        result["reason"] = from_union([from_str, from_none], self.reason)
        result["scheme"] = from_union([from_str, from_none], self.scheme)
        result["size"] = from_union([from_int, from_none], self.size)
        result["time"] = from_union([from_str, from_none], self.time)
        return result


class RequestMetadata:
    caller_ip: Optional[str]
    caller_network: Optional[str]
    caller_supplied_user_agent: Optional[str]
    destination_attributes: Optional[Peer]
    request_attributes: Optional[Request]

    def __init__(self, caller_ip: Optional[str], caller_network: Optional[str], caller_supplied_user_agent: Optional[str], destination_attributes: Optional[Peer], request_attributes: Optional[Request]) -> None:
        self.caller_ip = caller_ip
        self.caller_network = caller_network
        self.caller_supplied_user_agent = caller_supplied_user_agent
        self.destination_attributes = destination_attributes
        self.request_attributes = request_attributes

    @staticmethod
    def from_dict(obj: Any) -> 'RequestMetadata':
        assert isinstance(obj, dict)
        caller_ip = from_union([from_str, from_none], obj.get("caller_ip"))
        caller_network = from_union([from_str, from_none], obj.get("caller_network"))
        caller_supplied_user_agent = from_union([from_str, from_none], obj.get("caller_supplied_user_agent"))
        destination_attributes = from_union([Peer.from_dict, from_none], obj.get("destination_attributes"))
        request_attributes = from_union([Request.from_dict, from_none], obj.get("request_attributes"))
        return RequestMetadata(caller_ip, caller_network, caller_supplied_user_agent, destination_attributes, request_attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["caller_ip"] = from_union([from_str, from_none], self.caller_ip)
        result["caller_network"] = from_union([from_str, from_none], self.caller_network)
        result["caller_supplied_user_agent"] = from_union([from_str, from_none], self.caller_supplied_user_agent)
        result["destination_attributes"] = from_union([lambda x: to_class(Peer, x), from_none], self.destination_attributes)
        result["request_attributes"] = from_union([lambda x: to_class(Request, x), from_none], self.request_attributes)
        return result


class ResourceLocation:
    current_locations: Optional[List[str]]
    original_locations: Optional[List[str]]

    def __init__(self, current_locations: Optional[List[str]], original_locations: Optional[List[str]]) -> None:
        self.current_locations = current_locations
        self.original_locations = original_locations

    @staticmethod
    def from_dict(obj: Any) -> 'ResourceLocation':
        assert isinstance(obj, dict)
        current_locations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("current_locations"))
        original_locations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("original_locations"))
        return ResourceLocation(current_locations, original_locations)

    def to_dict(self) -> dict:
        result: dict = {}
        result["current_locations"] = from_union([lambda x: from_list(from_str, x), from_none], self.current_locations)
        result["original_locations"] = from_union([lambda x: from_list(from_str, x), from_none], self.original_locations)
        return result


class Status:
    code: Optional[int]
    details: Any
    message: Optional[str]

    def __init__(self, code: Optional[int], details: Any, message: Optional[str]) -> None:
        self.code = code
        self.details = details
        self.message = message

    @staticmethod
    def from_dict(obj: Any) -> 'Status':
        assert isinstance(obj, dict)
        code = from_union([from_int, from_none], obj.get("code"))
        details = obj.get("details")
        message = from_union([from_str, from_none], obj.get("message"))
        return Status(code, details, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_union([from_int, from_none], self.code)
        result["details"] = self.details
        result["message"] = from_union([from_str, from_none], self.message)
        return result


class AuditLog:
    authentication_info: Optional[AuthenticationInfo]
    authorization_info: Optional[List[AuthorizationInfo]]
    metadata: Optional[Dict[str, Any]]
    method_name: Optional[str]
    num_response_items: Optional[int]
    request: Optional[Dict[str, Any]]
    request_metadata: Optional[RequestMetadata]
    resource_location: Optional[ResourceLocation]
    resource_name: Optional[str]
    resource_original_state: Optional[Dict[str, Any]]
    response: Optional[Dict[str, Any]]
    service_data: Optional[Dict[str, Any]]
    service_name: Optional[str]
    status: Optional[Status]

    def __init__(self, authentication_info: Optional[AuthenticationInfo], authorization_info: Optional[List[AuthorizationInfo]], metadata: Optional[Dict[str, Any]], method_name: Optional[str], num_response_items: Optional[int], request: Optional[Dict[str, Any]], request_metadata: Optional[RequestMetadata], resource_location: Optional[ResourceLocation], resource_name: Optional[str], resource_original_state: Optional[Dict[str, Any]], response: Optional[Dict[str, Any]], service_data: Optional[Dict[str, Any]], service_name: Optional[str], status: Optional[Status]) -> None:
        self.authentication_info = authentication_info
        self.authorization_info = authorization_info
        self.metadata = metadata
        self.method_name = method_name
        self.num_response_items = num_response_items
        self.request = request
        self.request_metadata = request_metadata
        self.resource_location = resource_location
        self.resource_name = resource_name
        self.resource_original_state = resource_original_state
        self.response = response
        self.service_data = service_data
        self.service_name = service_name
        self.status = status

    @staticmethod
    def from_dict(obj: Any) -> 'AuditLog':
        assert isinstance(obj, dict)
        authentication_info = from_union([AuthenticationInfo.from_dict, from_none], obj.get("authentication_info"))
        authorization_info = from_union([lambda x: from_list(AuthorizationInfo.from_dict, x), from_none], obj.get("authorization_info"))
        metadata = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("metadata"))
        method_name = from_union([from_str, from_none], obj.get("method_name"))
        num_response_items = from_union([from_int, from_none], obj.get("num_response_items"))
        request = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("request"))
        request_metadata = from_union([RequestMetadata.from_dict, from_none], obj.get("request_metadata"))
        resource_location = from_union([ResourceLocation.from_dict, from_none], obj.get("resource_location"))
        resource_name = from_union([from_str, from_none], obj.get("resource_name"))
        resource_original_state = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("resource_original_state"))
        response = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("response"))
        service_data = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("service_data"))
        service_name = from_union([from_str, from_none], obj.get("service_name"))
        status = from_union([Status.from_dict, from_none], obj.get("status"))
        return AuditLog(authentication_info, authorization_info, metadata, method_name, num_response_items, request, request_metadata, resource_location, resource_name, resource_original_state, response, service_data, service_name, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authentication_info"] = from_union([lambda x: to_class(AuthenticationInfo, x), from_none], self.authentication_info)
        result["authorization_info"] = from_union([lambda x: from_list(lambda x: to_class(AuthorizationInfo, x), x), from_none], self.authorization_info)
        result["metadata"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.metadata)
        result["method_name"] = from_union([from_str, from_none], self.method_name)
        result["num_response_items"] = from_union([from_int, from_none], self.num_response_items)
        result["request"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.request)
        result["request_metadata"] = from_union([lambda x: to_class(RequestMetadata, x), from_none], self.request_metadata)
        result["resource_location"] = from_union([lambda x: to_class(ResourceLocation, x), from_none], self.resource_location)
        result["resource_name"] = from_union([from_str, from_none], self.resource_name)
        result["resource_original_state"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.resource_original_state)
        result["response"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.response)
        result["service_data"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.service_data)
        result["service_name"] = from_union([from_str, from_none], self.service_name)
        result["status"] = from_union([lambda x: to_class(Status, x), from_none], self.status)
        return result


class MonitoredResource:
    labels: Optional[Dict[str, Any]]
    type: Optional[str]

    def __init__(self, labels: Optional[Dict[str, Any]], type: Optional[str]) -> None:
        self.labels = labels
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'MonitoredResource':
        assert isinstance(obj, dict)
        labels = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("labels"))
        type = from_union([from_str, from_none], obj.get("type"))
        return MonitoredResource(labels, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["labels"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.labels)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


class AuditLogWrittenEvent:
    """This event is triggered when a new audit log entry is written."""
    insert_id: Optional[str]
    labels: Optional[Dict[str, Any]]
    log_name: Optional[str]
    operation: Optional[LogEntryOperation]
    proto_payload: Optional[AuditLog]
    receive_timestamp: Optional[str]
    resource: Optional[MonitoredResource]
    severity: Optional[int]
    span_id: Optional[str]
    timestamp: Optional[str]
    trace: Optional[str]

    def __init__(self, insert_id: Optional[str], labels: Optional[Dict[str, Any]], log_name: Optional[str], operation: Optional[LogEntryOperation], proto_payload: Optional[AuditLog], receive_timestamp: Optional[str], resource: Optional[MonitoredResource], severity: Optional[int], span_id: Optional[str], timestamp: Optional[str], trace: Optional[str]) -> None:
        self.insert_id = insert_id
        self.labels = labels
        self.log_name = log_name
        self.operation = operation
        self.proto_payload = proto_payload
        self.receive_timestamp = receive_timestamp
        self.resource = resource
        self.severity = severity
        self.span_id = span_id
        self.timestamp = timestamp
        self.trace = trace

    @staticmethod
    def from_dict(obj: Any) -> 'AuditLogWrittenEvent':
        assert isinstance(obj, dict)
        insert_id = from_union([from_str, from_none], obj.get("insert_id"))
        labels = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("labels"))
        log_name = from_union([from_str, from_none], obj.get("log_name"))
        operation = from_union([LogEntryOperation.from_dict, from_none], obj.get("operation"))
        proto_payload = from_union([AuditLog.from_dict, from_none], obj.get("proto_payload"))
        receive_timestamp = from_union([from_str, from_none], obj.get("receive_timestamp"))
        resource = from_union([MonitoredResource.from_dict, from_none], obj.get("resource"))
        severity = from_union([from_int, from_none], obj.get("severity"))
        span_id = from_union([from_str, from_none], obj.get("span_id"))
        timestamp = from_union([from_str, from_none], obj.get("timestamp"))
        trace = from_union([from_str, from_none], obj.get("trace"))
        return AuditLogWrittenEvent(insert_id, labels, log_name, operation, proto_payload, receive_timestamp, resource, severity, span_id, timestamp, trace)

    def to_dict(self) -> dict:
        result: dict = {}
        result["insert_id"] = from_union([from_str, from_none], self.insert_id)
        result["labels"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.labels)
        result["log_name"] = from_union([from_str, from_none], self.log_name)
        result["operation"] = from_union([lambda x: to_class(LogEntryOperation, x), from_none], self.operation)
        result["proto_payload"] = from_union([lambda x: to_class(AuditLog, x), from_none], self.proto_payload)
        result["receive_timestamp"] = from_union([from_str, from_none], self.receive_timestamp)
        result["resource"] = from_union([lambda x: to_class(MonitoredResource, x), from_none], self.resource)
        result["severity"] = from_union([from_int, from_none], self.severity)
        result["span_id"] = from_union([from_str, from_none], self.span_id)
        result["timestamp"] = from_union([from_str, from_none], self.timestamp)
        result["trace"] = from_union([from_str, from_none], self.trace)
        return result


class EventClass:
    """This event is triggered when a new audit log entry is written."""
    audit_log_written_event: Optional[AuditLogWrittenEvent]

    def __init__(self, audit_log_written_event: Optional[AuditLogWrittenEvent]) -> None:
        self.audit_log_written_event = audit_log_written_event

    @staticmethod
    def from_dict(obj: Any) -> 'EventClass':
        assert isinstance(obj, dict)
        audit_log_written_event = from_union([AuditLogWrittenEvent.from_dict, from_none], obj.get("AuditLogWrittenEvent"))
        return EventClass(audit_log_written_event)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AuditLogWrittenEvent"] = from_union([lambda x: to_class(AuditLogWrittenEvent, x), from_none], self.audit_log_written_event)
        return result


def event_from_dict(s: Any) -> Union[List[Any], bool, EventClass, float, int, None, str]:
    return from_union([from_none, from_float, from_int, from_bool, from_str, lambda x: from_list(lambda x: x, x), EventClass.from_dict], s)


def event_to_dict(x: Union[List[Any], bool, EventClass, float, int, None, str]) -> Any:
    return from_union([from_none, to_float, from_int, from_bool, from_str, lambda x: from_list(lambda x: x, x), lambda x: to_class(EventClass, x)], x)
