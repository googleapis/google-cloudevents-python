# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.events.cloud.networkservices.v1',
    manifest={
        'TrafficPortSelector',
        'EndpointMatcher',
        'EndpointPolicy',
        'Gateway',
        'GrpcRoute',
        'HttpRoute',
        'Mesh',
        'ServiceBinding',
        'TcpRoute',
        'TlsRoute',
        'EndpointPolicyEventData',
        'HttpRouteEventData',
        'ServiceBindingEventData',
        'GatewayEventData',
        'TlsRouteEventData',
        'GrpcRouteEventData',
        'MeshEventData',
        'TcpRouteEventData',
    },
)


class TrafficPortSelector(proto.Message):
    r"""Specification of a port-based selector.

    Attributes:
        ports (MutableSequence[str]):
            Optional. A list of ports. Can be port numbers or port range
            (example, [80-90] specifies all ports from 80 to 90,
            including 80 and 90) or named ports or \* to specify all
            ports. If the list is empty, all ports are selected.
    """

    ports: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class EndpointMatcher(proto.Message):
    r"""A definition of a matcher that selects endpoints to which the
    policies should be applied.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        metadata_label_matcher (google.events.cloud.networkservices_v1.types.EndpointMatcher.MetadataLabelMatcher):
            The matcher is based on node metadata
            presented by xDS clients.

            This field is a member of `oneof`_ ``matcher_type``.
    """

    class MetadataLabelMatcher(proto.Message):
        r"""The matcher that is based on node metadata presented by xDS
        clients.

        Attributes:
            metadata_label_match_criteria (google.events.cloud.networkservices_v1.types.EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria):
                Specifies how matching should be done.

                Supported values are: MATCH_ANY: At least one of the Labels
                specified in the matcher should match the metadata presented
                by xDS client. MATCH_ALL: The metadata presented by the xDS
                client should contain all of the labels specified here.

                The selection is determined based on the best match. For
                example, suppose there are three EndpointPolicy resources
                P1, P2 and P3 and if P1 has a the matcher as MATCH_ANY <A:1,
                B:1>, P2 has MATCH_ALL <A:1,B:1>, and P3 has MATCH_ALL
                <A:1,B:1,C:1>.

                If a client with label <A:1> connects, the config from P1
                will be selected.

                If a client with label <A:1,B:1> connects, the config from
                P2 will be selected.

                If a client with label <A:1,B:1,C:1> connects, the config
                from P3 will be selected.

                If there is more than one best match, (for example, if a
                config P4 with selector <A:1,D:1> exists and if a client
                with label <A:1,B:1,D:1> connects), an error will be thrown.
            metadata_labels (MutableSequence[google.events.cloud.networkservices_v1.types.EndpointMatcher.MetadataLabelMatcher.MetadataLabels]):
                The list of label value pairs that must match labels in the
                provided metadata based on filterMatchCriteria This list can
                have at most 64 entries. The list can be empty if the match
                criteria is MATCH_ANY, to specify a wildcard match (i.e this
                matches any client).
        """
        class MetadataLabelMatchCriteria(proto.Enum):
            r"""Possible criteria values that define logic of how matching is
            made.

            Values:
                METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED (0):
                    Default value. Should not be used.
                MATCH_ANY (1):
                    At least one of the Labels specified in the
                    matcher should match the metadata presented by
                    xDS client.
                MATCH_ALL (2):
                    The metadata presented by the xDS client
                    should contain all of the labels specified here.
            """
            METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED = 0
            MATCH_ANY = 1
            MATCH_ALL = 2

        class MetadataLabels(proto.Message):
            r"""Defines a name-pair value for a single label.

            Attributes:
                label_name (str):
                    Required. Label name presented as key in xDS
                    Node Metadata.
                label_value (str):
                    Required. Label value presented as value
                    corresponding to the above key, in xDS Node
                    Metadata.
            """

            label_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            label_value: str = proto.Field(
                proto.STRING,
                number=2,
            )

        metadata_label_match_criteria: 'EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria' = proto.Field(
            proto.ENUM,
            number=1,
            enum='EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria',
        )
        metadata_labels: MutableSequence['EndpointMatcher.MetadataLabelMatcher.MetadataLabels'] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message='EndpointMatcher.MetadataLabelMatcher.MetadataLabels',
        )

    metadata_label_matcher: MetadataLabelMatcher = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='matcher_type',
        message=MetadataLabelMatcher,
    )


class EndpointPolicy(proto.Message):
    r"""EndpointPolicy is a resource that helps apply desired
    configuration on the endpoints that match specific criteria. For
    example, this resource can be used to apply "authentication
    config" an all endpoints that serve on port 8080.

    Attributes:
        name (str):
            Required. Name of the EndpointPolicy resource. It matches
            pattern
            ``projects/{project}/locations/global/endpointPolicies/{endpoint_policy}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the EndpointPolicy resource.
        type_ (google.events.cloud.networkservices_v1.types.EndpointPolicy.EndpointPolicyType):
            Required. The type of endpoint policy. This
            is primarily used to validate the configuration.
        authorization_policy (str):
            Optional. This field specifies the URL of
            AuthorizationPolicy resource that applies
            authorization policies to the inbound traffic at
            the matched endpoints. Refer to Authorization.
            If this field is not specified, authorization is
            disabled(no authz checks) for this endpoint.
        endpoint_matcher (google.events.cloud.networkservices_v1.types.EndpointMatcher):
            Required. A matcher that selects endpoints to
            which the policies should be applied.
        traffic_port_selector (google.events.cloud.networkservices_v1.types.TrafficPortSelector):
            Optional. Port selector for the (matched)
            endpoints. If no port selector is provided, the
            matched config is applied to all ports.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        server_tls_policy (str):
            Optional. A URL referring to ServerTlsPolicy
            resource. ServerTlsPolicy is used to determine
            the authentication policy to be applied to
            terminate the inbound traffic at the identified
            backends. If this field is not set,
            authentication is disabled(open) for this
            endpoint.
        client_tls_policy (str):
            Optional. A URL referring to a ClientTlsPolicy resource.
            ClientTlsPolicy can be set to specify the authentication for
            traffic from the proxy to the actual endpoints. More
            specifically, it is applied to the outgoing traffic from the
            proxy to the endpoint. This is typically used for sidecar
            model where the proxy identifies itself as endpoint to the
            control plane, with the connection between sidecar and
            endpoint requiring authentication. If this field is not set,
            authentication is disabled(open). Applicable only when
            EndpointPolicyType is SIDECAR_PROXY.
    """
    class EndpointPolicyType(proto.Enum):
        r"""The type of endpoint policy.

        Values:
            ENDPOINT_POLICY_TYPE_UNSPECIFIED (0):
                Default value. Must not be used.
            SIDECAR_PROXY (1):
                Represents a proxy deployed as a sidecar.
            GRPC_SERVER (2):
                Represents a proxyless gRPC backend.
        """
        ENDPOINT_POLICY_TYPE_UNSPECIFIED = 0
        SIDECAR_PROXY = 1
        GRPC_SERVER = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    type_: EndpointPolicyType = proto.Field(
        proto.ENUM,
        number=5,
        enum=EndpointPolicyType,
    )
    authorization_policy: str = proto.Field(
        proto.STRING,
        number=7,
    )
    endpoint_matcher: 'EndpointMatcher' = proto.Field(
        proto.MESSAGE,
        number=9,
        message='EndpointMatcher',
    )
    traffic_port_selector: 'TrafficPortSelector' = proto.Field(
        proto.MESSAGE,
        number=10,
        message='TrafficPortSelector',
    )
    description: str = proto.Field(
        proto.STRING,
        number=11,
    )
    server_tls_policy: str = proto.Field(
        proto.STRING,
        number=12,
    )
    client_tls_policy: str = proto.Field(
        proto.STRING,
        number=13,
    )


