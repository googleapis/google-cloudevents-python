from typing import Optional, Dict, Any, List, Union
from datetime import datetime


class Operation:
    """Information about an operation associated with the log entry, if applicable."""
    """True if this is the first log entry in the operation."""
    first: Optional[bool]
    """An arbitrary operation identifier. Log entries with the same
    identifier are assumed to be part of the same operation.
    """
    id: Optional[str]
    """True if this is the last log entry in the operation."""
    last: Optional[bool]
    """An arbitrary producer identifier. The combination of `id` and
    `producer` must be globally unique. Examples for `producer`:
    `"MyDivision.MyBigCompany.com"`, `"github.com/MyProject/MyApplication"`.
    """
    producer: Optional[str]

    def __init__(self, first: Optional[bool], id: Optional[str], last: Optional[bool], producer: Optional[str]) -> None:
        self.first = first
        self.id = id
        self.last = last
        self.producer = producer


class ServiceMetadata:
    """Metadata about the service that uses the service account."""
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields


class FirstPartyPrincipal:
    """First party (Google) identity as the real authority."""
    """The email address of a Google account."""
    principal_email: Optional[str]
    """Metadata about the service that uses the service account."""
    service_metadata: Optional[ServiceMetadata]

    def __init__(self, principal_email: Optional[str], service_metadata: Optional[ServiceMetadata]) -> None:
        self.principal_email = principal_email
        self.service_metadata = service_metadata


class ThirdPartyClaims:
    """Metadata about third party identity."""
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields


class ServiceAccountDelegationInfoThirdPartyPrincipal:
    """Third party identity as the real authority."""
    """Metadata about third party identity."""
    third_party_claims: Optional[ThirdPartyClaims]

    def __init__(self, third_party_claims: Optional[ThirdPartyClaims]) -> None:
        self.third_party_claims = third_party_claims


class ServiceAccountDelegationInfo:
    """Identity delegation history of an authenticated service account."""
    """First party (Google) identity as the real authority."""
    first_party_principal: Optional[FirstPartyPrincipal]
    """Third party identity as the real authority."""
    third_party_principal: Optional[ServiceAccountDelegationInfoThirdPartyPrincipal]

    def __init__(self, first_party_principal: Optional[FirstPartyPrincipal], third_party_principal: Optional[ServiceAccountDelegationInfoThirdPartyPrincipal]) -> None:
        self.first_party_principal = first_party_principal
        self.third_party_principal = third_party_principal


class AuthenticationInfoThirdPartyPrincipal:
    """The third party identification (if any) of the authenticated user making
    the request.
    When the JSON object represented here has a proto equivalent, the proto
    name will be indicated in the `@type` property.
    """
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields


class AuthenticationInfo:
    """Authentication information."""
    """The authority selector specified by the requestor, if any.
    It is not guaranteed that the principal was allowed to use this authority.
    """
    authority_selector: Optional[str]
    """The email address of the authenticated user (or service account on behalf
    of third party principal) making the request. For privacy reasons, the
    principal email address is redacted for all read-only operations that fail
    with a "permission denied" error.
    """
    principal_email: Optional[str]
    """String representation of identity of requesting party.
    Populated for both first and third party identities.
    """
    principal_subject: Optional[str]
    """Identity delegation history of an authenticated service account that makes
    the request. It contains information on the real authorities that try to
    access GCP resources by delegating on a service account. When multiple
    authorities present, they are guaranteed to be sorted based on the original
    ordering of the identity delegation events.
    """
    service_account_delegation_info: Optional[List[ServiceAccountDelegationInfo]]
    """The name of the service account key used to create or exchange
    credentials for authenticating the service account making the request.
    This is a scheme-less URI full resource name. For example:
    
    "//iam.googleapis.com/projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}"
    """
    service_account_key_name: Optional[str]
    """The third party identification (if any) of the authenticated user making
    the request.
    When the JSON object represented here has a proto equivalent, the proto
    name will be indicated in the `@type` property.
    """
    third_party_principal: Optional[AuthenticationInfoThirdPartyPrincipal]

    def __init__(self, authority_selector: Optional[str], principal_email: Optional[str], principal_subject: Optional[str], service_account_delegation_info: Optional[List[ServiceAccountDelegationInfo]], service_account_key_name: Optional[str], third_party_principal: Optional[AuthenticationInfoThirdPartyPrincipal]) -> None:
        self.authority_selector = authority_selector
        self.principal_email = principal_email
        self.principal_subject = principal_subject
        self.service_account_delegation_info = service_account_delegation_info
        self.service_account_key_name = service_account_key_name
        self.third_party_principal = third_party_principal


