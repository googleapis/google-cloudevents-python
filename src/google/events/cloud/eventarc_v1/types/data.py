# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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
from google.rpc import code_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.events.cloud.eventarc.v1',
    manifest={
        'Channel',
        'ChannelConnection',
        'Enrollment',
        'LoggingConfig',
        'GoogleApiSource',
        'NetworkConfig',
        'MessageBus',
        'Pipeline',
        'Trigger',
        'EventFilter',
        'StateCondition',
        'Destination',
        'Transport',
        'CloudRun',
        'GKE',
        'Pubsub',
        'HttpEndpoint',
        'TriggerEventData',
        'ChannelEventData',
        'ChannelConnectionEventData',
        'MessageBusEventData',
        'EnrollmentEventData',
        'PipelineEventData',
        'GoogleApiSourceEventData',
    },
)


class Channel(proto.Message):
    r"""A representation of the Channel resource.
    A Channel is a resource on which event providers publish their
    events. The published events are delivered through the transport
    associated with the channel. Note that a channel is associated
    with exactly one event provider.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The resource name of the channel. Must be unique
            within the location on the project and must be in
            ``projects/{project}/locations/{location}/channels/{channel_id}``
            format.
        uid (str):
            Output only. Server assigned unique
            identifier for the channel. The value is a UUID4
            string and guaranteed to remain unchanged until
            the resource is deleted.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        provider (str):
            The name of the event provider (e.g. Eventarc SaaS partner)
            associated with the channel. This provider will be granted
            permissions to publish events to the channel. Format:
            ``projects/{project}/locations/{location}/providers/{provider_id}``.
        pubsub_topic (str):
            Output only. The name of the Pub/Sub topic created and
            managed by Eventarc system as a transport for the event
            delivery. Format: ``projects/{project}/topics/{topic_id}``.

            This field is a member of `oneof`_ ``transport``.
        state (google.events.cloud.eventarc_v1.types.Channel.State):
            Output only. The state of a Channel.
        activation_token (str):
            Output only. The activation token for the
            channel. The token must be used by the provider
            to register the channel for publishing.
        crypto_key_name (str):
            Optional. Resource name of a KMS crypto key (managed by the
            user) used to encrypt/decrypt their event data.

            It must match the pattern
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
        satisfies_pzs (bool):
            Output only. Whether or not this Channel
            satisfies the requirements of physical zone
            separation
        labels (MutableMapping[str, str]):
            Optional. Resource labels.
    """
    class State(proto.Enum):
        r"""State lists all the possible states of a Channel

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            PENDING (1):
                The PENDING state indicates that a Channel
                has been created successfully and there is a new
                activation token available for the subscriber to
                use to convey the Channel to the provider in
                order to create a Connection.
            ACTIVE (2):
                The ACTIVE state indicates that a Channel has
                been successfully connected with the event
                provider. An ACTIVE Channel is ready to receive
                and route events from the event provider.
            INACTIVE (3):
                The INACTIVE state indicates that the Channel
                cannot receive events permanently. There are two
                possible cases this state can happen:

                1. The SaaS provider disconnected from this
                    Channel.
                2. The Channel activation token has expired but
                    the SaaS provider    wasn't connected.

                To re-establish a Connection with a provider,
                the subscriber should create a new Channel and
                give it to the provider.
        """
        STATE_UNSPECIFIED = 0
        PENDING = 1
        ACTIVE = 2
        INACTIVE = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    provider: str = proto.Field(
        proto.STRING,
        number=7,
    )
    pubsub_topic: str = proto.Field(
        proto.STRING,
        number=8,
        oneof='transport',
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    activation_token: str = proto.Field(
        proto.STRING,
        number=10,
    )
    crypto_key_name: str = proto.Field(
        proto.STRING,
        number=11,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=13,
    )


class ChannelConnection(proto.Message):
    r"""A representation of the ChannelConnection resource.
    A ChannelConnection is a resource which event providers create
    during the activation process to establish a connection between
    the provider and the subscriber channel.

    Attributes:
        name (str):
            Required. The name of the connection.
        uid (str):
            Output only. Server assigned ID of the
            resource. The server guarantees uniqueness and
            immutability until deleted.
        channel (str):
            Required. The name of the connected subscriber Channel. This
            is a weak reference to avoid cross project and cross
            accounts references. This must be in
            ``projects/{project}/location/{location}/channels/{channel_id}``
            format.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (MutableMapping[str, str]):
            Optional. Resource labels.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    channel: str = proto.Field(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )


class Enrollment(proto.Message):
    r"""An enrollment represents a subscription for messages on a
    particular message bus. It defines a matching criteria for
    messages on the bus and the subscriber endpoint where matched
    messages should be delivered.

    Attributes:
        name (str):
            Identifier. Resource name of the form
            projects/{project}/locations/{location}/enrollments/{enrollment}
        uid (str):
            Output only. Server assigned unique
            identifier for the channel. The value is a UUID4
            string and guaranteed to remain unchanged until
            the resource is deleted.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            might be sent only on update and delete requests
            to ensure that the client has an up-to-date
            value before proceeding.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (MutableMapping[str, str]):
            Optional. Resource labels.
        annotations (MutableMapping[str, str]):
            Optional. Resource annotations.
        display_name (str):
            Optional. Resource display name.
        cel_match (str):
            Required. A CEL expression identifying which
            messages this enrollment applies to.
        message_bus (str):
            Required. Immutable. Resource name of the
            message bus identifying the source of the
            messages. It matches the form
            projects/{project}/locations/{location}/messageBuses/{messageBus}.
        destination (str):
            Required. Destination is the Pipeline that the Enrollment is
            delivering to. It must point to the full resource name of a
            Pipeline. Format:
            "projects/{PROJECT_ID}/locations/{region}/pipelines/{PIPELINE_ID)".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    cel_match: str = proto.Field(
        proto.STRING,
        number=9,
    )
    message_bus: str = proto.Field(
        proto.STRING,
        number=10,
    )
    destination: str = proto.Field(
        proto.STRING,
        number=11,
    )


class LoggingConfig(proto.Message):
    r"""The configuration for Platform Telemetry logging for Eventarc
    Advanced resources.

    Attributes:
        log_severity (google.events.cloud.eventarc_v1.types.LoggingConfig.LogSeverity):
            Optional. The minimum severity of logs that
            will be sent to Stackdriver/Platform Telemetry.
            Logs at severitiy ≥ this value will be sent,
            unless it is NONE.
    """
    class LogSeverity(proto.Enum):
        r"""The different severities for logging supported by Eventarc
        Advanced resources.
        This enum is an exhaustive list of log severities and is FROZEN.
        Do not expect new values to be added.

        Values:
            LOG_SEVERITY_UNSPECIFIED (0):
                Log severity is not specified. This value is treated the
                same as NONE, but is used to distinguish between no update
                and update to NONE in update_masks.
            NONE (1):
                Default value at resource creation, presence
                of this value must be treated as no
                logging/disable logging.
            DEBUG (2):
                Debug or trace level logging.
            INFO (3):
                Routine information, such as ongoing status
                or performance.
            NOTICE (4):
                Normal but significant events, such as start
                up, shut down, or a configuration change.
            WARNING (5):
                Warning events might cause problems.
            ERROR (6):
                Error events are likely to cause problems.
            CRITICAL (7):
                Critical events cause more severe problems or
                outages.
            ALERT (8):
                A person must take action immediately.
            EMERGENCY (9):
                One or more systems are unusable.
        """
        LOG_SEVERITY_UNSPECIFIED = 0
        NONE = 1
        DEBUG = 2
        INFO = 3
        NOTICE = 4
        WARNING = 5
        ERROR = 6
        CRITICAL = 7
        ALERT = 8
        EMERGENCY = 9

    log_severity: LogSeverity = proto.Field(
        proto.ENUM,
        number=1,
        enum=LogSeverity,
    )


class GoogleApiSource(proto.Message):
    r"""A GoogleApiSource represents a subscription of 1P events from
    a MessageBus.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Resource name of the form
            projects/{project}/locations/{location}/googleApiSources/{google_api_source}
        uid (str):
            Output only. Server assigned unique
            identifier for the channel. The value is a UUID4
            string and guaranteed to remain unchanged until
            the resource is deleted.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            might be sent only on update and delete requests
            to ensure that the client has an up-to-date
            value before proceeding.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (MutableMapping[str, str]):
            Optional. Resource labels.
        annotations (MutableMapping[str, str]):
            Optional. Resource annotations.
        display_name (str):
            Optional. Resource display name.
        destination (str):
            Required. Destination is the message bus that the
            GoogleApiSource is delivering to. It must be point to the
            full resource name of a MessageBus. Format:
            "projects/{PROJECT_ID}/locations/{region}/messagesBuses/{MESSAGE_BUS_ID)
        crypto_key_name (str):
            Optional. Resource name of a KMS crypto key (managed by the
            user) used to encrypt/decrypt their event data.

            It must match the pattern
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
        logging_config (google.events.cloud.eventarc_v1.types.LoggingConfig):
            Optional. Config to control Platform logging
            for the GoogleApiSource.
        organization_subscription (google.events.cloud.eventarc_v1.types.GoogleApiSource.OrganizationSubscription):
            Optional. Config to enable subscribing to
            events from all projects in the
            GoogleApiSource's org.

            This field is a member of `oneof`_ ``wide_scope_subscription``.
        project_subscriptions (google.events.cloud.eventarc_v1.types.GoogleApiSource.ProjectSubscriptions):
            Optional. Config to enable subscribing to all
            events from a list of projects.

            All the projects must be in the same org as the
            GoogleApiSource.

            This field is a member of `oneof`_ ``wide_scope_subscription``.
    """

    class ProjectSubscriptions(proto.Message):
        r"""Config to enable subscribing to all events from a list of
        projects.

        Attributes:
            list_ (MutableSequence[str]):
                Required. A list of projects to receive
                events from.
                All the projects must be in the same org. The
                listed projects should have the format
                project/{identifier} where identifier can be
                either the project id for project number. A
                single list may contain both formats. At most
                100 projects can be listed.
        """

        list_: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class OrganizationSubscription(proto.Message):
        r"""Config to enabled subscribing to events from other projects
        in the org.

        Attributes:
            enabled (bool):
                Required. Enable org level subscription.
        """

        enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    destination: str = proto.Field(
        proto.STRING,
        number=9,
    )
    crypto_key_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    logging_config: 'LoggingConfig' = proto.Field(
        proto.MESSAGE,
        number=11,
        message='LoggingConfig',
    )
    organization_subscription: OrganizationSubscription = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof='wide_scope_subscription',
        message=OrganizationSubscription,
    )
    project_subscriptions: ProjectSubscriptions = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof='wide_scope_subscription',
        message=ProjectSubscriptions,
    )


