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
    package='google.events.cloud.deploy.v1',
    manifest={
        'SkaffoldSupportState',
        'BackoffMode',
        'DeliveryPipeline',
        'SerialPipeline',
        'Stage',
        'DeployParameters',
        'Strategy',
        'Predeploy',
        'Postdeploy',
        'Standard',
        'Canary',
        'CanaryDeployment',
        'CustomCanaryDeployment',
        'KubernetesConfig',
        'CloudRunConfig',
        'RuntimeConfig',
        'PipelineReadyCondition',
        'TargetsPresentCondition',
        'TargetsTypeCondition',
        'PipelineCondition',
        'Target',
        'ExecutionConfig',
        'DefaultPool',
        'PrivatePool',
        'GkeCluster',
        'AnthosCluster',
        'CloudRunLocation',
        'MultiTarget',
        'CustomTarget',
        'CustomTargetType',
        'CustomTargetSkaffoldActions',
        'SkaffoldModules',
        'TargetAttribute',
        'Release',
        'BuildArtifact',
        'TargetArtifact',
        'CloudRunRenderMetadata',
        'RenderMetadata',
        'Rollout',
        'Metadata',
        'CloudRunMetadata',
        'AutomationRolloutMetadata',
        'CustomMetadata',
        'Phase',
        'DeploymentJobs',
        'ChildRolloutJobs',
        'Job',
        'DeployJob',
        'VerifyJob',
        'PredeployJob',
        'PostdeployJob',
        'CreateChildRolloutJob',
        'AdvanceChildRolloutJob',
        'Automation',
        'AutomationResourceSelector',
        'AutomationRule',
        'PromoteReleaseRule',
        'AdvanceRolloutRule',
        'RepairRolloutRule',
        'RepairMode',
        'Retry',
        'Rollback',
        'AutomationRuleCondition',
        'DeliveryPipelineEventData',
        'TargetEventData',
        'CustomTargetTypeEventData',
        'ReleaseEventData',
        'RolloutEventData',
        'AutomationEventData',
    },
)


class SkaffoldSupportState(proto.Enum):
    r"""The support state of a specific Skaffold version.

    Values:
        SKAFFOLD_SUPPORT_STATE_UNSPECIFIED (0):
            Default value. This value is unused.
        SKAFFOLD_SUPPORT_STATE_SUPPORTED (1):
            This Skaffold version is currently supported.
        SKAFFOLD_SUPPORT_STATE_MAINTENANCE_MODE (2):
            This Skaffold version is in maintenance mode.
        SKAFFOLD_SUPPORT_STATE_UNSUPPORTED (3):
            This Skaffold version is no longer supported.
    """
    SKAFFOLD_SUPPORT_STATE_UNSPECIFIED = 0
    SKAFFOLD_SUPPORT_STATE_SUPPORTED = 1
    SKAFFOLD_SUPPORT_STATE_MAINTENANCE_MODE = 2
    SKAFFOLD_SUPPORT_STATE_UNSUPPORTED = 3


class BackoffMode(proto.Enum):
    r"""The pattern of how wait time is increased.

    Values:
        BACKOFF_MODE_UNSPECIFIED (0):
            No WaitMode is specified.
        BACKOFF_MODE_LINEAR (1):
            Increases the wait time linearly.
        BACKOFF_MODE_EXPONENTIAL (2):
            Increases the wait time exponentially.
    """
    BACKOFF_MODE_UNSPECIFIED = 0
    BACKOFF_MODE_LINEAR = 1
    BACKOFF_MODE_EXPONENTIAL = 2


