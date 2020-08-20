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
import os
import shutil
import subprocess

from jinja2 import Environment, FileSystemLoader

SRC_PATH = 'src'
WORKPLACE_PATH = 'workplace'
SCHEMA_FILENAME = 'events.json'
GEN_PY_FILENAME = 'events.py'
TEMPLATE_PATH = 'templates'
INIT_PY_TEMPLATE = 'init_py.template'
PACKAGE_ROOT = 'google/events'

jinja2_env = Environment(loader=FileSystemLoader(searchpath=TEMPLATE_PATH))

def clean_up():
    """Clean up leftover artifacts (if any) from previous runs.
    """
    try:
        shutil.rmtree(SRC_PATH)
    except FileNotFoundError:
        pass

def run():
    """Generate the Google Events Library for Python using quicktype.
    """
    all_events = []
    paths = os.walk(WORKPLACE_PATH)
    for i in paths:
        path = i[0]
        subdirectories = i[1]
        files = i[2]
        if SCHEMA_FILENAME in files:
            # Run the quicktype generator
            args = [
                'quicktype',
                '--src',
                '{}/{}'.format(path, SCHEMA_FILENAME),
                '--src-lang',
                'schema',
                '--lang',
                'python',
                '--python-version',
                '3.7'
            ]
            process = subprocess.run(args, capture_output=True, check=True, text=True)
            gen_data = process.stdout
            # Extract from the specification the package declaration and
            # the event types
            with open('{}/{}'.format(path, SCHEMA_FILENAME)) as f:
                spec_data = f.read()
            spec = json.loads(spec_data)
            pkg = spec['title']
            pkg_path = pkg.replace('.', '/')
            included_events = list(spec['properties'].keys())
            # Write the generated script
            os.makedirs('{}/{}'.format(SRC_PATH, pkg_path), exist_ok=True)
            with open('{}/{}/{}'.format(SRC_PATH, pkg_path, GEN_PY_FILENAME), 'w') as f:
                f.write(gen_data)
            # Collect processed events
            for e in included_events:
                all_events.append((pkg, e))
    # Generate the __init__.py script
    imports = [ ( t[0] + '.' + GEN_PY_FILENAME.replace('.py', ''), t[1] ) for t in all_events ]
    init_py_template = jinja2_env.get_template(INIT_PY_TEMPLATE)
    init_py = init_py_template.render(imports=imports)
    with open('{}/{}/{}'.format(SRC_PATH, PACKAGE_ROOT, '__init__.py'), 'w') as f:
        f.write(init_py)
               
if __name__ == '__main__':
    clean_up()
    run()
