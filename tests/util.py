# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Utility functions for writing tests for google-cloudevents

import importlib


def make_test_case(filename, pkg, cls):
    """Returns a test function that loads the given file as the supplied proto class."""

    def testfn():
        with open(filename) as f:
            raw_data = f.read()
        klass = getattr(importlib.import_module(pkg), cls)
        obj = klass.from_json(raw_data, ignore_unknown_fields=True)
        emptyobj = klass()
        assert obj != emptyobj
        return obj

    return testfn