class DeliveryPipeline(proto.Message):
    r"""A ``DeliveryPipeline`` resource in the Cloud Deploy API.

    A ``DeliveryPipeline`` defines a pipeline through which a Skaffold
    configuration can progress.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Optional. Name of the ``DeliveryPipeline``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/[a-z][a-z0-9\-]{0,62}``.
        uid (str):
            Output only. Unique identifier of the ``DeliveryPipeline``.
        description (str):
            Description of the ``DeliveryPipeline``. Max length is 255
            characters.
        annotations (MutableMapping[str, str]):
            User annotations. These attributes can only
            be set and used by the user, and not by Cloud
            Deploy.
        labels (MutableMapping[str, str]):
            Labels are attributes that can be set and used by both the
            user and by Cloud Deploy. Labels must meet the following
            constraints:

            -  Keys and values can contain only lowercase letters,
               numeric characters, underscores, and dashes.
            -  All characters must use UTF-8 encoding, and international
               characters are allowed.
            -  Keys must start with a lowercase letter or international
               character.
            -  Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the pipeline was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Most recent time at which the
            pipeline was updated.
        serial_pipeline (google.events.cloud.deploy_v1.types.SerialPipeline):
            SerialPipeline defines a sequential set of stages for a
            ``DeliveryPipeline``.

            This field is a member of `oneof`_ ``pipeline``.
        condition (google.events.cloud.deploy_v1.types.PipelineCondition):
            Output only. Information around the state of
            the Delivery Pipeline.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
        suspended (bool):
            When suspended, no new releases or rollouts
            can be created, but in-progress ones will
            complete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
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
    serial_pipeline: 'SerialPipeline' = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof='pipeline',
        message='SerialPipeline',
    )
    condition: 'PipelineCondition' = proto.Field(
        proto.MESSAGE,
        number=11,
        message='PipelineCondition',
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10,
    )
    suspended: bool = proto.Field(
        proto.BOOL,
        number=12,
    )


class SerialPipeline(proto.Message):
    r"""SerialPipeline defines a sequential set of stages for a
    ``DeliveryPipeline``.

    Attributes:
        stages (MutableSequence[google.events.cloud.deploy_v1.types.Stage]):
            Each stage specifies configuration for a ``Target``. The
            ordering of this list defines the promotion flow.
    """

    stages: MutableSequence['Stage'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Stage',
    )


class Stage(proto.Message):
    r"""Stage specifies a location to which to deploy.

    Attributes:
        target_id (str):
            The target_id to which this stage points. This field refers
            exclusively to the last segment of a target name. For
            example, this field would just be ``my-target`` (rather than
            ``projects/project/locations/location/targets/my-target``).
            The location of the ``Target`` is inferred to be the same as
            the location of the ``DeliveryPipeline`` that contains this
            ``Stage``.
        profiles (MutableSequence[str]):
            Skaffold profiles to use when rendering the manifest for
            this stage's ``Target``.
        strategy (google.events.cloud.deploy_v1.types.Strategy):
            Optional. The strategy to use for a ``Rollout`` to this
            stage.
        deploy_parameters (MutableSequence[google.events.cloud.deploy_v1.types.DeployParameters]):
            Optional. The deploy parameters to use for
            the target in this stage.
    """

    target_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    profiles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    strategy: 'Strategy' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='Strategy',
    )
    deploy_parameters: MutableSequence['DeployParameters'] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message='DeployParameters',
    )


class DeployParameters(proto.Message):
    r"""DeployParameters contains deploy parameters information.

    Attributes:
        values (MutableMapping[str, str]):
            Required. Values are deploy parameters in
            key-value pairs.
        match_target_labels (MutableMapping[str, str]):
            Optional. Deploy parameters are applied to
            targets with match labels. If unspecified,
            deploy parameters are applied to all targets
            (including child targets of a multi-target).
    """

    values: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    match_target_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class Strategy(proto.Message):
    r"""Strategy contains deployment strategy information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        standard (google.events.cloud.deploy_v1.types.Standard):
            Standard deployment strategy executes a
            single deploy and allows verifying the
            deployment.

            This field is a member of `oneof`_ ``deployment_strategy``.
        canary (google.events.cloud.deploy_v1.types.Canary):
            Canary deployment strategy provides
            progressive percentage based deployments to a
            Target.

            This field is a member of `oneof`_ ``deployment_strategy``.
    """

    standard: 'Standard' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='deployment_strategy',
        message='Standard',
    )
    canary: 'Canary' = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='deployment_strategy',
        message='Canary',
    )


class Predeploy(proto.Message):
    r"""Predeploy contains the predeploy job configuration
    information.

    Attributes:
        actions (MutableSequence[str]):
            Optional. A sequence of Skaffold custom
            actions to invoke during execution of the
            predeploy job.
    """

    actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class Postdeploy(proto.Message):
    r"""Postdeploy contains the postdeploy job configuration
    information.

    Attributes:
        actions (MutableSequence[str]):
            Optional. A sequence of Skaffold custom
            actions to invoke during execution of the
            postdeploy job.
    """

    actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class Standard(proto.Message):
    r"""Standard represents the standard deployment strategy.

    Attributes:
        verify (bool):
            Whether to verify a deployment.
        predeploy (google.events.cloud.deploy_v1.types.Predeploy):
            Optional. Configuration for the predeploy
            job. If this is not configured, predeploy job
            will not be present.
        postdeploy (google.events.cloud.deploy_v1.types.Postdeploy):
            Optional. Configuration for the postdeploy
            job. If this is not configured, postdeploy job
            will not be present.
    """

    verify: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    predeploy: 'Predeploy' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='Predeploy',
    )
    postdeploy: 'Postdeploy' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='Postdeploy',
    )


class Canary(proto.Message):
    r"""Canary represents the canary deployment strategy.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        runtime_config (google.events.cloud.deploy_v1.types.RuntimeConfig):
            Optional. Runtime specific configurations for
            the deployment strategy. The runtime
            configuration is used to determine how Cloud
            Deploy will split traffic to enable a
            progressive deployment.
        canary_deployment (google.events.cloud.deploy_v1.types.CanaryDeployment):
            Configures the progressive based deployment
            for a Target.

            This field is a member of `oneof`_ ``mode``.
        custom_canary_deployment (google.events.cloud.deploy_v1.types.CustomCanaryDeployment):
            Configures the progressive based deployment
            for a Target, but allows customizing at the
            phase level where a phase represents each of the
            percentage deployments.

            This field is a member of `oneof`_ ``mode``.
    """

    runtime_config: 'RuntimeConfig' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='RuntimeConfig',
    )
    canary_deployment: 'CanaryDeployment' = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='mode',
        message='CanaryDeployment',
    )
    custom_canary_deployment: 'CustomCanaryDeployment' = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof='mode',
        message='CustomCanaryDeployment',
    )


class CanaryDeployment(proto.Message):
    r"""CanaryDeployment represents the canary deployment
    configuration

    Attributes:
        percentages (MutableSequence[int]):
            Required. The percentage based deployments that will occur
            as a part of a ``Rollout``. List is expected in ascending
            order and each integer n is 0 <= n < 100.
        verify (bool):
            Whether to run verify tests after each
            percentage deployment.
        predeploy (google.events.cloud.deploy_v1.types.Predeploy):
            Optional. Configuration for the predeploy job
            of the first phase. If this is not configured,
            there will be no predeploy job for this phase.
        postdeploy (google.events.cloud.deploy_v1.types.Postdeploy):
            Optional. Configuration for the postdeploy
            job of the last phase. If this is not
            configured, there will be no postdeploy job for
            this phase.
    """

    percentages: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=1,
    )
    verify: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    predeploy: 'Predeploy' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='Predeploy',
    )
    postdeploy: 'Postdeploy' = proto.Field(
        proto.MESSAGE,
        number=4,
        message='Postdeploy',
    )


class CustomCanaryDeployment(proto.Message):
    r"""CustomCanaryDeployment represents the custom canary
    deployment configuration.

    Attributes:
        phase_configs (MutableSequence[google.events.cloud.deploy_v1.types.CustomCanaryDeployment.PhaseConfig]):
            Required. Configuration for each phase in the
            canary deployment in the order executed.
    """

    class PhaseConfig(proto.Message):
        r"""PhaseConfig represents the configuration for a phase in the
        custom canary deployment.

        Attributes:
            phase_id (str):
                Required. The ID to assign to the ``Rollout`` phase. This
                value must consist of lower-case letters, numbers, and
                hyphens, start with a letter and end with a letter or a
                number, and have a max length of 63 characters. In other
                words, it must match the following regex:
                ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$``.
            percentage (int):
                Required. Percentage deployment for the
                phase.
            profiles (MutableSequence[str]):
                Skaffold profiles to use when rendering the manifest for
                this phase. These are in addition to the profiles list
                specified in the ``DeliveryPipeline`` stage.
            verify (bool):
                Whether to run verify tests after the
                deployment.
            predeploy (google.events.cloud.deploy_v1.types.Predeploy):
                Optional. Configuration for the predeploy job
                of this phase. If this is not configured, there
                will be no predeploy job for this phase.
            postdeploy (google.events.cloud.deploy_v1.types.Postdeploy):
                Optional. Configuration for the postdeploy
                job of this phase. If this is not configured,
                there will be no postdeploy job for this phase.
        """

        phase_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        percentage: int = proto.Field(
            proto.INT32,
            number=2,
        )
        profiles: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        verify: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        predeploy: 'Predeploy' = proto.Field(
            proto.MESSAGE,
            number=5,
            message='Predeploy',
        )
        postdeploy: 'Postdeploy' = proto.Field(
            proto.MESSAGE,
            number=6,
            message='Postdeploy',
        )

    phase_configs: MutableSequence[PhaseConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=PhaseConfig,
    )


class KubernetesConfig(proto.Message):
    r"""KubernetesConfig contains the Kubernetes runtime
    configuration.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gateway_service_mesh (google.events.cloud.deploy_v1.types.KubernetesConfig.GatewayServiceMesh):
            Kubernetes Gateway API service mesh
            configuration.

            This field is a member of `oneof`_ ``service_definition``.
        service_networking (google.events.cloud.deploy_v1.types.KubernetesConfig.ServiceNetworking):
            Kubernetes Service networking configuration.

            This field is a member of `oneof`_ ``service_definition``.
    """

    class GatewayServiceMesh(proto.Message):
        r"""Information about the Kubernetes Gateway API service mesh
        configuration.

        Attributes:
            http_route (str):
                Required. Name of the Gateway API HTTPRoute.
            service (str):
                Required. Name of the Kubernetes Service.
            deployment (str):
                Required. Name of the Kubernetes Deployment
                whose traffic is managed by the specified
                HTTPRoute and Service.
            route_update_wait_time (google.protobuf.duration_pb2.Duration):
                Optional. The time to wait for route updates
                to propagate. The maximum configurable time is 3
                hours, in seconds format. If unspecified, there
                is no wait time.
            stable_cutback_duration (google.protobuf.duration_pb2.Duration):
                Optional. The amount of time to migrate
                traffic back from the canary Service to the
                original Service during the stable phase
                deployment. If specified, must be between 15s
                and 3600s. If unspecified, there is no cutback
                time.
        """

        http_route: str = proto.Field(
            proto.STRING,
            number=1,
        )
        service: str = proto.Field(
            proto.STRING,
            number=2,
        )
        deployment: str = proto.Field(
            proto.STRING,
            number=3,
        )
        route_update_wait_time: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        stable_cutback_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )

    class ServiceNetworking(proto.Message):
        r"""Information about the Kubernetes Service networking
        configuration.

        Attributes:
            service (str):
                Required. Name of the Kubernetes Service.
            deployment (str):
                Required. Name of the Kubernetes Deployment
                whose traffic is managed by the specified
                Service.
            disable_pod_overprovisioning (bool):
                Optional. Whether to disable Pod
                overprovisioning. If Pod overprovisioning is
                disabled then Cloud Deploy will limit the number
                of total Pods used for the deployment strategy
                to the number of Pods the Deployment has on the
                cluster.
        """

        service: str = proto.Field(
            proto.STRING,
            number=1,
        )
        deployment: str = proto.Field(
            proto.STRING,
            number=2,
        )
        disable_pod_overprovisioning: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    gateway_service_mesh: GatewayServiceMesh = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='service_definition',
        message=GatewayServiceMesh,
    )
    service_networking: ServiceNetworking = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='service_definition',
        message=ServiceNetworking,
    )


class CloudRunConfig(proto.Message):
    r"""CloudRunConfig contains the Cloud Run runtime configuration.

    Attributes:
        automatic_traffic_control (bool):
            Whether Cloud Deploy should update the
            traffic stanza in a Cloud Run Service on the
            user's behalf to facilitate traffic splitting.
            This is required to be true for
            CanaryDeployments, but optional for
            CustomCanaryDeployments.
        canary_revision_tags (MutableSequence[str]):
            Optional. A list of tags that are added to
            the canary revision while the canary phase is in
            progress.
        prior_revision_tags (MutableSequence[str]):
            Optional. A list of tags that are added to
            the prior revision while the canary phase is in
            progress.
        stable_revision_tags (MutableSequence[str]):
            Optional. A list of tags that are added to
            the final stable revision when the stable phase
            is applied.
    """

    automatic_traffic_control: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    canary_revision_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    prior_revision_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    stable_revision_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class RuntimeConfig(proto.Message):
    r"""RuntimeConfig contains the runtime specific configurations
    for a deployment strategy.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kubernetes (google.events.cloud.deploy_v1.types.KubernetesConfig):
            Kubernetes runtime configuration.

            This field is a member of `oneof`_ ``runtime_config``.
        cloud_run (google.events.cloud.deploy_v1.types.CloudRunConfig):
            Cloud Run runtime configuration.

            This field is a member of `oneof`_ ``runtime_config``.
    """

    kubernetes: 'KubernetesConfig' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='runtime_config',
        message='KubernetesConfig',
    )
    cloud_run: 'CloudRunConfig' = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='runtime_config',
        message='CloudRunConfig',
    )


class PipelineReadyCondition(proto.Message):
    r"""PipelineReadyCondition contains information around the status
    of the Pipeline.

    Attributes:
        status (bool):
            True if the Pipeline is in a valid state. Otherwise at least
            one condition in ``PipelineCondition`` is in an invalid
            state. Iterate over those conditions and see which
            condition(s) has status = false to find out what is wrong
            with the Pipeline.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time the condition was updated.
    """

    status: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class TargetsPresentCondition(proto.Message):
    r"""``TargetsPresentCondition`` contains information on any Targets
    referenced in the Delivery Pipeline that do not actually exist.

    Attributes:
        status (bool):
            True if there aren't any missing Targets.
        missing_targets (MutableSequence[str]):
            The list of Target names that do not exist. For example,
            ``projects/{project_id}/locations/{location_name}/targets/{target_name}``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time the condition was updated.
    """

    status: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    missing_targets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class TargetsTypeCondition(proto.Message):
    r"""TargetsTypeCondition contains information on whether the
    Targets defined in the Delivery Pipeline are of the same type.

    Attributes:
        status (bool):
            True if the targets are all a comparable
            type. For example this is true if all targets
            are GKE clusters. This is false if some targets
            are Cloud Run targets and others are GKE
            clusters.
        error_details (str):
            Human readable error message.
    """

    status: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    error_details: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PipelineCondition(proto.Message):
    r"""PipelineCondition contains all conditions relevant to a
    Delivery Pipeline.

    Attributes:
        pipeline_ready_condition (google.events.cloud.deploy_v1.types.PipelineReadyCondition):
            Details around the Pipeline's overall status.
        targets_present_condition (google.events.cloud.deploy_v1.types.TargetsPresentCondition):
            Details around targets enumerated in the
            pipeline.
        targets_type_condition (google.events.cloud.deploy_v1.types.TargetsTypeCondition):
            Details on the whether the targets enumerated
            in the pipeline are of the same type.
    """

    pipeline_ready_condition: 'PipelineReadyCondition' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='PipelineReadyCondition',
    )
    targets_present_condition: 'TargetsPresentCondition' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='TargetsPresentCondition',
    )
    targets_type_condition: 'TargetsTypeCondition' = proto.Field(
        proto.MESSAGE,
        number=4,
        message='TargetsTypeCondition',
    )


class Target(proto.Message):
    r"""A ``Target`` resource in the Cloud Deploy API.

    A ``Target`` defines a location to which a Skaffold configuration
    can be deployed.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Optional. Name of the ``Target``. Format is
            ``projects/{project}/locations/{location}/targets/[a-z][a-z0-9\-]{0,62}``.
        target_id (str):
            Output only. Resource id of the ``Target``.
        uid (str):
            Output only. Unique identifier of the ``Target``.
        description (str):
            Optional. Description of the ``Target``. Max length is 255
            characters.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes
            can only be set and used by the user, and not by
            Cloud Deploy. See
            https://google.aip.dev/128#annotations for more
            details such as format and size limitations.
        labels (MutableMapping[str, str]):
            Optional. Labels are attributes that can be set and used by
            both the user and by Cloud Deploy. Labels must meet the
            following constraints:

            -  Keys and values can contain only lowercase letters,
               numeric characters, underscores, and dashes.
            -  All characters must use UTF-8 encoding, and international
               characters are allowed.
            -  Keys must start with a lowercase letter or international
               character.
            -  Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        require_approval (bool):
            Optional. Whether or not the ``Target`` requires approval.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Target`` was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Most recent time at which the ``Target`` was
            updated.
        gke (google.events.cloud.deploy_v1.types.GkeCluster):
            Optional. Information specifying a GKE
            Cluster.

            This field is a member of `oneof`_ ``deployment_target``.
        anthos_cluster (google.events.cloud.deploy_v1.types.AnthosCluster):
            Optional. Information specifying an Anthos
            Cluster.

            This field is a member of `oneof`_ ``deployment_target``.
        run (google.events.cloud.deploy_v1.types.CloudRunLocation):
            Optional. Information specifying a Cloud Run
            deployment target.

            This field is a member of `oneof`_ ``deployment_target``.
        multi_target (google.events.cloud.deploy_v1.types.MultiTarget):
            Optional. Information specifying a
            multiTarget.

            This field is a member of `oneof`_ ``deployment_target``.
        custom_target (google.events.cloud.deploy_v1.types.CustomTarget):
            Optional. Information specifying a Custom
            Target.

            This field is a member of `oneof`_ ``deployment_target``.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        execution_configs (MutableSequence[google.events.cloud.deploy_v1.types.ExecutionConfig]):
            Configurations for all execution that relates to this
            ``Target``. Each ``ExecutionEnvironmentUsage`` value may
            only be used in a single configuration; using the same value
            multiple times is an error. When one or more configurations
            are specified, they must include the ``RENDER`` and
            ``DEPLOY`` ``ExecutionEnvironmentUsage`` values. When no
            configurations are specified, execution will use the default
            specified in ``DefaultPool``.
        deploy_parameters (MutableMapping[str, str]):
            Optional. The deploy parameters to use for
            this target.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    require_approval: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    gke: 'GkeCluster' = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof='deployment_target',
        message='GkeCluster',
    )
    anthos_cluster: 'AnthosCluster' = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof='deployment_target',
        message='AnthosCluster',
    )
    run: 'CloudRunLocation' = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof='deployment_target',
        message='CloudRunLocation',
    )
    multi_target: 'MultiTarget' = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof='deployment_target',
        message='MultiTarget',
    )
    custom_target: 'CustomTarget' = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof='deployment_target',
        message='CustomTarget',
    )
    etag: str = proto.Field(
        proto.STRING,
        number=12,
    )
    execution_configs: MutableSequence['ExecutionConfig'] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message='ExecutionConfig',
    )
    deploy_parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=20,
    )


