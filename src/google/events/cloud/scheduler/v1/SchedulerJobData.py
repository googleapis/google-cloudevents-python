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
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = scheduler_job_data_from_dict(json.loads(json_string))

from typing import Optional, Any, TypeVar, Type, cast


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class SchedulerJobData:
    """Scheduler job data."""
    """The custom data the user specified when creating the scheduler source."""
    custom_data: Optional[str]

    def __init__(self, custom_data: Optional[str]) -> None:
        self.custom_data = custom_data

    @staticmethod
    def from_dict(obj: Any) -> 'SchedulerJobData':
        assert isinstance(obj, dict)
        custom_data = from_union([from_str, from_none], obj.get("customData"))
        return SchedulerJobData(custom_data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["customData"] = from_union([from_str, from_none], self.custom_data)
        return result


def scheduler_job_data_from_dict(s: Any) -> SchedulerJobData:
    return SchedulerJobData.from_dict(s)


def scheduler_job_data_to_dict(x: SchedulerJobData) -> Any:
    return to_class(SchedulerJobData, x)
