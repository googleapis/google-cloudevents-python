from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Artifacts(_message.Message):
    __slots__ = ["images", "objects"]

    class ArtifactObjects(_message.Message):
        __slots__ = ["location", "paths", "timing"]
        LOCATION_FIELD_NUMBER: ClassVar[int]
        PATHS_FIELD_NUMBER: ClassVar[int]
        TIMING_FIELD_NUMBER: ClassVar[int]
        location: str
        paths: _containers.RepeatedScalarFieldContainer[str]
        timing: TimeSpan
        def __init__(
            self,
            location: Optional[str] = ...,
            paths: Optional[Iterable[str]] = ...,
            timing: Optional[Union[TimeSpan, Mapping]] = ...,
        ) -> None: ...
    IMAGES_FIELD_NUMBER: ClassVar[int]
    OBJECTS_FIELD_NUMBER: ClassVar[int]
    images: _containers.RepeatedScalarFieldContainer[str]
    objects: Artifacts.ArtifactObjects
    def __init__(
        self,
        images: Optional[Iterable[str]] = ...,
        objects: Optional[Union[Artifacts.ArtifactObjects, Mapping]] = ...,
    ) -> None: ...

class BuildEventData(_message.Message):
    __slots__ = [
        "artifacts",
        "build_trigger_id",
        "create_time",
        "finish_time",
        "id",
        "images",
        "log_url",
        "logs_bucket",
        "options",
        "project_id",
        "queue_ttl",
        "results",
        "secrets",
        "source",
        "source_provenance",
        "start_time",
        "status",
        "status_detail",
        "steps",
        "substitutions",
        "tags",
        "timeout",
        "timing",
    ]

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class SubstitutionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: Optional[str] = ..., value: Optional[str] = ...
        ) -> None: ...

    class TimingEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: TimeSpan
        def __init__(
            self,
            key: Optional[str] = ...,
            value: Optional[Union[TimeSpan, Mapping]] = ...,
        ) -> None: ...
    ARTIFACTS_FIELD_NUMBER: ClassVar[int]
    BUILD_TRIGGER_ID_FIELD_NUMBER: ClassVar[int]
    CANCELLED: BuildEventData.Status
    CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    EXPIRED: BuildEventData.Status
    FAILURE: BuildEventData.Status
    FINISH_TIME_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    IMAGES_FIELD_NUMBER: ClassVar[int]
    INTERNAL_ERROR: BuildEventData.Status
    LOGS_BUCKET_FIELD_NUMBER: ClassVar[int]
    LOG_URL_FIELD_NUMBER: ClassVar[int]
    OPTIONS_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    QUEUED: BuildEventData.Status
    QUEUE_TTL_FIELD_NUMBER: ClassVar[int]
    RESULTS_FIELD_NUMBER: ClassVar[int]
    SECRETS_FIELD_NUMBER: ClassVar[int]
    SOURCE_FIELD_NUMBER: ClassVar[int]
    SOURCE_PROVENANCE_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    STATUS_UNKNOWN: BuildEventData.Status
    STEPS_FIELD_NUMBER: ClassVar[int]
    SUBSTITUTIONS_FIELD_NUMBER: ClassVar[int]
    SUCCESS: BuildEventData.Status
    TAGS_FIELD_NUMBER: ClassVar[int]
    TIMEOUT: BuildEventData.Status
    TIMEOUT_FIELD_NUMBER: ClassVar[int]
    TIMING_FIELD_NUMBER: ClassVar[int]
    WORKING: BuildEventData.Status
    artifacts: Artifacts
    build_trigger_id: str
    create_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp
    id: str
    images: _containers.RepeatedScalarFieldContainer[str]
    log_url: str
    logs_bucket: str
    options: BuildOptions
    project_id: str
    queue_ttl: _duration_pb2.Duration
    results: Results
    secrets: _containers.RepeatedCompositeFieldContainer[Secret]
    source: Source
    source_provenance: SourceProvenance
    start_time: _timestamp_pb2.Timestamp
    status: BuildEventData.Status
    status_detail: str
    steps: _containers.RepeatedCompositeFieldContainer[BuildStep]
    substitutions: _containers.ScalarMap[str, str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    timeout: _duration_pb2.Duration
    timing: _containers.MessageMap[str, TimeSpan]
    def __init__(
        self,
        id: Optional[str] = ...,
        project_id: Optional[str] = ...,
        status: Optional[Union[BuildEventData.Status, str]] = ...,
        status_detail: Optional[str] = ...,
        source: Optional[Union[Source, Mapping]] = ...,
        steps: Optional[Iterable[Union[BuildStep, Mapping]]] = ...,
        results: Optional[Union[Results, Mapping]] = ...,
        create_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        start_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        finish_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        timeout: Optional[Union[_duration_pb2.Duration, Mapping]] = ...,
        images: Optional[Iterable[str]] = ...,
        queue_ttl: Optional[Union[_duration_pb2.Duration, Mapping]] = ...,
        artifacts: Optional[Union[Artifacts, Mapping]] = ...,
        logs_bucket: Optional[str] = ...,
        source_provenance: Optional[Union[SourceProvenance, Mapping]] = ...,
        build_trigger_id: Optional[str] = ...,
        options: Optional[Union[BuildOptions, Mapping]] = ...,
        log_url: Optional[str] = ...,
        substitutions: Optional[Mapping[str, str]] = ...,
        tags: Optional[Iterable[str]] = ...,
        secrets: Optional[Iterable[Union[Secret, Mapping]]] = ...,
        timing: Optional[Mapping[str, TimeSpan]] = ...,
    ) -> None: ...

class BuildOptions(_message.Message):
    __slots__ = [
        "disk_size_gb",
        "env",
        "log_streaming_option",
        "logging",
        "machine_type",
        "requested_verify_option",
        "secret_env",
        "source_provenance_hash",
        "substitution_option",
        "volumes",
        "worker_pool",
    ]

    class LogStreamingOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class LoggingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class MachineType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class SubstitutionOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    class VerifyOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALLOW_LOOSE: BuildOptions.SubstitutionOption
    DISK_SIZE_GB_FIELD_NUMBER: ClassVar[int]
    ENV_FIELD_NUMBER: ClassVar[int]
    GCS_ONLY: BuildOptions.LoggingMode
    LEGACY: BuildOptions.LoggingMode
    LOGGING_FIELD_NUMBER: ClassVar[int]
    LOGGING_UNSPECIFIED: BuildOptions.LoggingMode
    LOG_STREAMING_OPTION_FIELD_NUMBER: ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: ClassVar[int]
    MUST_MATCH: BuildOptions.SubstitutionOption
    N1_HIGHCPU_32: BuildOptions.MachineType
    N1_HIGHCPU_8: BuildOptions.MachineType
    NOT_VERIFIED: BuildOptions.VerifyOption
    REQUESTED_VERIFY_OPTION_FIELD_NUMBER: ClassVar[int]
    SECRET_ENV_FIELD_NUMBER: ClassVar[int]
    SOURCE_PROVENANCE_HASH_FIELD_NUMBER: ClassVar[int]
    STREAM_DEFAULT: BuildOptions.LogStreamingOption
    STREAM_OFF: BuildOptions.LogStreamingOption
    STREAM_ON: BuildOptions.LogStreamingOption
    SUBSTITUTION_OPTION_FIELD_NUMBER: ClassVar[int]
    UNSPECIFIED: BuildOptions.MachineType
    VERIFIED: BuildOptions.VerifyOption
    VOLUMES_FIELD_NUMBER: ClassVar[int]
    WORKER_POOL_FIELD_NUMBER: ClassVar[int]
    disk_size_gb: int
    env: _containers.RepeatedScalarFieldContainer[str]
    log_streaming_option: BuildOptions.LogStreamingOption
    logging: BuildOptions.LoggingMode
    machine_type: BuildOptions.MachineType
    requested_verify_option: BuildOptions.VerifyOption
    secret_env: _containers.RepeatedScalarFieldContainer[str]
    source_provenance_hash: _containers.RepeatedScalarFieldContainer[Hash.HashType]
    substitution_option: BuildOptions.SubstitutionOption
    volumes: _containers.RepeatedCompositeFieldContainer[Volume]
    worker_pool: str
    def __init__(
        self,
        source_provenance_hash: Optional[Iterable[Union[Hash.HashType, str]]] = ...,
        requested_verify_option: Optional[Union[BuildOptions.VerifyOption, str]] = ...,
        machine_type: Optional[Union[BuildOptions.MachineType, str]] = ...,
        disk_size_gb: Optional[int] = ...,
        substitution_option: Optional[
            Union[BuildOptions.SubstitutionOption, str]
        ] = ...,
        log_streaming_option: Optional[
            Union[BuildOptions.LogStreamingOption, str]
        ] = ...,
        worker_pool: Optional[str] = ...,
        logging: Optional[Union[BuildOptions.LoggingMode, str]] = ...,
        env: Optional[Iterable[str]] = ...,
        secret_env: Optional[Iterable[str]] = ...,
        volumes: Optional[Iterable[Union[Volume, Mapping]]] = ...,
    ) -> None: ...

class BuildStep(_message.Message):
    __slots__ = [
        "args",
        "dir",
        "entrypoint",
        "env",
        "id",
        "name",
        "pull_timing",
        "secret_env",
        "status",
        "timeout",
        "timing",
        "volumes",
        "wait_for",
    ]
    ARGS_FIELD_NUMBER: ClassVar[int]
    DIR_FIELD_NUMBER: ClassVar[int]
    ENTRYPOINT_FIELD_NUMBER: ClassVar[int]
    ENV_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    PULL_TIMING_FIELD_NUMBER: ClassVar[int]
    SECRET_ENV_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    TIMEOUT_FIELD_NUMBER: ClassVar[int]
    TIMING_FIELD_NUMBER: ClassVar[int]
    VOLUMES_FIELD_NUMBER: ClassVar[int]
    WAIT_FOR_FIELD_NUMBER: ClassVar[int]
    args: _containers.RepeatedScalarFieldContainer[str]
    dir: str
    entrypoint: str
    env: _containers.RepeatedScalarFieldContainer[str]
    id: str
    name: str
    pull_timing: TimeSpan
    secret_env: _containers.RepeatedScalarFieldContainer[str]
    status: BuildEventData.Status
    timeout: _duration_pb2.Duration
    timing: TimeSpan
    volumes: _containers.RepeatedCompositeFieldContainer[Volume]
    wait_for: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        name: Optional[str] = ...,
        env: Optional[Iterable[str]] = ...,
        args: Optional[Iterable[str]] = ...,
        dir: Optional[str] = ...,
        id: Optional[str] = ...,
        wait_for: Optional[Iterable[str]] = ...,
        entrypoint: Optional[str] = ...,
        secret_env: Optional[Iterable[str]] = ...,
        volumes: Optional[Iterable[Union[Volume, Mapping]]] = ...,
        timing: Optional[Union[TimeSpan, Mapping]] = ...,
        pull_timing: Optional[Union[TimeSpan, Mapping]] = ...,
        timeout: Optional[Union[_duration_pb2.Duration, Mapping]] = ...,
        status: Optional[Union[BuildEventData.Status, str]] = ...,
    ) -> None: ...

