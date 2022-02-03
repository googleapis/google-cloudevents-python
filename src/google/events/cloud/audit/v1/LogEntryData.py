# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = log_entry_data_from_dict(json.loads(json_string))

from typing import Optional, Any, Dict, List, Union, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


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

    @staticmethod
    def from_dict(obj: Any) -> 'Operation':
        assert isinstance(obj, dict)
        first = from_union([from_bool, from_none], obj.get("first"))
        id = from_union([from_str, from_none], obj.get("id"))
        last = from_union([from_bool, from_none], obj.get("last"))
        producer = from_union([from_str, from_none], obj.get("producer"))
        return Operation(first, id, last, producer)

    def to_dict(self) -> dict:
        result: dict = {}
        result["first"] = from_union([from_bool, from_none], self.first)
        result["id"] = from_union([from_str, from_none], self.id)
        result["last"] = from_union([from_bool, from_none], self.last)
        result["producer"] = from_union([from_str, from_none], self.producer)
        return result


class ServiceMetadata:
    """Metadata about the service that uses the service account."""
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields

    @staticmethod
    def from_dict(obj: Any) -> 'ServiceMetadata':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], obj.get("fields"))
        return ServiceMetadata(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], self.fields)
        return result


class FirstPartyPrincipal:
    """First party (Google) identity as the real authority."""
    """The email address of a Google account."""
    principal_email: Optional[str]
    """Metadata about the service that uses the service account."""
    service_metadata: Optional[ServiceMetadata]

    def __init__(self, principal_email: Optional[str], service_metadata: Optional[ServiceMetadata]) -> None:
        self.principal_email = principal_email
        self.service_metadata = service_metadata

    @staticmethod
    def from_dict(obj: Any) -> 'FirstPartyPrincipal':
        assert isinstance(obj, dict)
        principal_email = from_union([from_str, from_none], obj.get("principalEmail"))
        service_metadata = from_union([ServiceMetadata.from_dict, from_none], obj.get("serviceMetadata"))
        return FirstPartyPrincipal(principal_email, service_metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        result["principalEmail"] = from_union([from_str, from_none], self.principal_email)
        result["serviceMetadata"] = from_union([lambda x: to_class(ServiceMetadata, x), from_none], self.service_metadata)
        return result


class ThirdPartyClaims:
    """Metadata about third party identity."""
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields

    @staticmethod
    def from_dict(obj: Any) -> 'ThirdPartyClaims':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], obj.get("fields"))
        return ThirdPartyClaims(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], self.fields)
        return result


class ServiceAccountDelegationInfoThirdPartyPrincipal:
    """Third party identity as the real authority."""
    """Metadata about third party identity."""
    third_party_claims: Optional[ThirdPartyClaims]

    def __init__(self, third_party_claims: Optional[ThirdPartyClaims]) -> None:
        self.third_party_claims = third_party_claims

    @staticmethod
    def from_dict(obj: Any) -> 'ServiceAccountDelegationInfoThirdPartyPrincipal':
        assert isinstance(obj, dict)
        third_party_claims = from_union([ThirdPartyClaims.from_dict, from_none], obj.get("thirdPartyClaims"))
        return ServiceAccountDelegationInfoThirdPartyPrincipal(third_party_claims)

    def to_dict(self) -> dict:
        result: dict = {}
        result["thirdPartyClaims"] = from_union([lambda x: to_class(ThirdPartyClaims, x), from_none], self.third_party_claims)
        return result


