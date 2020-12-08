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

import datetime

import stringcase

meta_fields = ['@type']

def compare_values(src, ref, field_name=None):
    if type(ref) in [int, float, bool, str]:
        if isinstance(src, datetime.datetime):
            assert type(ref) == str
            t = src.isoformat().replace('+00:00', '')
            while t.endswith('0'):
                t = t[:-1]
            t += 'Z'
            assert t == ref
        else:
            assert type(src) == type(ref)
            assert src == ref
    elif type(ref) == list:
        assert type(src) == type(ref)
        assert len(src) == len(ref)
        # Compare array (list) items one by one as order is preserved in a JSON list
        for i in range(len(ref)):
            compare_values(src[i], ref[i], field_name)
    elif type(ref) == dict:
        if type(src) == dict:
            assert len(ref) == len(src)
            for k in ref.keys():
                if k not in meta_fields:
                    compare_values(src[k], ref[k], k)
        else:
            for k in ref.keys():
                # Ignore meta fields in the reference data
                if k not in meta_fields:
                    formatted_k = stringcase.snakecase(k)
                    compare_values(getattr(src, formatted_k), ref[k], formatted_k)
    elif ref == None:
        assert src == None
    else:
        raise RuntimeError(f'The reference data ${field_name} is of an unsupported type ${type(ref)}.')
