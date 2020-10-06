# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = log_entry_data_from_dict(json.loads(json_string))

from typing import Optional, Any, Dict, List, TypeVar, Callable, Type, cast


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


class LogEntryOperation:
    """Information about an operation associated with the log entry, if applicable.
    
    Additional information about a potentially long-running operation with which a log entry
    is associated.
    """
    """True if this is the first log entry in the operation."""
    first: Optional[bool]
    """An arbitrary operation identifier. Log entries with the same identifier are assumed to be
    part of the same operation.
    """
    id: Optional[str]
    """True if this is the last log entry in the operation."""
    last: Optional[bool]
    """An arbitrary producer identifier. The combination of `id` and `producer` must be globally
    unique. Examples for `producer`: `"MyDivision.MyBigCompany.com"`,
    `"github.com/MyProject/MyApplication"`.
    """
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
    """Identity delegation history of an authenticated service account"""
    """The email address of a Google account."""
    principal_email: Optional[str]
    """Metadata about the service that uses the service account."""
    service_metadata: Optional[Dict[str, Any]]
    """Metadata about third party identity."""
    third_party_claims: Optional[Dict[str, Any]]

    def __init__(self, principal_email: Optional[str], service_metadata: Optional[Dict[str, Any]], third_party_claims: Optional[Dict[str, Any]]) -> None:
        self.principal_email = principal_email
        self.service_metadata = service_metadata
        self.third_party_claims = third_party_claims

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


