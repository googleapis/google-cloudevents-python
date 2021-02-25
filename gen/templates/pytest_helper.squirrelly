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
    """Compares the serialized and deserialized forms of a value.

    Args:
        src: The deserialized form of a value.
        ref: The serialized form of a value.
        field_name: The name of the field associated with the value.
    
    Returns: None
    """
    # If the serialized form (ref) is of a basic Python data type,
    # compare the forms directly (after conversion, if applicable)
    if type(ref) in [int, float, bool, str]:
        # If the deserialized form (src) is a datetime object, compare
        # it with the serialized form using its ISO 8601 string representation
        if isinstance(src, datetime.datetime):
            assert type(ref) == str
            # Python's datetime package does not support timezone suffixes,
            # and has a variable precision level. Here we manipulate the string
            # representation directly to make the forms comparable
            t = src.isoformat().replace('+00:00', '')
            while t.endswith('0'):
                t = t[:-1]
            t += 'Z'
            assert t == ref
        else:
            assert type(src) == type(ref)
            assert src == ref
    # If the serialized form (ref) is a Python list, assert that
    # the deserialized form is also a list of the same length and
    # compare the items in the list recursively
    elif type(ref) == list:
        assert type(src) == type(ref)
        assert len(src) == len(ref)
        # Compare array (list) items one by one as order is preserved in a
        # JSON list
        for i in range(len(ref)):
            compare_values(src[i], ref[i], field_name)
    # If the serialized form (ref) is a Python dict,
    # assert that the deserialized form (src) is either a dict
    # (free-form object) or a regular Python object
    elif type(ref) == dict:
        # If the deserialized form (src) is a dict, assert that the two forms
        # have the same length and for each key in the dict, compare
        # the values recursively
        if type(src) == dict:
            assert len(ref) == len(src)
            for k in ref.keys():
                if k not in meta_fields:
                    compare_values(src[k], ref[k], k)
        # If the deserialized form (src) is an object, compare
        # each value in the dict (ref) with its corresponding attribute
        # in the object recursively
        else:
            for k in ref.keys():
                # Ignore meta fields in the reference data
                if k not in meta_fields:
                    formatted_k = stringcase.snakecase(k)
                    compare_values(getattr(src, formatted_k), ref[k], formatted_k)
    # If the serialized form (ref) is None, assert that the deserialized form
    # is also None
    elif ref == None:
        assert src == None
    # Raise an exception if the serialized form (ref) is of unrecognizable type
    else:
        raise RuntimeError(f'The reference data ${field_name} is of an unsupported type ${type(ref)}.')
