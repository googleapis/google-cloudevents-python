# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from enum import Enum
from typing import Optional, Union
from datetime import datetime


class UpdateOriginEnum(Enum):
    ADMIN_SDK_NODE = "ADMIN_SDK_NODE"
    CONSOLE = "CONSOLE"
    REMOTE_CONFIG_UPDATE_ORIGIN_UNSPECIFIED = "REMOTE_CONFIG_UPDATE_ORIGIN_UNSPECIFIED"
    REST_API = "REST_API"


class UpdateTypeEnum(Enum):
    FORCED_UPDATE = "FORCED_UPDATE"
    INCREMENTAL_UPDATE = "INCREMENTAL_UPDATE"
    REMOTE_CONFIG_UPDATE_TYPE_UNSPECIFIED = "REMOTE_CONFIG_UPDATE_TYPE_UNSPECIFIED"
    ROLLBACK = "ROLLBACK"


class User:
    """Aggregation of all metadata fields about the account that performed the
    update.
    
    All the fields associated with the person/service account
    that wrote a Remote Config template.
    """
    """Email address."""
    email: Optional[str]
    """Image URL."""
    image_url: Optional[str]
    """Display name."""
    name: Optional[str]

    def __init__(self, email: Optional[str], image_url: Optional[str], name: Optional[str]) -> None:
        self.email = email
        self.image_url = image_url
        self.name = name


class RemoteConfigEventData:
    """The data within all Firebase Remote Config events."""
    """The user-provided description of the corresponding Remote Config template."""
    description: Optional[str]
    """Only present if this version is the result of a rollback, and will be the
    version number of the Remote Config template that was rolled-back to.
    """
    rollback_source: Optional[int]
    """Where the update action originated."""
    update_origin: Union[UpdateOriginEnum, int, None]
    """When the Remote Config template was written to the Remote Config server."""
    update_time: Optional[datetime]
    """What type of update was made."""
    update_type: Union[UpdateTypeEnum, int, None]
    """Aggregation of all metadata fields about the account that performed the
    update.
    """
    update_user: Optional[User]
    """The version number of the version's corresponding Remote Config template."""
    version_number: Optional[int]

    def __init__(self, description: Optional[str], rollback_source: Optional[int], update_origin: Union[UpdateOriginEnum, int, None], update_time: Optional[datetime], update_type: Union[UpdateTypeEnum, int, None], update_user: Optional[User], version_number: Optional[int]) -> None:
        self.description = description
        self.rollback_source = rollback_source
        self.update_origin = update_origin
        self.update_time = update_time
        self.update_type = update_type
        self.update_user = update_user
        self.version_number = version_number
