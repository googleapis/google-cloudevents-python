# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.events.cloud.beyondcorp.appconnectors.v1',
    manifest={
        'HealthStatus',
        'ResourceInfo',
        'AppConnector',
        'AppConnectorEventData',
    },
)


class HealthStatus(proto.Enum):
    r"""HealthStatus represents the health status.

    Values:
        HEALTH_STATUS_UNSPECIFIED (0):
            Health status is unknown: not initialized or
            failed to retrieve.
        HEALTHY (1):
            The resource is healthy.
        UNHEALTHY (2):
            The resource is unhealthy.
        UNRESPONSIVE (3):
            The resource is unresponsive.
        DEGRADED (4):
            Some sub-resources are UNHEALTHY.
    """
    HEALTH_STATUS_UNSPECIFIED = 0
    HEALTHY = 1
    UNHEALTHY = 2
    UNRESPONSIVE = 3
    DEGRADED = 4


class ResourceInfo(proto.Message):
    r"""ResourceInfo represents the information/status of an app connector
    resource. Such as:

    -  remote_agent

       -  container

          -  runtime
          -  appgateway

             -  appconnector

                -  appconnection

                   -  tunnel

             -  logagent

    Attributes:
        id (str):
            Required. Unique Id for the resource.
        status (google.events.cloud.beyondcorp.appconnectors_v1.types.HealthStatus):
            Overall health status. Overall status is
            derived based on the status of each sub level
            resources.
        time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp to collect the info. It is
            suggested to be set by the topmost level
            resource only.
        sub (MutableSequence[google.events.cloud.beyondcorp.appconnectors_v1.types.ResourceInfo]):
            List of Info for the sub level resources.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    status: 'HealthStatus' = proto.Field(
        proto.ENUM,
        number=2,
        enum='HealthStatus',
    )
    time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    sub: MutableSequence['ResourceInfo'] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message='ResourceInfo',
    )


class AppConnector(proto.Message):
    r"""A BeyondCorp connector resource that represents an
    application facing component deployed proximal to and with
    direct access to the application instances. It is used to
    establish connectivity between the remote enterprise environment
    and GCP. It initiates connections to the applications and can
    proxy the data from users over the connection.

    Attributes:
        name (str):
            Required. Unique resource name of the
            AppConnector. The name is ignored when creating
            a AppConnector.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the resource was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the resource was
            last modified.
        labels (MutableMapping[str, str]):
            Optional. Resource labels to represent user
            provided metadata.
        display_name (str):
            Optional. An arbitrary user-provided name for
            the AppConnector. Cannot exceed 64 characters.
        uid (str):
            Output only. A unique identifier for the
            instance generated by the system.
        state (google.events.cloud.beyondcorp.appconnectors_v1.types.AppConnector.State):
            Output only. The current state of the
            AppConnector.
        principal_info (google.events.cloud.beyondcorp.appconnectors_v1.types.AppConnector.PrincipalInfo):
            Required. Principal information about the
            Identity of the AppConnector.
        resource_info (google.events.cloud.beyondcorp.appconnectors_v1.types.ResourceInfo):
            Optional. Resource info of the connector.
    """
    class State(proto.Enum):
        r"""Represents the different states of a AppConnector.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            CREATING (1):
                AppConnector is being created.
            CREATED (2):
                AppConnector has been created.
            UPDATING (3):
                AppConnector's configuration is being
                updated.
            DELETING (4):
                AppConnector is being deleted.
            DOWN (5):
                AppConnector is down and may be restored in
                the future. This happens when CCFE sends
                ProjectState = OFF.
        """
        STATE_UNSPECIFIED = 0
        CREATING = 1
        CREATED = 2
        UPDATING = 3
        DELETING = 4
        DOWN = 5

    class PrincipalInfo(proto.Message):
        r"""PrincipalInfo represents an Identity oneof.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            service_account (google.events.cloud.beyondcorp.appconnectors_v1.types.AppConnector.PrincipalInfo.ServiceAccount):
                A GCP service account.

                This field is a member of `oneof`_ ``type``.
        """

        class ServiceAccount(proto.Message):
            r"""ServiceAccount represents a GCP service account.

            Attributes:
                email (str):
                    Email address of the service account.
            """

            email: str = proto.Field(
                proto.STRING,
                number=1,
            )

        service_account: 'AppConnector.PrincipalInfo.ServiceAccount' = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof='type',
            message='AppConnector.PrincipalInfo.ServiceAccount',
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
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    principal_info: PrincipalInfo = proto.Field(
        proto.MESSAGE,
        number=8,
        message=PrincipalInfo,
    )
    resource_info: 'ResourceInfo' = proto.Field(
        proto.MESSAGE,
        number=11,
        message='ResourceInfo',
    )


class AppConnectorEventData(proto.Message):
    r"""The data within all AppConnector events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.beyondcorp.appconnectors_v1.types.AppConnector):
            Optional. The AppConnector event payload.
            Unset for deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'AppConnector' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='AppConnector',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
