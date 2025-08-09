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
from google.events.cloud.apihub import gapic_version as package_version

__version__ = package_version.__version__



from google.events.cloud.apihub_v1.types.data import Api
from google.events.cloud.apihub_v1.types.data import ApiEventData
from google.events.cloud.apihub_v1.types.data import ApiHubInstance
from google.events.cloud.apihub_v1.types.data import ApiHubInstanceEventData
from google.events.cloud.apihub_v1.types.data import Attribute
from google.events.cloud.apihub_v1.types.data import AttributeEventData
from google.events.cloud.apihub_v1.types.data import AttributeValues
from google.events.cloud.apihub_v1.types.data import Dependency
from google.events.cloud.apihub_v1.types.data import DependencyEntityReference
from google.events.cloud.apihub_v1.types.data import DependencyErrorDetail
from google.events.cloud.apihub_v1.types.data import DependencyEventData
from google.events.cloud.apihub_v1.types.data import Deployment
from google.events.cloud.apihub_v1.types.data import DeploymentEventData
from google.events.cloud.apihub_v1.types.data import Documentation
from google.events.cloud.apihub_v1.types.data import ExternalApi
from google.events.cloud.apihub_v1.types.data import ExternalApiEventData
from google.events.cloud.apihub_v1.types.data import HostProjectRegistration
from google.events.cloud.apihub_v1.types.data import HostProjectRegistrationEventData
from google.events.cloud.apihub_v1.types.data import Issue
from google.events.cloud.apihub_v1.types.data import LintResponse
from google.events.cloud.apihub_v1.types.data import OpenApiSpecDetails
from google.events.cloud.apihub_v1.types.data import Owner
from google.events.cloud.apihub_v1.types.data import Point
from google.events.cloud.apihub_v1.types.data import Range
from google.events.cloud.apihub_v1.types.data import RuntimeProjectAttachment
from google.events.cloud.apihub_v1.types.data import RuntimeProjectAttachmentEventData
from google.events.cloud.apihub_v1.types.data import Spec
from google.events.cloud.apihub_v1.types.data import SpecContents
from google.events.cloud.apihub_v1.types.data import SpecDetails
from google.events.cloud.apihub_v1.types.data import SpecEventData
from google.events.cloud.apihub_v1.types.data import Version
from google.events.cloud.apihub_v1.types.data import VersionEventData
from google.events.cloud.apihub_v1.types.data import Linter
from google.events.cloud.apihub_v1.types.data import LintState
from google.events.cloud.apihub_v1.types.data import Severity

__all__ = ('Api',
    'ApiEventData',
    'ApiHubInstance',
    'ApiHubInstanceEventData',
    'Attribute',
    'AttributeEventData',
    'AttributeValues',
    'Dependency',
    'DependencyEntityReference',
    'DependencyErrorDetail',
    'DependencyEventData',
    'Deployment',
    'DeploymentEventData',
    'Documentation',
    'ExternalApi',
    'ExternalApiEventData',
    'HostProjectRegistration',
    'HostProjectRegistrationEventData',
    'Issue',
    'LintResponse',
    'OpenApiSpecDetails',
    'Owner',
    'Point',
    'Range',
    'RuntimeProjectAttachment',
    'RuntimeProjectAttachmentEventData',
    'Spec',
    'SpecContents',
    'SpecDetails',
    'SpecEventData',
    'Version',
    'VersionEventData',
    'Linter',
    'LintState',
    'Severity',
)