class ResourceAttributes:
    """Resource attributes used in IAM condition evaluation. This field contains
    resource attributes like resource type and resource name.
    
    To get the whole view of the attributes used in IAM
    condition evaluation, the user must also look into
    `AuditLogData.request_metadata.request_attributes`.
    """
    """The labels or tags on the resource, such as AWS resource tags and
    Kubernetes resource labels.
    """
    labels: Optional[Dict[str, str]]
    """The stable identifier (name) of a resource on the `service`. A resource
    can be logically identified as "//{resource.service}/{resource.name}".
    The differences between a resource name and a URI are:
    
    *   Resource name is a logical identifier, independent of network
    protocol and API version. For example,
    `//pubsub.googleapis.com/projects/123/topics/news-feed`.
    *   URI often includes protocol and version information, so it can
    be used directly by applications. For example,
    `https://pubsub.googleapis.com/v1/projects/123/topics/news-feed`.
    
    See https://cloud.google.com/apis/design/resource_names for details.
    """
    name: Optional[str]
    """The name of the service that this resource belongs to, such as
    `pubsub.googleapis.com`. The service may be different from the DNS
    hostname that actually serves the request.
    """
    service: Optional[str]
    """The type of the resource. The syntax is platform-specific because
    different platforms define their resources differently.
    
    For Google APIs, the type format must be "{service}/{kind}".
    """
    type: Optional[str]

    def __init__(self, labels: Optional[Dict[str, str]], name: Optional[str], service: Optional[str], type: Optional[str]) -> None:
        self.labels = labels
        self.name = name
        self.service = service
        self.type = type


class AuthorizationInfo:
    """Authorization information for the operation."""
    """Whether or not authorization for `resource` and `permission`
    was granted.
    """
    granted: Optional[bool]
    """The required IAM permission."""
    permission: Optional[str]
    """The resource being accessed, as a REST-style string. For example:
    
    bigquery.googleapis.com/projects/PROJECTID/datasets/DATASETID
    """
    resource: Optional[str]
    """Resource attributes used in IAM condition evaluation. This field contains
    resource attributes like resource type and resource name.
    
    To get the whole view of the attributes used in IAM
    condition evaluation, the user must also look into
    `AuditLogData.request_metadata.request_attributes`.
    """
    resource_attributes: Optional[ResourceAttributes]

    def __init__(self, granted: Optional[bool], permission: Optional[str], resource: Optional[str], resource_attributes: Optional[ResourceAttributes]) -> None:
        self.granted = granted
        self.permission = permission
        self.resource = resource
        self.resource_attributes = resource_attributes


class Metadata:
    """Other service-specific data about the request, response, and other
    information associated with the current audited event.
    """
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields


class Request:
    """The operation request. This may not include all request parameters,
    such as those that are too large, privacy-sensitive, or duplicated
    elsewhere in the log record.
    It should never include user-generated data, such as file contents.
    When the JSON object represented here has a proto equivalent, the proto
    name will be indicated in the `@type` property.
    """
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields


class DestinationAttributes:
    """The destination of a network activity, such as accepting a TCP connection.
    In a multi hop network activity, the destination represents the receiver of
    the last hop. Only two fields are used in this message, Peer.port and
    Peer.ip. These fields are optionally populated by those services utilizing
    the IAM condition feature.
    """
    """The IP address of the peer."""
    ip: Optional[str]
    """The labels associated with the peer."""
    labels: Optional[Dict[str, str]]
    """The network port of the peer."""
    port: Union[int, None, str]
    """The identity of this peer. Similar to `Request.auth.principal`, but
    relative to the peer instead of the request. For example, the
    idenity associated with a load balancer that forwared the request.
    """
    principal: Optional[str]
    """The CLDR country/region code associated with the above IP address.
    If the IP address is private, the `region_code` should reflect the
    physical location where this peer is running.
    """
    region_code: Optional[str]

    def __init__(self, ip: Optional[str], labels: Optional[Dict[str, str]], port: Union[int, None, str], principal: Optional[str], region_code: Optional[str]) -> None:
        self.ip = ip
        self.labels = labels
        self.port = port
        self.principal = principal
        self.region_code = region_code


