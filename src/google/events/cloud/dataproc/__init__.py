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
from google.events.cloud.dataproc import gapic_version as package_version

__version__ = package_version.__version__



from google.events.cloud.dataproc_v1.types.data import Attachment
from google.events.cloud.dataproc_v1.types.data import AttachmentEventPayload
from google.events.cloud.dataproc_v1.types.data import KubernetesJob
from google.events.cloud.dataproc_v1.types.data import KubernetesJobEventPayload
from google.events.cloud.dataproc_v1.types.data import VirtualCluster
from google.events.cloud.dataproc_v1.types.data import VirtualClusterEventPayload

__all__ = ('Attachment',
    'AttachmentEventPayload',
    'KubernetesJob',
    'KubernetesJobEventPayload',
    'VirtualCluster',
    'VirtualClusterEventPayload',
)