class NetworkConfig(proto.Message):
    r"""Network Configuration that can be inherited by other protos.

    Attributes:
        network_attachment (str):
            Required. Name of the NetworkAttachment that allows access
            to the customer's VPC. Format:
            ``projects/{PROJECT_ID}/regions/{REGION}/networkAttachments/{NETWORK_ATTACHMENT_NAME}``
    """

    network_attachment: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MessageBus(proto.Message):
    r"""MessageBus for the messages flowing through the system. The
    admin has visibility and control over the messages being
    published and consumed and can restrict publishers and
    subscribers to only a subset of data available in the system by
    defining authorization policies.

    Attributes:
        name (str):
            Identifier. Resource name of the form
            projects/{project}/locations/{location}/messageBuses/{message_bus}
        uid (str):
            Output only. Server assigned unique
            identifier for the channel. The value is a UUID4
            string and guaranteed to remain unchanged until
            the resource is deleted.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            might be sent only on update and delete requests
            to ensure that the client has an up-to-date
            value before proceeding.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (MutableMapping[str, str]):
            Optional. Resource labels.
        annotations (MutableMapping[str, str]):
            Optional. Resource annotations.
        display_name (str):
            Optional. Resource display name.
        crypto_key_name (str):
            Optional. Resource name of a KMS crypto key (managed by the
            user) used to encrypt/decrypt their event data.

            It must match the pattern
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
        logging_config (google.events.cloud.eventarc_v1.types.LoggingConfig):
            Optional. Config to control Platform logging
            for the Message Bus. This log configuration is
            applied to the Message Bus itself, and all the
            Enrollments attached to it.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    crypto_key_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    logging_config: 'LoggingConfig' = proto.Field(
        proto.MESSAGE,
        number=11,
        message='LoggingConfig',
    )


class Pipeline(proto.Message):
    r"""A representation of the Pipeline resource.

    Attributes:
        name (str):
            Identifier. The resource name of the Pipeline. Must be
            unique within the location of the project and must be in
            ``projects/{project}/locations/{location}/pipelines/{pipeline}``
            format.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
            A timestamp in RFC3339 UTC "Zulu" format, with
            nanosecond resolution and up to nine fractional
            digits. Examples: "2014-10-02T15:01:23Z" and
            "2014-10-02T15:01:23.045123456Z".
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
            A timestamp in RFC3339 UTC "Zulu" format, with
            nanosecond resolution and up to nine fractional
            digits. Examples: "2014-10-02T15:01:23Z" and
            "2014-10-02T15:01:23.045123456Z".
        labels (MutableMapping[str, str]):
            Optional. User labels attached to the
            Pipeline that can be used to group resources. An
            object containing a list of "key": value pairs.
            Example: { "name": "wrench", "mass": "1.3kg",
            "count": "3" }.
        uid (str):
            Output only. Server-assigned unique
            identifier for the Pipeline. The value is a
            UUID4 string and guaranteed to remain unchanged
            until the resource is deleted.
        annotations (MutableMapping[str, str]):
            Optional. User-defined annotations. See
            https://google.aip.dev/128#annotations.
        display_name (str):
            Optional. Display name of resource.
        destinations (MutableSequence[google.events.cloud.eventarc_v1.types.Pipeline.Destination]):
            Required. List of destinations to which
            messages will be forwarded. Currently, exactly
            one destination is supported per Pipeline.
        mediations (MutableSequence[google.events.cloud.eventarc_v1.types.Pipeline.Mediation]):
            Optional. List of mediation operations to be
            performed on the message. Currently, only one
            Transformation operation is allowed in each
            Pipeline.
        crypto_key_name (str):
            Optional. Resource name of a KMS crypto key
            (managed by the user) used to encrypt/decrypt
            the event data. If not set, an internal
            Google-owned key will be used to encrypt
            messages. It must match the pattern
            "projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}".
        input_payload_format (google.events.cloud.eventarc_v1.types.Pipeline.MessagePayloadFormat):
            Optional. The payload format expected for the messages
            received by the Pipeline. If input_payload_format is set
            then any messages not matching this format will be treated
            as persistent errors. If input_payload_format is not set,
            then the message data will be treated as an opaque binary
            and no output format can be set on the Pipeline through the
            Pipeline.Destination.output_payload_format field. Any
            Mediations on the Pipeline that involve access to the data
            field will fail as persistent errors.
        logging_config (google.events.cloud.eventarc_v1.types.LoggingConfig):
            Optional. Config to control Platform Logging
            for Pipelines.
        retry_policy (google.events.cloud.eventarc_v1.types.Pipeline.RetryPolicy):
            Optional. The retry policy to use in the
            pipeline.
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            might be sent only on create requests to ensure
            that the client has an up-to-date value before
            proceeding.
        satisfies_pzs (bool):
            Output only. Whether or not this Pipeline
            satisfies the requirements of physical zone
            separation
    """

    class MessagePayloadFormat(proto.Message):
        r"""Represents the format of message data.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            protobuf (google.events.cloud.eventarc_v1.types.Pipeline.MessagePayloadFormat.ProtobufFormat):
                Optional. Protobuf format.

                This field is a member of `oneof`_ ``kind``.
            avro (google.events.cloud.eventarc_v1.types.Pipeline.MessagePayloadFormat.AvroFormat):
                Optional. Avro format.

                This field is a member of `oneof`_ ``kind``.
            json (google.events.cloud.eventarc_v1.types.Pipeline.MessagePayloadFormat.JsonFormat):
                Optional. JSON format.

                This field is a member of `oneof`_ ``kind``.
        """

        class JsonFormat(proto.Message):
            r"""The format of a JSON message payload.
            """

        class ProtobufFormat(proto.Message):
            r"""The format of a Protobuf message payload.

            Attributes:
                schema_definition (str):
                    Optional. The entire schema definition is
                    stored in this field.
            """

            schema_definition: str = proto.Field(
                proto.STRING,
                number=1,
            )

        class AvroFormat(proto.Message):
            r"""The format of an AVRO message payload.

            Attributes:
                schema_definition (str):
                    Optional. The entire schema definition is
                    stored in this field.
            """

            schema_definition: str = proto.Field(
                proto.STRING,
                number=1,
            )

        protobuf: 'Pipeline.MessagePayloadFormat.ProtobufFormat' = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof='kind',
            message='Pipeline.MessagePayloadFormat.ProtobufFormat',
        )
        avro: 'Pipeline.MessagePayloadFormat.AvroFormat' = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof='kind',
            message='Pipeline.MessagePayloadFormat.AvroFormat',
        )
        json: 'Pipeline.MessagePayloadFormat.JsonFormat' = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof='kind',
            message='Pipeline.MessagePayloadFormat.JsonFormat',
        )

    class Destination(proto.Message):
        r"""Represents a target of an invocation over HTTP.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            network_config (google.events.cloud.eventarc_v1.types.Pipeline.Destination.NetworkConfig):
                Optional. Network config is used to configure
                how Pipeline resolves and connects to a
                destination.
            http_endpoint (google.events.cloud.eventarc_v1.types.Pipeline.Destination.HttpEndpoint):
                Optional. An HTTP endpoint destination described by an URI.
                If a DNS FQDN is provided as the endpoint, Pipeline will
                create a peering zone to the consumer VPC and forward DNS
                requests to the VPC specified by network config to resolve
                the service endpoint. See:
                https://cloud.google.com/dns/docs/zones/zones-overview#peering_zones

                This field is a member of `oneof`_ ``destination_descriptor``.
            workflow (str):
                Optional. The resource name of the Workflow whose Executions
                are triggered by the events. The Workflow resource should be
                deployed in the same project as the Pipeline. Format:
                ``projects/{project}/locations/{location}/workflows/{workflow}``

                This field is a member of `oneof`_ ``destination_descriptor``.
            message_bus (str):
                Optional. The resource name of the Message Bus to which
                events should be published. The Message Bus resource should
                exist in the same project as the Pipeline. Format:
                ``projects/{project}/locations/{location}/messageBuses/{message_bus}``

                This field is a member of `oneof`_ ``destination_descriptor``.
            topic (str):
                Optional. The resource name of the Pub/Sub topic to which
                events should be published. Format:
                ``projects/{project}/locations/{location}/topics/{topic}``

                This field is a member of `oneof`_ ``destination_descriptor``.
            authentication_config (google.events.cloud.eventarc_v1.types.Pipeline.Destination.AuthenticationConfig):
                Optional. An authentication config used to
                authenticate message requests, such that
                destinations can verify the source. For example,
                this can be used with private Google Cloud
                destinations that require Google Cloud
                credentials for access like Cloud Run. This
                field is optional and should be set only by
                users interested in authenticated push.
            output_payload_format (google.events.cloud.eventarc_v1.types.Pipeline.MessagePayloadFormat):
                Optional. The message format before it is delivered to the
                destination. If not set, the message will be delivered in
                the format it was originally delivered to the Pipeline. This
                field can only be set if Pipeline.input_payload_format is
                also set.
        """

        class NetworkConfig(proto.Message):
            r"""Represents a network config to be used for destination
            resolution and connectivity.

            Attributes:
                network_attachment (str):
                    Required. Name of the NetworkAttachment that allows access
                    to the consumer VPC. Format:
                    ``projects/{PROJECT_ID}/regions/{REGION}/networkAttachments/{NETWORK_ATTACHMENT_NAME}``
            """

            network_attachment: str = proto.Field(
                proto.STRING,
                number=1,
            )

        class HttpEndpoint(proto.Message):
            r"""Represents a HTTP endpoint destination.

            Attributes:
                uri (str):
                    Required. The URI of the HTTP endpoint.

                    The value must be a RFC2396 URI string. Examples:
                    ``https://svc.us-central1.p.local:8080/route``. Only the
                    HTTPS protocol is supported.
                message_binding_template (str):
                    Optional. The CEL expression used to modify how the
                    destination-bound HTTP request is constructed.

                    If a binding expression is not specified here, the message
                    is treated as a CloudEvent and is mapped to the HTTP request
                    according to the CloudEvent HTTP Protocol Binding Binary
                    Content Mode
                    (https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/http-protocol-binding.md#31-binary-content-mode).
                    In this representation, all fields except the ``data`` and
                    ``datacontenttype`` field on the message are mapped to HTTP
                    request headers with a prefix of ``ce-``.

                    To construct the HTTP request payload and the value of the
                    content-type HTTP header, the payload format is defined as
                    follows:

                    1) Use the output_payload_format_type on the
                       Pipeline.Destination if it is set, else:
                    2) Use the input_payload_format_type on the Pipeline if it
                       is set, else:
                    3) Treat the payload as opaque binary data.

                    The ``data`` field of the message is converted to the
                    payload format or left as-is for case 3) and then attached
                    as the payload of the HTTP request. The ``content-type``
                    header on the HTTP request is set to the payload format type
                    or left empty for case 3). However, if a mediation has
                    updated the ``datacontenttype`` field on the message so that
                    it is not the same as the payload format type but it is
                    still a prefix of the payload format type, then the
                    ``content-type`` header on the HTTP request is set to this
                    ``datacontenttype`` value. For example, if the
                    ``datacontenttype`` is "application/json" and the payload
                    format type is "application/json; charset=utf-8", then the
                    ``content-type`` header on the HTTP request is set to
                    "application/json; charset=utf-8".

                    If a non-empty binding expression is specified then this
                    expression is used to modify the default CloudEvent HTTP
                    Protocol Binding Binary Content representation. The result
                    of the CEL expression must be a map of key/value pairs which
                    is used as follows:

                    - If a map named ``headers`` exists on the result of the
                      expression, then its key/value pairs are directly mapped
                      to the HTTP request headers. The headers values are
                      constructed from the corresponding value type's canonical
                      representation. If the ``headers`` field doesn't exist
                      then the resulting HTTP request will be the headers of the
                      CloudEvent HTTP Binding Binary Content Mode representation
                      of the final message. Note: If the specified binding
                      expression, has updated the ``datacontenttype`` field on
                      the message so that it is not the same as the payload
                      format type but it is still a prefix of the payload format
                      type, then the ``content-type`` header in the ``headers``
                      map is set to this ``datacontenttype`` value.
                    - If a field named ``body`` exists on the result of the
                      expression then its value is directly mapped to the body
                      of the request. If the value of the ``body`` field is of
                      type bytes or string then it is used for the HTTP request
                      body as-is, with no conversion. If the body field is of
                      any other type then it is converted to a JSON string. If
                      the body field does not exist then the resulting payload
                      of the HTTP request will be data value of the CloudEvent
                      HTTP Binding Binary Content Mode representation of the
                      final message as described earlier.
                    - Any other fields in the resulting expression will be
                      ignored.

                    The CEL expression may access the incoming CloudEvent
                    message in its definition, as follows:

                    - The ``data`` field of the incoming CloudEvent message can
                      be accessed using the ``message.data`` value. Subfields of
                      ``message.data`` may also be accessed if an
                      input_payload_format has been specified on the Pipeline.
                    - Each attribute of the incoming CloudEvent message can be
                      accessed using the ``message.<key>`` value, where is
                      replaced with the name of the attribute.
                    - Existing headers can be accessed in the CEL expression
                      using the ``headers`` variable. The ``headers`` variable
                      defines a map of key/value pairs corresponding to the HTTP
                      headers of the CloudEvent HTTP Binding Binary Content Mode
                      representation of the final message as described earlier.
                      For example, the following CEL expression can be used to
                      construct an HTTP request by adding an additional header
                      to the HTTP headers of the CloudEvent HTTP Binding Binary
                      Content Mode representation of the final message and by
                      overwriting the body of the request:

                    ::

                       {
                         "headers": headers.merge({"new-header-key": "new-header-value"}),
                         "body": "new-body"
                       }

                    - The default binding for the message payload can be
                      accessed using the ``body`` variable. It conatins a string
                      representation of the message payload in the format
                      specified by the ``output_payload_format`` field. If the
                      ``input_payload_format`` field is not set, the ``body``
                      variable contains the same message payload bytes that were
                      published.

                    Additionally, the following CEL extension functions are
                    provided for use in this CEL expression:

                    - toBase64Url: map.toBase64Url() -> string

                      - Converts a CelValue to a base64url encoded string

                    - toJsonString: map.toJsonString() -> string

                      - Converts a CelValue to a JSON string

                    - merge: map1.merge(map2) -> map3

                      - Merges the passed CEL map with the existing CEL map the
                        function is applied to.
                      - If the same key exists in both maps, if the key's value
                        is type map both maps are merged else the value from the
                        passed map is used.

                    - denormalize: map.denormalize() -> map

                      - Denormalizes a CEL map such that every value of type map
                        or key in the map is expanded to return a single level
                        map.
                      - The resulting keys are "." separated indices of the map
                        keys.
                      - For example: { "a": 1, "b": { "c": 2, "d": 3 } "e": [4,
                        5] } .denormalize() -> { "a": 1, "b.c": 2, "b.d": 3,
                        "e.0": 4, "e.1": 5 }

                    - setField: map.setField(key, value) -> message

                      - Sets the field of the message with the given key to the
                        given value.
                      - If the field is not present it will be added.
                      - If the field is present it will be overwritten.
                      - The key can be a dot separated path to set a field in a
                        nested message.
                      - Key must be of type string.
                      - Value may be any valid type.

                    - removeFields: map.removeFields([key1, key2, ...]) ->
                      message

                      - Removes the fields of the map with the given keys.
                      - The keys can be a dot separated path to remove a field
                        in a nested message.
                      - If a key is not found it will be ignored.
                      - Keys must be of type string.

                    - toMap: [map1, map2, ...].toMap() -> map

                      - Converts a CEL list of CEL maps to a single CEL map

                    - toCloudEventJsonWithPayloadFormat:
                      message.toCloudEventJsonWithPayloadFormat() -> map

                      - Converts a message to the corresponding structure of
                        JSON format for CloudEvents.
                      - It converts ``data`` to destination payload format
                        specified in ``output_payload_format``. If
                        ``output_payload_format`` is not set, the data will
                        remain unchanged.
                      - It also sets the corresponding datacontenttype of the
                        CloudEvent, as indicated by ``output_payload_format``.
                        If no ``output_payload_format`` is set it will use the
                        value of the "datacontenttype" attribute on the
                        CloudEvent if present, else remove "datacontenttype"
                        attribute.
                      - This function expects that the content of the message
                        will adhere to the standard CloudEvent format. If it
                        doesn't then this function will fail.
                      - The result is a CEL map that corresponds to the JSON
                        representation of the CloudEvent. To convert that data
                        to a JSON string it can be chained with the toJsonString
                        function.

                    The Pipeline expects that the message it receives adheres to
                    the standard CloudEvent format. If it doesn't then the
                    outgoing message request may fail with a persistent error.
            """

            uri: str = proto.Field(
                proto.STRING,
                number=1,
            )
            message_binding_template: str = proto.Field(
                proto.STRING,
                number=3,
            )

        class AuthenticationConfig(proto.Message):
            r"""Represents a config used to authenticate message requests.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                google_oidc (google.events.cloud.eventarc_v1.types.Pipeline.Destination.AuthenticationConfig.OidcToken):
                    Optional. This authenticate method will apply
                    Google OIDC tokens signed by a Google Cloud
                    service account to the requests.

                    This field is a member of `oneof`_ ``authentication_method_descriptor``.
                oauth_token (google.events.cloud.eventarc_v1.types.Pipeline.Destination.AuthenticationConfig.OAuthToken):
                    Optional. If specified, an `OAuth
                    token <https://developers.google.com/identity/protocols/OAuth2>`__
                    will be generated and attached as an ``Authorization``
                    header in the HTTP request.

                    This type of authorization should generally only be used
                    when calling Google APIs hosted on \*.googleapis.com.

                    This field is a member of `oneof`_ ``authentication_method_descriptor``.
            """

            class OidcToken(proto.Message):
                r"""Represents a config used to authenticate with a Google OIDC
                token using a Google Cloud service account. Use this
                authentication method to invoke your Cloud Run and Cloud
                Functions destinations or HTTP endpoints that support Google
                OIDC.

                Attributes:
                    service_account (str):
                        Required. Service account email used to
                        generate the OIDC Token. The principal who calls
                        this API must have iam.serviceAccounts.actAs
                        permission in the service account. See
                        https://cloud.google.com/iam/docs/understanding-service-accounts
                        for more information. Eventarc service agents
                        must have
                        roles/roles/iam.serviceAccountTokenCreator role
                        to allow the Pipeline to create OpenID tokens
                        for authenticated requests.
                    audience (str):
                        Optional. Audience to be used to generate the
                        OIDC Token. The audience claim identifies the
                        recipient that the JWT is intended for. If
                        unspecified, the destination URI will be used.
                """

                service_account: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                audience: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            class OAuthToken(proto.Message):
                r"""Contains information needed for generating an `OAuth
                token <https://developers.google.com/identity/protocols/OAuth2>`__.
                This type of authorization should generally only be used when
                calling Google APIs hosted on \*.googleapis.com.

                Attributes:
                    service_account (str):
                        Required. Service account email used to generate the `OAuth
                        token <https://developers.google.com/identity/protocols/OAuth2>`__.
                        The principal who calls this API must have
                        iam.serviceAccounts.actAs permission in the service account.
                        See
                        https://cloud.google.com/iam/docs/understanding-service-accounts
                        for more information. Eventarc service agents must have
                        roles/roles/iam.serviceAccountTokenCreator role to allow
                        Pipeline to create OAuth2 tokens for authenticated requests.
                    scope (str):
                        Optional. OAuth scope to be used for
                        generating OAuth access token. If not specified,
                        "https://www.googleapis.com/auth/cloud-platform"
                        will be used.
                """

                service_account: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                scope: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            google_oidc: 'Pipeline.Destination.AuthenticationConfig.OidcToken' = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof='authentication_method_descriptor',
                message='Pipeline.Destination.AuthenticationConfig.OidcToken',
            )
            oauth_token: 'Pipeline.Destination.AuthenticationConfig.OAuthToken' = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof='authentication_method_descriptor',
                message='Pipeline.Destination.AuthenticationConfig.OAuthToken',
            )

        network_config: 'Pipeline.Destination.NetworkConfig' = proto.Field(
            proto.MESSAGE,
            number=1,
            message='Pipeline.Destination.NetworkConfig',
        )
        http_endpoint: 'Pipeline.Destination.HttpEndpoint' = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof='destination_descriptor',
            message='Pipeline.Destination.HttpEndpoint',
        )
        workflow: str = proto.Field(
            proto.STRING,
            number=3,
            oneof='destination_descriptor',
        )
        message_bus: str = proto.Field(
            proto.STRING,
            number=4,
            oneof='destination_descriptor',
        )
        topic: str = proto.Field(
            proto.STRING,
            number=8,
            oneof='destination_descriptor',
        )
        authentication_config: 'Pipeline.Destination.AuthenticationConfig' = proto.Field(
            proto.MESSAGE,
            number=5,
            message='Pipeline.Destination.AuthenticationConfig',
        )
        output_payload_format: 'Pipeline.MessagePayloadFormat' = proto.Field(
            proto.MESSAGE,
            number=6,
            message='Pipeline.MessagePayloadFormat',
        )

    class Mediation(proto.Message):
        r"""Mediation defines different ways to modify the Pipeline.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            transformation (google.events.cloud.eventarc_v1.types.Pipeline.Mediation.Transformation):
                Optional. How the Pipeline is to transform
                messages

                This field is a member of `oneof`_ ``mediation_descriptor``.
        """

        class Transformation(proto.Message):
            r"""Transformation defines the way to transform an incoming
            message.

            Attributes:
                transformation_template (str):
                    Optional. The CEL expression template to apply to transform
                    messages. The following CEL extension functions are provided
                    for use in this CEL expression:

                    - merge: map1.merge(map2) -> map3

                      - Merges the passed CEL map with the existing CEL map the
                        function is applied to.
                      - If the same key exists in both maps, if the key's value
                        is type map both maps are merged else the value from the
                        passed map is used.

                    - denormalize: map.denormalize() -> map

                      - Denormalizes a CEL map such that every value of type map
                        or key in the map is expanded to return a single level
                        map.
                      - The resulting keys are "." separated indices of the map
                        keys.
                      - For example: { "a": 1, "b": { "c": 2, "d": 3 } "e": [4,
                        5] } .denormalize() -> { "a": 1, "b.c": 2, "b.d": 3,
                        "e.0": 4, "e.1": 5 }

                    - setField: map.setField(key, value) -> message

                      - Sets the field of the message with the given key to the
                        given value.
                      - If the field is not present it will be added.
                      - If the field is present it will be overwritten.
                      - The key can be a dot separated path to set a field in a
                        nested message.
                      - Key must be of type string.
                      - Value may be any valid type.

                    - removeFields: map.removeFields([key1, key2, ...]) ->
                      message

                      - Removes the fields of the map with the given keys.
                      - The keys can be a dot separated path to remove a field
                        in a nested message.
                      - If a key is not found it will be ignored.
                      - Keys must be of type string.

                    - toMap: [map1, map2, ...].toMap() -> map

                      - Converts a CEL list of CEL maps to a single CEL map

                    - toDestinationPayloadFormat():
                      message.data.toDestinationPayloadFormat() -> string or
                      bytes

                      - Converts the message data to the destination payload
                        format specified in
                        Pipeline.Destination.output_payload_format
                      - This function is meant to be applied to the message.data
                        field.
                      - If the destination payload format is not set, the
                        function will return the message data unchanged.

                    - toCloudEventJsonWithPayloadFormat:
                      message.toCloudEventJsonWithPayloadFormat() -> map

                      - Converts a message to the corresponding structure of
                        JSON format for CloudEvents
                      - This function applies toDestinationPayloadFormat() to
                        the message data. It also sets the corresponding
                        datacontenttype of the CloudEvent, as indicated by
                        Pipeline.Destination.output_payload_format. If no
                        output_payload_format is set it will use the existing
                        datacontenttype on the CloudEvent if present, else leave
                        datacontenttype absent.
                      - This function expects that the content of the message
                        will adhere to the standard CloudEvent format. If it
                        doesn't then this function will fail.
                      - The result is a CEL map that corresponds to the JSON
                        representation of the CloudEvent. To convert that data
                        to a JSON string it can be chained with the toJsonString
                        function.
            """

            transformation_template: str = proto.Field(
                proto.STRING,
                number=1,
            )

        transformation: 'Pipeline.Mediation.Transformation' = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof='mediation_descriptor',
            message='Pipeline.Mediation.Transformation',
        )

    class RetryPolicy(proto.Message):
        r"""The retry policy configuration for the Pipeline. The pipeline
        exponentially backs off in case the destination is non responsive or
        returns a retryable error code. The default semantics are as
        follows: The backoff starts with a 5 second delay and doubles the
        delay after each failed attempt (10 seconds, 20 seconds, 40 seconds,
        etc.). The delay is capped at 60 seconds by default. Please note
        that if you set the min_retry_delay and max_retry_delay fields to
        the same value this will make the duration between retries constant.

        Attributes:
            max_attempts (int):
                Optional. The maximum number of delivery
                attempts for any message. The value must be
                between 1 and 100. The default value for this
                field is 5.
            min_retry_delay (google.protobuf.duration_pb2.Duration):
                Optional. The minimum amount of seconds to
                wait between retry attempts. The value must be
                between 1 and 600. The default value for this
                field is 5.
            max_retry_delay (google.protobuf.duration_pb2.Duration):
                Optional. The maximum amount of seconds to
                wait between retry attempts. The value must be
                between 1 and 600. The default value for this
                field is 60.
        """

        max_attempts: int = proto.Field(
            proto.INT32,
            number=1,
        )
        min_retry_delay: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        max_retry_delay: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )

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
    uid: str = proto.Field(
        proto.STRING,
        number=5,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    destinations: MutableSequence[Destination] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=Destination,
    )
    mediations: MutableSequence[Mediation] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=Mediation,
    )
    crypto_key_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    input_payload_format: MessagePayloadFormat = proto.Field(
        proto.MESSAGE,
        number=11,
        message=MessagePayloadFormat,
    )
    logging_config: 'LoggingConfig' = proto.Field(
        proto.MESSAGE,
        number=12,
        message='LoggingConfig',
    )
    retry_policy: RetryPolicy = proto.Field(
        proto.MESSAGE,
        number=13,
        message=RetryPolicy,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=99,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=14,
    )


class Trigger(proto.Message):
    r"""A representation of the trigger resource.

    Attributes:
        name (str):
            Required. The resource name of the trigger. Must be unique
            within the location of the project and must be in
            ``projects/{project}/locations/{location}/triggers/{trigger}``
            format.
        uid (str):
            Output only. Server-assigned unique
            identifier for the trigger. The value is a UUID4
            string and guaranteed to remain unchanged until
            the resource is deleted.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        event_filters (MutableSequence[google.events.cloud.eventarc_v1.types.EventFilter]):
            Required. Unordered list. The list of filters
            that applies to event attributes. Only events
            that match all the provided filters are sent to
            the destination.
        service_account (str):
            Optional. The IAM service account email associated with the
            trigger. The service account represents the identity of the
            trigger.

            The ``iam.serviceAccounts.actAs`` permission must be granted
            on the service account to allow a principal to impersonate
            the service account. For more information, see the `Roles
            and permissions </eventarc/docs/all-roles-permissions>`__
            page specific to the trigger destination.
        destination (google.events.cloud.eventarc_v1.types.Destination):
            Required. Destination specifies where the
            events should be sent to.
        transport (google.events.cloud.eventarc_v1.types.Transport):
            Optional. To deliver messages, Eventarc might
            use other Google Cloud products as a transport
            intermediary. This field contains a reference to
            that transport intermediary. This information
            can be used for debugging purposes.
        labels (MutableMapping[str, str]):
            Optional. User labels attached to the
            triggers that can be used to group resources.
        channel (str):
            Optional. The name of the channel associated with the
            trigger in
            ``projects/{project}/locations/{location}/channels/{channel}``
            format. You must provide a channel to receive events from
            Eventarc SaaS partners.
        conditions (MutableMapping[str, google.events.cloud.eventarc_v1.types.StateCondition]):
            Output only. The reason(s) why a trigger is
            in FAILED state.
        event_data_content_type (str):
            Optional. EventDataContentType specifies the type of payload
            in MIME format that is expected from the CloudEvent data
            field. This is set to ``application/json`` if the value is
            not defined.
        satisfies_pzs (bool):
            Output only. Whether or not this Trigger
            satisfies the requirements of physical zone
            separation
        retry_policy (google.events.cloud.eventarc_v1.types.Trigger.RetryPolicy):
            Optional. The retry policy to use in the
            Trigger.
            If unset, event delivery will be retried for up
            to 24 hours by default:

            https://cloud.google.com/eventarc/docs/retry-events
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            might be sent only on create requests to ensure
            that the client has an up-to-date value before
            proceeding.
    """

    class RetryPolicy(proto.Message):
        r"""The retry policy configuration for the Trigger.

        Can only be set with Cloud Run destinations.

        Attributes:
            max_attempts (int):
                Optional. The maximum number of delivery
                attempts for any message. The only valid value
                is 1.
        """

        max_attempts: int = proto.Field(
            proto.INT32,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    event_filters: MutableSequence['EventFilter'] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message='EventFilter',
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=9,
    )
    destination: 'Destination' = proto.Field(
        proto.MESSAGE,
        number=10,
        message='Destination',
    )
    transport: 'Transport' = proto.Field(
        proto.MESSAGE,
        number=11,
        message='Transport',
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    channel: str = proto.Field(
        proto.STRING,
        number=13,
    )
    conditions: MutableMapping[str, 'StateCondition'] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=15,
        message='StateCondition',
    )
    event_data_content_type: str = proto.Field(
        proto.STRING,
        number=16,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    retry_policy: RetryPolicy = proto.Field(
        proto.MESSAGE,
        number=20,
        message=RetryPolicy,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=99,
    )


class EventFilter(proto.Message):
    r"""Filters events based on exact matches on the CloudEvents
    attributes.

    Attributes:
        attribute (str):
            Required. The name of a CloudEvents attribute. Currently,
            only a subset of attributes are supported for filtering. You
            can `retrieve a specific provider's supported event
            types </eventarc/docs/list-providers#describe-provider>`__.

            All triggers MUST provide a filter for the 'type' attribute.
        value (str):
            Required. The value for the attribute.
        operator (str):
            Optional. The operator used for matching the events with the
            value of the filter. If not specified, only events that have
            an exact key-value pair specified in the filter are matched.
            The allowed values are ``path_pattern`` and
            ``match-path-pattern``. ``path_pattern`` is only allowed for
            GCFv1 triggers.
    """

    attribute: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    operator: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StateCondition(proto.Message):
    r"""A condition that is part of the trigger state computation.

    Attributes:
        code (google.rpc.code_pb2.Code):
            The canonical code of the condition.
        message (str):
            Human-readable message.
    """

    code: code_pb2.Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=code_pb2.Code,
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Destination(proto.Message):
    r"""Represents a target of an invocation over HTTP.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_run (google.events.cloud.eventarc_v1.types.CloudRun):
            Cloud Run fully-managed resource that
            receives the events. The resource should be in
            the same project as the trigger.

            This field is a member of `oneof`_ ``descriptor``.
        cloud_function (str):
            The Cloud Function resource name. Cloud Functions V1 and V2
            are supported. Format:
            ``projects/{project}/locations/{location}/functions/{function}``

            This is a read-only field. Creating Cloud Functions V1/V2
            triggers is only supported via the Cloud Functions product.
            An error will be returned if the user sets this value.

            This field is a member of `oneof`_ ``descriptor``.
        gke (google.events.cloud.eventarc_v1.types.GKE):
            A GKE service capable of receiving events.
            The service should be running in the same
            project as the trigger.

            This field is a member of `oneof`_ ``descriptor``.
        workflow (str):
            The resource name of the Workflow whose Executions are
            triggered by the events. The Workflow resource should be
            deployed in the same project as the trigger. Format:
            ``projects/{project}/locations/{location}/workflows/{workflow}``

            This field is a member of `oneof`_ ``descriptor``.
        http_endpoint (google.events.cloud.eventarc_v1.types.HttpEndpoint):
            An HTTP endpoint destination described by an
            URI.

            This field is a member of `oneof`_ ``descriptor``.
        network_config (google.events.cloud.eventarc_v1.types.NetworkConfig):
            Optional. Network config is used to configure
            how Eventarc resolves and connect to a
            destination. This should only be used with
            HttpEndpoint destination type.
    """

    cloud_run: 'CloudRun' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='descriptor',
        message='CloudRun',
    )
    cloud_function: str = proto.Field(
        proto.STRING,
        number=2,
        oneof='descriptor',
    )
    gke: 'GKE' = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof='descriptor',
        message='GKE',
    )
    workflow: str = proto.Field(
        proto.STRING,
        number=4,
        oneof='descriptor',
    )
    http_endpoint: 'HttpEndpoint' = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof='descriptor',
        message='HttpEndpoint',
    )
    network_config: 'NetworkConfig' = proto.Field(
        proto.MESSAGE,
        number=6,
        message='NetworkConfig',
    )


class Transport(proto.Message):
    r"""Represents the transport intermediaries created for the
    trigger to deliver events.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        pubsub (google.events.cloud.eventarc_v1.types.Pubsub):
            The Pub/Sub topic and subscription used by
            Eventarc as a transport intermediary.

            This field is a member of `oneof`_ ``intermediary``.
    """

    pubsub: 'Pubsub' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='intermediary',
        message='Pubsub',
    )


class CloudRun(proto.Message):
    r"""Represents a Cloud Run destination.

    Attributes:
        service (str):
            Required. The name of the Cloud Run service
            being addressed. See
            https://cloud.google.com/run/docs/reference/rest/v1/namespaces.services.

            Only services located in the same project as the
            trigger object can be addressed.
        path (str):
            Optional. The relative path on the Cloud Run
            service the events should be sent to.

            The value must conform to the definition of a
            URI path segment (section 3.3 of RFC2396).
            Examples: "/route", "route", "route/subroute".
        region (str):
            Required. The region the Cloud Run service is
            deployed in.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GKE(proto.Message):
    r"""Represents a GKE destination.

    Attributes:
        cluster (str):
            Required. The name of the cluster the GKE
            service is running in. The cluster must be
            running in the same project as the trigger being
            created.
        location (str):
            Required. The name of the Google Compute
            Engine in which the cluster resides, which can
            either be compute zone (for example,
            us-central1-a) for the zonal clusters or region
            (for example, us-central1) for regional
            clusters.
        namespace (str):
            Required. The namespace the GKE service is
            running in.
        service (str):
            Required. Name of the GKE service.
        path (str):
            Optional. The relative path on the GKE
            service the events should be sent to.

            The value must conform to the definition of a
            URI path segment (section 3.3 of RFC2396).
            Examples: "/route", "route", "route/subroute".
    """

    cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    namespace: str = proto.Field(
        proto.STRING,
        number=3,
    )
    service: str = proto.Field(
        proto.STRING,
        number=4,
    )
    path: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Pubsub(proto.Message):
    r"""Represents a Pub/Sub transport.

    Attributes:
        topic (str):
            Optional. The name of the Pub/Sub topic created and managed
            by Eventarc as a transport for the event delivery. Format:
            ``projects/{PROJECT_ID}/topics/{TOPIC_NAME}``.

            You can set an existing topic for triggers of the type
            ``google.cloud.pubsub.topic.v1.messagePublished``. The topic
            you provide here is not deleted by Eventarc at trigger
            deletion.
        subscription (str):
            Output only. The name of the Pub/Sub subscription created
            and managed by Eventarc as a transport for the event
            delivery. Format:
            ``projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_NAME}``.
    """

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subscription: str = proto.Field(
        proto.STRING,
        number=2,
    )