class Claims:
    """Structured claims presented with the credential. JWTs include
    `{key: value}` pairs for standard and private claims. The following
    is a subset of the standard required and optional claims that would
    typically be presented for a Google-based JWT:
    
    {'iss': 'accounts.google.com',
    'sub': '113289723416554971153',
    'aud': ['123456789012', 'pubsub.googleapis.com'],
    'azp': '123456789012.apps.googleusercontent.com',
    'email': 'jsmith@example.com',
    'iat': 1353601026,
    'exp': 1353604926}
    
    SAML assertions are similarly specified, but with an identity provider
    dependent structure.
    """
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields


class Auth:
    """The request authentication. May be absent for unauthenticated requests.
    Derived from the HTTP request `Authorization` header or equivalent.
    """
    """A list of access level resource names that allow resources to be
    accessed by authenticated requester. It is part of Secure GCP processing
    for the incoming request. An access level string has the format:
    "//{api_service_name}/accessPolicies/{policy_id}/accessLevels/{short_name}"
    
    Example:
    "//accesscontextmanager.googleapis.com/accessPolicies/MY_POLICY_ID/accessLevels/MY_LEVEL"
    """
    access_levels: Optional[List[str]]
    """The intended audience(s) for this authentication information. Reflects
    the audience (`aud`) claim within a JWT. The audience
    value(s) depends on the `issuer`, but typically include one or more of
    the following pieces of information:
    
    *  The services intended to receive the credential such as
    ["pubsub.googleapis.com", "storage.googleapis.com"]
    *  A set of service-based scopes. For example,
    ["https://www.googleapis.com/auth/cloud-platform"]
    *  The client id of an app, such as the Firebase project id for JWTs
    from Firebase Auth.
    
    Consult the documentation for the credential issuer to determine the
    information provided.
    """
    audiences: Optional[List[str]]
    """Structured claims presented with the credential. JWTs include
    `{key: value}` pairs for standard and private claims. The following
    is a subset of the standard required and optional claims that would
    typically be presented for a Google-based JWT:
    
    {'iss': 'accounts.google.com',
    'sub': '113289723416554971153',
    'aud': ['123456789012', 'pubsub.googleapis.com'],
    'azp': '123456789012.apps.googleusercontent.com',
    'email': 'jsmith@example.com',
    'iat': 1353601026,
    'exp': 1353604926}
    
    SAML assertions are similarly specified, but with an identity provider
    dependent structure.
    """
    claims: Optional[Claims]
    """The authorized presenter of the credential. Reflects the optional
    Authorized Presenter (`azp`) claim within a JWT or the
    OAuth client id. For example, a Google Cloud Platform client id looks
    as follows: "123456789012.apps.googleusercontent.com".
    """
    presenter: Optional[str]
    """The authenticated principal. Reflects the issuer (`iss`) and subject
    (`sub`) claims within a JWT. The issuer and subject should be `/`
    delimited, with `/` percent-encoded within the subject fragment. For
    Google accounts, the principal format is:
    "https://accounts.google.com/{id}"
    """
    principal: Optional[str]

    def __init__(self, access_levels: Optional[List[str]], audiences: Optional[List[str]], claims: Optional[Claims], presenter: Optional[str], principal: Optional[str]) -> None:
        self.access_levels = access_levels
        self.audiences = audiences
        self.claims = claims
        self.presenter = presenter
        self.principal = principal


