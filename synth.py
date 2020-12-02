# Copyright 2018 Google LLC
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

"""This script is used to synthesize generated parts of this library."""

import re

import synthtool as s
from synthtool import gcp

common = gcp.CommonTemplates()
# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library()

# Copy templates for relases
s.move(templated_files / ".kokoro")  # not everything in this directory is used
s.move(templated_files / ".github" / "release-please.yml")

# Add a docs directory
s.move(templated_files / "docs", excludes=["docs/multiprocessing.rst"])

# Config files
s.move(templated_files / ".trampolinerc")
s.move(templated_files / ".github" / "snippet-bot.yml")
s.move(templated_files / "renovate.json")

# Files for releasing
s.move(templated_files / "MANIFEST.in")
s.move(templated_files / "setup.cfg")