class ServiceAccountDelegationInfo:
    """Identity delegation history of an authenticated service account."""
    """First party (Google) identity as the real authority."""
    first_party_principal: Optional[FirstPartyPrincipal]
    """Third party identity as the real authority."""
    third_party_principal: Optional[ServiceAccountDelegationInfoThirdPartyPrincipal]

    def __init__(self, first_party_principal: Optional[FirstPartyPrincipal], third_party_principal: Optional[ServiceAccountDelegationInfoThirdPartyPrincipal]) -> None:
        self.first_party_principal = first_party_principal
        self.third_party_principal = third_party_principal

    @staticmethod
    def from_dict(obj: Any) -> 'ServiceAccountDelegationInfo':
        assert isinstance(obj, dict)
        first_party_principal = from_union([FirstPartyPrincipal.from_dict, from_none], obj.get("firstPartyPrincipal"))
        third_party_principal = from_union([ServiceAccountDelegationInfoThirdPartyPrincipal.from_dict, from_none], obj.get("thirdPartyPrincipal"))
        return ServiceAccountDelegationInfo(first_party_principal, third_party_principal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["firstPartyPrincipal"] = from_union([lambda x: to_class(FirstPartyPrincipal, x), from_none], self.first_party_principal)
        result["thirdPartyPrincipal"] = from_union([lambda x: to_class(ServiceAccountDelegationInfoThirdPartyPrincipal, x), from_none], self.third_party_principal)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'AuthenticationInfoThirdPartyPrincipal':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], obj.get("fields"))
        return AuthenticationInfoThirdPartyPrincipal(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], self.fields)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'AuthenticationInfo':
        assert isinstance(obj, dict)
        authority_selector = from_union([from_str, from_none], obj.get("authoritySelector"))
        principal_email = from_union([from_str, from_none], obj.get("principalEmail"))
        principal_subject = from_union([from_str, from_none], obj.get("principalSubject"))
        service_account_delegation_info = from_union([lambda x: from_list(ServiceAccountDelegationInfo.from_dict, x), from_none], obj.get("serviceAccountDelegationInfo"))
        service_account_key_name = from_union([from_str, from_none], obj.get("serviceAccountKeyName"))
        third_party_principal = from_union([AuthenticationInfoThirdPartyPrincipal.from_dict, from_none], obj.get("thirdPartyPrincipal"))
        return AuthenticationInfo(authority_selector, principal_email, principal_subject, service_account_delegation_info, service_account_key_name, third_party_principal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authoritySelector"] = from_union([from_str, from_none], self.authority_selector)
        result["principalEmail"] = from_union([from_str, from_none], self.principal_email)
        result["principalSubject"] = from_union([from_str, from_none], self.principal_subject)
        result["serviceAccountDelegationInfo"] = from_union([lambda x: from_list(lambda x: to_class(ServiceAccountDelegationInfo, x), x), from_none], self.service_account_delegation_info)
        result["serviceAccountKeyName"] = from_union([from_str, from_none], self.service_account_key_name)
        result["thirdPartyPrincipal"] = from_union([lambda x: to_class(AuthenticationInfoThirdPartyPrincipal, x), from_none], self.third_party_principal)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'ResourceAttributes':
        assert isinstance(obj, dict)
        labels = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("labels"))
        name = from_union([from_str, from_none], obj.get("name"))
        service = from_union([from_str, from_none], obj.get("service"))
        type = from_union([from_str, from_none], obj.get("type"))
        return ResourceAttributes(labels, name, service, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["labels"] = from_union([lambda x: from_dict(from_str, x), from_none], self.labels)
        result["name"] = from_union([from_str, from_none], self.name)
        result["service"] = from_union([from_str, from_none], self.service)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'AuthorizationInfo':
        assert isinstance(obj, dict)
        granted = from_union([from_bool, from_none], obj.get("granted"))
        permission = from_union([from_str, from_none], obj.get("permission"))
        resource = from_union([from_str, from_none], obj.get("resource"))
        resource_attributes = from_union([ResourceAttributes.from_dict, from_none], obj.get("resourceAttributes"))
        return AuthorizationInfo(granted, permission, resource, resource_attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["granted"] = from_union([from_bool, from_none], self.granted)
        result["permission"] = from_union([from_str, from_none], self.permission)
        result["resource"] = from_union([from_str, from_none], self.resource)
        result["resourceAttributes"] = from_union([lambda x: to_class(ResourceAttributes, x), from_none], self.resource_attributes)
        return result


class Metadata:
    """Other service-specific data about the request, response, and other
    information associated with the current audited event.
    """
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], obj.get("fields"))
        return Metadata(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], self.fields)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'Request':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], obj.get("fields"))
        return Request(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], self.fields)
        return result


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
    port: Optional[str]
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

    def __init__(self, ip: Optional[str], labels: Optional[Dict[str, str]], port: Optional[str], principal: Optional[str], region_code: Optional[str]) -> None:
        self.ip = ip
        self.labels = labels
        self.port = port
        self.principal = principal
        self.region_code = region_code

    @staticmethod
    def from_dict(obj: Any) -> 'DestinationAttributes':
        assert isinstance(obj, dict)
        ip = from_union([from_str, from_none], obj.get("ip"))
        labels = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("labels"))
        port = from_union([from_str, from_none], obj.get("port"))
        principal = from_union([from_str, from_none], obj.get("principal"))
        region_code = from_union([from_str, from_none], obj.get("regionCode"))
        return DestinationAttributes(ip, labels, port, principal, region_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ip"] = from_union([from_str, from_none], self.ip)
        result["labels"] = from_union([lambda x: from_dict(from_str, x), from_none], self.labels)
        result["port"] = from_union([from_str, from_none], self.port)
        result["principal"] = from_union([from_str, from_none], self.principal)
        result["regionCode"] = from_union([from_str, from_none], self.region_code)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'Claims':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], obj.get("fields"))
        return Claims(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], self.fields)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'Auth':
        assert isinstance(obj, dict)
        access_levels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("accessLevels"))
        audiences = from_union([lambda x: from_list(from_str, x), from_none], obj.get("audiences"))
        claims = from_union([Claims.from_dict, from_none], obj.get("claims"))
        presenter = from_union([from_str, from_none], obj.get("presenter"))
        principal = from_union([from_str, from_none], obj.get("principal"))
        return Auth(access_levels, audiences, claims, presenter, principal)

    def to_dict(self) -> dict:
        result: dict = {}
        result["accessLevels"] = from_union([lambda x: from_list(from_str, x), from_none], self.access_levels)
        result["audiences"] = from_union([lambda x: from_list(from_str, x), from_none], self.audiences)
        result["claims"] = from_union([lambda x: to_class(Claims, x), from_none], self.claims)
        result["presenter"] = from_union([from_str, from_none], self.presenter)
        result["principal"] = from_union([from_str, from_none], self.principal)
        return result


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
    size: Optional[str]
    """The timestamp when the `destination` service receives the first byte of
    the request.
    """
    time: Optional[datetime]

    def __init__(self, auth: Optional[Auth], headers: Optional[Dict[str, str]], host: Optional[str], id: Optional[str], method: Optional[str], path: Optional[str], protocol: Optional[str], query: Optional[str], reason: Optional[str], scheme: Optional[str], size: Optional[str], time: Optional[datetime]) -> None:
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
    def from_dict(obj: Any) -> 'RequestAttributes':
        assert isinstance(obj, dict)
        auth = from_union([Auth.from_dict, from_none], obj.get("auth"))
        headers = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("headers"))
        host = from_union([from_str, from_none], obj.get("host"))
        id = from_union([from_str, from_none], obj.get("id"))
        method = from_union([from_str, from_none], obj.get("method"))
        path = from_union([from_str, from_none], obj.get("path"))
        protocol = from_union([from_str, from_none], obj.get("protocol"))
        query = from_union([from_str, from_none], obj.get("query"))
        reason = from_union([from_str, from_none], obj.get("reason"))
        scheme = from_union([from_str, from_none], obj.get("scheme"))
        size = from_union([from_str, from_none], obj.get("size"))
        time = from_union([from_datetime, from_none], obj.get("time"))
        return RequestAttributes(auth, headers, host, id, method, path, protocol, query, reason, scheme, size, time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["auth"] = from_union([lambda x: to_class(Auth, x), from_none], self.auth)
        result["headers"] = from_union([lambda x: from_dict(from_str, x), from_none], self.headers)
        result["host"] = from_union([from_str, from_none], self.host)
        result["id"] = from_union([from_str, from_none], self.id)
        result["method"] = from_union([from_str, from_none], self.method)
        result["path"] = from_union([from_str, from_none], self.path)
        result["protocol"] = from_union([from_str, from_none], self.protocol)
        result["query"] = from_union([from_str, from_none], self.query)
        result["reason"] = from_union([from_str, from_none], self.reason)
        result["scheme"] = from_union([from_str, from_none], self.scheme)
        result["size"] = from_union([from_str, from_none], self.size)
        result["time"] = from_union([lambda x: x.isoformat(), from_none], self.time)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'RequestMetadata':
        assert isinstance(obj, dict)
        caller_ip = from_union([from_str, from_none], obj.get("callerIp"))
        caller_network = from_union([from_str, from_none], obj.get("callerNetwork"))
        caller_supplied_user_agent = from_union([from_str, from_none], obj.get("callerSuppliedUserAgent"))
        destination_attributes = from_union([DestinationAttributes.from_dict, from_none], obj.get("destinationAttributes"))
        request_attributes = from_union([RequestAttributes.from_dict, from_none], obj.get("requestAttributes"))
        return RequestMetadata(caller_ip, caller_network, caller_supplied_user_agent, destination_attributes, request_attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["callerIp"] = from_union([from_str, from_none], self.caller_ip)
        result["callerNetwork"] = from_union([from_str, from_none], self.caller_network)
        result["callerSuppliedUserAgent"] = from_union([from_str, from_none], self.caller_supplied_user_agent)
        result["destinationAttributes"] = from_union([lambda x: to_class(DestinationAttributes, x), from_none], self.destination_attributes)
        result["requestAttributes"] = from_union([lambda x: to_class(RequestAttributes, x), from_none], self.request_attributes)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'ResourceOriginalState':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], obj.get("fields"))
        return ResourceOriginalState(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], self.fields)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'Response':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], obj.get("fields"))
        return Response(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], self.fields)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'ServiceData':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], obj.get("fields"))
        return ServiceData(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], self.fields)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'Detail':
        assert isinstance(obj, dict)
        type_url = from_union([from_str, from_none], obj.get("typeUrl"))
        value = from_union([from_str, from_none], obj.get("value"))
        return Detail(type_url, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["typeUrl"] = from_union([from_str, from_none], self.type_url)
        result["value"] = from_union([from_str, from_none], self.value)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'Status':
        assert isinstance(obj, dict)
        code = from_union([from_int, from_none], obj.get("code"))
        details = from_union([lambda x: from_list(Detail.from_dict, x), from_none], obj.get("details"))
        message = from_union([from_str, from_none], obj.get("message"))
        return Status(code, details, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_union([from_int, from_none], self.code)
        result["details"] = from_union([lambda x: from_list(lambda x: to_class(Detail, x), x), from_none], self.details)
        result["message"] = from_union([from_str, from_none], self.message)
        return result


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
    num_response_items: Optional[str]
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

    def __init__(self, authentication_info: Optional[AuthenticationInfo], authorization_info: Optional[List[AuthorizationInfo]], metadata: Optional[Metadata], method_name: Optional[str], num_response_items: Optional[str], request: Optional[Request], request_metadata: Optional[RequestMetadata], resource_location: Optional[ResourceLocation], resource_name: Optional[str], resource_original_state: Optional[ResourceOriginalState], response: Optional[Response], service_data: Optional[ServiceData], service_name: Optional[str], status: Optional[Status]) -> None:
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
    def from_dict(obj: Any) -> 'ProtoPayload':
        assert isinstance(obj, dict)
        authentication_info = from_union([AuthenticationInfo.from_dict, from_none], obj.get("authenticationInfo"))
        authorization_info = from_union([lambda x: from_list(AuthorizationInfo.from_dict, x), from_none], obj.get("authorizationInfo"))
        metadata = from_union([Metadata.from_dict, from_none], obj.get("metadata"))
        method_name = from_union([from_str, from_none], obj.get("methodName"))
        num_response_items = from_union([from_str, from_none], obj.get("numResponseItems"))
        request = from_union([Request.from_dict, from_none], obj.get("request"))
        request_metadata = from_union([RequestMetadata.from_dict, from_none], obj.get("requestMetadata"))
        resource_location = from_union([ResourceLocation.from_dict, from_none], obj.get("resourceLocation"))
        resource_name = from_union([from_str, from_none], obj.get("resourceName"))
        resource_original_state = from_union([ResourceOriginalState.from_dict, from_none], obj.get("resourceOriginalState"))
        response = from_union([Response.from_dict, from_none], obj.get("response"))
        service_data = from_union([ServiceData.from_dict, from_none], obj.get("serviceData"))
        service_name = from_union([from_str, from_none], obj.get("serviceName"))
        status = from_union([Status.from_dict, from_none], obj.get("status"))
        return ProtoPayload(authentication_info, authorization_info, metadata, method_name, num_response_items, request, request_metadata, resource_location, resource_name, resource_original_state, response, service_data, service_name, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authenticationInfo"] = from_union([lambda x: to_class(AuthenticationInfo, x), from_none], self.authentication_info)
        result["authorizationInfo"] = from_union([lambda x: from_list(lambda x: to_class(AuthorizationInfo, x), x), from_none], self.authorization_info)
        result["metadata"] = from_union([lambda x: to_class(Metadata, x), from_none], self.metadata)
        result["methodName"] = from_union([from_str, from_none], self.method_name)
        result["numResponseItems"] = from_union([from_str, from_none], self.num_response_items)
        result["request"] = from_union([lambda x: to_class(Request, x), from_none], self.request)
        result["requestMetadata"] = from_union([lambda x: to_class(RequestMetadata, x), from_none], self.request_metadata)
        result["resourceLocation"] = from_union([lambda x: to_class(ResourceLocation, x), from_none], self.resource_location)
        result["resourceName"] = from_union([from_str, from_none], self.resource_name)
        result["resourceOriginalState"] = from_union([lambda x: to_class(ResourceOriginalState, x), from_none], self.resource_original_state)
        result["response"] = from_union([lambda x: to_class(Response, x), from_none], self.response)
        result["serviceData"] = from_union([lambda x: to_class(ServiceData, x), from_none], self.service_data)
        result["serviceName"] = from_union([from_str, from_none], self.service_name)
        result["status"] = from_union([lambda x: to_class(Status, x), from_none], self.status)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'Resource':
        assert isinstance(obj, dict)
        labels = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("labels"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Resource(labels, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["labels"] = from_union([lambda x: from_dict(from_str, x), from_none], self.labels)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


class LogEntryData:
    """The data within all Cloud Audit Logs log entry events."""
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

    @staticmethod
    def from_dict(obj: Any) -> 'LogEntryData':
        assert isinstance(obj, dict)
        insert_id = from_union([from_str, from_none], obj.get("insertId"))
        labels = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("labels"))
        log_name = from_union([from_str, from_none], obj.get("logName"))
        operation = from_union([Operation.from_dict, from_none], obj.get("operation"))
        proto_payload = from_union([ProtoPayload.from_dict, from_none], obj.get("protoPayload"))
        receive_timestamp = from_union([from_datetime, from_none], obj.get("receiveTimestamp"))
        resource = from_union([Resource.from_dict, from_none], obj.get("resource"))
        severity = from_union([from_int, from_str, from_none], obj.get("severity"))
        span_id = from_union([from_str, from_none], obj.get("spanId"))
        timestamp = from_union([from_datetime, from_none], obj.get("timestamp"))
        trace = from_union([from_str, from_none], obj.get("trace"))
        return LogEntryData(insert_id, labels, log_name, operation, proto_payload, receive_timestamp, resource, severity, span_id, timestamp, trace)

    def to_dict(self) -> dict:
        result: dict = {}
        result["insertId"] = from_union([from_str, from_none], self.insert_id)
        result["labels"] = from_union([lambda x: from_dict(from_str, x), from_none], self.labels)
        result["logName"] = from_union([from_str, from_none], self.log_name)
        result["operation"] = from_union([lambda x: to_class(Operation, x), from_none], self.operation)
        result["protoPayload"] = from_union([lambda x: to_class(ProtoPayload, x), from_none], self.proto_payload)
        result["receiveTimestamp"] = from_union([lambda x: x.isoformat(), from_none], self.receive_timestamp)
        result["resource"] = from_union([lambda x: to_class(Resource, x), from_none], self.resource)
        result["severity"] = from_union([from_int, from_str, from_none], self.severity)
        result["spanId"] = from_union([from_str, from_none], self.span_id)
        result["timestamp"] = from_union([lambda x: x.isoformat(), from_none], self.timestamp)
        result["trace"] = from_union([from_str, from_none], self.trace)
        return result


def log_entry_data_from_dict(s: Any) -> LogEntryData:
    return LogEntryData.from_dict(s)


def log_entry_data_to_dict(x: LogEntryData) -> Any:
    return to_class(LogEntryData, x)