class RequestAttributes:
    """Request attributes used in IAM condition evaluation. This field contains
    request attributes like request time and access levels associated with
    the request.
    
    
    To get the whole view of the attributes used in IAM
    condition evaluation, the user must also look into
    `AuditLog.authentication_info.resource_attributes`.
    """
    """The request authentication. May be absent for unauthenticated requests.
    Derived from the HTTP request `Authorization` header or equivalent.
    """
    auth: Optional[Auth]
    """The HTTP request headers. If multiple headers share the same key, they
    must be merged according to the HTTP spec. All header keys must be
    lowercased, because HTTP header keys are case-insensitive.
    """
    headers: Optional[Dict[str, str]]
    """The HTTP request `Host` header value."""
    host: Optional[str]
    """The unique ID for a request, which can be propagated to downstream
    systems. The ID should have low probability of collision
    within a single day for a specific service.
    """
    id: Optional[str]
    """The HTTP request method, such as `GET`, `POST`."""
    method: Optional[str]
    """The HTTP URL path."""
    path: Optional[str]
    """The network protocol used with the request, such as "http/1.1",
    "spdy/3", "h2", "h2c", "webrtc", "tcp", "udp", "quic". See
    
    https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#alpn-protocol-ids
    for details.
    """
    protocol: Optional[str]
    """The HTTP URL query in the format of `name1=value1&name2=value2`, as it
    appears in the first line of the HTTP request. No decoding is performed.
    """
    query: Optional[str]
    """A special parameter for request reason. It is used by security systems
    to associate auditing information with a request.
    """
    reason: Optional[str]
    """The HTTP URL scheme, such as `http` and `https`."""
    scheme: Optional[str]
    """The HTTP request size in bytes. If unknown, it must be -1."""
    size: Union[int, None, str]
    """The timestamp when the `destination` service receives the first byte of
    the request.
    """
    time: Optional[datetime]

    def __init__(self, auth: Optional[Auth], headers: Optional[Dict[str, str]], host: Optional[str], id: Optional[str], method: Optional[str], path: Optional[str], protocol: Optional[str], query: Optional[str], reason: Optional[str], scheme: Optional[str], size: Union[int, None, str], time: Optional[datetime]) -> None:
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


class RequestMetadata:
    """Metadata about the operation."""
    """The IP address of the caller.
    For caller from internet, this will be public IPv4 or IPv6 address.
    For caller from a Compute Engine VM with external IP address, this
    will be the VM's external IP address. For caller from a Compute
    Engine VM without external IP address, if the VM is in the same
    organization (or project) as the accessed resource, `caller_ip` will
    be the VM's internal IPv4 address, otherwise the `caller_ip` will be
    redacted to "gce-internal-ip".
    See https://cloud.google.com/compute/docs/vpc/ for more information.
    """
    caller_ip: Optional[str]
    """The network of the caller.
    Set only if the network host project is part of the same GCP organization
    (or project) as the accessed resource.
    See https://cloud.google.com/compute/docs/vpc/ for more information.
    This is a scheme-less URI full resource name. For example:
    
    "//compute.googleapis.com/projects/PROJECT_ID/global/networks/NETWORK_ID"
    """
    caller_network: Optional[str]
    """The user agent of the caller.
    This information is not authenticated and should be treated accordingly.
    For example:
    
    +   `google-api-python-client/1.4.0`:
    The request was made by the Google API client for Python.
    +   `Cloud SDK Command Line Tool apitools-client/1.0 gcloud/0.9.62`:
    The request was made by the Google Cloud SDK CLI (gcloud).
    +   `AppEngine-Google; (+http://code.google.com/appengine; appid:
    s~my-project`:
    The request was made from the `my-project` App Engine app.
    """
    caller_supplied_user_agent: Optional[str]
    """The destination of a network activity, such as accepting a TCP connection.
    In a multi hop network activity, the destination represents the receiver of
    the last hop. Only two fields are used in this message, Peer.port and
    Peer.ip. These fields are optionally populated by those services utilizing
    the IAM condition feature.
    """
    destination_attributes: Optional[DestinationAttributes]
    """Request attributes used in IAM condition evaluation. This field contains
    request attributes like request time and access levels associated with
    the request.
    
    
    To get the whole view of the attributes used in IAM
    condition evaluation, the user must also look into
    `AuditLog.authentication_info.resource_attributes`.
    """
    request_attributes: Optional[RequestAttributes]

    def __init__(self, caller_ip: Optional[str], caller_network: Optional[str], caller_supplied_user_agent: Optional[str], destination_attributes: Optional[DestinationAttributes], request_attributes: Optional[RequestAttributes]) -> None:
        self.caller_ip = caller_ip
        self.caller_network = caller_network
        self.caller_supplied_user_agent = caller_supplied_user_agent
        self.destination_attributes = destination_attributes
        self.request_attributes = request_attributes


