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
from google.events.cloud.deploy_v1 import gapic_version as package_version

__version__ = package_version.__version__



from .types.data import AdvanceChildRolloutJob
from .types.data import AdvanceRolloutRule
from .types.data import AnthosCluster
from .types.data import Automation
from .types.data import AutomationEventData
from .types.data import AutomationResourceSelector
from .types.data import AutomationRolloutMetadata
from .types.data import AutomationRule
from .types.data import AutomationRuleCondition
from .types.data import BuildArtifact
from .types.data import Canary
from .types.data import CanaryDeployment
from .types.data import ChildRolloutJobs
from .types.data import CloudRunConfig
from .types.data import CloudRunLocation
from .types.data import CloudRunMetadata
from .types.data import CloudRunRenderMetadata
from .types.data import CreateChildRolloutJob
from .types.data import CustomCanaryDeployment
from .types.data import CustomMetadata
from .types.data import CustomTarget
from .types.data import CustomTargetSkaffoldActions
from .types.data import CustomTargetType
from .types.data import CustomTargetTypeEventData
from .types.data import DefaultPool
from .types.data import DeliveryPipeline
from .types.data import DeliveryPipelineEventData
from .types.data import DeployJob
from .types.data import DeploymentJobs
from .types.data import DeployParameters
from .types.data import ExecutionConfig
from .types.data import GkeCluster
from .types.data import Job
from .types.data import KubernetesConfig
from .types.data import Metadata
from .types.data import MultiTarget
from .types.data import Phase
from .types.data import PipelineCondition
from .types.data import PipelineReadyCondition
from .types.data import Postdeploy
from .types.data import PostdeployJob
from .types.data import Predeploy
from .types.data import PredeployJob
from .types.data import PrivatePool
from .types.data import PromoteReleaseRule
from .types.data import Release
from .types.data import ReleaseEventData
from .types.data import RenderMetadata
from .types.data import RepairMode
from .types.data import RepairRolloutRule
from .types.data import Retry
from .types.data import Rollback
from .types.data import Rollout
from .types.data import RolloutEventData
from .types.data import RuntimeConfig
from .types.data import SerialPipeline
from .types.data import SkaffoldModules
from .types.data import Stage
from .types.data import Standard
from .types.data import Strategy
from .types.data import Target
from .types.data import TargetArtifact
from .types.data import TargetAttribute
from .types.data import TargetEventData
from .types.data import TargetsPresentCondition
from .types.data import TargetsTypeCondition
from .types.data import VerifyJob
from .types.data import BackoffMode
from .types.data import SkaffoldSupportState

__all__ = (
'AdvanceChildRolloutJob',
'AdvanceRolloutRule',
'AnthosCluster',
'Automation',
'AutomationEventData',
'AutomationResourceSelector',
'AutomationRolloutMetadata',
'AutomationRule',
'AutomationRuleCondition',
'BackoffMode',
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
'DeployParameters',
'DeploymentJobs',
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
'SkaffoldSupportState',
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
)
