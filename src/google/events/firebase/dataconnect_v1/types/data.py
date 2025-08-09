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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import struct_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import code_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.events.firebase.dataconnect.v1',
    manifest={
        'SqlSchemaValidation',
        'SqlSchemaMigration',
        'Service',
        'Datasource',
        'PostgreSql',
        'CloudSqlInstance',
        'Schema',
        'Connector',
        'Source',
        'File',
        'ServiceEventData',
        'SchemaEventData',
        'ConnectorEventData',
        'GraphqlError',
        'GraphqlErrorExtensions',
        'SourceLocation',
        'Mutation',
        'MutationEventData',
    },
)


class SqlSchemaValidation(proto.Enum):
    r"""Configure how much SQL Schema to perform for the given
    schema.

    Values:
        SQL_SCHEMA_VALIDATION_UNSPECIFIED (0):
            Unspecified SQL schema validation.
            Default to STRICT.
        NONE (1):
            Skip no SQL schema validation. Use it with
            extreme caution. CreateSchema or UpdateSchema
            will succeed even if SQL database is unavailable
            or SQL schema is incompatible.
            Generated SQL may fail at execution time.
        STRICT (2):
            Connect to the SQL database and validate that the SQL DDL
            matches the schema exactly. Surface any discrepancies as
            ``FAILED_PRECONDITION`` with an
            ``IncompatibleSqlSchemaError`` error detail.
        COMPATIBLE (3):
            Connect to the SQL database and validate that the SQL DDL
            has all the SQL resources used in the given Firebase Data
            Connect Schema. Surface any missing resources as
            ``FAILED_PRECONDITION`` with an
            ``IncompatibleSqlSchemaError`` error detail. Succeed even if
            there are unknown tables and columns.
    """
    SQL_SCHEMA_VALIDATION_UNSPECIFIED = 0
    NONE = 1
    STRICT = 2
    COMPATIBLE = 3


class SqlSchemaMigration(proto.Enum):
    r"""Configure how to perform SQL Schema migration before
    deploying the Schema.

    Values:
        SQL_SCHEMA_MIGRATION_UNSPECIFIED (0):
            Unspecified SQL schema migration.
        MIGRATE_COMPATIBLE (1):
            Connect to the SQL database and identify any missing SQL
            resources used in the given Firebase Data Connect Schema.
            Automatically create necessary SQL resources (SQL table,
            column, etc) before deploying the schema. During migration
            steps, the SQL Schema must comply with the previous
            before_deploy setting in case the migration is interrupted.
            Therefore, the previous before_deploy setting must not be
            ``schema_validation=STRICT``.
    """
    SQL_SCHEMA_MIGRATION_UNSPECIFIED = 0
    MIGRATE_COMPATIBLE = 1


