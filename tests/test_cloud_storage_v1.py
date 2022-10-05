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

import google.protobuf.json_format as json_format
def test_cloud_storage_v1_storageobjectdata_simple():
    from google.events.cloud.storage.v1.data_pb2 import StorageObjectData
    with open('tests/data/cloud_storage_v1_storageobjectdata_simple.json') as f:
        raw_data = f.read()
    obj = json_format.Parse(raw_data, StorageObjectData(), ignore_unknown_fields=True)
    # Ensure the parsed object is valid and not empty.
    assert obj.IsInitialized()
    assert obj != StorageObjectData()
    