class ResourceLocation:
    """The resource location information."""
    """The locations of a resource after the execution of the operation.
    Requests to create or delete a location based resource must populate
    the 'current_locations' field and not the 'original_locations' field.
    For example:
    
    "europe-west1-a"
    "us-east1"
    "nam3"
    """
    current_locations: Optional[List[str]]
    """The locations of a resource prior to the execution of the operation.
    Requests that mutate the resource's location must populate both the
    'original_locations' as well as the 'current_locations' fields.
    For example:
    
    "europe-west1-a"
    "us-east1"
    "nam3"
    """
    original_locations: Optional[List[str]]

    def __init__(self, current_locations: Optional[List[str]], original_locations: Optional[List[str]]) -> None:
        self.current_locations = current_locations
        self.original_locations = original_locations


class ResourceOriginalState:
    """The resource's original state before mutation. Present only for
    operations which have successfully modified the targeted resource(s).
    In general, this field should contain all changed fields, except those
    that are already been included in `request`, `response`, `metadata` or
    `service_data` fields.
    When the JSON object represented here has a proto equivalent,
    the proto name will be indicated in the `@type` property.
    """
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields


class Response:
    """The operation response. This may not include all response elements,
    such as those that are too large, privacy-sensitive, or duplicated
    elsewhere in the log record.
    It should never include user-generated data, such as file contents.
    When the JSON object represented here has a proto equivalent, the proto
    name will be indicated in the `@type` property.
    """
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields


class ServiceData:
    """Deprecated, use `metadata` field instead.
    Other service-specific data about the request, response, and other
    activities.
    When the JSON object represented here has a proto equivalent, the proto
    name will be indicated in the `@type` property.
    """
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields


class Detail:
    """`Any` contains an arbitrary serialized protocol buffer message along with a
    URL that describes the type of the serialized message.
    
    Protobuf library provides support to pack/unpack Any values in the form
    of utility functions or additional generated methods of the Any type.
    
    Example 1: Pack and unpack a message in C++.
    
    Foo foo = ...;
    Any any;
    any.PackFrom(foo);
    ...
    if (any.UnpackTo(&foo)) {
    ...
    }
    
    Example 2: Pack and unpack a message in Java.
    
    Foo foo = ...;
    Any any = Any.pack(foo);
    ...
    if (any.is(Foo.class)) {
    foo = any.unpack(Foo.class);
    }
    
    Example 3: Pack and unpack a message in Python.
    
    foo = Foo(...)
    any = Any()
    any.Pack(foo)
    ...
    if any.Is(Foo.DESCRIPTOR):
    any.Unpack(foo)
    ...
    
    Example 4: Pack and unpack a message in Go
    
    foo := &pb.Foo{...}
    any, err := ptypes.MarshalAny(foo)
    ...
    foo := &pb.Foo{}
    if err := ptypes.UnmarshalAny(any, foo); err != nil {
    ...
    }
    
    The pack methods provided by protobuf library will by default use
    'type.googleapis.com/full.type.name' as the type URL and the unpack
    methods only use the fully qualified type name after the last '/'
    in the type URL, for example "foo.bar.com/x/y.z" will yield type
    name "y.z".
    
    
    JSON
    ====
    The JSON representation of an `Any` value uses the regular
    representation of the deserialized, embedded message, with an
    additional field `@type` which contains the type URL. Example:
    
    package google.profile;
    message Person {
    string first_name = 1;
    string last_name = 2;
    }
    
    {
    "@type": "type.googleapis.com/google.profile.Person",
    "firstName": <string>,
    "lastName": <string>
    }
    
    If the embedded message type is well-known and has a custom JSON
    representation, that representation will be embedded adding a field
    `value` which holds the custom JSON in addition to the `@type`
    field. Example (for message [google.protobuf.Duration][]):
    
    {
    "@type": "type.googleapis.com/google.protobuf.Duration",
    "value": "1.212s"
    }
    """
    """A URL/resource name that uniquely identifies the type of the serialized
    protocol buffer message. This string must contain at least
    one "/" character. The last segment of the URL's path must represent
    the fully qualified name of the type (as in
    `path/google.protobuf.Duration`). The name should be in a canonical form
    (e.g., leading "." is not accepted).
    
    In practice, teams usually precompile into the binary all types that they
    expect it to use in the context of Any. However, for URLs which use the
    scheme `http`, `https`, or no scheme, one can optionally set up a type
    server that maps type URLs to message definitions as follows:
    
    * If no scheme is provided, `https` is assumed.
    * An HTTP GET on the URL must yield a [google.protobuf.Type][]
    value in binary format, or produce an error.
    * Applications are allowed to cache lookup results based on the
    URL, or have them precompiled into a binary to avoid any
    lookup. Therefore, binary compatibility needs to be preserved
    on changes to types. (Use versioned type names to manage
    breaking changes.)
    
    Note: this functionality is not currently available in the official
    protobuf release, and it is not used for type URLs beginning with
    type.googleapis.com.
    
    Schemes other than `http`, `https` (or the empty scheme) might be
    used with implementation specific semantics.
    """
    type_url: Optional[str]
    """Must be a valid serialized protocol buffer of the above specified type."""
    value: Optional[str]

    def __init__(self, type_url: Optional[str], value: Optional[str]) -> None:
        self.type_url = type_url
        self.value = value