class ExecutionConfig(proto.Message):
    r"""Configuration of the environment to use when calling
    Skaffold.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        usages (MutableSequence[google.events.cloud.deploy_v1.types.ExecutionConfig.ExecutionEnvironmentUsage]):
            Required. Usages when this configuration
            should be applied.
        default_pool (google.events.cloud.deploy_v1.types.DefaultPool):
            Optional. Use default Cloud Build pool.

            This field is a member of `oneof`_ ``execution_environment``.
        private_pool (google.events.cloud.deploy_v1.types.PrivatePool):
            Optional. Use private Cloud Build pool.

            This field is a member of `oneof`_ ``execution_environment``.
        worker_pool (str):
            Optional. The resource name of the ``WorkerPool``, with the
            format
            ``projects/{project}/locations/{location}/workerPools/{worker_pool}``.
            If this optional field is unspecified, the default Cloud
            Build pool will be used.
        service_account (str):
            Optional. Google service account to use for execution. If
            unspecified, the project execution service account
            (<PROJECT_NUMBER>-compute@developer.gserviceaccount.com) is
            used.
        artifact_storage (str):
            Optional. Cloud Storage location in which to
            store execution outputs. This can either be a
            bucket ("gs://my-bucket") or a path within a
            bucket ("gs://my-bucket/my-dir").
            If unspecified, a default bucket located in the
            same region will be used.
        execution_timeout (google.protobuf.duration_pb2.Duration):
            Optional. Execution timeout for a Cloud Build
            Execution. This must be between 10m and 24h in
            seconds format. If unspecified, a default
            timeout of 1h is used.
    """
    class ExecutionEnvironmentUsage(proto.Enum):
        r"""Possible usages of this configuration.

        Values:
            EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED (0):
                Default value. This value is unused.
            RENDER (1):
                Use for rendering.
            DEPLOY (2):
                Use for deploying and deployment hooks.
            VERIFY (3):
                Use for deployment verification.
            PREDEPLOY (4):
                Use for predeploy job execution.
            POSTDEPLOY (5):
                Use for postdeploy job execution.
        """
        EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED = 0
        RENDER = 1
        DEPLOY = 2
        VERIFY = 3
        PREDEPLOY = 4
        POSTDEPLOY = 5

    usages: MutableSequence[ExecutionEnvironmentUsage] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=ExecutionEnvironmentUsage,
    )
    default_pool: 'DefaultPool' = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='execution_environment',
        message='DefaultPool',
    )
    private_pool: 'PrivatePool' = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof='execution_environment',
        message='PrivatePool',
    )
    worker_pool: str = proto.Field(
        proto.STRING,
        number=4,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )
    artifact_storage: str = proto.Field(
        proto.STRING,
        number=6,
    )
    execution_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )


class DefaultPool(proto.Message):
    r"""Execution using the default Cloud Build pool.

    Attributes:
        service_account (str):
            Optional. Google service account to use for execution. If
            unspecified, the project execution service account
            (<PROJECT_NUMBER>-compute@developer.gserviceaccount.com)
            will be used.
        artifact_storage (str):
            Optional. Cloud Storage location where
            execution outputs should be stored. This can
            either be a bucket ("gs://my-bucket") or a path
            within a bucket ("gs://my-bucket/my-dir").
            If unspecified, a default bucket located in the
            same region will be used.
    """

    service_account: str = proto.Field(
        proto.STRING,
        number=1,
    )
    artifact_storage: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PrivatePool(proto.Message):
    r"""Execution using a private Cloud Build pool.

    Attributes:
        worker_pool (str):
            Required. Resource name of the Cloud Build worker pool to
            use. The format is
            ``projects/{project}/locations/{location}/workerPools/{pool}``.
        service_account (str):
            Optional. Google service account to use for execution. If
            unspecified, the project execution service account
            (<PROJECT_NUMBER>-compute@developer.gserviceaccount.com)
            will be used.
        artifact_storage (str):
            Optional. Cloud Storage location where
            execution outputs should be stored. This can
            either be a bucket ("gs://my-bucket") or a path
            within a bucket ("gs://my-bucket/my-dir").
            If unspecified, a default bucket located in the
            same region will be used.
    """

    worker_pool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    artifact_storage: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GkeCluster(proto.Message):
    r"""Information specifying a GKE Cluster.

    Attributes:
        cluster (str):
            Information specifying a GKE Cluster. Format is
            ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}``.
        internal_ip (bool):
            Optional. If true, ``cluster`` is accessed using the private
            IP address of the control plane endpoint. Otherwise, the
            default IP address of the control plane endpoint is used.
            The default IP address is the private IP address for
            clusters with private control-plane endpoints and the public
            IP address otherwise.

            Only specify this option when ``cluster`` is a `private GKE
            cluster <https://cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept>`__.
    """

    cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )
    internal_ip: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class AnthosCluster(proto.Message):
    r"""Information specifying an Anthos Cluster.

    Attributes:
        membership (str):
            Membership of the GKE Hub-registered cluster to which to
            apply the Skaffold configuration. Format is
            ``projects/{project}/locations/{location}/memberships/{membership_name}``.
    """

    membership: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CloudRunLocation(proto.Message):
    r"""Information specifying where to deploy a Cloud Run Service.

    Attributes:
        location (str):
            Required. The location for the Cloud Run Service. Format
            must be ``projects/{project}/locations/{location}``.
    """

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MultiTarget(proto.Message):
    r"""Information specifying a multiTarget.

    Attributes:
        target_ids (MutableSequence[str]):
            Required. The target_ids of this multiTarget.
    """

    target_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class CustomTarget(proto.Message):
    r"""Information specifying a Custom Target.

    Attributes:
        custom_target_type (str):
            Required. The name of the CustomTargetType. Format must be
            ``projects/{project}/locations/{location}/customTargetTypes/{custom_target_type}``.
    """

    custom_target_type: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CustomTargetType(proto.Message):
    r"""A ``CustomTargetType`` resource in the Cloud Deploy API.

    A ``CustomTargetType`` defines a type of custom target that can be
    referenced in a ``Target`` in order to facilitate deploying to other
    systems besides the supported runtimes.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Optional. Name of the ``CustomTargetType``. Format is
            ``projects/{project}/locations/{location}/customTargetTypes/[a-z][a-z0-9\-]{0,62}``.
        custom_target_type_id (str):
            Output only. Resource id of the ``CustomTargetType``.
        uid (str):
            Output only. Unique identifier of the ``CustomTargetType``.
        description (str):
            Optional. Description of the ``CustomTargetType``. Max
            length is 255 characters.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes
            can only be set and used by the user, and not by
            Cloud Deploy. See
            https://google.aip.dev/128#annotations for more
            details such as format and size limitations.
        labels (MutableMapping[str, str]):
            Optional. Labels are attributes that can be set and used by
            both the user and by Cloud Deploy. Labels must meet the
            following constraints:

            -  Keys and values can contain only lowercase letters,
               numeric characters, underscores, and dashes.
            -  All characters must use UTF-8 encoding, and international
               characters are allowed.
            -  Keys must start with a lowercase letter or international
               character.
            -  Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``CustomTargetType`` was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Most recent time at which the
            ``CustomTargetType`` was updated.
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        custom_actions (google.events.cloud.deploy_v1.types.CustomTargetSkaffoldActions):
            Configures render and deploy for the ``CustomTargetType``
            using Skaffold custom actions.

            This field is a member of `oneof`_ ``definition``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_target_type_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=9,
    )
    custom_actions: 'CustomTargetSkaffoldActions' = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof='definition',
        message='CustomTargetSkaffoldActions',
    )


class CustomTargetSkaffoldActions(proto.Message):
    r"""CustomTargetSkaffoldActions represents the ``CustomTargetType``
    configuration using Skaffold custom actions.

    Attributes:
        render_action (str):
            Optional. The Skaffold custom action responsible for render
            operations. If not provided then Cloud Deploy will perform
            the render operations via ``skaffold render``.
        deploy_action (str):
            Required. The Skaffold custom action
            responsible for deploy operations.
        include_skaffold_modules (MutableSequence[google.events.cloud.deploy_v1.types.SkaffoldModules]):
            Optional. List of Skaffold modules Cloud
            Deploy will include in the Skaffold Config as
            required before performing diagnose.
    """

    render_action: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deploy_action: str = proto.Field(
        proto.STRING,
        number=2,
    )
    include_skaffold_modules: MutableSequence['SkaffoldModules'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='SkaffoldModules',
    )


class SkaffoldModules(proto.Message):
    r"""Skaffold Config modules and their remote source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        configs (MutableSequence[str]):
            Optional. The Skaffold Config modules to use
            from the specified source.
        git (google.events.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGitSource):
            Remote git repository containing the Skaffold
            Config modules.

            This field is a member of `oneof`_ ``source``.
        google_cloud_storage (google.events.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGCSSource):
            Cloud Storage bucket containing the Skaffold
            Config modules.

            This field is a member of `oneof`_ ``source``.
    """

    class SkaffoldGitSource(proto.Message):
        r"""Git repository containing Skaffold Config modules.

        Attributes:
            repo (str):
                Required. Git repository the package should
                be cloned from.
            path (str):
                Optional. Relative path from the repository
                root to the Skaffold file.
            ref (str):
                Optional. Git ref the package should be
                cloned from.
        """

        repo: str = proto.Field(
            proto.STRING,
            number=1,
        )
        path: str = proto.Field(
            proto.STRING,
            number=2,
        )
        ref: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class SkaffoldGCSSource(proto.Message):
        r"""Cloud Storage bucket containing Skaffold Config modules.

        Attributes:
            source (str):
                Required. Cloud Storage source paths to copy recursively.
                For example, providing "gs://my-bucket/dir/configs/*" will
                result in Skaffold copying all files within the
                "dir/configs" directory in the bucket "my-bucket".
            path (str):
                Optional. Relative path from the source to
                the Skaffold file.
        """

        source: str = proto.Field(
            proto.STRING,
            number=1,
        )
        path: str = proto.Field(
            proto.STRING,
            number=2,
        )

    configs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    git: SkaffoldGitSource = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='source',
        message=SkaffoldGitSource,
    )
    google_cloud_storage: SkaffoldGCSSource = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof='source',
        message=SkaffoldGCSSource,
    )


class TargetAttribute(proto.Message):
    r"""Contains criteria for selecting Targets.

    Attributes:
        id (str):
            ID of the ``Target``. The value of this field could be one
            of the following:

            -  The last segment of a target name. It only needs the ID
               to determine which target is being referred to
            -  "*", all targets in a location.
        labels (MutableMapping[str, str]):
            Target labels.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class Release(proto.Message):
    r"""A ``Release`` resource in the Cloud Deploy API.

    A ``Release`` defines a specific Skaffold configuration instance
    that can be deployed.

    Attributes:
        name (str):
            Optional. Name of the ``Release``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/[a-z][a-z0-9\-]{0,62}``.
        uid (str):
            Output only. Unique identifier of the ``Release``.
        description (str):
            Description of the ``Release``. Max length is 255
            characters.
        annotations (MutableMapping[str, str]):
            User annotations. These attributes can only
            be set and used by the user, and not by Cloud
            Deploy. See
            https://google.aip.dev/128#annotations for more
            details such as format and size limitations.
        labels (MutableMapping[str, str]):
            Labels are attributes that can be set and used by both the
            user and by Cloud Deploy. Labels must meet the following
            constraints:

            -  Keys and values can contain only lowercase letters,
               numeric characters, underscores, and dashes.
            -  All characters must use UTF-8 encoding, and international
               characters are allowed.
            -  Keys must start with a lowercase letter or international
               character.
            -  Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        abandoned (bool):
            Output only. Indicates whether this is an
            abandoned release.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Release`` was created.
        render_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the render began.
        render_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the render
            completed.
        skaffold_config_uri (str):
            Cloud Storage URI of tar.gz archive
            containing Skaffold configuration.
        skaffold_config_path (str):
            Filepath of the Skaffold config inside of the
            config URI.
        build_artifacts (MutableSequence[google.events.cloud.deploy_v1.types.BuildArtifact]):
            List of artifacts to pass through to Skaffold
            command.
        delivery_pipeline_snapshot (google.events.cloud.deploy_v1.types.DeliveryPipeline):
            Output only. Snapshot of the parent pipeline
            taken at release creation time.
        target_snapshots (MutableSequence[google.events.cloud.deploy_v1.types.Target]):
            Output only. Snapshot of the targets taken at
            release creation time.
        custom_target_type_snapshots (MutableSequence[google.events.cloud.deploy_v1.types.CustomTargetType]):
            Output only. Snapshot of the custom target
            types referenced by the targets taken at release
            creation time.
        render_state (google.events.cloud.deploy_v1.types.Release.RenderState):
            Output only. Current state of the render
            operation.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
        skaffold_version (str):
            The Skaffold version to use when operating on
            this release, such as "1.20.0". Not all versions
            are valid; Cloud Deploy supports a specific set
            of versions.

            If unset, the most recent supported Skaffold
            version will be used.
        target_artifacts (MutableMapping[str, google.events.cloud.deploy_v1.types.TargetArtifact]):
            Output only. Map from target ID to the target
            artifacts created during the render operation.
        target_renders (MutableMapping[str, google.events.cloud.deploy_v1.types.Release.TargetRender]):
            Output only. Map from target ID to details of
            the render operation for that target.
        condition (google.events.cloud.deploy_v1.types.Release.ReleaseCondition):
            Output only. Information around the state of
            the Release.
        deploy_parameters (MutableMapping[str, str]):
            Optional. The deploy parameters to use for
            all targets in this release.
    """
    class RenderState(proto.Enum):
        r"""Valid states of the render operation.

        Values:
            RENDER_STATE_UNSPECIFIED (0):
                The render state is unspecified.
            SUCCEEDED (1):
                All rendering operations have completed
                successfully.
            FAILED (2):
                All rendering operations have completed, and
                one or more have failed.
            IN_PROGRESS (3):
                Rendering has started and is not complete.
        """
        RENDER_STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2
        IN_PROGRESS = 3

    class TargetRender(proto.Message):
        r"""Details of rendering for a single target.

        Attributes:
            rendering_build (str):
                Output only. The resource name of the Cloud Build ``Build``
                object that is used to render the manifest for this target.
                Format is
                ``projects/{project}/locations/{location}/builds/{build}``.
            rendering_state (google.events.cloud.deploy_v1.types.Release.TargetRender.TargetRenderState):
                Output only. Current state of the render
                operation for this Target.
            metadata (google.events.cloud.deploy_v1.types.RenderMetadata):
                Output only. Metadata related to the ``Release`` render for
                this Target.
            failure_cause (google.events.cloud.deploy_v1.types.Release.TargetRender.FailureCause):
                Output only. Reason this render failed. This
                will always be unspecified while the render in
                progress.
            failure_message (str):
                Output only. Additional information about the
                render failure, if available.
        """
        class TargetRenderState(proto.Enum):
            r"""Valid states of the render operation.

            Values:
                TARGET_RENDER_STATE_UNSPECIFIED (0):
                    The render operation state is unspecified.
                SUCCEEDED (1):
                    The render operation has completed
                    successfully.
                FAILED (2):
                    The render operation has failed.
                IN_PROGRESS (3):
                    The render operation is in progress.
            """
            TARGET_RENDER_STATE_UNSPECIFIED = 0
            SUCCEEDED = 1
            FAILED = 2
            IN_PROGRESS = 3

        class FailureCause(proto.Enum):
            r"""Well-known rendering failures.

            Values:
                FAILURE_CAUSE_UNSPECIFIED (0):
                    No reason for failure is specified.
                CLOUD_BUILD_UNAVAILABLE (1):
                    Cloud Build is not available, either because it is not
                    enabled or because Cloud Deploy has insufficient
                    permissions. See `required
                    permission <https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions>`__.
                EXECUTION_FAILED (2):
                    The render operation did not complete
                    successfully; check Cloud Build logs.
                CLOUD_BUILD_REQUEST_FAILED (3):
                    Cloud Build failed to fulfill Cloud Deploy's request. See
                    failure_message for additional details.
                VERIFICATION_CONFIG_NOT_FOUND (4):
                    The render operation did not complete
                    successfully because the verification stanza
                    required for verify was not found on the
                    Skaffold configuration.
                CUSTOM_ACTION_NOT_FOUND (5):
                    The render operation did not complete successfully because
                    the custom action required for predeploy or postdeploy was
                    not found in the Skaffold configuration. See failure_message
                    for additional details.
                DEPLOYMENT_STRATEGY_NOT_SUPPORTED (6):
                    Release failed during rendering because the
                    release configuration is not supported with the
                    specified deployment strategy.
                RENDER_FEATURE_NOT_SUPPORTED (7):
                    The render operation had a feature configured
                    that is not supported.
            """
            FAILURE_CAUSE_UNSPECIFIED = 0
            CLOUD_BUILD_UNAVAILABLE = 1
            EXECUTION_FAILED = 2
            CLOUD_BUILD_REQUEST_FAILED = 3
            VERIFICATION_CONFIG_NOT_FOUND = 4
            CUSTOM_ACTION_NOT_FOUND = 5
            DEPLOYMENT_STRATEGY_NOT_SUPPORTED = 6
            RENDER_FEATURE_NOT_SUPPORTED = 7

        rendering_build: str = proto.Field(
            proto.STRING,
            number=1,
        )
        rendering_state: 'Release.TargetRender.TargetRenderState' = proto.Field(
            proto.ENUM,
            number=2,
            enum='Release.TargetRender.TargetRenderState',
        )
        metadata: 'RenderMetadata' = proto.Field(
            proto.MESSAGE,
            number=6,
            message='RenderMetadata',
        )
        failure_cause: 'Release.TargetRender.FailureCause' = proto.Field(
            proto.ENUM,
            number=4,
            enum='Release.TargetRender.FailureCause',
        )
        failure_message: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class ReleaseReadyCondition(proto.Message):
        r"""ReleaseReadyCondition contains information around the status
        of the Release. If a release is not ready, you cannot create a
        rollout with the release.

        Attributes:
            status (bool):
                True if the Release is in a valid state. Otherwise at least
                one condition in ``ReleaseCondition`` is in an invalid
                state. Iterate over those conditions and see which
                condition(s) has status = false to find out what is wrong
                with the Release.
        """

        status: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    class SkaffoldSupportedCondition(proto.Message):
        r"""SkaffoldSupportedCondition contains information about when
        support for the release's version of Skaffold ends.

        Attributes:
            status (bool):
                True if the version of Skaffold used by this
                release is supported.
            skaffold_support_state (google.events.cloud.deploy_v1.types.SkaffoldSupportState):
                The Skaffold support state for this release's
                version of Skaffold.
            maintenance_mode_time (google.protobuf.timestamp_pb2.Timestamp):
                The time at which this release's version of
                Skaffold will enter maintenance mode.
            support_expiration_time (google.protobuf.timestamp_pb2.Timestamp):
                The time at which this release's version of
                Skaffold will no longer be supported.
        """

        status: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        skaffold_support_state: 'SkaffoldSupportState' = proto.Field(
            proto.ENUM,
            number=2,
            enum='SkaffoldSupportState',
        )
        maintenance_mode_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        support_expiration_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    class ReleaseCondition(proto.Message):
        r"""ReleaseCondition contains all conditions relevant to a
        Release.

        Attributes:
            release_ready_condition (google.events.cloud.deploy_v1.types.Release.ReleaseReadyCondition):
                Details around the Releases's overall status.
            skaffold_supported_condition (google.events.cloud.deploy_v1.types.Release.SkaffoldSupportedCondition):
                Details around the support state of the
                release's Skaffold version.
        """

        release_ready_condition: 'Release.ReleaseReadyCondition' = proto.Field(
            proto.MESSAGE,
            number=1,
            message='Release.ReleaseReadyCondition',
        )
        skaffold_supported_condition: 'Release.SkaffoldSupportedCondition' = proto.Field(
            proto.MESSAGE,
            number=2,
            message='Release.SkaffoldSupportedCondition',
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    abandoned: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    render_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    render_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    skaffold_config_uri: str = proto.Field(
        proto.STRING,
        number=17,
    )
    skaffold_config_path: str = proto.Field(
        proto.STRING,
        number=9,
    )
    build_artifacts: MutableSequence['BuildArtifact'] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message='BuildArtifact',
    )
    delivery_pipeline_snapshot: 'DeliveryPipeline' = proto.Field(
        proto.MESSAGE,
        number=11,
        message='DeliveryPipeline',
    )
    target_snapshots: MutableSequence['Target'] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message='Target',
    )
    custom_target_type_snapshots: MutableSequence['CustomTargetType'] = proto.RepeatedField(
        proto.MESSAGE,
        number=27,
        message='CustomTargetType',
    )
    render_state: RenderState = proto.Field(
        proto.ENUM,
        number=13,
        enum=RenderState,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=16,
    )
    skaffold_version: str = proto.Field(
        proto.STRING,
        number=19,
    )
    target_artifacts: MutableMapping[str, 'TargetArtifact'] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=20,
        message='TargetArtifact',
    )
    target_renders: MutableMapping[str, TargetRender] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=22,
        message=TargetRender,
    )
    condition: ReleaseCondition = proto.Field(
        proto.MESSAGE,
        number=24,
        message=ReleaseCondition,
    )
    deploy_parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=25,
    )