class Gateway(proto.Message):
    r"""Gateway represents the configuration for a proxy, typically a
    load balancer. It captures the ip:port over which the services
    are exposed by the proxy, along with any policy configurations.
    Routes have reference to to Gateways to dictate how requests
    should be routed by this Gateway.

    Attributes:
        name (str):
            Required. Name of the Gateway resource. It matches pattern
            ``projects/*/locations/*/gateways/<gateway_name>``.
        self_link (str):
            Output only. Server-defined URL of this
            resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the Gateway resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        type_ (google.events.cloud.networkservices_v1.types.Gateway.Type):
            Immutable. The type of the customer managed
            gateway. This field is required. If unspecified,
            an error is returned.
        addresses (MutableSequence[str]):
            Optional. Zero or one IPv4 or IPv6 address on which the
            Gateway will receive the traffic. When no address is
            provided, an IP from the subnetwork is allocated

            This field only applies to gateways of type
            'SECURE_WEB_GATEWAY'. Gateways of type 'OPEN_MESH' listen on
            0.0.0.0 for IPv4 and :: for IPv6.
        ports (MutableSequence[int]):
            Required. One or more port numbers (1-65535), on which the
            Gateway will receive traffic. The proxy binds to the
            specified ports. Gateways of type 'SECURE_WEB_GATEWAY' are
            limited to 1 port. Gateways of type 'OPEN_MESH' listen on
            0.0.0.0 for IPv4 and :: for IPv6 and support multiple ports.
        scope (str):
            Optional. Scope determines how configuration
            across multiple Gateway instances are merged.
            The configuration for multiple Gateway instances
            with the same scope will be merged as presented
            as a single coniguration to the proxy/load
            balancer.

            Max length 64 characters.
            Scope should start with a letter and can only
            have letters, numbers, hyphens.
        server_tls_policy (str):
            Optional. A fully-qualified ServerTLSPolicy
            URL reference. Specifies how TLS traffic is
            terminated. If empty, TLS termination is
            disabled.
        certificate_urls (MutableSequence[str]):
            Optional. A fully-qualified Certificates URL reference. The
            proxy presents a Certificate (selected based on SNI) when
            establishing a TLS connection. This feature only applies to
            gateways of type 'SECURE_WEB_GATEWAY'.
        gateway_security_policy (str):
            Optional. A fully-qualified GatewaySecurityPolicy URL
            reference. Defines how a server should apply security policy
            to inbound (VM to Proxy) initiated connections.

            For example:
            ``projects/*/locations/*/gatewaySecurityPolicies/swg-policy``.

            This policy is specific to gateways of type
            'SECURE_WEB_GATEWAY'.
        network (str):
            Optional. The relative resource name identifying the VPC
            network that is using this configuration. For example:
            ``projects/*/global/networks/network-1``.

            Currently, this field is specific to gateways of type
            'SECURE_WEB_GATEWAY'.
        subnetwork (str):
            Optional. The relative resource name identifying the
            subnetwork in which this SWG is allocated. For example:
            ``projects/*/regions/us-central1/subnetworks/network-1``

            Currently, this field is specific to gateways of type
            'SECURE_WEB_GATEWAY".
    """
    class Type(proto.Enum):
        r"""The type of the customer-managed gateway. Possible values are:

        -  OPEN_MESH
        -  SECURE_WEB_GATEWAY

        Values:
            TYPE_UNSPECIFIED (0):
                The type of the customer managed gateway is
                unspecified.
            OPEN_MESH (1):
                The type of the customer managed gateway is
                TrafficDirector Open Mesh.
            SECURE_WEB_GATEWAY (2):
                The type of the customer managed gateway is
                SecureWebGateway (SWG).
        """
        TYPE_UNSPECIFIED = 0
        OPEN_MESH = 1
        SECURE_WEB_GATEWAY = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=13,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=6,
        enum=Type,
    )
    addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    ports: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=11,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=8,
    )
    server_tls_policy: str = proto.Field(
        proto.STRING,
        number=9,
    )
    certificate_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    gateway_security_policy: str = proto.Field(
        proto.STRING,
        number=18,
    )
    network: str = proto.Field(
        proto.STRING,
        number=16,
    )
    subnetwork: str = proto.Field(
        proto.STRING,
        number=17,
    )


