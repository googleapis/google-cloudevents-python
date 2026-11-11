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

from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.events.cloud.dataproc.v1',
    manifest={
        'Attachment',
        'VirtualCluster',
        'KubernetesJob',
        'AttachmentEventPayload',
        'VirtualClusterEventPayload',
        'KubernetesJobEventPayload',
    },
)


class Attachment(proto.Message):
    r"""Message describing Attachment object.

    Attributes:
        name (str):
            The resource name of the attachment, in the format:
            ``projects/{project}/locations/{location}/attachments/{attachment}``
        uid (str):
            The unique identifier for the attachment.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the attachment was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the attachment was last
            updated.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        gke_cluster (str):
            The GKE cluster resource name. Format:
            ``projects/{project}/locations/{location}/clusters/{cluster}``
        state (str):
            The current state of the attachment.
            Example values: CREATING, FAILED, ACTIVE,
            DELETING.
        error_details (google.rpc.status_pb2.Status):
            Error details if the attachment is in a
            FAILED state.
    """

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
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    gke_cluster: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: str = proto.Field(
        proto.STRING,
        number=7,
    )
    error_details: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=8,
        message=status_pb2.Status,
    )


class VirtualCluster(proto.Message):
    r"""Message describing VirtualCluster object.

    Attributes:
        name (str):
            The resource name of the virtual cluster, in the format:
            ``projects/{project}/locations/{location}/attachments/{attachment}/virtualClusters/{virtual_cluster}``
        uid (str):
            The unique identifier for the virtual
            cluster.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the virtual cluster was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the virtual cluster was last
            updated.
        labels (MutableMapping[str, str]):
            User-provided labels for the virtual cluster.
        kubernetes_namespace (str):
            Target Kubernetes namespace on the attached
            GKE cluster.
        state (str):
            Current operational state of the Virtual
            Cluster. Example values: CREATING, FAILED,
            ACTIVE, DELETING.
        error_details (google.rpc.status_pb2.Status):
            Error details populated if state is FAILED.
    """

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
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    kubernetes_namespace: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: str = proto.Field(
        proto.STRING,
        number=7,
    )
    error_details: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=8,
        message=status_pb2.Status,
    )


class KubernetesJob(proto.Message):
    r"""Message describing KubernetesJob object.

    Attributes:
        name (str):
            The resource name of the kubernetes job, in the format:
            ``projects/{project}/locations/{location}/kubernetesJobs/{kubernetes_job}``
        virtual_cluster (str):
            The virtual cluster. Format:
            ``projects/{project}/locations/{location}/attachments/{attachment}/virtualClusters/{virtual_cluster}``
        labels (MutableMapping[str, str]):
            The labels to associate with this job.
        state (str):
            The state of the job.
            Example values: PENDING, CREATING, RUNNING,
            FAILED, SUCCEEDED, CANCELING, CANCELLED.
        error_details (google.rpc.status_pb2.Status):
            Error details.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Update time stamp.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    virtual_cluster: str = proto.Field(
        proto.STRING,
        number=2,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    state: str = proto.Field(
        proto.STRING,
        number=4,
    )
    error_details: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=5,
        message=status_pb2.Status,
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


class AttachmentEventPayload(proto.Message):
    r"""The data within all Dataproc MSG Attachment state changed
    events.

    Attributes:
        attachment (google.events.cloud.dataproc_v1.types.Attachment):
            The Attachment event payload.
    """

    attachment: 'Attachment' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Attachment',
    )


class VirtualClusterEventPayload(proto.Message):
    r"""The data within all Dataproc MSG VirtualCluster state changed
    events.

    Attributes:
        virtual_cluster (google.events.cloud.dataproc_v1.types.VirtualCluster):
            The VirtualCluster event payload.
    """

    virtual_cluster: 'VirtualCluster' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='VirtualCluster',
    )


class KubernetesJobEventPayload(proto.Message):
    r"""The data within all Dataproc MSG KubernetesJob state changed
    events.

    Attributes:
        kubernetes_job (google.events.cloud.dataproc_v1.types.KubernetesJob):
            The KubernetesJob event payload.
    """

    kubernetes_job: 'KubernetesJob' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='KubernetesJob',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