class Status:
    """The status of the overall operation."""
    """The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code]."""
    code: Optional[int]
    """A list of messages that carry the error details.  There is a common set of
    message types for APIs to use.
    """
    details: Optional[List[Detail]]
    """A developer-facing error message, which should be in English. Any
    user-facing error message should be localized and sent in the
    [google.rpc.Status.details][google.rpc.Status.details] field, or localized by the client.
    """
    message: Optional[str]

    def __init__(self, code: Optional[int], details: Optional[List[Detail]], message: Optional[str]) -> None:
        self.code = code
        self.details = details
        self.message = message


class ProtoPayload:
    """The log entry payload, which is always an AuditLog for Cloud Audit Log events."""
    """Authentication information."""
    authentication_info: Optional[AuthenticationInfo]
    """Authorization information. If there are multiple
    resources or permissions involved, then there is
    one AuthorizationInfo element for each {resource, permission} tuple.
    """
    authorization_info: Optional[List[AuthorizationInfo]]
    """Other service-specific data about the request, response, and other
    information associated with the current audited event.
    """
    metadata: Optional[Metadata]
    """The name of the service method or operation.
    For API calls, this should be the name of the API method.
    For example,
    
    "google.datastore.v1.Datastore.RunQuery"
    "google.logging.v1.LoggingService.DeleteLog"
    """
    method_name: Optional[str]
    """The number of items returned from a List or Query API method,
    if applicable.
    """
    num_response_items: Union[int, None, str]
    """The operation request. This may not include all request parameters,
    such as those that are too large, privacy-sensitive, or duplicated
    elsewhere in the log record.
    It should never include user-generated data, such as file contents.
    When the JSON object represented here has a proto equivalent, the proto
    name will be indicated in the `@type` property.
    """
    request: Optional[Request]
    """Metadata about the operation."""
    request_metadata: Optional[RequestMetadata]
    """The resource location information."""
    resource_location: Optional[ResourceLocation]
    """The resource or collection that is the target of the operation.
    The name is a scheme-less URI, not including the API service name.
    For example:
    
    "shelves/SHELF_ID/books"
    "shelves/SHELF_ID/books/BOOK_ID"
    """
    resource_name: Optional[str]
    """The resource's original state before mutation. Present only for
    operations which have successfully modified the targeted resource(s).
    In general, this field should contain all changed fields, except those
    that are already been included in `request`, `response`, `metadata` or
    `service_data` fields.
    When the JSON object represented here has a proto equivalent,
    the proto name will be indicated in the `@type` property.
    """
    resource_original_state: Optional[ResourceOriginalState]
    """The operation response. This may not include all response elements,
    such as those that are too large, privacy-sensitive, or duplicated
    elsewhere in the log record.
    It should never include user-generated data, such as file contents.
    When the JSON object represented here has a proto equivalent, the proto
    name will be indicated in the `@type` property.
    """
    response: Optional[Response]
    """Deprecated, use `metadata` field instead.
    Other service-specific data about the request, response, and other
    activities.
    When the JSON object represented here has a proto equivalent, the proto
    name will be indicated in the `@type` property.
    """
    service_data: Optional[ServiceData]
    """The name of the API service performing the operation. For example,
    `"datastore.googleapis.com"`.
    """
    service_name: Optional[str]
    """The status of the overall operation."""
    status: Optional[Status]

    def __init__(self, authentication_info: Optional[AuthenticationInfo], authorization_info: Optional[List[AuthorizationInfo]], metadata: Optional[Metadata], method_name: Optional[str], num_response_items: Union[int, None, str], request: Optional[Request], request_metadata: Optional[RequestMetadata], resource_location: Optional[ResourceLocation], resource_name: Optional[str], resource_original_state: Optional[ResourceOriginalState], response: Optional[Response], service_data: Optional[ServiceData], service_name: Optional[str], status: Optional[Status]) -> None:
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