class BuildArtifact(proto.Message):
    r"""Description of an a image to use during Skaffold rendering.

    Attributes:
        image (str):
            Image name in Skaffold configuration.
        tag (str):
            Image tag to use. This will generally be the
            full path to an image, such as
            "gcr.io/my-project/busybox:1.2.3" or
            "gcr.io/my-project/busybox@sha256:abc123".
    """

    image: str = proto.Field(
        proto.STRING,
        number=3,
    )
    tag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TargetArtifact(proto.Message):
    r"""The artifacts produced by a target render operation.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        artifact_uri (str):
            Output only. URI of a directory containing
            the artifacts. This contains deployment
            configuration used by Skaffold during a rollout,
            and all paths are relative to this location.

            This field is a member of `oneof`_ ``uri``.
        skaffold_config_path (str):
            Output only. File path of the resolved
            Skaffold configuration relative to the URI.
        manifest_path (str):
            Output only. File path of the rendered
            manifest relative to the URI.
        phase_artifacts (MutableMapping[str, google.events.cloud.deploy_v1.types.TargetArtifact.PhaseArtifact]):
            Output only. Map from the phase ID to the phase artifacts
            for the ``Target``.
    """

    class PhaseArtifact(proto.Message):
        r"""Contains the paths to the artifacts, relative to the URI, for
        a phase.

        Attributes:
            skaffold_config_path (str):
                Output only. File path of the resolved
                Skaffold configuration relative to the URI.
            manifest_path (str):
                Output only. File path of the rendered
                manifest relative to the URI.
            job_manifests_path (str):
                Output only. File path of the directory of
                rendered job manifests relative to the URI. This
                is only set if it is applicable.
        """

        skaffold_config_path: str = proto.Field(
            proto.STRING,
            number=1,
        )
        manifest_path: str = proto.Field(
            proto.STRING,
            number=3,
        )
        job_manifests_path: str = proto.Field(
            proto.STRING,
            number=4,
        )

    artifact_uri: str = proto.Field(
        proto.STRING,
        number=4,
        oneof='uri',
    )
    skaffold_config_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    manifest_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    phase_artifacts: MutableMapping[str, PhaseArtifact] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=5,
        message=PhaseArtifact,
    )


