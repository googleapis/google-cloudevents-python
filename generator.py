import importlib
import os
import shutil

from jinja2 import Environment, FileSystemLoader

EVENTS_PY_FILENAME = 'events_pb2.py'
GEN_PACKAGE_PATH = 'gen_package'
INTERNAL_IMPORT_PREFIX = 'google_dot_events'
PACKAGE_ROOT = 'google/events'
PROTOS_ROOT = 'google'
TEMPLATE_PATH = 'templates'
INIT_PY_TEMPLATE = 'init_py.template'
SETUP_PY_TEMPLATE = 'setup_py.template'
LICENSE_TEMPLATE = 'LICENSE.template'
README_TEMPLATE = 'README.template'

jinja2_env = Environment(loader=FileSystemLoader(searchpath=TEMPLATE_PATH))

def clean_up():
    try:
        shutil.rmtree(GEN_PACKAGE_PATH)
    except FileNotFoundError:
        pass

def run():
    events = []
    paths = os.walk(PROTOS_ROOT)
    for i in paths:
        path = i[0]
        subdirectories = i[1]
        files = i[2]
        if EVENTS_PY_FILENAME in files:
            import_path = '{}/{}'.format(path, EVENTS_PY_FILENAME.replace('.py', '')).replace('/', '.')
            mod = importlib.import_module(import_path)
            #
            for name in dir(mod):
                if name == 'DESCRIPTOR' or name.startswith('_') or name.startswith(INTERNAL_IMPORT_PREFIX):
                    pass
                else:
                    events.append((path, name))
            #
    imports = [ ( t[0].replace('/', '.') + '.' + EVENTS_PY_FILENAME.replace('.py', ''), t[1] ) for t in events ]
    init_py_template = jinja2_env.get_template('init_py.template')
    init_py = init_py_template.render(imports=imports)
    #
    with open(PACKAGE_ROOT + '/' + '__init__.py', 'w') as f:
        f.write(init_py)
    #
    os.mkdir(GEN_PACKAGE_PATH)
    shutil.copytree(PROTOS_ROOT, '{}/src/{}'.format(GEN_PACKAGE_PATH, PROTOS_ROOT))
    shutil.rmtree(PROTOS_ROOT)
    #
    shutil.copyfile(TEMPLATE_PATH + '/' + SETUP_PY_TEMPLATE, GEN_PACKAGE_PATH + '/' + 'setup.py')
    shutil.copyfile(TEMPLATE_PATH + '/' + LICENSE_TEMPLATE, GEN_PACKAGE_PATH + '/' + 'LICENSE')
    shutil.copyfile(TEMPLATE_PATH + '/' + README_TEMPLATE, GEN_PACKAGE_PATH + '/' + 'README.md')
               
if __name__ == '__main__':
    clean_up()
    run()
