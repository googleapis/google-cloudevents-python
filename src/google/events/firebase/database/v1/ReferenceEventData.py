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
#     result = reference_event_data_from_dict(json.loads(json_string))

from typing import Optional, Dict, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


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


class ReferenceEventData:
    """The data within all Firebase Real Time Database reference events."""
    data: Optional[Dict[str, Any]]
    delta: Optional[Dict[str, Any]]

    def __init__(self, data: Optional[Dict[str, Any]], delta: Optional[Dict[str, Any]]) -> None:
        self.data = data
        self.delta = delta

    @staticmethod
    def from_dict(obj: Any) -> 'ReferenceEventData':
        assert isinstance(obj, dict)
        data = from_union([from_none, lambda x: from_dict(lambda x: x, x)], obj.get("data"))
        delta = from_union([from_none, lambda x: from_dict(lambda x: x, x)], obj.get("delta"))
        return ReferenceEventData(data, delta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_union([from_none, lambda x: from_dict(lambda x: x, x)], self.data)
        result["delta"] = from_union([from_none, lambda x: from_dict(lambda x: x, x)], self.delta)
        return result


def reference_event_data_from_dict(s: Any) -> ReferenceEventData:
    return ReferenceEventData.from_dict(s)


def reference_event_data_to_dict(x: ReferenceEventData) -> Any:
    return to_class(ReferenceEventData, x)