class CloudRunRenderMetadata(proto.Message):
    r"""CloudRunRenderMetadata contains Cloud Run information associated
    with a ``Release`` render.

    Attributes:
        service (str):
            Output only. The name of the Cloud Run Service in the
            rendered manifest. Format is
            ``projects/{project}/locations/{location}/services/{service}``.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RenderMetadata(proto.Message):
    r"""RenderMetadata includes information associated with a ``Release``
    render.

    Attributes:
        cloud_run (google.events.cloud.deploy_v1.types.CloudRunRenderMetadata):
            Output only. Metadata associated with
            rendering for Cloud Run.
        custom (google.events.cloud.deploy_v1.types.CustomMetadata):
            Output only. Custom metadata provided by
            user-defined render operation.
    """

    cloud_run: 'CloudRunRenderMetadata' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='CloudRunRenderMetadata',
    )
    custom: 'CustomMetadata' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='CustomMetadata',
    )


class Rollout(proto.Message):
    r"""A ``Rollout`` resource in the Cloud Deploy API.

    A ``Rollout`` contains information around a specific deployment to a
    ``Target``.

    Attributes:
        name (str):
            Optional. Name of the ``Rollout``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/[a-z][a-z0-9\-]{0,62}``.
        uid (str):
            Output only. Unique identifier of the ``Rollout``.
        description (str):
            Description of the ``Rollout`` for user purposes. Max length
            is 255 characters.
        annotations (MutableMapping[str, str]):
            User annotations. These attributes can only
            be set and used by the user, and not by Cloud
            Deploy. See
            https://google.aip.dev/128#annotations for more
            details such as format and size limitations.
        labels (MutableMapping[str, str]):
            Labels are attributes that can be set and used by both the
            user and by Cloud Deploy. Labels must meet the following
            constraints:

            -  Keys and values can contain only lowercase letters,
               numeric characters, underscores, and dashes.
            -  All characters must use UTF-8 encoding, and international
               characters are allowed.
            -  Keys must start with a lowercase letter or international
               character.
            -  Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            128 bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Rollout`` was created.
        approve_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Rollout`` was approved.
        enqueue_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Rollout`` was enqueued.
        deploy_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Rollout`` started
            deploying.
        deploy_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the ``Rollout`` finished
            deploying.
        target_id (str):
            Required. The ID of Target to which this ``Rollout`` is
            deploying.
        approval_state (google.events.cloud.deploy_v1.types.Rollout.ApprovalState):
            Output only. Approval state of the ``Rollout``.
        state (google.events.cloud.deploy_v1.types.Rollout.State):
            Output only. Current state of the ``Rollout``.
        failure_reason (str):
            Output only. Additional information about the
            rollout failure, if available.
        deploying_build (str):
            Output only. The resource name of the Cloud Build ``Build``
            object that is used to deploy the Rollout. Format is
            ``projects/{project}/locations/{location}/builds/{build}``.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
        deploy_failure_cause (google.events.cloud.deploy_v1.types.Rollout.FailureCause):
            Output only. The reason this rollout failed.
            This will always be unspecified while the
            rollout is in progress.
        phases (MutableSequence[google.events.cloud.deploy_v1.types.Phase]):
            Output only. The phases that represent the workflows of this
            ``Rollout``.
        metadata (google.events.cloud.deploy_v1.types.Metadata):
            Output only. Metadata contains information
            about the rollout.
        controller_rollout (str):
            Output only. Name of the ``ControllerRollout``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/[a-z][a-z0-9\-]{0,62}``.
        rollback_of_rollout (str):
            Output only. Name of the ``Rollout`` that is rolled back by
            this ``Rollout``. Empty if this ``Rollout`` wasn't created
            as a rollback.
        rolled_back_by_rollouts (MutableSequence[str]):
            Output only. Names of ``Rollouts`` that rolled back this
            ``Rollout``.
    """
    class ApprovalState(proto.Enum):
        r"""Valid approval states of a ``Rollout``.

        Values:
            APPROVAL_STATE_UNSPECIFIED (0):
                The ``Rollout`` has an unspecified approval state.
            NEEDS_APPROVAL (1):
                The ``Rollout`` requires approval.
            DOES_NOT_NEED_APPROVAL (2):
                The ``Rollout`` does not require approval.
            APPROVED (3):
                The ``Rollout`` has been approved.
            REJECTED (4):
                The ``Rollout`` has been rejected.
        """
        APPROVAL_STATE_UNSPECIFIED = 0
        NEEDS_APPROVAL = 1
        DOES_NOT_NEED_APPROVAL = 2
        APPROVED = 3
        REJECTED = 4

    class State(proto.Enum):
        r"""Valid states of a ``Rollout``.

        Values:
            STATE_UNSPECIFIED (0):
                The ``Rollout`` has an unspecified state.
            SUCCEEDED (1):
                The ``Rollout`` has completed successfully.
            FAILED (2):
                The ``Rollout`` has failed.
            IN_PROGRESS (3):
                The ``Rollout`` is being deployed.
            PENDING_APPROVAL (4):
                The ``Rollout`` needs approval.
            APPROVAL_REJECTED (5):
                An approver rejected the ``Rollout``.
            PENDING (6):
                The ``Rollout`` is waiting for an earlier Rollout(s) to
                complete on this ``Target``.
            PENDING_RELEASE (7):
                The ``Rollout`` is waiting for the ``Release`` to be fully
                rendered.
            CANCELLING (8):
                The ``Rollout`` is in the process of being cancelled.
            CANCELLED (9):
                The ``Rollout`` has been cancelled.
            HALTED (10):
                The ``Rollout`` is halted.
        """
        STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2
        IN_PROGRESS = 3
        PENDING_APPROVAL = 4
        APPROVAL_REJECTED = 5
        PENDING = 6
        PENDING_RELEASE = 7
        CANCELLING = 8
        CANCELLED = 9
        HALTED = 10

    class FailureCause(proto.Enum):
        r"""Well-known rollout failures.

        Values:
            FAILURE_CAUSE_UNSPECIFIED (0):
                No reason for failure is specified.
            CLOUD_BUILD_UNAVAILABLE (1):
                Cloud Build is not available, either because it is not
                enabled or because Cloud Deploy has insufficient
                permissions. See `required
                permission <https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions>`__.
            EXECUTION_FAILED (2):
                The deploy operation did not complete
                successfully; check Cloud Build logs.
            DEADLINE_EXCEEDED (3):
                Deployment did not complete within the
                alloted time.
            RELEASE_FAILED (4):
                Release is in a failed state.
            RELEASE_ABANDONED (5):
                Release is abandoned.
            VERIFICATION_CONFIG_NOT_FOUND (6):
                No Skaffold verify configuration was found.
            CLOUD_BUILD_REQUEST_FAILED (7):
                Cloud Build failed to fulfill Cloud Deploy's request. See
                failure_message for additional details.
            OPERATION_FEATURE_NOT_SUPPORTED (8):
                A Rollout operation had a feature configured
                that is not supported.
        """
        FAILURE_CAUSE_UNSPECIFIED = 0
        CLOUD_BUILD_UNAVAILABLE = 1
        EXECUTION_FAILED = 2
        DEADLINE_EXCEEDED = 3
        RELEASE_FAILED = 4
        RELEASE_ABANDONED = 5
        VERIFICATION_CONFIG_NOT_FOUND = 6
        CLOUD_BUILD_REQUEST_FAILED = 7
        OPERATION_FEATURE_NOT_SUPPORTED = 8

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    approve_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    enqueue_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    deploy_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    deploy_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    target_id: str = proto.Field(
        proto.STRING,
        number=18,
    )
    approval_state: ApprovalState = proto.Field(
        proto.ENUM,
        number=12,
        enum=ApprovalState,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=13,
        enum=State,
    )
    failure_reason: str = proto.Field(
        proto.STRING,
        number=14,
    )
    deploying_build: str = proto.Field(
        proto.STRING,
        number=17,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=16,
    )
    deploy_failure_cause: FailureCause = proto.Field(
        proto.ENUM,
        number=19,
        enum=FailureCause,
    )
    phases: MutableSequence['Phase'] = proto.RepeatedField(
        proto.MESSAGE,
        number=23,
        message='Phase',
    )
    metadata: 'Metadata' = proto.Field(
        proto.MESSAGE,
        number=24,
        message='Metadata',
    )
    controller_rollout: str = proto.Field(
        proto.STRING,
        number=25,
    )
    rollback_of_rollout: str = proto.Field(
        proto.STRING,
        number=26,
    )
    rolled_back_by_rollouts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=27,
    )


class Metadata(proto.Message):
    r"""Metadata includes information associated with a ``Rollout``.

    Attributes:
        cloud_run (google.events.cloud.deploy_v1.types.CloudRunMetadata):
            Output only. The name of the Cloud Run Service that is
            associated with a ``Rollout``.
        automation (google.events.cloud.deploy_v1.types.AutomationRolloutMetadata):
            Output only. AutomationRolloutMetadata
            contains the information about the interactions
            between Automation service and this rollout.
        custom (google.events.cloud.deploy_v1.types.CustomMetadata):
            Output only. Custom metadata provided by user-defined
            ``Rollout`` operations.
    """

    cloud_run: 'CloudRunMetadata' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='CloudRunMetadata',
    )
    automation: 'AutomationRolloutMetadata' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='AutomationRolloutMetadata',
    )
    custom: 'CustomMetadata' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='CustomMetadata',
    )


class CloudRunMetadata(proto.Message):
    r"""CloudRunMetadata contains information from a Cloud Run
    deployment.

    Attributes:
        service (str):
            Output only. The name of the Cloud Run Service that is
            associated with a ``Rollout``. Format is
            ``projects/{project}/locations/{location}/services/{service}``.
        service_urls (MutableSequence[str]):
            Output only. The Cloud Run Service urls that are associated
            with a ``Rollout``.
        revision (str):
            Output only. The Cloud Run Revision id associated with a
            ``Rollout``.
        job (str):
            Output only. The name of the Cloud Run job that is
            associated with a ``Rollout``. Format is
            ``projects/{project}/locations/{location}/jobs/{job_name}``.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    revision: str = proto.Field(
        proto.STRING,
        number=3,
    )
    job: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AutomationRolloutMetadata(proto.Message):
    r"""AutomationRolloutMetadata contains Automation-related actions
    that were performed on a rollout.

    Attributes:
        promote_automation_run (str):
            Output only. The ID of the AutomationRun
            initiated by a promote release rule.
        advance_automation_runs (MutableSequence[str]):
            Output only. The IDs of the AutomationRuns
            initiated by an advance rollout rule.
        repair_automation_runs (MutableSequence[str]):
            Output only. The IDs of the AutomationRuns
            initiated by a repair rollout rule.
        current_repair_automation_run (str):
            Output only. The current AutomationRun
            repairing the rollout.
    """

    promote_automation_run: str = proto.Field(
        proto.STRING,
        number=1,
    )
    advance_automation_runs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    repair_automation_runs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    current_repair_automation_run: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CustomMetadata(proto.Message):
    r"""CustomMetadata contains information from a user-defined
    operation.

    Attributes:
        values (MutableMapping[str, str]):
            Output only. Key-value pairs provided by the
            user-defined operation.
    """

    values: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