class BuiltImage(_message.Message):
    __slots__ = ["digest", "name", "push_timing"]
    DIGEST_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    PUSH_TIMING_FIELD_NUMBER: ClassVar[int]
    digest: str
    name: str
    push_timing: TimeSpan
    def __init__(
        self,
        name: Optional[str] = ...,
        digest: Optional[str] = ...,
        push_timing: Optional[Union[TimeSpan, Mapping]] = ...,
    ) -> None: ...

class FileHashes(_message.Message):
    __slots__ = ["file_hash"]
    FILE_HASH_FIELD_NUMBER: ClassVar[int]
    file_hash: _containers.RepeatedCompositeFieldContainer[Hash]
    def __init__(
        self, file_hash: Optional[Iterable[Union[Hash, Mapping]]] = ...
    ) -> None: ...

class Hash(_message.Message):
    __slots__ = ["type", "value"]

    class HashType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    MD5: Hash.HashType
    NONE: Hash.HashType
    SHA256: Hash.HashType
    TYPE_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    type: Hash.HashType
    value: bytes
    def __init__(
        self,
        type: Optional[Union[Hash.HashType, str]] = ...,
        value: Optional[bytes] = ...,
    ) -> None: ...

class RepoSource(_message.Message):
    __slots__ = [
        "branch_name",
        "commit_sha",
        "dir",
        "invert_regex",
        "project_id",
        "repo_name",
        "substitutions",
        "tag_name",
    ]

    class SubstitutionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: Optional[str] = ..., value: Optional[str] = ...
        ) -> None: ...
    BRANCH_NAME_FIELD_NUMBER: ClassVar[int]
    COMMIT_SHA_FIELD_NUMBER: ClassVar[int]
    DIR_FIELD_NUMBER: ClassVar[int]
    INVERT_REGEX_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    REPO_NAME_FIELD_NUMBER: ClassVar[int]
    SUBSTITUTIONS_FIELD_NUMBER: ClassVar[int]
    TAG_NAME_FIELD_NUMBER: ClassVar[int]
    branch_name: str
    commit_sha: str
    dir: str
    invert_regex: bool
    project_id: str
    repo_name: str
    substitutions: _containers.ScalarMap[str, str]
    tag_name: str
    def __init__(
        self,
        project_id: Optional[str] = ...,
        repo_name: Optional[str] = ...,
        branch_name: Optional[str] = ...,
        tag_name: Optional[str] = ...,
        commit_sha: Optional[str] = ...,
        dir: Optional[str] = ...,
        invert_regex: bool = ...,
        substitutions: Optional[Mapping[str, str]] = ...,
    ) -> None: ...