class Service(proto.Message):
    r"""A Firebase Data Connect service.

    Attributes:
        name (str):
            Identifier. The relative resource name of the Firebase Data
            Connect service, in the format:

            ::

               projects/{project}/locations/{location}/services/{service}

            Note that the service ID is specific to Firebase Data
            Connect and does not correspond to any of the instance IDs
            of the underlying data source connections.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs.
        annotations (MutableMapping[str, str]):
            Optional. Stores small amounts of arbitrary
            data.
        uid (str):
            Output only. System-assigned, unique
            identifier.
        reconciling (bool):
            Output only. A field that if true, indicates
            that the system is working update the service.
        display_name (str):
            Optional. Mutable human-readable name. 63
            character limit.
        etag (str):
            Output only. This checksum is computed by the server based
            on the value of other fields, and may be sent on update and
            delete requests to ensure the client has an up-to-date value
            before proceeding. `AIP-154 <https://google.aip.dev/154>`__
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=6,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=99,
    )


class Datasource(proto.Message):
    r"""A data source that backs Firebase Data Connect services.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        postgresql (google.events.firebase.dataconnect_v1.types.PostgreSql):
            PostgreSQL configurations.

            This field is a member of `oneof`_ ``configuration``.
    """

    postgresql: 'PostgreSql' = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='configuration',
        message='PostgreSql',
    )


class PostgreSql(proto.Message):
    r"""Settings for PostgreSQL data source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        schema_validation (google.events.firebase.dataconnect_v1.types.SqlSchemaValidation):
            Optional. Configure how much Postgresql
            schema validation to perform.

            This field is a member of `oneof`_ ``before_deploy``.
        schema_migration (google.events.firebase.dataconnect_v1.types.SqlSchemaMigration):
            Optional. Configure how to perform Postgresql
            schema migration.

            This field is a member of `oneof`_ ``before_deploy``.
        unlinked (bool):
            No Postgres data source is linked. If set, don't allow
            ``database`` and ``schema_validation`` to be configured.

            This field is a member of `oneof`_ ``configuration``.
        cloud_sql (google.events.firebase.dataconnect_v1.types.CloudSqlInstance):
            Cloud SQL configurations.

            This field is a member of `oneof`_ ``configuration``.
        database (str):
            Required. Name of the PostgreSQL database.
    """

    schema_validation: 'SqlSchemaValidation' = proto.Field(
        proto.ENUM,
        number=3,
        oneof='before_deploy',
        enum='SqlSchemaValidation',
    )
    schema_migration: 'SqlSchemaMigration' = proto.Field(
        proto.ENUM,
        number=5,
        oneof='before_deploy',
        enum='SqlSchemaMigration',
    )
    unlinked: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof='configuration',
    )
    cloud_sql: 'CloudSqlInstance' = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='configuration',
        message='CloudSqlInstance',
    )
    database: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CloudSqlInstance(proto.Message):
    r"""Settings for CloudSQL instance configuration.

    Attributes:
        instance (str):
            Required. Name of the CloudSQL instance, in the format:

            ::

               projects/{project}/locations/{location}/instances/{instance}
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Schema(proto.Message):
    r"""The application schema of a Firebase Data Connect service.

    Attributes:
        name (str):
            Identifier. The relative resource name of the schema, in the
            format:

            ::

               projects/{project}/locations/{location}/services/{service}/schemas/{schema}

            Right now, the only supported schema is "main".
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs.
        annotations (MutableMapping[str, str]):
            Optional. Stores small amounts of arbitrary
            data.
        datasources (MutableSequence[google.events.firebase.dataconnect_v1.types.Datasource]):
            Required. The data sources linked in the
            schema.
        source (google.events.firebase.dataconnect_v1.types.Source):
            Required. The source files that comprise the
            application schema.
        uid (str):
            Output only. System-assigned, unique
            identifier.
        reconciling (bool):
            Output only. A field that if true, indicates
            that the system is working to compile and deploy
            the schema.
        display_name (str):
            Optional. Mutable human-readable name. 63
            character limit.
        etag (str):
            Output only. This checksum is computed by the server based
            on the value of other fields, and may be sent on update and
            delete requests to ensure the client has an up-to-date value
            before proceeding. `AIP-154 <https://google.aip.dev/154>`__
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    datasources: MutableSequence['Datasource'] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message='Datasource',
    )
    source: 'Source' = proto.Field(
        proto.MESSAGE,
        number=7,
        message='Source',
    )
    uid: str = proto.Field(
        proto.STRING,
        number=8,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=99,
    )


class Connector(proto.Message):
    r"""Connector consists of a set of operations, i.e. queries and
    mutations.

    Attributes:
        name (str):
            Identifier. The relative resource name of the connector, in
            the format:

            ::

               projects/{project}/locations/{location}/services/{service}/connectors/{connector}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp.
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs.
        annotations (MutableMapping[str, str]):
            Optional. Stores small amounts of arbitrary
            data.
        source (google.events.firebase.dataconnect_v1.types.Source):
            Required. The source files that comprise the
            connector.
        uid (str):
            Output only. System-assigned, unique
            identifier.
        reconciling (bool):
            Output only. A field that if true, indicates
            that the system is working to compile and deploy
            the connector.
        display_name (str):
            Optional. Mutable human-readable name. 63
            character limit.
        etag (str):
            Output only. This checksum is computed by the server based
            on the value of other fields, and may be sent on update and
            delete requests to ensure the client has an up-to-date value
            before proceeding. `AIP-154 <https://google.aip.dev/154>`__
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    source: 'Source' = proto.Field(
        proto.MESSAGE,
        number=6,
        message='Source',
    )
    uid: str = proto.Field(
        proto.STRING,
        number=7,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=99,
    )


class Source(proto.Message):
    r"""Used to represent a set of source files.

    Attributes:
        files (MutableSequence[google.events.firebase.dataconnect_v1.types.File]):
            Required. The files that comprise the source
            set.
    """

    files: MutableSequence['File'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='File',
    )


