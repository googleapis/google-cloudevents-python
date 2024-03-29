# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
from google.events.cloud.batch_v1 import gapic_version as package_version

__version__ = package_version.__version__



from .types.data import AllocationPolicy
from .types.data import ComputeResource
from .types.data import Environment
from .types.data import GCS
from .types.data import Job
from .types.data import JobEventData
from .types.data import JobNotification
from .types.data import JobStatus
from .types.data import LifecyclePolicy
from .types.data import LogsPolicy
from .types.data import NFS
from .types.data import Runnable
from .types.data import ServiceAccount
from .types.data import StatusEvent
from .types.data import TaskExecution
from .types.data import TaskGroup
from .types.data import TaskSpec
from .types.data import TaskStatus
from .types.data import Volume

__all__ = (
'AllocationPolicy',
'ComputeResource',
'Environment',
'GCS',
'Job',
'JobEventData',
'JobNotification',
'JobStatus',
'LifecyclePolicy',
'LogsPolicy',
'NFS',
'Runnable',
'ServiceAccount',
'StatusEvent',
'TaskExecution',
'TaskGroup',
'TaskSpec',
'TaskStatus',
'Volume',
)