class HttpEndpoint(proto.Message):
    r"""Represents a HTTP endpoint destination.

    Attributes:
        uri (str):
            Required. The URI of the HTTP endpoint.

            The value must be a RFC2396 URI string. Examples:
            ``http://10.10.10.8:80/route``,
            ``http://svc.us-central1.p.local:8080/``. Only HTTP and
            HTTPS protocols are supported. The host can be either a
            static IP addressable from the VPC specified by the network
            config, or an internal DNS hostname of the service
            resolvable via Cloud DNS.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TriggerEventData(proto.Message):
    r"""The data within all Trigger events.

    Attributes:
        payload (google.events.cloud.eventarc_v1.types.Trigger):
            The Trigger event payload.
    """

    payload: 'Trigger' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Trigger',
    )


class ChannelEventData(proto.Message):
    r"""The data within all Channel events.

    Attributes:
        payload (google.events.cloud.eventarc_v1.types.Channel):
            The Channel event payload.
    """

    payload: 'Channel' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Channel',
    )


class ChannelConnectionEventData(proto.Message):
    r"""The data within all ChannelConnection events.

    Attributes:
        payload (google.events.cloud.eventarc_v1.types.ChannelConnection):
            The ChannelConnection event payload.
    """

    payload: 'ChannelConnection' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='ChannelConnection',
    )


class MessageBusEventData(proto.Message):
    r"""The data within all MessageBus events.

    Attributes:
        payload (google.events.cloud.eventarc_v1.types.MessageBus):
            The MessageBus event payload.
    """

    payload: 'MessageBus' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='MessageBus',
    )


class EnrollmentEventData(proto.Message):
    r"""The data within all Enrollment events.

    Attributes:
        payload (google.events.cloud.eventarc_v1.types.Enrollment):
            The Enrollment event payload.
    """

    payload: 'Enrollment' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Enrollment',
    )


class PipelineEventData(proto.Message):
    r"""The data within all Pipeline events.

    Attributes:
        payload (google.events.cloud.eventarc_v1.types.Pipeline):
            The Pipeline event payload.
    """

    payload: 'Pipeline' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Pipeline',
    )


class GoogleApiSourceEventData(proto.Message):
    r"""The data within all GoogleApiSource events.

    Attributes:
        payload (google.events.cloud.eventarc_v1.types.GoogleApiSource):
            The GoogleApiSource event payload.
    """

    payload: 'GoogleApiSource' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='GoogleApiSource',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