class File(proto.Message):
    r"""Individual files.

    Attributes:
        path (str):
            Required. The file name including folder path, if
            applicable. The path should be relative to a local workspace
            (e.g. dataconnect/(schema|connector)/*.gql) and not an
            absolute path (e.g.
            /absolute/path/(schema|connector)/*.gql).
        content (str):
            Required. The file's textual content.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ServiceEventData(proto.Message):
    r"""The data within all Service events.

    Attributes:
        payload (google.events.firebase.dataconnect_v1.types.Service):
            Optional. The Service event payload. Unset
            for deletion events.
    """

    payload: 'Service' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Service',
    )


class SchemaEventData(proto.Message):
    r"""The data within all Schema events.

    Attributes:
        payload (google.events.firebase.dataconnect_v1.types.Schema):
            Optional. The Schema event payload. Unset for
            deletion events.
    """

    payload: 'Schema' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Schema',
    )


class ConnectorEventData(proto.Message):
    r"""The data within all Connector events.

    Attributes:
        payload (google.events.firebase.dataconnect_v1.types.Connector):
            Optional. The Connector event payload. Unset
            for deletion events.
    """

    payload: 'Connector' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Connector',
    )


class GraphqlError(proto.Message):
    r"""GraphqlError contains the error information of a GraphQL
    query or mutation.

    Attributes:
        message (str):
            The detailed error message.
            The message should help developer understand the
            underlying problem without leaking internal
            data.
        locations (MutableSequence[google.events.firebase.dataconnect_v1.types.SourceLocation]):
            The source locations where the error occurred. Locations
            should help developers and toolings identify the source of
            error quickly.

            Included in admin endpoints (``ExecuteGraphql``,
            ``ExecuteGraphqlRead``, ``UpdateSchema`` and
            ``UpdateConnector``) to reference the provided GraphQL GQL
            document.

            Omitted in ``ExecuteMutation`` and ``ExecuteQuery`` since
            the caller shouldn't have access access the underlying GQL
            source.
        path (google.protobuf.struct_pb2.ListValue):
            The result field which could not be populated
            due to error.
            Clients can use path to identify whether a null
            result is intentional or caused by a runtime
            error.
            It should be a list of string or index from the
            root of GraphQL query document.
        extensions (google.events.firebase.dataconnect_v1.types.GraphqlErrorExtensions):
            Additional error information.
    """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    locations: MutableSequence['SourceLocation'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='SourceLocation',
    )
    path: struct_pb2.ListValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.ListValue,
    )
    extensions: 'GraphqlErrorExtensions' = proto.Field(
        proto.MESSAGE,
        number=4,
        message='GraphqlErrorExtensions',
    )


class GraphqlErrorExtensions(proto.Message):
    r"""GraphqlErrorExtensions contains additional information of
    ``GraphqlError``.

    Attributes:
        file (str):
            The source file name where the error occurred. Included only
            for ``UpdateSchema`` and ``UpdateConnector``, it corresponds
            to ``File.path`` of the provided ``Source``.
        code (google.rpc.code_pb2.Code):
            Maps to canonical gRPC codes. If not specified, it
            represents ``Code.INTERNAL``.
        debug_details (str):
            More detailed error message to assist debugging. It contains
            application business logic that are inappropriate to leak
            publicly.

            In the emulator, Data Connect API always includes it to
            assist local development and debugging. In the backend,
            ConnectorService always hides it. GraphqlService without
            impersonation always include it. GraphqlService with
            impersonation includes it only if explicitly opted-in with
            ``include_debug_details`` in ``GraphqlRequestExtensions``.
    """

    file: str = proto.Field(
        proto.STRING,
        number=1,
    )
    code: code_pb2.Code = proto.Field(
        proto.ENUM,
        number=2,
        enum=code_pb2.Code,
    )
    debug_details: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SourceLocation(proto.Message):
    r"""SourceLocation references a location in a GraphQL source.

    Attributes:
        line (int):
            Line number starting at 1.
        column (int):
            Column number starting at 1.
    """

    line: int = proto.Field(
        proto.INT32,
        number=1,
    )
    column: int = proto.Field(
        proto.INT32,
        number=2,
    )


class Mutation(proto.Message):
    r"""

    Attributes:
        data (google.protobuf.struct_pb2.Struct):
            The result of the execution of the requested
            operation. If an error was raised before
            execution begins, the data entry should not be
            present in the result. (a request error:

            https://spec.graphql.org/draft/#sec-Errors.Request-Errors)
            If an error was raised during the execution that
            prevented a valid response, the data entry in
            the response should be null. (a field error:

            https://spec.graphql.org/draft/#sec-Errors.Error-Result-Format)
        variables (google.protobuf.struct_pb2.Struct):
            Values for GraphQL variables provided in this
            request.
        errors (MutableSequence[google.events.firebase.dataconnect_v1.types.GraphqlError]):
            Errors of this response.
            If the data entry in the response is not
            present, the errors entry must be present.
            It conforms to
            https://spec.graphql.org/draft/#sec-Errors.
    """

    data: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )
    variables: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    errors: MutableSequence['GraphqlError'] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='GraphqlError',
    )


class MutationEventData(proto.Message):
    r"""The data within all Mutation events.

    Attributes:
        payload (google.events.firebase.dataconnect_v1.types.Mutation):

    """

    payload: 'Mutation' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Mutation',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
