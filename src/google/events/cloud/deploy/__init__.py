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
from google.events.cloud.deploy import gapic_version as package_version

__version__ = package_version.__version__



from google.events.cloud.deploy_v1.types.data import AdvanceChildRolloutJob
from google.events.cloud.deploy_v1.types.data import AdvanceRolloutRule
from google.events.cloud.deploy_v1.types.data import AnthosCluster
from google.events.cloud.deploy_v1.types.data import Automation
from google.events.cloud.deploy_v1.types.data import AutomationEventData
from google.events.cloud.deploy_v1.types.data import AutomationResourceSelector
from google.events.cloud.deploy_v1.types.data import AutomationRolloutMetadata
from google.events.cloud.deploy_v1.types.data import AutomationRule
from google.events.cloud.deploy_v1.types.data import AutomationRuleCondition
from google.events.cloud.deploy_v1.types.data import BuildArtifact
from google.events.cloud.deploy_v1.types.data import Canary
from google.events.cloud.deploy_v1.types.data import CanaryDeployment
from google.events.cloud.deploy_v1.types.data import ChildRolloutJobs
from google.events.cloud.deploy_v1.types.data import CloudRunConfig
from google.events.cloud.deploy_v1.types.data import CloudRunLocation
from google.events.cloud.deploy_v1.types.data import CloudRunMetadata
from google.events.cloud.deploy_v1.types.data import CloudRunRenderMetadata
from google.events.cloud.deploy_v1.types.data import CreateChildRolloutJob
from google.events.cloud.deploy_v1.types.data import CustomCanaryDeployment
from google.events.cloud.deploy_v1.types.data import CustomMetadata
from google.events.cloud.deploy_v1.types.data import CustomTarget
from google.events.cloud.deploy_v1.types.data import CustomTargetSkaffoldActions
from google.events.cloud.deploy_v1.types.data import CustomTargetType
from google.events.cloud.deploy_v1.types.data import CustomTargetTypeEventData
from google.events.cloud.deploy_v1.types.data import DefaultPool
from google.events.cloud.deploy_v1.types.data import DeliveryPipeline
from google.events.cloud.deploy_v1.types.data import DeliveryPipelineEventData
from google.events.cloud.deploy_v1.types.data import DeployJob
from google.events.cloud.deploy_v1.types.data import DeploymentJobs
from google.events.cloud.deploy_v1.types.data import DeployParameters
from google.events.cloud.deploy_v1.types.data import ExecutionConfig
from google.events.cloud.deploy_v1.types.data import GkeCluster
from google.events.cloud.deploy_v1.types.data import Job
from google.events.cloud.deploy_v1.types.data import KubernetesConfig
from google.events.cloud.deploy_v1.types.data import Metadata
from google.events.cloud.deploy_v1.types.data import MultiTarget
from google.events.cloud.deploy_v1.types.data import Phase
from google.events.cloud.deploy_v1.types.data import PipelineCondition
from google.events.cloud.deploy_v1.types.data import PipelineReadyCondition
from google.events.cloud.deploy_v1.types.data import Postdeploy
from google.events.cloud.deploy_v1.types.data import PostdeployJob
from google.events.cloud.deploy_v1.types.data import Predeploy
from google.events.cloud.deploy_v1.types.data import PredeployJob
from google.events.cloud.deploy_v1.types.data import PrivatePool
from google.events.cloud.deploy_v1.types.data import PromoteReleaseRule
from google.events.cloud.deploy_v1.types.data import Release
from google.events.cloud.deploy_v1.types.data import ReleaseEventData
from google.events.cloud.deploy_v1.types.data import RenderMetadata
from google.events.cloud.deploy_v1.types.data import RepairMode
from google.events.cloud.deploy_v1.types.data import RepairRolloutRule
from google.events.cloud.deploy_v1.types.data import Retry
from google.events.cloud.deploy_v1.types.data import Rollback
from google.events.cloud.deploy_v1.types.data import Rollout
from google.events.cloud.deploy_v1.types.data import RolloutEventData
from google.events.cloud.deploy_v1.types.data import RuntimeConfig
from google.events.cloud.deploy_v1.types.data import SerialPipeline
from google.events.cloud.deploy_v1.types.data import SkaffoldModules
from google.events.cloud.deploy_v1.types.data import Stage
from google.events.cloud.deploy_v1.types.data import Standard
from google.events.cloud.deploy_v1.types.data import Strategy
from google.events.cloud.deploy_v1.types.data import Target
from google.events.cloud.deploy_v1.types.data import TargetArtifact
from google.events.cloud.deploy_v1.types.data import TargetAttribute
from google.events.cloud.deploy_v1.types.data import TargetEventData
from google.events.cloud.deploy_v1.types.data import TargetsPresentCondition
from google.events.cloud.deploy_v1.types.data import TargetsTypeCondition
from google.events.cloud.deploy_v1.types.data import VerifyJob
from google.events.cloud.deploy_v1.types.data import BackoffMode
from google.events.cloud.deploy_v1.types.data import SkaffoldSupportState

__all__ = ('AdvanceChildRolloutJob',
    'AdvanceRolloutRule',
    'AnthosCluster',
    'Automation',
    'AutomationEventData',
    'AutomationResourceSelector',
    'AutomationRolloutMetadata',
    'AutomationRule',
    'AutomationRuleCondition',
    'BuildArtifact',
    'Canary',
    'CanaryDeployment',
    'ChildRolloutJobs',
    'CloudRunConfig',
    'CloudRunLocation',
    'CloudRunMetadata',
    'CloudRunRenderMetadata',
    'CreateChildRolloutJob',
    'CustomCanaryDeployment',
    'CustomMetadata',
    'CustomTarget',
    'CustomTargetSkaffoldActions',
    'CustomTargetType',
    'CustomTargetTypeEventData',
    'DefaultPool',
    'DeliveryPipeline',
    'DeliveryPipelineEventData',
    'DeployJob',
    'DeploymentJobs',
    'DeployParameters',
    'ExecutionConfig',
    'GkeCluster',
    'Job',
    'KubernetesConfig',
    'Metadata',
    'MultiTarget',
    'Phase',
    'PipelineCondition',
    'PipelineReadyCondition',
    'Postdeploy',
    'PostdeployJob',
    'Predeploy',
    'PredeployJob',
    'PrivatePool',
    'PromoteReleaseRule',
    'Release',
    'ReleaseEventData',
    'RenderMetadata',
    'RepairMode',
    'RepairRolloutRule',
    'Retry',
    'Rollback',
    'Rollout',
    'RolloutEventData',
    'RuntimeConfig',
    'SerialPipeline',
    'SkaffoldModules',
    'Stage',
    'Standard',
    'Strategy',
    'Target',
    'TargetArtifact',
    'TargetAttribute',
    'TargetEventData',
    'TargetsPresentCondition',
    'TargetsTypeCondition',
    'VerifyJob',
    'BackoffMode',
    'SkaffoldSupportState',
)
