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
from google.events.firebase.dataconnect import gapic_version as package_version

__version__ = package_version.__version__



from google.events.firebase.dataconnect_v1.types.data import CloudSqlInstance
from google.events.firebase.dataconnect_v1.types.data import Connector
from google.events.firebase.dataconnect_v1.types.data import ConnectorEventData
from google.events.firebase.dataconnect_v1.types.data import Datasource
from google.events.firebase.dataconnect_v1.types.data import File
from google.events.firebase.dataconnect_v1.types.data import GraphqlError
from google.events.firebase.dataconnect_v1.types.data import GraphqlErrorExtensions
from google.events.firebase.dataconnect_v1.types.data import Mutation
from google.events.firebase.dataconnect_v1.types.data import MutationEventData
from google.events.firebase.dataconnect_v1.types.data import PostgreSql
from google.events.firebase.dataconnect_v1.types.data import Schema
from google.events.firebase.dataconnect_v1.types.data import SchemaEventData
from google.events.firebase.dataconnect_v1.types.data import Service
from google.events.firebase.dataconnect_v1.types.data import ServiceEventData
from google.events.firebase.dataconnect_v1.types.data import Source
from google.events.firebase.dataconnect_v1.types.data import SourceLocation
from google.events.firebase.dataconnect_v1.types.data import SqlSchemaMigration
from google.events.firebase.dataconnect_v1.types.data import SqlSchemaValidation

__all__ = ('CloudSqlInstance',
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