class Phase(proto.Message):
    r"""Phase represents a collection of jobs that are logically grouped
    together for a ``Rollout``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Output only. The ID of the Phase.
        state (google.events.cloud.deploy_v1.types.Phase.State):
            Output only. Current state of the Phase.
        skip_message (str):
            Output only. Additional information on why
            the Phase was skipped, if available.
        deployment_jobs (google.events.cloud.deploy_v1.types.DeploymentJobs):
            Output only. Deployment job composition.

            This field is a member of `oneof`_ ``jobs``.
        child_rollout_jobs (google.events.cloud.deploy_v1.types.ChildRolloutJobs):
            Output only. ChildRollout job composition.

            This field is a member of `oneof`_ ``jobs``.
    """
    class State(proto.Enum):
        r"""Valid states of a Phase.

        Values:
            STATE_UNSPECIFIED (0):
                The Phase has an unspecified state.
            PENDING (1):
                The Phase is waiting for an earlier Phase(s)
                to complete.
            IN_PROGRESS (2):
                The Phase is in progress.
            SUCCEEDED (3):
                The Phase has succeeded.
            FAILED (4):
                The Phase has failed.
            ABORTED (5):
                The Phase was aborted.
            SKIPPED (6):
                The Phase was skipped.
        """
        STATE_UNSPECIFIED = 0
        PENDING = 1
        IN_PROGRESS = 2
        SUCCEEDED = 3
        FAILED = 4
        ABORTED = 5
        SKIPPED = 6

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    skip_message: str = proto.Field(
        proto.STRING,
        number=6,
    )
    deployment_jobs: 'DeploymentJobs' = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof='jobs',
        message='DeploymentJobs',
    )
    child_rollout_jobs: 'ChildRolloutJobs' = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof='jobs',
        message='ChildRolloutJobs',
    )


class DeploymentJobs(proto.Message):
    r"""Deployment job composition.

    Attributes:
        deploy_job (google.events.cloud.deploy_v1.types.Job):
            Output only. The deploy Job. This is the
            deploy job in the phase.
        verify_job (google.events.cloud.deploy_v1.types.Job):
            Output only. The verify Job. Runs after a
            deploy if the deploy succeeds.
        predeploy_job (google.events.cloud.deploy_v1.types.Job):
            Output only. The predeploy Job, which is the
            first job on the phase.
        postdeploy_job (google.events.cloud.deploy_v1.types.Job):
            Output only. The postdeploy Job, which is the
            last job on the phase.
    """

    deploy_job: 'Job' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Job',
    )
    verify_job: 'Job' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='Job',
    )
    predeploy_job: 'Job' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='Job',
    )
    postdeploy_job: 'Job' = proto.Field(
        proto.MESSAGE,
        number=4,
        message='Job',
    )


class ChildRolloutJobs(proto.Message):
    r"""ChildRollouts job composition

    Attributes:
        create_rollout_jobs (MutableSequence[google.events.cloud.deploy_v1.types.Job]):
            Output only. List of CreateChildRolloutJobs
        advance_rollout_jobs (MutableSequence[google.events.cloud.deploy_v1.types.Job]):
            Output only. List of AdvanceChildRolloutJobs
    """

    create_rollout_jobs: MutableSequence['Job'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Job',
    )
    advance_rollout_jobs: MutableSequence['Job'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='Job',
    )


class Job(proto.Message):
    r"""Job represents an operation for a ``Rollout``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Output only. The ID of the Job.
        state (google.events.cloud.deploy_v1.types.Job.State):
            Output only. The current state of the Job.
        skip_message (str):
            Output only. Additional information on why
            the Job was skipped, if available.
        job_run (str):
            Output only. The name of the ``JobRun`` responsible for the
            most recent invocation of this Job.
        deploy_job (google.events.cloud.deploy_v1.types.DeployJob):
            Output only. A deploy Job.

            This field is a member of `oneof`_ ``job_type``.
        verify_job (google.events.cloud.deploy_v1.types.VerifyJob):
            Output only. A verify Job.

            This field is a member of `oneof`_ ``job_type``.
        predeploy_job (google.events.cloud.deploy_v1.types.PredeployJob):
            Output only. A predeploy Job.

            This field is a member of `oneof`_ ``job_type``.
        postdeploy_job (google.events.cloud.deploy_v1.types.PostdeployJob):
            Output only. A postdeploy Job.

            This field is a member of `oneof`_ ``job_type``.
        create_child_rollout_job (google.events.cloud.deploy_v1.types.CreateChildRolloutJob):
            Output only. A createChildRollout Job.

            This field is a member of `oneof`_ ``job_type``.
        advance_child_rollout_job (google.events.cloud.deploy_v1.types.AdvanceChildRolloutJob):
            Output only. An advanceChildRollout Job.

            This field is a member of `oneof`_ ``job_type``.
    """
    class State(proto.Enum):
        r"""Valid states of a Job.

        Values:
            STATE_UNSPECIFIED (0):
                The Job has an unspecified state.
            PENDING (1):
                The Job is waiting for an earlier Phase(s) or
                Job(s) to complete.
            DISABLED (2):
                The Job is disabled.
            IN_PROGRESS (3):
                The Job is in progress.
            SUCCEEDED (4):
                The Job succeeded.
            FAILED (5):
                The Job failed.
            ABORTED (6):
                The Job was aborted.
            SKIPPED (7):
                The Job was skipped.
            IGNORED (8):
                The Job was ignored.
        """
        STATE_UNSPECIFIED = 0
        PENDING = 1
        DISABLED = 2
        IN_PROGRESS = 3
        SUCCEEDED = 4
        FAILED = 5
        ABORTED = 6
        SKIPPED = 7
        IGNORED = 8

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    skip_message: str = proto.Field(
        proto.STRING,
        number=8,
    )
    job_run: str = proto.Field(
        proto.STRING,
        number=3,
    )
    deploy_job: 'DeployJob' = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof='job_type',
        message='DeployJob',
    )
    verify_job: 'VerifyJob' = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof='job_type',
        message='VerifyJob',
    )
    predeploy_job: 'PredeployJob' = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof='job_type',
        message='PredeployJob',
    )
    postdeploy_job: 'PostdeployJob' = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof='job_type',
        message='PostdeployJob',
    )
    create_child_rollout_job: 'CreateChildRolloutJob' = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof='job_type',
        message='CreateChildRolloutJob',
    )
    advance_child_rollout_job: 'AdvanceChildRolloutJob' = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof='job_type',
        message='AdvanceChildRolloutJob',
    )


class DeployJob(proto.Message):
    r"""A deploy Job.
    """


class VerifyJob(proto.Message):
    r"""A verify Job.
    """


class PredeployJob(proto.Message):
    r"""A predeploy Job.

    Attributes:
        actions (MutableSequence[str]):
            Output only. The custom actions that the
            predeploy Job executes.
    """

    actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class PostdeployJob(proto.Message):
    r"""A postdeploy Job.

    Attributes:
        actions (MutableSequence[str]):
            Output only. The custom actions that the
            postdeploy Job executes.
    """

    actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class CreateChildRolloutJob(proto.Message):
    r"""A createChildRollout Job.
    """


class AdvanceChildRolloutJob(proto.Message):
    r"""An advanceChildRollout Job.
    """


