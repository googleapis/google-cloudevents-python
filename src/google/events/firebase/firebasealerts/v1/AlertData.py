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
from typing import Optional, Dict, Any
from datetime import datetime


class AlertData:
    """The data within all Firebase Alerts."""
    """Time that the event has created"""
    create_time: Optional[datetime]
    """Time that the event has ended. Optional, only present for alertsthat are
    ongoing
    """
    end_time: Optional[datetime]
    """Payload of the event, which includes the details of the specific alert.
    It's a map of keys of String type and values of various types
    """
    payload: Optional[Dict[str, Any]]

    def __init__(self, create_time: Optional[datetime], end_time: Optional[datetime], payload: Optional[Dict[str, Any]]) -> None:
        self.create_time = create_time
        self.end_time = end_time
        self.payload = payload