class AuthenticationInfo:
    """Authentication information.
    
    Authentication information for the operation.
    """
    """The authority selector specified by the requestor, if any. It is not guaranteed that the
    principal was allowed to use this authority.
    """
    authority_selector: Optional[str]
    """The email address of the authenticated user (or service account on behalf of third party
    principal) making the request. For privacy reasons, the principal email address is
    redacted for all read-only operations that fail with a "permission denied" error.
    """
    principal_email: Optional[str]
    """String representation of identity of requesting party. Populated for both first and third
    party identities.
    """
    principal_subject: Optional[str]
    """Identity delegation history of an authenticated service account that makes the request.
    It contains information on the real authorities that try to access GCP resources by
    delegating on a service account. When multiple authorities present, they are guaranteed
    to be sorted based on the original ordering of the identity delegation events.
    """
    service_account_delegation_info: Optional[List[ServiceAccountDelegationInfo]]
    """The name of the service account key used to create or exchange credentials for
    authenticating the service account making the request. This is a scheme-less URI full
    resource name.
    """
    service_account_key_name: Optional[str]
    """The third party identification (if any) of the authenticated user making the request.
    When the JSON object represented here has a proto equivalent, the proto name will be
    indicated in the @type property.
    """
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
        authority_selector = from_union([from_str, from_none], obj.get("authoritySelector"))
        principal_email = from_union([from_str, from_none], obj.get("principalEmail"))
        principal_subject = from_union([from_str, from_none], obj.get("principalSubject"))
        service_account_delegation_info = from_union([lambda x: from_list(ServiceAccountDelegationInfo.from_dict, x), from_none], obj.get("serviceAccountDelegationInfo"))
        service_account_key_name = from_union([from_str, from_none], obj.get("serviceAccountKeyName"))
        third_party_principal = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("thirdPartyPrincipal"))
        return AuthenticationInfo(authority_selector, principal_email, principal_subject, service_account_delegation_info, service_account_key_name, third_party_principal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authoritySelector"] = from_union([from_str, from_none], self.authority_selector)
        result["principalEmail"] = from_union([from_str, from_none], self.principal_email)
        result["principalSubject"] = from_union([from_str, from_none], self.principal_subject)
        result["serviceAccountDelegationInfo"] = from_union([lambda x: from_list(lambda x: to_class(ServiceAccountDelegationInfo, x), x), from_none], self.service_account_delegation_info)
        result["serviceAccountKeyName"] = from_union([from_str, from_none], self.service_account_key_name)
        result["thirdPartyPrincipal"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.third_party_principal)
        return result


class Resource:
    """Resource attributes used in IAM condition evaluation. This field contains resource
    attributes like resource type and resource name. To get the whole view of the attributes
    used in IAM condition evaluation, the user must also look into
    AuditLog.requestMetadata.requestAttributes.
    """
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
    """Authorization information. If there are multiple resources or permissions involved, then
    there is one AuthorizationInfo element for each {resource, permission} tuple.
    """
    """Whether or not authorization for resource and permission was granted."""
    granted: Optional[bool]
    """The required IAM permission."""
    permission: Optional[str]
    """The resource being accessed, as a REST-style string."""
    resource: Optional[str]
    """Resource attributes used in IAM condition evaluation. This field contains resource
    attributes like resource type and resource name. To get the whole view of the attributes
    used in IAM condition evaluation, the user must also look into
    AuditLog.requestMetadata.requestAttributes.
    """
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
        resource_attributes = from_union([Resource.from_dict, from_none], obj.get("resourceAttributes"))
        return AuthorizationInfo(granted, permission, resource, resource_attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["granted"] = from_union([from_bool, from_none], self.granted)
        result["permission"] = from_union([from_str, from_none], self.permission)
        result["resource"] = from_union([from_str, from_none], self.resource)
        result["resourceAttributes"] = from_union([lambda x: to_class(Resource, x), from_none], self.resource_attributes)
        return result


class Peer:
    """The destination of a network activity, such as accepting a TCP connection."""
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


class Request:
    """Request attributes used in IAM condition evaluation. This field contains request
    attributes like request time and access levels associated with the request.
    """
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
    """Metadata about the operation."""
    """The IP address of the caller. For caller from internet, this will be public IPv4 or IPv6
    address. For caller from a Compute Engine VM with external IP address, this will be the
    VM's external IP address. For caller from a Compute Engine VM without external IP
    address, if the VM is in the same organization (or project) as the accessed resource,
    `callerIp` will be the VM's internal IPv4 address, otherwise the `callerIp` will be
    redacted to "gce-internal-ip". See https://cloud.google.com/compute/docs/vpc/ for more
    information."
    """
    caller_ip: Optional[str]
    """The network of the caller."""
    caller_network: Optional[str]
    """The user agent of the caller. This information is not authenticated and should be treated
    accordingly.
    """
    caller_supplied_user_agent: Optional[str]
    """The destination of a network activity, such as accepting a TCP connection."""
    destination_attributes: Optional[Peer]
    """Request attributes used in IAM condition evaluation. This field contains request
    attributes like request time and access levels associated with the request.
    """
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


class ResourceLocation:
    """The resource location information.
    
    Location information about a resource.
    """
    """The locations of a resource after the execution of the operation. Requests to create or
    delete a location based resource must populate the 'currentLocations' field and not the
    'originalLocations' field.
    """
    current_locations: Optional[List[str]]
    """The locations of a resource prior to the execution of the operation. Requests that mutate
    the resource's location must populate both the 'originalLocations' as well as the
    'currentLocations' fields. For example:
    """
    original_locations: Optional[List[str]]

    def __init__(self, current_locations: Optional[List[str]], original_locations: Optional[List[str]]) -> None:
        self.current_locations = current_locations
        self.original_locations = original_locations

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


class Status:
    """The status of the overall operation."""
    """The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code]."""
    code: Optional[int]
    """A list of messages that carry the error details.  There is a common set of message types
    for APIs to use.
    """
    details: Any
    """A developer-facing error message, which should be in English. Any user-facing error
    message should be localized and sent in the
    [google.rpc.Status.details][google.rpc.Status.details] field, or localized by the client.
    """
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
    """The log entry payload, which is always an AuditLog for Cloud Audit Log events."""
    """Authentication information."""
    authentication_info: Optional[AuthenticationInfo]
    """Authorization information. If there are multiple resources or permissions involved, then
    there is one AuthorizationInfo element for each {resource, permission} tuple.
    """
    authorization_info: Optional[List[AuthorizationInfo]]
    """Other service-specific data about the request, response, and other information associated
    with the current audited event.
    """
    metadata: Optional[Dict[str, Any]]
    """The name of the service method or operation. For example
    "google.datastore.v1.Datastore.RunQuery"
    """
    method_name: Optional[str]
    """The number of items returned from a List or Query API method, if applicable."""
    num_response_items: Optional[int]
    """The operation request. This may not include all request parameters, such as those that
    are too large, privacy-sensitive, or duplicated elsewhere in the log record. It should
    never include user-generated data, such as file contents. When the JSON object
    represented here has a proto equivalent, the proto name will be indicated in the `@type`
    property.
    """
    request: Optional[Dict[str, Any]]
    """Metadata about the operation."""
    request_metadata: Optional[RequestMetadata]
    """The resource location information."""
    resource_location: Optional[ResourceLocation]
    """The resource or collection that is the target of the operation. For example
    "shelves/SHELF_ID/books"
    """
    resource_name: Optional[str]
    """The resource's original state before mutation."""
    resource_original_state: Optional[Dict[str, Any]]
    """The operation response. This may not include all response elements, such as those that
    are too large, privacy-sensitive, or duplicated elsewhere in the log record. It should
    never include user-generated data, such as file contents. When the JSON object
    represented here has a proto equivalent, the proto name will be indicated in the `@type`
    property.
    """
    response: Optional[Dict[str, Any]]
    """Deprecated, use `metadata` field instead. Other service-specific data about the request,
    response, and other activities. When the JSON object represented here has a proto
    equivalent, the proto name will be indicated in the `@type` property.
    """
    service_data: Optional[Dict[str, Any]]
    """The name of the API service performing the operation. For example,
    `"datastore.googleapis.com"`.
    """
    service_name: Optional[str]
    """The status of the overall operation."""
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
        authentication_info = from_union([AuthenticationInfo.from_dict, from_none], obj.get("authenticationInfo"))
        authorization_info = from_union([lambda x: from_list(AuthorizationInfo.from_dict, x), from_none], obj.get("authorizationInfo"))
        metadata = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("metadata"))
        method_name = from_union([from_str, from_none], obj.get("methodName"))
        num_response_items = from_union([from_int, from_none], obj.get("numResponseItems"))
        request = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("request"))
        request_metadata = from_union([RequestMetadata.from_dict, from_none], obj.get("requestMetadata"))
        resource_location = from_union([ResourceLocation.from_dict, from_none], obj.get("resourceLocation"))
        resource_name = from_union([from_str, from_none], obj.get("resourceName"))
        resource_original_state = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("resourceOriginalState"))
        response = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("response"))
        service_data = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("serviceData"))
        service_name = from_union([from_str, from_none], obj.get("serviceName"))
        status = from_union([Status.from_dict, from_none], obj.get("status"))
        return AuditLog(authentication_info, authorization_info, metadata, method_name, num_response_items, request, request_metadata, resource_location, resource_name, resource_original_state, response, service_data, service_name, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authenticationInfo"] = from_union([lambda x: to_class(AuthenticationInfo, x), from_none], self.authentication_info)
        result["authorizationInfo"] = from_union([lambda x: from_list(lambda x: to_class(AuthorizationInfo, x), x), from_none], self.authorization_info)
        result["metadata"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.metadata)
        result["methodName"] = from_union([from_str, from_none], self.method_name)
        result["numResponseItems"] = from_union([from_int, from_none], self.num_response_items)
        result["request"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.request)
        result["requestMetadata"] = from_union([lambda x: to_class(RequestMetadata, x), from_none], self.request_metadata)
        result["resourceLocation"] = from_union([lambda x: to_class(ResourceLocation, x), from_none], self.resource_location)
        result["resourceName"] = from_union([from_str, from_none], self.resource_name)
        result["resourceOriginalState"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.resource_original_state)
        result["response"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.response)
        result["serviceData"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.service_data)
        result["serviceName"] = from_union([from_str, from_none], self.service_name)
        result["status"] = from_union([lambda x: to_class(Status, x), from_none], self.status)
        return result


class MonitoredResource:
    """The monitored resource that produced this log entry. Example: a log entry that reports a
    database error would be associated with the monitored resource designating the particular
    database that reported the error.
    
    The monitored resource that produced this log entry.
    """
    """Values for all of the labels listed in the associated monitored resource descriptor. For
    example, Compute Engine VM instances use the labels `"projectId"`, `"instanceId"`, and
    `"zone"`.
    """
    labels: Optional[Dict[str, Any]]
    """Required. The monitored resource type. For example, the type of a Compute Engine VM
    instance is `gceInstance`.
    """
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


class LogEntryData:
    """This event is triggered when a new audit log entry is written."""
    """A unique identifier for the log entry."""
    insert_id: Optional[str]
    """A set of user-defined (key, value) data that provides additional information about the
    log entry.
    """
    labels: Optional[Dict[str, Any]]
    """The resource name of the log to which this log entry belongs."""
    log_name: Optional[str]
    """Information about an operation associated with the log entry, if applicable."""
    operation: Optional[LogEntryOperation]
    """The log entry payload, which is always an AuditLog for Cloud Audit Log events."""
    proto_payload: Optional[AuditLog]
    """The time the log entry was received by Logging."""
    receive_timestamp: Optional[str]
    """The monitored resource that produced this log entry. Example: a log entry that reports a
    database error would be associated with the monitored resource designating the particular
    database that reported the error.
    """
    resource: Optional[MonitoredResource]
    """The severity of the log entry."""
    severity: Optional[str]
    """The span ID within the trace associated with the log entry, if any. For Trace spans, this
    is the same format that the Trace API v2 uses: a 16-character hexadecimal encoding of an
    8-byte array, such as `000000000000004a`.
    """
    span_id: Optional[str]
    """The time the event described by the log entry occurred."""
    timestamp: Optional[str]
    """Resource name of the trace associated with the log entry, if any. If it contains a
    relative resource name, the name is assumed to be relative to `//tracing.googleapis.com`.
    Example: `projects/my-projectid/traces/06796866738c859f2f19b7cfb3214824`
    """
    trace: Optional[str]

    def __init__(self, insert_id: Optional[str], labels: Optional[Dict[str, Any]], log_name: Optional[str], operation: Optional[LogEntryOperation], proto_payload: Optional[AuditLog], receive_timestamp: Optional[str], resource: Optional[MonitoredResource], severity: Optional[str], span_id: Optional[str], timestamp: Optional[str], trace: Optional[str]) -> None:
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
    def from_dict(obj: Any) -> 'LogEntryData':
        assert isinstance(obj, dict)
        insert_id = from_union([from_str, from_none], obj.get("insertId"))
        labels = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("labels"))
        log_name = from_union([from_str, from_none], obj.get("logName"))
        operation = from_union([LogEntryOperation.from_dict, from_none], obj.get("operation"))
        proto_payload = from_union([AuditLog.from_dict, from_none], obj.get("protoPayload"))
        receive_timestamp = from_union([from_str, from_none], obj.get("receiveTimestamp"))
        resource = from_union([MonitoredResource.from_dict, from_none], obj.get("resource"))
        severity = from_union([from_str, from_none], obj.get("severity"))
        span_id = from_union([from_str, from_none], obj.get("spanId"))
        timestamp = from_union([from_str, from_none], obj.get("timestamp"))
        trace = from_union([from_str, from_none], obj.get("trace"))
        return LogEntryData(insert_id, labels, log_name, operation, proto_payload, receive_timestamp, resource, severity, span_id, timestamp, trace)

    def to_dict(self) -> dict:
        result: dict = {}
        result["insertId"] = from_union([from_str, from_none], self.insert_id)
        result["labels"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.labels)
        result["logName"] = from_union([from_str, from_none], self.log_name)
        result["operation"] = from_union([lambda x: to_class(LogEntryOperation, x), from_none], self.operation)
        result["protoPayload"] = from_union([lambda x: to_class(AuditLog, x), from_none], self.proto_payload)
        result["receiveTimestamp"] = from_union([from_str, from_none], self.receive_timestamp)
        result["resource"] = from_union([lambda x: to_class(MonitoredResource, x), from_none], self.resource)
        result["severity"] = from_union([from_str, from_none], self.severity)
        result["spanId"] = from_union([from_str, from_none], self.span_id)
        result["timestamp"] = from_union([from_str, from_none], self.timestamp)
        result["trace"] = from_union([from_str, from_none], self.trace)
        return result


def log_entry_data_from_dict(s: Any) -> LogEntryData:
    return LogEntryData.from_dict(s)


def log_entry_data_to_dict(x: LogEntryData) -> Any:
    return to_class(LogEntryData, x)
