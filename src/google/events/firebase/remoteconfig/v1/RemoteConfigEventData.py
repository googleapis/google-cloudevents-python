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
# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = remote_config_event_data_from_dict(json.loads(json_string))

from typing import Optional, Any, Union, TypeVar, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class UpdateUser:
    """Aggregation of all metadata fields about the account that performed the update."""
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

    @staticmethod
    def from_dict(obj: Any) -> 'UpdateUser':
        assert isinstance(obj, dict)
        email = from_union([from_str, from_none], obj.get("email"))
        image_url = from_union([from_str, from_none], obj.get("imageUrl"))
        name = from_union([from_str, from_none], obj.get("name"))
        return UpdateUser(email, image_url, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["email"] = from_union([from_str, from_none], self.email)
        result["imageUrl"] = from_union([from_str, from_none], self.image_url)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


class RemoteConfigEventData:
    """The data within all Firebase Remote Config events."""
    """The user-provided description of the corresponding Remote Config template."""
    description: Optional[str]
    """Only present if this version is the result of a rollback, and will be the
    version number of the Remote Config template that was rolled-back to.
    """
    rollback_source: Optional[str]
    """Where the update action originated."""
    update_origin: Union[int, None, str]
    """When the Remote Config template was written to the Remote Config server."""
    update_time: Optional[datetime]
    """What type of update was made."""
    update_type: Union[int, None, str]
    """Aggregation of all metadata fields about the account that performed the update."""
    update_user: Optional[UpdateUser]
    """The version number of the version's corresponding Remote Config template."""
    version_number: Optional[str]

    def __init__(self, description: Optional[str], rollback_source: Optional[str], update_origin: Union[int, None, str], update_time: Optional[datetime], update_type: Union[int, None, str], update_user: Optional[UpdateUser], version_number: Optional[str]) -> None:
        self.description = description
        self.rollback_source = rollback_source
        self.update_origin = update_origin
        self.update_time = update_time
        self.update_type = update_type
        self.update_user = update_user
        self.version_number = version_number

    @staticmethod
    def from_dict(obj: Any) -> 'RemoteConfigEventData':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        rollback_source = from_union([from_str, from_none], obj.get("rollbackSource"))
        update_origin = from_union([from_int, from_str, from_none], obj.get("updateOrigin"))
        update_time = from_union([from_datetime, from_none], obj.get("updateTime"))
        update_type = from_union([from_int, from_str, from_none], obj.get("updateType"))
        update_user = from_union([UpdateUser.from_dict, from_none], obj.get("updateUser"))
        version_number = from_union([from_str, from_none], obj.get("versionNumber"))
        return RemoteConfigEventData(description, rollback_source, update_origin, update_time, update_type, update_user, version_number)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_union([from_str, from_none], self.description)
        result["rollbackSource"] = from_union([from_str, from_none], self.rollback_source)
        result["updateOrigin"] = from_union([from_int, from_str, from_none], self.update_origin)
        result["updateTime"] = from_union([lambda x: x.isoformat(), from_none], self.update_time)
        result["updateType"] = from_union([from_int, from_str, from_none], self.update_type)
        result["updateUser"] = from_union([lambda x: to_class(UpdateUser, x), from_none], self.update_user)
        result["versionNumber"] = from_union([from_str, from_none], self.version_number)
        return result


def remote_config_event_data_from_dict(s: Any) -> RemoteConfigEventData:
    return RemoteConfigEventData.from_dict(s)


def remote_config_event_data_to_dict(x: RemoteConfigEventData) -> Any:
    return to_class(RemoteConfigEventData, x)
