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
from google.events.cloud.scheduler import gapic_version as package_version

__version__ = package_version.__version__



from google.events.cloud.scheduler_v1.types.data import AppEngineHttpTarget
from google.events.cloud.scheduler_v1.types.data import AppEngineRouting
from google.events.cloud.scheduler_v1.types.data import HttpTarget
from google.events.cloud.scheduler_v1.types.data import Job
from google.events.cloud.scheduler_v1.types.data import JobEventData
from google.events.cloud.scheduler_v1.types.data import OAuthToken
from google.events.cloud.scheduler_v1.types.data import OidcToken
from google.events.cloud.scheduler_v1.types.data import PubsubTarget
from google.events.cloud.scheduler_v1.types.data import RetryConfig
from google.events.cloud.scheduler_v1.types.data import SchedulerJobData
from google.events.cloud.scheduler_v1.types.data import HttpMethod

__all__ = ('AppEngineHttpTarget',
    'AppEngineRouting',
    'HttpTarget',
    'Job',
    'JobEventData',
    'OAuthToken',
    'OidcToken',
    'PubsubTarget',
    'RetryConfig',
    'SchedulerJobData',
    'HttpMethod',
)
