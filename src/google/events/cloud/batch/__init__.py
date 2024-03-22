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
from google.events.cloud.batch import gapic_version as package_version

__version__ = package_version.__version__



from google.events.cloud.batch_v1.types.data import AllocationPolicy
from google.events.cloud.batch_v1.types.data import ComputeResource
from google.events.cloud.batch_v1.types.data import Environment
from google.events.cloud.batch_v1.types.data import GCS
from google.events.cloud.batch_v1.types.data import Job
from google.events.cloud.batch_v1.types.data import JobEventData
from google.events.cloud.batch_v1.types.data import JobNotification
from google.events.cloud.batch_v1.types.data import JobStatus
from google.events.cloud.batch_v1.types.data import LifecyclePolicy
from google.events.cloud.batch_v1.types.data import LogsPolicy
from google.events.cloud.batch_v1.types.data import NFS
from google.events.cloud.batch_v1.types.data import Runnable
from google.events.cloud.batch_v1.types.data import ServiceAccount
from google.events.cloud.batch_v1.types.data import StatusEvent
from google.events.cloud.batch_v1.types.data import TaskExecution
from google.events.cloud.batch_v1.types.data import TaskGroup
from google.events.cloud.batch_v1.types.data import TaskSpec
from google.events.cloud.batch_v1.types.data import TaskStatus
from google.events.cloud.batch_v1.types.data import Volume

__all__ = ('AllocationPolicy',
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