class Results(_message.Message):
    __slots__ = [
        "artifact_manifest",
        "artifact_timing",
        "build_step_images",
        "build_step_outputs",
        "images",
        "num_artifacts",
    ]
    ARTIFACT_MANIFEST_FIELD_NUMBER: ClassVar[int]
    ARTIFACT_TIMING_FIELD_NUMBER: ClassVar[int]
    BUILD_STEP_IMAGES_FIELD_NUMBER: ClassVar[int]
    BUILD_STEP_OUTPUTS_FIELD_NUMBER: ClassVar[int]
    IMAGES_FIELD_NUMBER: ClassVar[int]
    NUM_ARTIFACTS_FIELD_NUMBER: ClassVar[int]
    artifact_manifest: str
    artifact_timing: TimeSpan
    build_step_images: _containers.RepeatedScalarFieldContainer[str]
    build_step_outputs: _containers.RepeatedScalarFieldContainer[bytes]
    images: _containers.RepeatedCompositeFieldContainer[BuiltImage]
    num_artifacts: int
    def __init__(
        self,
        images: Optional[Iterable[Union[BuiltImage, Mapping]]] = ...,
        build_step_images: Optional[Iterable[str]] = ...,
        artifact_manifest: Optional[str] = ...,
        num_artifacts: Optional[int] = ...,
        build_step_outputs: Optional[Iterable[bytes]] = ...,
        artifact_timing: Optional[Union[TimeSpan, Mapping]] = ...,
    ) -> None: ...

