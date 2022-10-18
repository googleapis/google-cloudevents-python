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


def test_cloud_audit_v1_logentrydata_pubsubcreatetopic():
    from google.events.cloud.audit_v1 import LogEntryData

    with open("tests/data/cloud_audit_v1_logentrydata_pubsubcreatetopic.json") as f:
        raw_data = f.read()

    obj = LogEntryData.from_json(raw_data, ignore_unknown_fields=True)
    # Ensure the parsed object is not empty.
    assert obj != LogEntryData()