class GrpcRoute(proto.Message):
    r"""GrpcRoute is the resource defining how gRPC traffic routed by
    a Mesh or Gateway resource is routed.

    Attributes:
        name (str):
            Required. Name of the GrpcRoute resource. It matches pattern
            ``projects/*/locations/global/grpcRoutes/<grpc_route_name>``
        self_link (str):
            Output only. Server-defined URL of this
            resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the GrpcRoute resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        hostnames (MutableSequence[str]):
            Required. Service hostnames with an optional port for which
            this route describes traffic.

            Format: [:]

            Hostname is the fully qualified domain name of a network
            host. This matches the RFC 1123 definition of a hostname
            with 2 notable exceptions:

            -  IPs are not allowed.
            -  A hostname may be prefixed with a wildcard label
               (``*.``). The wildcard label must appear by itself as the
               first label.

            Hostname can be "precise" which is a domain name without the
            terminating dot of a network host (e.g. ``foo.example.com``)
            or "wildcard", which is a domain name prefixed with a single
            wildcard label (e.g. ``*.example.com``).

            Note that as per RFC1035 and RFC1123, a label must consist
            of lower case alphanumeric characters or '-', and must start
            and end with an alphanumeric character. No other punctuation
            is allowed.

            The routes associated with a Mesh or Gateway must have
            unique hostnames. If you attempt to attach multiple routes
            with conflicting hostnames, the configuration will be
            rejected.

            For example, while it is acceptable for routes for the
            hostnames ``*.foo.bar.com`` and ``*.bar.com`` to be
            associated with the same route, it is not possible to
            associate two routes both with ``*.bar.com`` or both with
            ``bar.com``.

            If a port is specified, then gRPC clients must use the
            channel URI with the port to match this rule (i.e.
            "xds:///service:123"), otherwise they must supply the URI
            without a port (i.e. "xds:///service").
        meshes (MutableSequence[str]):
            Optional. Meshes defines a list of meshes this GrpcRoute is
            attached to, as one of the routing rules to route the
            requests served by the mesh.

            Each mesh reference should match the pattern:
            ``projects/*/locations/global/meshes/<mesh_name>``
        gateways (MutableSequence[str]):
            Optional. Gateways defines a list of gateways this GrpcRoute
            is attached to, as one of the routing rules to route the
            requests served by the gateway.

            Each gateway reference should match the pattern:
            ``projects/*/locations/global/gateways/<gateway_name>``
        rules (MutableSequence[google.events.cloud.networkservices_v1.types.GrpcRoute.RouteRule]):
            Required. A list of detailed rules defining
            how to route traffic.
            Within a single GrpcRoute, the
            GrpcRoute.RouteAction associated with the first
            matching GrpcRoute.RouteRule will be executed.
            At least one rule must be supplied.
    """

    class MethodMatch(proto.Message):
        r"""Specifies a match against a method.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            type_ (google.events.cloud.networkservices_v1.types.GrpcRoute.MethodMatch.Type):
                Optional. Specifies how to match against the
                name. If not specified, a default value of
                "EXACT" is used.
            grpc_service (str):
                Required. Name of the service to match
                against. If unspecified, will match all
                services.
            grpc_method (str):
                Required. Name of the method to match
                against. If unspecified, will match all methods.
            case_sensitive (bool):
                Optional. Specifies that matches are case sensitive. The
                default value is true. case_sensitive must not be used with
                a type of REGULAR_EXPRESSION.

                This field is a member of `oneof`_ ``_case_sensitive``.
        """
        class Type(proto.Enum):
            r"""The type of the match.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified.
                EXACT (1):
                    Will only match the exact name provided.
                REGULAR_EXPRESSION (2):
                    Will interpret grpc_method and grpc_service as regexes. RE2
                    syntax is supported.
            """
            TYPE_UNSPECIFIED = 0
            EXACT = 1
            REGULAR_EXPRESSION = 2

        type_: 'GrpcRoute.MethodMatch.Type' = proto.Field(
            proto.ENUM,
            number=1,
            enum='GrpcRoute.MethodMatch.Type',
        )
        grpc_service: str = proto.Field(
            proto.STRING,
            number=2,
        )
        grpc_method: str = proto.Field(
            proto.STRING,
            number=3,
        )
        case_sensitive: bool = proto.Field(
            proto.BOOL,
            number=4,
            optional=True,
        )

    class HeaderMatch(proto.Message):
        r"""A match against a collection of headers.

        Attributes:
            type_ (google.events.cloud.networkservices_v1.types.GrpcRoute.HeaderMatch.Type):
                Optional. Specifies how to match against the
                value of the header. If not specified, a default
                value of EXACT is used.
            key (str):
                Required. The key of the header.
            value (str):
                Required. The value of the header.
        """
        class Type(proto.Enum):
            r"""The type of match.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified.
                EXACT (1):
                    Will only match the exact value provided.
                REGULAR_EXPRESSION (2):
                    Will match paths conforming to the prefix
                    specified by value. RE2 syntax is supported.
            """
            TYPE_UNSPECIFIED = 0
            EXACT = 1
            REGULAR_EXPRESSION = 2

        type_: 'GrpcRoute.HeaderMatch.Type' = proto.Field(
            proto.ENUM,
            number=1,
            enum='GrpcRoute.HeaderMatch.Type',
        )
        key: str = proto.Field(
            proto.STRING,
            number=2,
        )
        value: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class RouteMatch(proto.Message):
        r"""Criteria for matching traffic. A RouteMatch will be
        considered to match when all supplied fields match.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            method (google.events.cloud.networkservices_v1.types.GrpcRoute.MethodMatch):
                Optional. A gRPC method to match against. If
                this field is empty or omitted, will match all
                methods.

                This field is a member of `oneof`_ ``_method``.
            headers (MutableSequence[google.events.cloud.networkservices_v1.types.GrpcRoute.HeaderMatch]):
                Optional. Specifies a collection of headers
                to match.
        """

        method: 'GrpcRoute.MethodMatch' = proto.Field(
            proto.MESSAGE,
            number=1,
            optional=True,
            message='GrpcRoute.MethodMatch',
        )
        headers: MutableSequence['GrpcRoute.HeaderMatch'] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message='GrpcRoute.HeaderMatch',
        )

    class Destination(proto.Message):
        r"""The destination to which traffic will be routed.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            service_name (str):
                Required. The URL of a destination service to
                which to route traffic. Must refer to either a
                BackendService or ServiceDirectoryService.

                This field is a member of `oneof`_ ``destination_type``.
            weight (int):
                Optional. Specifies the proportion of
                requests forwarded to the backend referenced by
                the serviceName field. This is computed as:

                        weight/Sum(weights in this destination
                list). For non-zero values, there may be some
                epsilon from the exact proportion defined here
                depending on the precision an implementation
                supports.

                If only one serviceName is specified and it has
                a weight greater than 0, 100% of the traffic is
                forwarded to that backend.

                If weights are specified for any one service
                name, they need to be specified for all of them.

                If weights are unspecified for all services,
                then, traffic is distributed in equal
                proportions to all of them.

                This field is a member of `oneof`_ ``_weight``.
        """

        service_name: str = proto.Field(
            proto.STRING,
            number=1,
            oneof='destination_type',
        )
        weight: int = proto.Field(
            proto.INT32,
            number=2,
            optional=True,
        )

    class FaultInjectionPolicy(proto.Message):
        r"""The specification for fault injection introduced into traffic
        to test the resiliency of clients to destination service
        failure. As part of fault injection, when clients send requests
        to a destination, delays can be introduced on a percentage of
        requests before sending those requests to the destination
        service. Similarly requests from clients can be aborted by for a
        percentage of requests.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            delay (google.events.cloud.networkservices_v1.types.GrpcRoute.FaultInjectionPolicy.Delay):
                The specification for injecting delay to
                client requests.

                This field is a member of `oneof`_ ``_delay``.
            abort (google.events.cloud.networkservices_v1.types.GrpcRoute.FaultInjectionPolicy.Abort):
                The specification for aborting to client
                requests.

                This field is a member of `oneof`_ ``_abort``.
        """

        class Delay(proto.Message):
            r"""Specification of how client requests are delayed as part of
            fault injection before being sent to a destination.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                fixed_delay (google.protobuf.duration_pb2.Duration):
                    Specify a fixed delay before forwarding the
                    request.

                    This field is a member of `oneof`_ ``_fixed_delay``.
                percentage (int):
                    The percentage of traffic on which delay will be injected.

                    The value must be between [0, 100]

                    This field is a member of `oneof`_ ``_percentage``.
            """

            fixed_delay: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=1,
                optional=True,
                message=duration_pb2.Duration,
            )
            percentage: int = proto.Field(
                proto.INT32,
                number=2,
                optional=True,
            )

        class Abort(proto.Message):
            r"""Specification of how client requests are aborted as part of
            fault injection before being sent to a destination.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                http_status (int):
                    The HTTP status code used to abort the
                    request.
                    The value must be between 200 and 599 inclusive.

                    This field is a member of `oneof`_ ``_http_status``.
                percentage (int):
                    The percentage of traffic which will be aborted.

                    The value must be between [0, 100]

                    This field is a member of `oneof`_ ``_percentage``.
            """

            http_status: int = proto.Field(
                proto.INT32,
                number=1,
                optional=True,
            )
            percentage: int = proto.Field(
                proto.INT32,
                number=2,
                optional=True,
            )

        delay: 'GrpcRoute.FaultInjectionPolicy.Delay' = proto.Field(
            proto.MESSAGE,
            number=1,
            optional=True,
            message='GrpcRoute.FaultInjectionPolicy.Delay',
        )
        abort: 'GrpcRoute.FaultInjectionPolicy.Abort' = proto.Field(
            proto.MESSAGE,
            number=2,
            optional=True,
            message='GrpcRoute.FaultInjectionPolicy.Abort',
        )

    class RetryPolicy(proto.Message):
        r"""The specifications for retries.

        Attributes:
            retry_conditions (MutableSequence[str]):
                -  connect-failure: Router will retry on failures connecting
                   to Backend Services, for example due to connection
                   timeouts.
                -  refused-stream: Router will retry if the backend service
                   resets the stream with a REFUSED_STREAM error code. This
                   reset type indicates that it is safe to retry.
                -  cancelled: Router will retry if the gRPC status code in
                   the response header is set to cancelled
                -  deadline-exceeded: Router will retry if the gRPC status
                   code in the response header is set to deadline-exceeded
                -  resource-exhausted: Router will retry if the gRPC status
                   code in the response header is set to resource-exhausted
                -  unavailable: Router will retry if the gRPC status code in
                   the response header is set to unavailable
            num_retries (int):
                Specifies the allowed number of retries. This
                number must be > 0. If not specified, default to
                1.
        """

        retry_conditions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        num_retries: int = proto.Field(
            proto.UINT32,
            number=2,
        )

    class RouteAction(proto.Message):
        r"""Specifies how to route matched traffic.

        Attributes:
            destinations (MutableSequence[google.events.cloud.networkservices_v1.types.GrpcRoute.Destination]):
                Optional. The destination services to which
                traffic should be forwarded. If multiple
                destinations are specified, traffic will be
                split between Backend Service(s) according to
                the weight field of these destinations.
            fault_injection_policy (google.events.cloud.networkservices_v1.types.GrpcRoute.FaultInjectionPolicy):
                Optional. The specification for fault injection introduced
                into traffic to test the resiliency of clients to
                destination service failure. As part of fault injection,
                when clients send requests to a destination, delays can be
                introduced on a percentage of requests before sending those
                requests to the destination service. Similarly requests from
                clients can be aborted by for a percentage of requests.

                timeout and retry_policy will be ignored by clients that are
                configured with a fault_injection_policy
            timeout (google.protobuf.duration_pb2.Duration):
                Optional. Specifies the timeout for selected
                route. Timeout is computed from the time the
                request has been fully processed (i.e. end of
                stream) up until the response has been
                completely processed. Timeout includes all
                retries.
            retry_policy (google.events.cloud.networkservices_v1.types.GrpcRoute.RetryPolicy):
                Optional. Specifies the retry policy
                associated with this route.
        """

        destinations: MutableSequence['GrpcRoute.Destination'] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message='GrpcRoute.Destination',
        )
        fault_injection_policy: 'GrpcRoute.FaultInjectionPolicy' = proto.Field(
            proto.MESSAGE,
            number=3,
            message='GrpcRoute.FaultInjectionPolicy',
        )
        timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=7,
            message=duration_pb2.Duration,
        )
        retry_policy: 'GrpcRoute.RetryPolicy' = proto.Field(
            proto.MESSAGE,
            number=8,
            message='GrpcRoute.RetryPolicy',
        )

    class RouteRule(proto.Message):
        r"""Describes how to route traffic.

        Attributes:
            matches (MutableSequence[google.events.cloud.networkservices_v1.types.GrpcRoute.RouteMatch]):
                Optional. Matches define conditions used for
                matching the rule against incoming gRPC
                requests. Each match is independent, i.e. this
                rule will be matched if ANY one of the matches
                is satisfied.  If no matches field is specified,
                this rule will unconditionally match traffic.
            action (google.events.cloud.networkservices_v1.types.GrpcRoute.RouteAction):
                Required. A detailed rule defining how to
                route traffic. This field is required.
        """

        matches: MutableSequence['GrpcRoute.RouteMatch'] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message='GrpcRoute.RouteMatch',
        )
        action: 'GrpcRoute.RouteAction' = proto.Field(
            proto.MESSAGE,
            number=2,
            message='GrpcRoute.RouteAction',
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=12,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    hostnames: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    meshes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    gateways: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    rules: MutableSequence[RouteRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=RouteRule,
    )


class HttpRoute(proto.Message):
    r"""HttpRoute is the resource defining how HTTP traffic should be
    routed by a Mesh or Gateway resource.

    Attributes:
        name (str):
            Required. Name of the HttpRoute resource. It matches pattern
            ``projects/*/locations/global/httpRoutes/http_route_name>``.
        self_link (str):
            Output only. Server-defined URL of this
            resource
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        hostnames (MutableSequence[str]):
            Required. Hostnames define a set of hosts that should match
            against the HTTP host header to select a HttpRoute to
            process the request. Hostname is the fully qualified domain
            name of a network host, as defined by RFC 1123 with the
            exception that:

            -  IPs are not allowed.
            -  A hostname may be prefixed with a wildcard label
               (``*.``). The wildcard label must appear by itself as the
               first label.

            Hostname can be "precise" which is a domain name without the
            terminating dot of a network host (e.g. ``foo.example.com``)
            or "wildcard", which is a domain name prefixed with a single
            wildcard label (e.g. ``*.example.com``).

            Note that as per RFC1035 and RFC1123, a label must consist
            of lower case alphanumeric characters or '-', and must start
            and end with an alphanumeric character. No other punctuation
            is allowed.

            The routes associated with a Mesh or Gateways must have
            unique hostnames. If you attempt to attach multiple routes
            with conflicting hostnames, the configuration will be
            rejected.

            For example, while it is acceptable for routes for the
            hostnames ``*.foo.bar.com`` and ``*.bar.com`` to be
            associated with the same Mesh (or Gateways under the same
            scope), it is not possible to associate two routes both with
            ``*.bar.com`` or both with ``bar.com``.
        meshes (MutableSequence[str]):
            Optional. Meshes defines a list of meshes this HttpRoute is
            attached to, as one of the routing rules to route the
            requests served by the mesh.

            Each mesh reference should match the pattern:
            ``projects/*/locations/global/meshes/<mesh_name>``

            The attached Mesh should be of a type SIDECAR
        gateways (MutableSequence[str]):
            Optional. Gateways defines a list of gateways this HttpRoute
            is attached to, as one of the routing rules to route the
            requests served by the gateway.

            Each gateway reference should match the pattern:
            ``projects/*/locations/global/gateways/<gateway_name>``
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the HttpRoute resource.
        rules (MutableSequence[google.events.cloud.networkservices_v1.types.HttpRoute.RouteRule]):
            Required. Rules that define how traffic is
            routed and handled. Rules will be matched
            sequentially based on the RouteMatch specified
            for the rule.
    """

    class HeaderMatch(proto.Message):
        r"""Specifies how to select a route rule based on HTTP request
        headers.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            exact_match (str):
                The value of the header should match exactly the content of
                exact_match.

                This field is a member of `oneof`_ ``MatchType``.
            regex_match (str):
                The value of the header must match the regular expression
                specified in regex_match. For regular expression grammar,
                please see: https://github.com/google/re2/wiki/Syntax

                This field is a member of `oneof`_ ``MatchType``.
            prefix_match (str):
                The value of the header must start with the contents of
                prefix_match.

                This field is a member of `oneof`_ ``MatchType``.
            present_match (bool):
                A header with header_name must exist. The match takes place
                whether or not the header has a value.

                This field is a member of `oneof`_ ``MatchType``.
            suffix_match (str):
                The value of the header must end with the contents of
                suffix_match.

                This field is a member of `oneof`_ ``MatchType``.
            range_match (google.events.cloud.networkservices_v1.types.HttpRoute.HeaderMatch.IntegerRange):
                If specified, the rule will match if the
                request header value is within the range.

                This field is a member of `oneof`_ ``MatchType``.
            header (str):
                The name of the HTTP header to match against.
            invert_match (bool):
                If specified, the match result will be
                inverted before checking. Default value is set
                to false.
        """

        class IntegerRange(proto.Message):
            r"""Represents an integer value range.

            Attributes:
                start (int):
                    Start of the range (inclusive)
                end (int):
                    End of the range (exclusive)
            """

            start: int = proto.Field(
                proto.INT32,
                number=1,
            )
            end: int = proto.Field(
                proto.INT32,
                number=2,
            )

        exact_match: str = proto.Field(
            proto.STRING,
            number=2,
            oneof='MatchType',
        )
        regex_match: str = proto.Field(
            proto.STRING,
            number=3,
            oneof='MatchType',
        )
        prefix_match: str = proto.Field(
            proto.STRING,
            number=4,
            oneof='MatchType',
        )
        present_match: bool = proto.Field(
            proto.BOOL,
            number=5,
            oneof='MatchType',
        )
        suffix_match: str = proto.Field(
            proto.STRING,
            number=6,
            oneof='MatchType',
        )
        range_match: 'HttpRoute.HeaderMatch.IntegerRange' = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof='MatchType',
            message='HttpRoute.HeaderMatch.IntegerRange',
        )
        header: str = proto.Field(
            proto.STRING,
            number=1,
        )
        invert_match: bool = proto.Field(
            proto.BOOL,
            number=8,
        )

    class QueryParameterMatch(proto.Message):
        r"""Specifications to match a query parameter in the request.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            exact_match (str):
                The value of the query parameter must exactly match the
                contents of exact_match.

                Only one of exact_match, regex_match, or present_match must
                be set.

                This field is a member of `oneof`_ ``MatchType``.
            regex_match (str):
                The value of the query parameter must match the regular
                expression specified by regex_match. For regular expression
                grammar, please see
                https://github.com/google/re2/wiki/Syntax

                Only one of exact_match, regex_match, or present_match must
                be set.

                This field is a member of `oneof`_ ``MatchType``.
            present_match (bool):
                Specifies that the QueryParameterMatcher matches if request
                contains query parameter, irrespective of whether the
                parameter has a value or not.

                Only one of exact_match, regex_match, or present_match must
                be set.

                This field is a member of `oneof`_ ``MatchType``.
            query_parameter (str):
                The name of the query parameter to match.
        """

        exact_match: str = proto.Field(
            proto.STRING,
            number=2,
            oneof='MatchType',
        )
        regex_match: str = proto.Field(
            proto.STRING,
            number=3,
            oneof='MatchType',
        )
        present_match: bool = proto.Field(
            proto.BOOL,
            number=4,
            oneof='MatchType',
        )
        query_parameter: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class RouteMatch(proto.Message):
        r"""RouteMatch defines specifications used to match requests. If
        multiple match types are set, this RouteMatch will match if ALL
        type of matches are matched.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            full_path_match (str):
                The HTTP request path value should exactly match this value.

                Only one of full_path_match, prefix_match, or regex_match
                should be used.

                This field is a member of `oneof`_ ``PathMatch``.
            prefix_match (str):
                The HTTP request path value must begin with specified
                prefix_match. prefix_match must begin with a /.

                Only one of full_path_match, prefix_match, or regex_match
                should be used.

                This field is a member of `oneof`_ ``PathMatch``.
            regex_match (str):
                The HTTP request path value must satisfy the regular
                expression specified by regex_match after removing any query
                parameters and anchor supplied with the original URL. For
                regular expression grammar, please see
                https://github.com/google/re2/wiki/Syntax

                Only one of full_path_match, prefix_match, or regex_match
                should be used.

                This field is a member of `oneof`_ ``PathMatch``.
            ignore_case (bool):
                Specifies if prefix_match and full_path_match matches are
                case sensitive. The default value is false.
            headers (MutableSequence[google.events.cloud.networkservices_v1.types.HttpRoute.HeaderMatch]):
                Specifies a list of HTTP request headers to
                match against. ALL of the supplied headers must
                be matched.
            query_parameters (MutableSequence[google.events.cloud.networkservices_v1.types.HttpRoute.QueryParameterMatch]):
                Specifies a list of query parameters to match
                against. ALL of the query parameters must be
                matched.
        """

        full_path_match: str = proto.Field(
            proto.STRING,
            number=1,
            oneof='PathMatch',
        )
        prefix_match: str = proto.Field(
            proto.STRING,
            number=2,
            oneof='PathMatch',
        )
        regex_match: str = proto.Field(
            proto.STRING,
            number=3,
            oneof='PathMatch',
        )
        ignore_case: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        headers: MutableSequence['HttpRoute.HeaderMatch'] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message='HttpRoute.HeaderMatch',
        )
        query_parameters: MutableSequence['HttpRoute.QueryParameterMatch'] = proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message='HttpRoute.QueryParameterMatch',
        )

    class Destination(proto.Message):
        r"""Specifications of a destination to which the request should
        be routed to.

        Attributes:
            service_name (str):
                The URL of a BackendService to route traffic
                to.
            weight (int):
                Specifies the proportion of requests
                forwarded to the backend referenced by the
                serviceName field. This is computed as:

                        weight/Sum(weights in this destination
                list). For non-zero values, there may be some
                epsilon from the exact proportion defined here
                depending on the precision an implementation
                supports.

                If only one serviceName is specified and it has
                a weight greater than 0, 100% of the traffic is
                forwarded to that backend.

                If weights are specified for any one service
                name, they need to be specified for all of them.

                If weights are unspecified for all services,
                then, traffic is distributed in equal
                proportions to all of them.
        """

        service_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        weight: int = proto.Field(
            proto.INT32,
            number=2,
        )

    class Redirect(proto.Message):
        r"""The specification for redirecting traffic.

        Attributes:
            host_redirect (str):
                The host that will be used in the redirect
                response instead of the one that was supplied in
                the request.
            path_redirect (str):
                The path that will be used in the redirect response instead
                of the one that was supplied in the request. path_redirect
                can not be supplied together with prefix_redirect. Supply
                one alone or neither. If neither is supplied, the path of
                the original request will be used for the redirect.
            prefix_rewrite (str):
                Indicates that during redirection, the
                matched prefix (or path) should be swapped with
                this value. This option allows URLs be
                dynamically created based on the request.
            response_code (google.events.cloud.networkservices_v1.types.HttpRoute.Redirect.ResponseCode):
                The HTTP Status code to use for the redirect.
            https_redirect (bool):
                If set to true, the URL scheme in the
                redirected request is set to https. If set to
                false, the URL scheme of the redirected request
                will remain the same as that of the request.

                The default is set to false.
            strip_query (bool):
                if set to true, any accompanying query
                portion of the original URL is removed prior to
                redirecting the request. If set to false, the
                query portion of the original URL is retained.

                The default is set to false.
            port_redirect (int):
                The port that will be used in the redirected
                request instead of the one that was supplied in
                the request.
        """
        class ResponseCode(proto.Enum):
            r"""Supported HTTP response code.

            Values:
                RESPONSE_CODE_UNSPECIFIED (0):
                    Default value
                MOVED_PERMANENTLY_DEFAULT (1):
                    Corresponds to 301.
                FOUND (2):
                    Corresponds to 302.
                SEE_OTHER (3):
                    Corresponds to 303.
                TEMPORARY_REDIRECT (4):
                    Corresponds to 307. In this case, the request
                    method will be retained.
                PERMANENT_REDIRECT (5):
                    Corresponds to 308. In this case, the request
                    method will be retained.
            """
            RESPONSE_CODE_UNSPECIFIED = 0
            MOVED_PERMANENTLY_DEFAULT = 1
            FOUND = 2
            SEE_OTHER = 3
            TEMPORARY_REDIRECT = 4
            PERMANENT_REDIRECT = 5

        host_redirect: str = proto.Field(
            proto.STRING,
            number=1,
        )
        path_redirect: str = proto.Field(
            proto.STRING,
            number=2,
        )
        prefix_rewrite: str = proto.Field(
            proto.STRING,
            number=3,
        )
        response_code: 'HttpRoute.Redirect.ResponseCode' = proto.Field(
            proto.ENUM,
            number=4,
            enum='HttpRoute.Redirect.ResponseCode',
        )
        https_redirect: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        strip_query: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        port_redirect: int = proto.Field(
            proto.INT32,
            number=7,
        )

    class FaultInjectionPolicy(proto.Message):
        r"""The specification for fault injection introduced into traffic
        to test the resiliency of clients to destination service
        failure. As part of fault injection, when clients send requests
        to a destination, delays can be introduced by client proxy on a
        percentage of requests before sending those requests to the
        destination service. Similarly requests can be aborted by client
        proxy for a percentage of requests.

        Attributes:
            delay (google.events.cloud.networkservices_v1.types.HttpRoute.FaultInjectionPolicy.Delay):
                The specification for injecting delay to
                client requests.
            abort (google.events.cloud.networkservices_v1.types.HttpRoute.FaultInjectionPolicy.Abort):
                The specification for aborting to client
                requests.
        """

        class Delay(proto.Message):
            r"""Specification of how client requests are delayed as part of
            fault injection before being sent to a destination.

            Attributes:
                fixed_delay (google.protobuf.duration_pb2.Duration):
                    Specify a fixed delay before forwarding the
                    request.
                percentage (int):
                    The percentage of traffic on which delay will be injected.

                    The value must be between [0, 100]
            """

            fixed_delay: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=1,
                message=duration_pb2.Duration,
            )
            percentage: int = proto.Field(
                proto.INT32,
                number=2,
            )

        class Abort(proto.Message):
            r"""Specification of how client requests are aborted as part of
            fault injection before being sent to a destination.

            Attributes:
                http_status (int):
                    The HTTP status code used to abort the
                    request.
                    The value must be between 200 and 599 inclusive.
                percentage (int):
                    The percentage of traffic which will be aborted.

                    The value must be between [0, 100]
            """

            http_status: int = proto.Field(
                proto.INT32,
                number=1,
            )
            percentage: int = proto.Field(
                proto.INT32,
                number=2,
            )

        delay: 'HttpRoute.FaultInjectionPolicy.Delay' = proto.Field(
            proto.MESSAGE,
            number=1,
            message='HttpRoute.FaultInjectionPolicy.Delay',
        )
        abort: 'HttpRoute.FaultInjectionPolicy.Abort' = proto.Field(
            proto.MESSAGE,
            number=2,
            message='HttpRoute.FaultInjectionPolicy.Abort',
        )

    class HeaderModifier(proto.Message):
        r"""The specification for modifying HTTP header in HTTP request
        and HTTP response.

        Attributes:
            set (MutableMapping[str, str]):
                Completely overwrite/replace the headers with
                given map where key is the name of the header,
                value is the value of the header.
            add (MutableMapping[str, str]):
                Add the headers with given map where key is
                the name of the header, value is the value of
                the header.
            remove (MutableSequence[str]):
                Remove headers (matching by header names)
                specified in the list.
        """

        set: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=1,
        )
        add: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )
        remove: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    class URLRewrite(proto.Message):
        r"""The specification for modifying the URL of the request, prior
        to forwarding the request to the destination.

        Attributes:
            path_prefix_rewrite (str):
                Prior to forwarding the request to the
                selected destination, the matching portion of
                the requests path is replaced by this value.
            host_rewrite (str):
                Prior to forwarding the request to the
                selected destination, the requests host header
                is replaced by this value.
        """

        path_prefix_rewrite: str = proto.Field(
            proto.STRING,
            number=1,
        )
        host_rewrite: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class RetryPolicy(proto.Message):
        r"""The specifications for retries.

        Attributes:
            retry_conditions (MutableSequence[str]):
                Specifies one or more conditions when this retry policy
                applies. Valid values are: 5xx: Proxy will attempt a retry
                if the destination service responds with any 5xx response
                code, of if the destination service does not respond at all,
                example: disconnect, reset, read timeout, connection failure
                and refused streams.

                gateway-error: Similar to 5xx, but only applies to response
                codes 502, 503, 504.

                reset: Proxy will attempt a retry if the destination service
                does not respond at all (disconnect/reset/read timeout)

                connect-failure: Proxy will retry on failures connecting to
                destination for example due to connection timeouts.

                retriable-4xx: Proxy will retry fro retriable 4xx response
                codes. Currently the only retriable error supported is 409.

                refused-stream: Proxy will retry if the destination resets
                the stream with a REFUSED_STREAM error code. This reset type
                indicates that it is safe to retry.
            num_retries (int):
                Specifies the allowed number of retries. This
                number must be > 0. If not specified, default to
                1.
            per_try_timeout (google.protobuf.duration_pb2.Duration):
                Specifies a non-zero timeout per retry
                attempt.
        """

        retry_conditions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        num_retries: int = proto.Field(
            proto.INT32,
            number=2,
        )
        per_try_timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )

    class RequestMirrorPolicy(proto.Message):
        r"""Specifies the policy on how requests are shadowed to a
        separate mirrored destination service. The proxy does not wait
        for responses from the shadow service. Prior to sending traffic
        to the shadow service, the host/authority header is suffixed
        with -shadow.

        Attributes:
            destination (google.events.cloud.networkservices_v1.types.HttpRoute.Destination):
                The destination the requests will be mirrored
                to. The weight of the destination will be
                ignored.
        """

        destination: 'HttpRoute.Destination' = proto.Field(
            proto.MESSAGE,
            number=1,
            message='HttpRoute.Destination',
        )

    class CorsPolicy(proto.Message):
        r"""The Specification for allowing client side cross-origin
        requests.

        Attributes:
            allow_origins (MutableSequence[str]):
                Specifies the list of origins that will be allowed to do
                CORS requests. An origin is allowed if it matches either an
                item in allow_origins or an item in allow_origin_regexes.
            allow_origin_regexes (MutableSequence[str]):
                Specifies the regular expression patterns
                that match allowed origins. For regular
                expression grammar, please see
                https://github.com/google/re2/wiki/Syntax.
            allow_methods (MutableSequence[str]):
                Specifies the content for
                Access-Control-Allow-Methods header.
            allow_headers (MutableSequence[str]):
                Specifies the content for
                Access-Control-Allow-Headers header.
            expose_headers (MutableSequence[str]):
                Specifies the content for
                Access-Control-Expose-Headers header.
            max_age (str):
                Specifies how long result of a preflight
                request can be cached in seconds. This
                translates to the Access-Control-Max-Age header.
            allow_credentials (bool):
                In response to a preflight request, setting
                this to true indicates that the actual request
                can include user credentials. This translates to
                the Access-Control-Allow-Credentials header.

                Default value is false.
            disabled (bool):
                If true, the CORS policy is disabled. The
                default value is false, which indicates that the
                CORS policy is in effect.
        """

        allow_origins: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        allow_origin_regexes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        allow_methods: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        allow_headers: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        expose_headers: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=5,
        )
        max_age: str = proto.Field(
            proto.STRING,
            number=6,
        )
        allow_credentials: bool = proto.Field(
            proto.BOOL,
            number=7,
        )
        disabled: bool = proto.Field(
            proto.BOOL,
            number=8,
        )

    class RouteAction(proto.Message):
        r"""The specifications for routing traffic and applying
        associated policies.

        Attributes:
            destinations (MutableSequence[google.events.cloud.networkservices_v1.types.HttpRoute.Destination]):
                The destination to which traffic should be
                forwarded.
            redirect (google.events.cloud.networkservices_v1.types.HttpRoute.Redirect):
                If set, the request is directed as configured
                by this field.
            fault_injection_policy (google.events.cloud.networkservices_v1.types.HttpRoute.FaultInjectionPolicy):
                The specification for fault injection introduced into
                traffic to test the resiliency of clients to backend service
                failure. As part of fault injection, when clients send
                requests to a backend service, delays can be introduced on a
                percentage of requests before sending those requests to the
                backend service. Similarly requests from clients can be
                aborted for a percentage of requests.

                timeout and retry_policy will be ignored by clients that are
                configured with a fault_injection_policy
            request_header_modifier (google.events.cloud.networkservices_v1.types.HttpRoute.HeaderModifier):
                The specification for modifying the headers
                of a matching request prior to delivery of the
                request to the destination.
            response_header_modifier (google.events.cloud.networkservices_v1.types.HttpRoute.HeaderModifier):
                The specification for modifying the headers
                of a response prior to sending the response back
                to the client.
            url_rewrite (google.events.cloud.networkservices_v1.types.HttpRoute.URLRewrite):
                The specification for rewrite URL before
                forwarding requests to the destination.
            timeout (google.protobuf.duration_pb2.Duration):
                Specifies the timeout for selected route.
                Timeout is computed from the time the request
                has been fully processed (i.e. end of stream) up
                until the response has been completely
                processed. Timeout includes all retries.
            retry_policy (google.events.cloud.networkservices_v1.types.HttpRoute.RetryPolicy):
                Specifies the retry policy associated with
                this route.
            request_mirror_policy (google.events.cloud.networkservices_v1.types.HttpRoute.RequestMirrorPolicy):
                Specifies the policy on how requests intended
                for the routes destination are shadowed to a
                separate mirrored destination. Proxy will not
                wait for the shadow destination to respond
                before returning the response. Prior to sending
                traffic to the shadow service, the
                host/authority header is suffixed with -shadow.
            cors_policy (google.events.cloud.networkservices_v1.types.HttpRoute.CorsPolicy):
                The specification for allowing client side
                cross-origin requests.
        """

        destinations: MutableSequence['HttpRoute.Destination'] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message='HttpRoute.Destination',
        )
        redirect: 'HttpRoute.Redirect' = proto.Field(
            proto.MESSAGE,
            number=2,
            message='HttpRoute.Redirect',
        )
        fault_injection_policy: 'HttpRoute.FaultInjectionPolicy' = proto.Field(
            proto.MESSAGE,
            number=4,
            message='HttpRoute.FaultInjectionPolicy',
        )
        request_header_modifier: 'HttpRoute.HeaderModifier' = proto.Field(
            proto.MESSAGE,
            number=5,
            message='HttpRoute.HeaderModifier',
        )
        response_header_modifier: 'HttpRoute.HeaderModifier' = proto.Field(
            proto.MESSAGE,
            number=6,
            message='HttpRoute.HeaderModifier',
        )
        url_rewrite: 'HttpRoute.URLRewrite' = proto.Field(
            proto.MESSAGE,
            number=7,
            message='HttpRoute.URLRewrite',
        )
        timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=8,
            message=duration_pb2.Duration,
        )
        retry_policy: 'HttpRoute.RetryPolicy' = proto.Field(
            proto.MESSAGE,
            number=9,
            message='HttpRoute.RetryPolicy',
        )
        request_mirror_policy: 'HttpRoute.RequestMirrorPolicy' = proto.Field(
            proto.MESSAGE,
            number=10,
            message='HttpRoute.RequestMirrorPolicy',
        )
        cors_policy: 'HttpRoute.CorsPolicy' = proto.Field(
            proto.MESSAGE,
            number=11,
            message='HttpRoute.CorsPolicy',
        )

    class RouteRule(proto.Message):
        r"""Specifies how to match traffic and how to route traffic when
        traffic is matched.

        Attributes:
            matches (MutableSequence[google.events.cloud.networkservices_v1.types.HttpRoute.RouteMatch]):
                A list of matches define conditions used for
                matching the rule against incoming HTTP
                requests. Each match is independent, i.e. this
                rule will be matched if ANY one of the matches
                is satisfied.

                If no matches field is specified, this rule will
                unconditionally match traffic.

                If a default rule is desired to be configured,
                add a rule with no matches specified to the end
                of the rules list.
            action (google.events.cloud.networkservices_v1.types.HttpRoute.RouteAction):
                The detailed rule defining how to route
                matched traffic.
        """

        matches: MutableSequence['HttpRoute.RouteMatch'] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message='HttpRoute.RouteMatch',
        )
        action: 'HttpRoute.RouteAction' = proto.Field(
            proto.MESSAGE,
            number=2,
            message='HttpRoute.RouteAction',
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=11,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    hostnames: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    meshes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    gateways: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    rules: MutableSequence[RouteRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=RouteRule,
    )


class Mesh(proto.Message):
    r"""Mesh represents a logical configuration grouping for workload
    to workload communication within a service mesh. Routes that
    point to mesh dictate how requests are routed within this
    logical mesh boundary.

    Attributes:
        name (str):
            Required. Name of the Mesh resource. It matches pattern
            ``projects/*/locations/global/meshes/<mesh_name>``.
        self_link (str):
            Output only. Server-defined URL of this
            resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the Mesh resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        interception_port (int):
            Optional. If set to a valid TCP port
            (1-65535), instructs the SIDECAR proxy to listen
            on the specified port of localhost (127.0.0.1)
            address. The SIDECAR proxy will expect all
            traffic to be redirected to this port regardless
            of its actual ip:port destination. If unset, a
            port '15001' is used as the interception port.
            This is applicable only for sidecar proxy
            deployments.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=9,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    interception_port: int = proto.Field(
        proto.INT32,
        number=8,
    )


class ServiceBinding(proto.Message):
    r"""ServiceBinding is the resource that defines a Service
    Directory Service to be used in a BackendService resource.

    Attributes:
        name (str):
            Required. Name of the ServiceBinding resource. It matches
            pattern
            ``projects/*/locations/global/serviceBindings/service_binding_name``.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        service (str):
            Required. The full Service Directory Service name of the
            format projects/*/locations/*/namespaces/*/services/*
        service_id (str):
            Output only. The unique identifier of the
            Service Directory Service against which the
            Service Binding resource is validated. This is
            populated when the Service Binding resource is
            used in another resource (like Backend Service).
            This is of the UUID4 format.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the ServiceBinding resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    service: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )


class TcpRoute(proto.Message):
    r"""TcpRoute is the resource defining how TCP traffic should be
    routed by a Mesh/Gateway resource.

    Attributes:
        name (str):
            Required. Name of the TcpRoute resource. It matches pattern
            ``projects/*/locations/global/tcpRoutes/tcp_route_name>``.
        self_link (str):
            Output only. Server-defined URL of this
            resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        rules (MutableSequence[google.events.cloud.networkservices_v1.types.TcpRoute.RouteRule]):
            Required. Rules that define how traffic is
            routed and handled. At least one RouteRule must
            be supplied. If there are multiple rules then
            the action taken will be the first rule to
            match.
        meshes (MutableSequence[str]):
            Optional. Meshes defines a list of meshes this TcpRoute is
            attached to, as one of the routing rules to route the
            requests served by the mesh.

            Each mesh reference should match the pattern:
            ``projects/*/locations/global/meshes/<mesh_name>``

            The attached Mesh should be of a type SIDECAR
        gateways (MutableSequence[str]):
            Optional. Gateways defines a list of gateways this TcpRoute
            is attached to, as one of the routing rules to route the
            requests served by the gateway.

            Each gateway reference should match the pattern:
            ``projects/*/locations/global/gateways/<gateway_name>``
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the TcpRoute resource.
    """

    class RouteRule(proto.Message):
        r"""Specifies how to match traffic and how to route traffic when
        traffic is matched.

        Attributes:
            matches (MutableSequence[google.events.cloud.networkservices_v1.types.TcpRoute.RouteMatch]):
                Optional. RouteMatch defines the predicate
                used to match requests to a given action.
                Multiple match types are "OR"ed for evaluation.
                If no routeMatch field is specified, this rule
                will unconditionally match traffic.
            action (google.events.cloud.networkservices_v1.types.TcpRoute.RouteAction):
                Required. The detailed rule defining how to
                route matched traffic.
        """

        matches: MutableSequence['TcpRoute.RouteMatch'] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message='TcpRoute.RouteMatch',
        )
        action: 'TcpRoute.RouteAction' = proto.Field(
            proto.MESSAGE,
            number=2,
            message='TcpRoute.RouteAction',
        )

    class RouteMatch(proto.Message):
        r"""RouteMatch defines the predicate used to match requests to a
        given action. Multiple match types are "OR"ed for evaluation. If
        no routeMatch field is specified, this rule will unconditionally
        match traffic.

        Attributes:
            address (str):
                Required. Must be specified in the CIDR range
                format. A CIDR range consists of an IP Address
                and a prefix length to construct the subnet
                mask. By default, the prefix length is 32 (i.e.
                matches a single IP address). Only IPV4
                addresses are supported. Examples: "10.0.0.1" -
                matches against this exact IP address.
                "10.0.0.0/8" - matches against any IP address
                within the 10.0.0.0 subnet and 255.255.255.0
                mask. "0.0.0.0/0"
                - matches against any IP address'.
            port (str):
                Required. Specifies the destination port to
                match against.
        """

        address: str = proto.Field(
            proto.STRING,
            number=1,
        )
        port: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class RouteAction(proto.Message):
        r"""The specifications for routing traffic and applying
        associated policies.

        Attributes:
            destinations (MutableSequence[google.events.cloud.networkservices_v1.types.TcpRoute.RouteDestination]):
                Optional. The destination services to which
                traffic should be forwarded. At least one
                destination service is required. Only one of
                route destination or original destination can be
                set.
            original_destination (bool):
                Optional. If true, Router will use the
                destination IP and port of the original
                connection as the destination of the request.
                Default is false. Only one of route destinations
                or original destination can be set.
        """

        destinations: MutableSequence['TcpRoute.RouteDestination'] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message='TcpRoute.RouteDestination',
        )
        original_destination: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class RouteDestination(proto.Message):
        r"""Describe the destination for traffic to be routed to.

        Attributes:
            service_name (str):
                Required. The URL of a BackendService to
                route traffic to.
            weight (int):
                Optional. Specifies the proportion of
                requests forwarded to the backend referenced by
                the serviceName field. This is computed as:

                        weight/Sum(weights in this destination
                list). For non-zero values, there may be some
                epsilon from the exact proportion defined here
                depending on the precision an implementation
                supports.

                If only one serviceName is specified and it has
                a weight greater than 0, 100% of the traffic is
                forwarded to that backend.

                If weights are specified for any one service
                name, they need to be specified for all of them.

                If weights are unspecified for all services,
                then, traffic is distributed in equal
                proportions to all of them.
        """

        service_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        weight: int = proto.Field(
            proto.INT32,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=11,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    rules: MutableSequence[RouteRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=RouteRule,
    )
    meshes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    gateways: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )


class TlsRoute(proto.Message):
    r"""TlsRoute defines how traffic should be routed based on SNI
    and other matching L3 attributes.

    Attributes:
        name (str):
            Required. Name of the TlsRoute resource. It matches pattern
            ``projects/*/locations/global/tlsRoutes/tls_route_name>``.
        self_link (str):
            Output only. Server-defined URL of this
            resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        rules (MutableSequence[google.events.cloud.networkservices_v1.types.TlsRoute.RouteRule]):
            Required. Rules that define how traffic is
            routed and handled. At least one RouteRule must
            be supplied. If there are multiple rules then
            the action taken will be the first rule to
            match.
        meshes (MutableSequence[str]):
            Optional. Meshes defines a list of meshes this TlsRoute is
            attached to, as one of the routing rules to route the
            requests served by the mesh.

            Each mesh reference should match the pattern:
            ``projects/*/locations/global/meshes/<mesh_name>``

            The attached Mesh should be of a type SIDECAR
        gateways (MutableSequence[str]):
            Optional. Gateways defines a list of gateways this TlsRoute
            is attached to, as one of the routing rules to route the
            requests served by the gateway.

            Each gateway reference should match the pattern:
            ``projects/*/locations/global/gateways/<gateway_name>``
    """

    class RouteRule(proto.Message):
        r"""Specifies how to match traffic and how to route traffic when
        traffic is matched.

        Attributes:
            matches (MutableSequence[google.events.cloud.networkservices_v1.types.TlsRoute.RouteMatch]):
                Required. RouteMatch defines the predicate
                used to match requests to a given action.
                Multiple match types are "OR"ed for evaluation.
            action (google.events.cloud.networkservices_v1.types.TlsRoute.RouteAction):
                Required. The detailed rule defining how to
                route matched traffic.
        """

        matches: MutableSequence['TlsRoute.RouteMatch'] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message='TlsRoute.RouteMatch',
        )
        action: 'TlsRoute.RouteAction' = proto.Field(
            proto.MESSAGE,
            number=2,
            message='TlsRoute.RouteAction',
        )

    class RouteMatch(proto.Message):
        r"""RouteMatch defines the predicate used to match requests to a
        given action. Multiple match types are "AND"ed for evaluation.
        If no routeMatch field is specified, this rule will
        unconditionally match traffic.

        Attributes:
            sni_host (MutableSequence[str]):
                Optional. SNI (server name indicator) to match against. SNI
                will be matched against all wildcard domains, i.e.
                ``www.example.com`` will be first matched against
                ``www.example.com``, then ``*.example.com``, then ``*.com.``
                Partial wildcards are not supported, and values like
                \*w.example.com are invalid. At least one of sni_host and
                alpn is required. Up to 5 sni hosts across all matches can
                be set.
            alpn (MutableSequence[str]):
                Optional. ALPN (Application-Layer Protocol Negotiation) to
                match against. Examples: "http/1.1", "h2". At least one of
                sni_host and alpn is required. Up to 5 alpns across all
                matches can be set.
        """

        sni_host: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        alpn: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class RouteAction(proto.Message):
        r"""The specifications for routing traffic and applying
        associated policies.

        Attributes:
            destinations (MutableSequence[google.events.cloud.networkservices_v1.types.TlsRoute.RouteDestination]):
                Required. The destination services to which
                traffic should be forwarded. At least one
                destination service is required.
        """

        destinations: MutableSequence['TlsRoute.RouteDestination'] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message='TlsRoute.RouteDestination',
        )

    class RouteDestination(proto.Message):
        r"""Describe the destination for traffic to be routed to.

        Attributes:
            service_name (str):
                Required. The URL of a BackendService to
                route traffic to.
            weight (int):
                Optional. Specifies the proportion of requests forwareded to
                the backend referenced by the service_name field. This is
                computed as: weight/Sum(weights in destinations) Weights in
                all destinations does not need to sum up to 100.
        """

        service_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        weight: int = proto.Field(
            proto.INT32,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    rules: MutableSequence[RouteRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=RouteRule,
    )
    meshes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    gateways: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class EndpointPolicyEventData(proto.Message):
    r"""The data within all EndpointPolicy events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.networkservices_v1.types.EndpointPolicy):
            Optional. The EndpointPolicy event payload.
            Unset for deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'EndpointPolicy' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='EndpointPolicy',
    )


class HttpRouteEventData(proto.Message):
    r"""The data within all HttpRoute events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.networkservices_v1.types.HttpRoute):
            Optional. The HttpRoute event payload. Unset
            for deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'HttpRoute' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='HttpRoute',
    )


class ServiceBindingEventData(proto.Message):
    r"""The data within all ServiceBinding events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.networkservices_v1.types.ServiceBinding):
            Optional. The ServiceBinding event payload.
            Unset for deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'ServiceBinding' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='ServiceBinding',
    )


class GatewayEventData(proto.Message):
    r"""The data within all Gateway events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.networkservices_v1.types.Gateway):
            Optional. The Gateway event payload. Unset
            for deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'Gateway' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='Gateway',
    )


class TlsRouteEventData(proto.Message):
    r"""The data within all TlsRoute events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.networkservices_v1.types.TlsRoute):
            Optional. The TlsRoute event payload. Unset
            for deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'TlsRoute' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='TlsRoute',
    )


class GrpcRouteEventData(proto.Message):
    r"""The data within all GrpcRoute events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.networkservices_v1.types.GrpcRoute):
            Optional. The GrpcRoute event payload. Unset
            for deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'GrpcRoute' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='GrpcRoute',
    )


class MeshEventData(proto.Message):
    r"""The data within all Mesh events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.networkservices_v1.types.Mesh):
            Optional. The Mesh event payload. Unset for
            deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'Mesh' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='Mesh',
    )


class TcpRouteEventData(proto.Message):
    r"""The data within all TcpRoute events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.networkservices_v1.types.TcpRoute):
            Optional. The TcpRoute event payload. Unset
            for deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'TcpRoute' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='TcpRoute',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
