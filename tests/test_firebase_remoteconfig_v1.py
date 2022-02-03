# Copyright 2020 Google LLC
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

import json

import stringcase

from helper import compare_values

def test_firebase_remoteconfig_v1_remoteconfigeventdata_simple():
    from google.events.firebase.remoteconfig.v1 import RemoteConfigEventData
    with open('tests/data/firebase_remoteconfig_v1_remoteconfigeventdata_simple.json') as f:
        raw_data = f.read()
    
    event_dikt = json.loads(raw_data)

    obj = RemoteConfigEventData.from_dict(event_dikt)
    compare_values(obj, event_dikt)

