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
from typing import List, Any, Dict, Union


class ReferenceEventData:
    """The data within all Firebase Real Time Database reference events."""
    """`Value` represents a dynamically typed value which can be either
    null, a number, a string, a boolean, a recursive struct value, or a
    list of values. A producer of value is expected to set one of that
    variants, absence of any variant indicates an error.
    
    The JSON representation for `Value` is JSON value.
    """
    data: Union[List[Any], bool, float, Dict[str, Any], None, str]
    """`Value` represents a dynamically typed value which can be either
    null, a number, a string, a boolean, a recursive struct value, or a
    list of values. A producer of value is expected to set one of that
    variants, absence of any variant indicates an error.
    
    The JSON representation for `Value` is JSON value.
    """
    delta: Union[List[Any], bool, float, Dict[str, Any], None, str]

    def __init__(self, data: Union[List[Any], bool, float, Dict[str, Any], None, str], delta: Union[List[Any], bool, float, Dict[str, Any], None, str]) -> None:
        self.data = data
        self.delta = delta