class Automation(proto.Message):
    r"""An ``Automation`` resource in the Cloud Deploy API.

    An ``Automation`` enables the automation of manually driven actions
    for a Delivery Pipeline, which includes Release promotion among
    Targets, Rollout repair and Rollout deployment strategy advancement.
    The intention of Automation is to reduce manual intervention in the
    continuous delivery process.

    Attributes:
        name (str):
            Output only. Name of the ``Automation``. Format is
            ``projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automations/{automation}``.
        uid (str):
            Output only. Unique identifier of the ``Automation``.
        description (str):
            Optional. Description of the ``Automation``. Max length is
            255 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the automation was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time at which the automation was
            updated.
        annotations (MutableMapping[str, str]):
            Optional. User annotations. These attributes can only be set
            and used by the user, and not by Cloud Deploy. Annotations
            must meet the following constraints:

            -  Annotations are key/value pairs.
            -  Valid annotation keys have two segments: an optional
               prefix and name, separated by a slash (``/``).
            -  The name segment is required and must be 63 characters or
               less, beginning and ending with an alphanumeric character
               (``[a-z0-9A-Z]``) with dashes (``-``), underscores
               (``_``), dots (``.``), and alphanumerics between.
            -  The prefix is optional. If specified, the prefix must be
               a DNS subdomain: a series of DNS labels separated by
               dots(``.``), not longer than 253 characters in total,
               followed by a slash (``/``).

            See
            https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set
            for more details.
        labels (MutableMapping[str, str]):
            Optional. Labels are attributes that can be set and used by
            both the user and by Cloud Deploy. Labels must meet the
            following constraints:

            -  Keys and values can contain only lowercase letters,
               numeric characters, underscores, and dashes.
            -  All characters must use UTF-8 encoding, and international
               characters are allowed.
            -  Keys must start with a lowercase letter or international
               character.
            -  Each resource is limited to a maximum of 64 labels.

            Both keys and values are additionally constrained to be <=
            63 characters.
        etag (str):
            Optional. The weak etag of the ``Automation`` resource. This
            checksum is computed by the server based on the value of
            other fields, and may be sent on update and delete requests
            to ensure the client has an up-to-date value before
            proceeding.
        suspended (bool):
            Optional. When Suspended, automation is
            deactivated from execution.
        service_account (str):
            Required. Email address of the user-managed
            IAM service account that creates Cloud Deploy
            release and rollout resources.
        selector (google.events.cloud.deploy_v1.types.AutomationResourceSelector):
            Required. Selected resources to which the
            automation will be applied.
        rules (MutableSequence[google.events.cloud.deploy_v1.types.AutomationRule]):
            Required. List of Automation rules associated
            with the Automation resource. Must have at least
            one rule and limited to 250 rules per Delivery
            Pipeline. Note: the order of the rules here is
            not the same as the order of execution.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
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
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    suspended: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=10,
    )
    selector: 'AutomationResourceSelector' = proto.Field(
        proto.MESSAGE,
        number=11,
        message='AutomationResourceSelector',
    )
    rules: MutableSequence['AutomationRule'] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message='AutomationRule',
    )


class AutomationResourceSelector(proto.Message):
    r"""AutomationResourceSelector contains the information to select
    the resources to which an Automation is going to be applied.

    Attributes:
        targets (MutableSequence[google.events.cloud.deploy_v1.types.TargetAttribute]):
            Contains attributes about a target.
    """

    targets: MutableSequence['TargetAttribute'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='TargetAttribute',
    )


class AutomationRule(proto.Message):
    r"""``AutomationRule`` defines the automation activities.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        promote_release_rule (google.events.cloud.deploy_v1.types.PromoteReleaseRule):
            Optional. ``PromoteReleaseRule`` will automatically promote
            a release from the current target to a specified target.

            This field is a member of `oneof`_ ``rule``.
        advance_rollout_rule (google.events.cloud.deploy_v1.types.AdvanceRolloutRule):
            Optional. The ``AdvanceRolloutRule`` will automatically
            advance a successful Rollout.

            This field is a member of `oneof`_ ``rule``.
        repair_rollout_rule (google.events.cloud.deploy_v1.types.RepairRolloutRule):
            Optional. The ``RepairRolloutRule`` will automatically
            repair a failed rollout.

            This field is a member of `oneof`_ ``rule``.
    """

    promote_release_rule: 'PromoteReleaseRule' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='rule',
        message='PromoteReleaseRule',
    )
    advance_rollout_rule: 'AdvanceRolloutRule' = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='rule',
        message='AdvanceRolloutRule',
    )
    repair_rollout_rule: 'RepairRolloutRule' = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof='rule',
        message='RepairRolloutRule',
    )


class PromoteReleaseRule(proto.Message):
    r"""``PromoteRelease`` rule will automatically promote a release from
    the current target to a specified target.

    Attributes:
        id (str):
            Required. ID of the rule. This id must be unique in the
            ``Automation`` resource to which this rule belongs. The
            format is ``[a-z][a-z0-9\-]{0,62}``.
        wait (google.protobuf.duration_pb2.Duration):
            Optional. How long the release need to be
            paused until being promoted to the next target.
        destination_target_id (str):
            Optional. The ID of the stage in the pipeline to which this
            ``Release`` is deploying. If unspecified, default it to the
            next stage in the promotion flow. The value of this field
            could be one of the following:

            -  The last segment of a target name. It only needs the ID
               to determine if the target is one of the stages in the
               promotion sequence defined in the pipeline.
            -  "@next", the next target in the promotion sequence.
        condition (google.events.cloud.deploy_v1.types.AutomationRuleCondition):
            Output only. Information around the state of
            the Automation rule.
        destination_phase (str):
            Optional. The starting phase of the rollout
            created by this operation. Default to the first
            phase.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    wait: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    destination_target_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    condition: 'AutomationRuleCondition' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='AutomationRuleCondition',
    )
    destination_phase: str = proto.Field(
        proto.STRING,
        number=8,
    )


class AdvanceRolloutRule(proto.Message):
    r"""The ``AdvanceRollout`` automation rule will automatically advance a
    successful Rollout to the next phase.

    Attributes:
        id (str):
            Required. ID of the rule. This id must be unique in the
            ``Automation`` resource to which this rule belongs. The
            format is ``[a-z][a-z0-9\-]{0,62}``.
        source_phases (MutableSequence[str]):
            Optional. Proceeds only after phase name matched any one in
            the list. This value must consist of lower-case letters,
            numbers, and hyphens, start with a letter and end with a
            letter or a number, and have a max length of 63 characters.
            In other words, it must match the following regex:
            ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$``.
        wait (google.protobuf.duration_pb2.Duration):
            Optional. How long to wait after a rollout is
            finished.
        condition (google.events.cloud.deploy_v1.types.AutomationRuleCondition):
            Output only. Information around the state of
            the Automation rule.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_phases: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    wait: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    condition: 'AutomationRuleCondition' = proto.Field(
        proto.MESSAGE,
        number=5,
        message='AutomationRuleCondition',
    )


class RepairRolloutRule(proto.Message):
    r"""The ``RepairRolloutRule`` automation rule will automatically repair
    a failed ``Rollout``.

    Attributes:
        id (str):
            Required. ID of the rule. This id must be unique in the
            ``Automation`` resource to which this rule belongs. The
            format is ``[a-z][a-z0-9\-]{0,62}``.
        source_phases (MutableSequence[str]):
            Optional. Phases within which jobs are subject to automatic
            repair actions on failure. Proceeds only after phase name
            matched any one in the list, or for all phases if
            unspecified. This value must consist of lower-case letters,
            numbers, and hyphens, start with a letter and end with a
            letter or a number, and have a max length of 63 characters.
            In other words, it must match the following regex:
            ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$``.
        jobs (MutableSequence[str]):
            Optional. Jobs to repair. Proceeds only after job name
            matched any one in the list, or for all jobs if unspecified
            or empty. The phase that includes the job must match the
            phase ID specified in ``source_phase``. This value must
            consist of lower-case letters, numbers, and hyphens, start
            with a letter and end with a letter or a number, and have a
            max length of 63 characters. In other words, it must match
            the following regex: ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$``.
        repair_modes (MutableSequence[google.events.cloud.deploy_v1.types.RepairMode]):
            Required. Defines the types of automatic
            repair actions for failed jobs.
        condition (google.events.cloud.deploy_v1.types.AutomationRuleCondition):
            Output only. Information around the state of
            the 'Automation' rule.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_phases: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    jobs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    repair_modes: MutableSequence['RepairMode'] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message='RepairMode',
    )
    condition: 'AutomationRuleCondition' = proto.Field(
        proto.MESSAGE,
        number=6,
        message='AutomationRuleCondition',
    )


class RepairMode(proto.Message):
    r"""Configuration of the repair action.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        retry (google.events.cloud.deploy_v1.types.Retry):
            Optional. Retries a failed job.

            This field is a member of `oneof`_ ``mode``.
        rollback (google.events.cloud.deploy_v1.types.Rollback):
            Optional. Rolls back a ``Rollout``.

            This field is a member of `oneof`_ ``mode``.
    """

    retry: 'Retry' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='mode',
        message='Retry',
    )
    rollback: 'Rollback' = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='mode',
        message='Rollback',
    )


class Retry(proto.Message):
    r"""Retries the failed job.

    Attributes:
        attempts (int):
            Required. Total number of retries. Retry is
            skipped if set to 0; The minimum value is 1, and
            the maximum value is 10.
        wait (google.protobuf.duration_pb2.Duration):
            Optional. How long to wait for the first
            retry. Default is 0, and the maximum value is
            14d.
        backoff_mode (google.events.cloud.deploy_v1.types.BackoffMode):
            Optional. The pattern of how wait time will be increased.
            Default is linear. Backoff mode will be ignored if ``wait``
            is 0.
    """

    attempts: int = proto.Field(
        proto.INT64,
        number=1,
    )
    wait: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    backoff_mode: 'BackoffMode' = proto.Field(
        proto.ENUM,
        number=3,
        enum='BackoffMode',
    )


class Rollback(proto.Message):
    r"""Rolls back a ``Rollout``.

    Attributes:
        destination_phase (str):
            Optional. The starting phase ID for the ``Rollout``. If
            unspecified, the ``Rollout`` will start in the stable phase.
    """

    destination_phase: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AutomationRuleCondition(proto.Message):
    r"""``AutomationRuleCondition`` contains conditions relevant to an
    ``Automation`` rule.

    Attributes:
        targets_present_condition (google.events.cloud.deploy_v1.types.TargetsPresentCondition):
            Optional. Details around targets enumerated
            in the rule.
    """

    targets_present_condition: 'TargetsPresentCondition' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='TargetsPresentCondition',
    )


class DeliveryPipelineEventData(proto.Message):
    r"""The data within all DeliveryPipeline events.

    Attributes:
        payload (google.events.cloud.deploy_v1.types.DeliveryPipeline):
            Optional. The DeliveryPipeline event payload.
            Unset for deletion events.
    """

    payload: 'DeliveryPipeline' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='DeliveryPipeline',
    )


class TargetEventData(proto.Message):
    r"""The data within all Target events.

    Attributes:
        payload (google.events.cloud.deploy_v1.types.Target):
            Optional. The Target event payload. Unset for
            deletion events.
    """

    payload: 'Target' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Target',
    )


class CustomTargetTypeEventData(proto.Message):
    r"""The data within all CustomTargetType events.

    Attributes:
        payload (google.events.cloud.deploy_v1.types.CustomTargetType):
            Optional. The CustomTargetType event payload.
            Unset for deletion events.
    """

    payload: 'CustomTargetType' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='CustomTargetType',
    )


class ReleaseEventData(proto.Message):
    r"""The data within all Release events.

    Attributes:
        payload (google.events.cloud.deploy_v1.types.Release):
            The Release event payload.
    """

    payload: 'Release' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Release',
    )


class RolloutEventData(proto.Message):
    r"""The data within all Rollout events.

    Attributes:
        payload (google.events.cloud.deploy_v1.types.Rollout):
            The Rollout event payload.
    """

    payload: 'Rollout' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Rollout',
    )


class AutomationEventData(proto.Message):
    r"""The data within all Automation events.

    Attributes:
        payload (google.events.cloud.deploy_v1.types.Automation):
            Optional. The Automation event payload. Unset
            for deletion events.
    """

    payload: 'Automation' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Automation',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