class Resource:
    """The monitored resource that produced this log entry.
    
    Example: a log entry that reports a database error would be associated with
    the monitored resource designating the particular database that reported
    the error.
    """
    """Values for all of the labels listed in the associated monitored
    resource descriptor. For example, Compute Engine VM instances use the
    labels `"project_id"`, `"instance_id"`, and `"zone"`.
    """
    labels: Optional[Dict[str, str]]
    """Required. The monitored resource type. For example, the type of a
    Compute Engine VM instance is `gce_instance`.
    """
    type: Optional[str]

    def __init__(self, labels: Optional[Dict[str, str]], type: Optional[str]) -> None:
        self.labels = labels
        self.type = type


class LogEntryData:
    """Generic log entry, used as a wrapper for Cloud Audit Logs in events.
    This is copied from
    https://github.com/googleapis/googleapis/blob/master/google/logging/v2/log_entry.proto
    and adapted appropriately.
    """
    """A unique identifier for the log entry."""
    insert_id: Optional[str]
    """A set of user-defined (key, value) data that provides additional
    information about the log entry.
    """
    labels: Optional[Dict[str, str]]
    """The resource name of the log to which this log entry belongs."""
    log_name: Optional[str]
    """Information about an operation associated with the log entry, if applicable."""
    operation: Optional[Operation]
    """The log entry payload, which is always an AuditLog for Cloud Audit Log events."""
    proto_payload: Optional[ProtoPayload]
    """The time the log entry was received by Logging."""
    receive_timestamp: Optional[datetime]
    """The monitored resource that produced this log entry.
    
    Example: a log entry that reports a database error would be associated with
    the monitored resource designating the particular database that reported
    the error.
    """
    resource: Optional[Resource]
    """The severity of the log entry."""
    severity: Union[int, None, str]
    """The span ID within the trace associated with the log entry, if any.
    
    For Trace spans, this is the same format that the Trace API v2 uses: a
    16-character hexadecimal encoding of an 8-byte array, such as
    `000000000000004a`.
    """
    span_id: Optional[str]
    """The time the event described by the log entry occurred."""
    timestamp: Optional[datetime]
    """Resource name of the trace associated with the log entry, if any. If it
    contains a relative resource name, the name is assumed to be relative to
    `//tracing.googleapis.com`. Example:
    `projects/my-projectid/traces/06796866738c859f2f19b7cfb3214824`
    """
    trace: Optional[str]

    def __init__(self, insert_id: Optional[str], labels: Optional[Dict[str, str]], log_name: Optional[str], operation: Optional[Operation], proto_payload: Optional[ProtoPayload], receive_timestamp: Optional[datetime], resource: Optional[Resource], severity: Union[int, None, str], span_id: Optional[str], timestamp: Optional[datetime], trace: Optional[str]) -> None:
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