class Secret(_message.Message):
    __slots__ = ["kms_key_name", "secret_env"]

    class SecretEnvEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: bytes
        def __init__(
            self, key: Optional[str] = ..., value: Optional[bytes] = ...
        ) -> None: ...
    KMS_KEY_NAME_FIELD_NUMBER: ClassVar[int]
    SECRET_ENV_FIELD_NUMBER: ClassVar[int]
    kms_key_name: str
    secret_env: _containers.ScalarMap[str, bytes]
    def __init__(
        self,
        kms_key_name: Optional[str] = ...,
        secret_env: Optional[Mapping[str, bytes]] = ...,
    ) -> None: ...

class Source(_message.Message):
    __slots__ = ["repo_source", "storage_source"]
    REPO_SOURCE_FIELD_NUMBER: ClassVar[int]
    STORAGE_SOURCE_FIELD_NUMBER: ClassVar[int]
    repo_source: RepoSource
    storage_source: StorageSource
    def __init__(
        self,
        storage_source: Optional[Union[StorageSource, Mapping]] = ...,
        repo_source: Optional[Union[RepoSource, Mapping]] = ...,
    ) -> None: ...

class SourceProvenance(_message.Message):
    __slots__ = ["file_hashes", "resolved_repo_source", "resolved_storage_source"]

    class FileHashesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: FileHashes
        def __init__(
            self,
            key: Optional[str] = ...,
            value: Optional[Union[FileHashes, Mapping]] = ...,
        ) -> None: ...
    FILE_HASHES_FIELD_NUMBER: ClassVar[int]
    RESOLVED_REPO_SOURCE_FIELD_NUMBER: ClassVar[int]
    RESOLVED_STORAGE_SOURCE_FIELD_NUMBER: ClassVar[int]
    file_hashes: _containers.MessageMap[str, FileHashes]
    resolved_repo_source: RepoSource
    resolved_storage_source: StorageSource
    def __init__(
        self,
        resolved_storage_source: Optional[Union[StorageSource, Mapping]] = ...,
        resolved_repo_source: Optional[Union[RepoSource, Mapping]] = ...,
        file_hashes: Optional[Mapping[str, FileHashes]] = ...,
    ) -> None: ...

class StorageSource(_message.Message):
    __slots__ = ["bucket", "generation", "object"]
    BUCKET_FIELD_NUMBER: ClassVar[int]
    GENERATION_FIELD_NUMBER: ClassVar[int]
    OBJECT_FIELD_NUMBER: ClassVar[int]
    bucket: str
    generation: int
    object: str
    def __init__(
        self,
        bucket: Optional[str] = ...,
        object: Optional[str] = ...,
        generation: Optional[int] = ...,
    ) -> None: ...

class TimeSpan(_message.Message):
    __slots__ = ["end_time", "start_time"]
    END_TIME_FIELD_NUMBER: ClassVar[int]
    START_TIME_FIELD_NUMBER: ClassVar[int]
    end_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        start_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
        end_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...,
    ) -> None: ...

class Volume(_message.Message):
    __slots__ = ["name", "path"]
    NAME_FIELD_NUMBER: ClassVar[int]
    PATH_FIELD_NUMBER: ClassVar[int]
    name: str
    path: str
    def __init__(
        self, name: Optional[str] = ..., path: Optional[str] = ...
    ) -> None: ...
