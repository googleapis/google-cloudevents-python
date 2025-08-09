# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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
#
from google.events.firebase.dataconnect_v1 import gapic_version as package_version

__version__ = package_version.__version__



from .types.data import CloudSqlInstance
from .types.data import Connector
from .types.data import ConnectorEventData
from .types.data import Datasource
from .types.data import File
from .types.data import GraphqlError
from .types.data import GraphqlErrorExtensions
from .types.data import Mutation
from .types.data import MutationEventData
from .types.data import PostgreSql
from .types.data import Schema
from .types.data import SchemaEventData
from .types.data import Service
from .types.data import ServiceEventData
from .types.data import Source
from .types.data import SourceLocation
from .types.data import SqlSchemaMigration
from .types.data import SqlSchemaValidation

__all__ = (
'CloudSqlInstance',
'Connector',
'ConnectorEventData',
'Datasource',
'File',
'GraphqlError',
'GraphqlErrorExtensions',
'Mutation',
'MutationEventData',
'PostgreSql',
'Schema',
'SchemaEventData',
'Service',
'ServiceEventData',
'Source',
'SourceLocation',
'SqlSchemaMigration',
'SqlSchemaValidation',
)
