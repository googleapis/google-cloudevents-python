# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.events.cloud.cloudbuild.v1",
    manifest={
        "BuildEventData",
        "Source",
        "StorageSource",
        "RepoSource",
        "BuildStep",
        "Volume",
        "Results",
        "BuiltImage",
        "Artifacts",
        "TimeSpan",
        "SourceProvenance",
        "FileHashes",
        "Hash",
        "Secret",
        "BuildOptions",
    },
)


class BuildEventData(proto.Message):
    r"""Build event data for Google Cloud Platform API operations.

    Attributes:
        id (str):
            Unique identifier of the build.
        project_id (str):
            ID of the project.
        status (google.events.cloud.cloudbuild_v1.types.BuildEventData.Status):
            Status of the build.
        status_detail (str):
            Customer-readable message about the current
            status.
        source (google.events.cloud.cloudbuild_v1.types.Source):
            The location of the source files to build.
        steps (Sequence[google.events.cloud.cloudbuild_v1.types.BuildStep]):
            The operations to be performed on the
            workspace.
        results (google.events.cloud.cloudbuild_v1.types.Results):
            Results of the build.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time at which the request to create the build
            was received.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Time at which execution of the build was
            started.
        finish_time (google.protobuf.timestamp_pb2.Timestamp):
            Time at which execution of the build was finished.

            The difference between finish_time and start_time is the
            duration of the build's execution.
        timeout (google.protobuf.duration_pb2.Duration):
            Amount of time that this build should be allowed to run, to
            second granularity. If this amount of time elapses, work on
            the build will cease and the build status will be
            ``TIMEOUT``.
        images (Sequence[str]):
            A list of images to be pushed upon the successful completion
            of all build steps.

            The images are pushed using the builder service account's
            credentials.

            The digests of the pushed images will be stored in the
            ``Build`` resource's results field.

            If any of the images fail to be pushed, the build status is
            marked ``FAILURE``.
        queue_ttl (google.protobuf.duration_pb2.Duration):
            TTL in queue for this build. If provided and the build is
            enqueued longer than this value, the build will expire and
            the build status will be ``EXPIRED``.

            The TTL starts ticking from create_time.
        artifacts (google.events.cloud.cloudbuild_v1.types.Artifacts):
            Artifacts produced by the build that should
            be uploaded upon successful completion of all
            build steps.
        logs_bucket (str):
            Google Cloud Storage bucket where logs should be written
            (see `Bucket Name
            Requirements <https://cloud.google.com/storage/docs/bucket-naming#requirements>`__).
            Logs file names will be of the format
            ``${logs_bucket}/log-${build_id}.txt``.
        source_provenance (google.events.cloud.cloudbuild_v1.types.SourceProvenance):
            A permanent fixed identifier for source.
        build_trigger_id (str):
            The ID of the ``BuildTrigger`` that triggered this build, if
            it was triggered automatically.
        options (google.events.cloud.cloudbuild_v1.types.BuildOptions):
            Special options for this build.
        log_url (str):
            URL to logs for this build in Google Cloud
            Console.
        substitutions (Mapping[str, str]):
            Substitutions data for ``Build`` resource.
        tags (Sequence[str]):
            Tags for annotation of a ``Build``. These are not docker
            tags.
        secrets (Sequence[google.events.cloud.cloudbuild_v1.types.Secret]):
            Secrets to decrypt using Cloud Key Management
            Service.
        timing (Mapping[str, google.events.cloud.cloudbuild_v1.types.TimeSpan]):
            Stores timing information for phases of the build. Valid
            keys are:

            -  BUILD: time to execute all build steps
            -  PUSH: time to push all specified images.
            -  FETCHSOURCE: time to fetch source.

            If the build does not specify source or images, these keys
            will not be included.
    """

    class Status(proto.Enum):
        r"""Possible status of a build or build step."""
        STATUS_UNKNOWN = 0
        QUEUED = 1
        WORKING = 2
        SUCCESS = 3
        FAILURE = 4
        INTERNAL_ERROR = 5
        TIMEOUT = 6
        CANCELLED = 7
        EXPIRED = 9

    id = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id = proto.Field(
        proto.STRING,
        number=16,
    )
    status = proto.Field(
        proto.ENUM,
        number=2,
        enum=Status,
    )
    status_detail = proto.Field(
        proto.STRING,
        number=24,
    )
    source = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Source",
    )
    steps = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="BuildStep",
    )
    results = proto.Field(
        proto.MESSAGE,
        number=10,
        message="Results",
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    start_time = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    finish_time = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    timeout = proto.Field(
        proto.MESSAGE,
        number=12,
        message=duration_pb2.Duration,
    )
    images = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    queue_ttl = proto.Field(
        proto.MESSAGE,
        number=40,
        message=duration_pb2.Duration,
    )
    artifacts = proto.Field(
        proto.MESSAGE,
        number=37,
        message="Artifacts",
    )
    logs_bucket = proto.Field(
        proto.STRING,
        number=19,
    )
    source_provenance = proto.Field(
        proto.MESSAGE,
        number=21,
        message="SourceProvenance",
    )
    build_trigger_id = proto.Field(
        proto.STRING,
        number=22,
    )
    options = proto.Field(
        proto.MESSAGE,
        number=23,
        message="BuildOptions",
    )
    log_url = proto.Field(
        proto.STRING,
        number=25,
    )
    substitutions = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=29,
    )
    tags = proto.RepeatedField(
        proto.STRING,
        number=31,
    )
    secrets = proto.RepeatedField(
        proto.MESSAGE,
        number=32,
        message="Secret",
    )
    timing = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=33,
        message="TimeSpan",
    )


class Source(proto.Message):
    r"""

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        storage_source (google.events.cloud.cloudbuild_v1.types.StorageSource):
            If provided, get the source from this
            location in Google Cloud Storage.

            This field is a member of `oneof`_ ``source``.
        repo_source (google.events.cloud.cloudbuild_v1.types.RepoSource):
            If provided, get the source from this
            location in a Cloud Source Repository.

            This field is a member of `oneof`_ ``source``.
    """

    storage_source = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="StorageSource",
    )
    repo_source = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message="RepoSource",
    )


class StorageSource(proto.Message):
    r"""Location of the source in an archive file in Google Cloud
    Storage.

    Attributes:
        bucket (str):
            Google Cloud Storage bucket containing the source (see
            `Bucket Name
            Requirements <https://cloud.google.com/storage/docs/bucket-naming#requirements>`__).
        object_ (str):
            Google Cloud Storage object containing the
            source.
        generation (int):
            Google Cloud Storage generation for the
            object. If the generation is omitted, the latest
            generation will be used.
    """

    bucket = proto.Field(
        proto.STRING,
        number=1,
    )
    object_ = proto.Field(
        proto.STRING,
        number=2,
    )
    generation = proto.Field(
        proto.INT64,
        number=3,
    )


class RepoSource(proto.Message):
    r"""Location of the source in a Google Cloud Source Repository.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        project_id (str):
            ID of the project that owns the Cloud Source
            Repository.
        repo_name (str):
            Name of the Cloud Source Repository.
        branch_name (str):
            Regex matching branches to build.
            The syntax of the regular expressions accepted
            is the syntax accepted by RE2 and described at
            https://github.com/google/re2/wiki/Syntax

            This field is a member of `oneof`_ ``revision``.
        tag_name (str):
            Regex matching tags to build.
            The syntax of the regular expressions accepted
            is the syntax accepted by RE2 and described at
            https://github.com/google/re2/wiki/Syntax

            This field is a member of `oneof`_ ``revision``.
        commit_sha (str):
            Explicit commit SHA to build.

            This field is a member of `oneof`_ ``revision``.
        dir_ (str):
            Directory, relative to the source root, in which to run the
            build.

            This must be a relative path. If a step's ``dir`` is
            specified and is an absolute path, this value is ignored for
            that step's execution.
        invert_regex (bool):
            Only trigger a build if the revision regex
            does NOT match the revision regex.
        substitutions (Mapping[str, str]):
            Substitutions to use in a triggered build.
            Should only be used with RunBuildTrigger
    """

    project_id = proto.Field(
        proto.STRING,
        number=1,
    )
    repo_name = proto.Field(
        proto.STRING,
        number=2,
    )
    branch_name = proto.Field(
        proto.STRING,
        number=3,
        oneof="revision",
    )
    tag_name = proto.Field(
        proto.STRING,
        number=4,
        oneof="revision",
    )
    commit_sha = proto.Field(
        proto.STRING,
        number=5,
        oneof="revision",
    )
    dir_ = proto.Field(
        proto.STRING,
        number=7,
    )
    invert_regex = proto.Field(
        proto.BOOL,
        number=8,
    )
    substitutions = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )


class BuildStep(proto.Message):
    r"""A step in the build pipeline.

    Attributes:
        name (str):
            The name of the container image that will run this
            particular build step.

            If the image is available in the host's Docker daemon's
            cache, it will be run directly. If not, the host will
            attempt to pull the image first, using the builder service
            account's credentials if necessary.

            The Docker daemon's cache will already have the latest
            versions of all of the officially supported build steps
            (https://github.com/GoogleCloudPlatform/cloud-builders). The
            Docker daemon will also have cached many of the layers for
            some popular images, like "ubuntu", "debian", but they will
            be refreshed at the time you attempt to use them.

            If you built an image in a previous build step, it will be
            stored in the host's Docker daemon's cache and is available
            to use as the name for a later build step.
        env (Sequence[str]):
            A list of environment variable definitions to
            be used when running a step.
            The elements are of the form "KEY=VALUE" for the
            environment variable "KEY" being given the value
            "VALUE".
        args (Sequence[str]):
            A list of arguments that will be presented to the step when
            it is started.

            If the image used to run the step's container has an
            entrypoint, the ``args`` are used as arguments to that
            entrypoint. If the image does not define an entrypoint, the
            first element in args is used as the entrypoint, and the
            remainder will be used as arguments.
        dir_ (str):
            Working directory to use when running this step's container.

            If this value is a relative path, it is relative to the
            build's working directory. If this value is absolute, it may
            be outside the build's working directory, in which case the
            contents of the path may not be persisted across build step
            executions, unless a ``volume`` for that path is specified.

            If the build specifies a ``RepoSource`` with ``dir`` and a
            step with a ``dir``, which specifies an absolute path, the
            ``RepoSource`` ``dir`` is ignored for the step's execution.
        id (str):
            Unique identifier for this build step, used in ``wait_for``
            to reference this build step as a dependency.
        wait_for (Sequence[str]):
            The ID(s) of the step(s) that this build step depends on.
            This build step will not start until all the build steps in
            ``wait_for`` have completed successfully. If ``wait_for`` is
            empty, this build step will start when all previous build
            steps in the ``Build.Steps`` list have completed
            successfully.
        entrypoint (str):
            Entrypoint to be used instead of the build
            step image's default entrypoint. If unset, the
            image's default entrypoint is used.
        secret_env (Sequence[str]):
            A list of environment variables which are encrypted using a
            Cloud Key Management Service crypto key. These values must
            be specified in the build's ``Secret``.
        volumes (Sequence[google.events.cloud.cloudbuild_v1.types.Volume]):
            List of volumes to mount into the build step.
            Each volume is created as an empty volume prior
            to execution of the build step. Upon completion
            of the build, volumes and their contents are
            discarded.

            Using a named volume in only one step is not
            valid as it is indicative of a build request
            with an incorrect configuration.
        timing (google.events.cloud.cloudbuild_v1.types.TimeSpan):
            Stores timing information for executing this
            build step.
        pull_timing (google.events.cloud.cloudbuild_v1.types.TimeSpan):
            Stores timing information for pulling this
            build step's builder image only.
        timeout (google.protobuf.duration_pb2.Duration):
            Time limit for executing this build step. If
            not defined, the step has no time limit and will
            be allowed to continue to run until either it
            completes or the build itself times out.
        status (google.events.cloud.cloudbuild_v1.types.BuildEventData.Status):
            Status of the build step. At this time, build
            step status is only updated on build completion;
            step status is not updated in real-time as the
            build progresses.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    env = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    args = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    dir_ = proto.Field(
        proto.STRING,
        number=4,
    )
    id = proto.Field(
        proto.STRING,
        number=5,
    )
    wait_for = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    entrypoint = proto.Field(
        proto.STRING,
        number=7,
    )
    secret_env = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    volumes = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Volume",
    )
    timing = proto.Field(
        proto.MESSAGE,
        number=10,
        message="TimeSpan",
    )
    pull_timing = proto.Field(
        proto.MESSAGE,
        number=13,
        message="TimeSpan",
    )
    timeout = proto.Field(
        proto.MESSAGE,
        number=11,
        message=duration_pb2.Duration,
    )
    status = proto.Field(
        proto.ENUM,
        number=12,
        enum="BuildEventData.Status",
    )


class Volume(proto.Message):
    r"""Volume describes a Docker container volume which is mounted
    into build steps in order to persist files across build step
    execution.

    Attributes:
        name (str):
            Name of the volume to mount.
            Volume names must be unique per build step and
            must be valid names for Docker volumes. Each
            named volume must be used by at least two build
            steps.
        path (str):
            Path at which to mount the volume.
            Paths must be absolute and cannot conflict with
            other volume paths on the same build step or
            with certain reserved volume paths.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    path = proto.Field(
        proto.STRING,
        number=2,
    )


class Results(proto.Message):
    r"""Artifacts created by the build pipeline.

    Attributes:
        images (Sequence[google.events.cloud.cloudbuild_v1.types.BuiltImage]):
            Container images that were built as a part of
            the build.
        build_step_images (Sequence[str]):
            List of build step digests, in the order
            corresponding to build step indices.
        artifact_manifest (str):
            Path to the artifact manifest. Only populated
            when artifacts are uploaded.
        num_artifacts (int):
            Number of artifacts uploaded. Only populated
            when artifacts are uploaded.
        build_step_outputs (Sequence[bytes]):
            List of build step outputs, produced by builder images, in
            the order corresponding to build step indices.

            `Cloud
            Builders <https://cloud.google.com/cloud-build/docs/cloud-builders>`__
            can produce this output by writing to
            ``$BUILDER_OUTPUT/output``. Only the first 4KB of data is
            stored.
        artifact_timing (google.events.cloud.cloudbuild_v1.types.TimeSpan):
            Time to push all non-container artifacts.
    """

    images = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="BuiltImage",
    )
    build_step_images = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    artifact_manifest = proto.Field(
        proto.STRING,
        number=4,
    )
    num_artifacts = proto.Field(
        proto.INT64,
        number=5,
    )
    build_step_outputs = proto.RepeatedField(
        proto.BYTES,
        number=6,
    )
    artifact_timing = proto.Field(
        proto.MESSAGE,
        number=7,
        message="TimeSpan",
    )


class BuiltImage(proto.Message):
    r"""An image built by the pipeline.

    Attributes:
        name (str):
            Name used to push the container image to Google Container
            Registry, as presented to ``docker push``.
        digest (str):
            Docker Registry 2.0 digest.
        push_timing (google.events.cloud.cloudbuild_v1.types.TimeSpan):
            Stores timing information for pushing the
            specified image.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    digest = proto.Field(
        proto.STRING,
        number=3,
    )
    push_timing = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TimeSpan",
    )


class Artifacts(proto.Message):
    r"""Artifacts produced by a build that should be uploaded upon
    successful completion of all build steps.

    Attributes:
        images (Sequence[str]):
            A list of images to be pushed upon the
            successful completion of all build steps.

            The images will be pushed using the builder
            service account's credentials.
            The digests of the pushed images will be stored
            in the Build resource's results field.

            If any of the images fail to be pushed, the
            build is marked FAILURE.
        objects (google.events.cloud.cloudbuild_v1.types.Artifacts.ArtifactObjects):
            A list of objects to be uploaded to Cloud
            Storage upon successful completion of all build
            steps.
            Files in the workspace matching specified paths
            globs will be uploaded to the specified Cloud
            Storage location using the builder service
            account's credentials.

            The location and generation of the uploaded
            objects will be stored in the Build resource's
            results field.

            If any objects fail to be pushed, the build is
            marked FAILURE.
    """

    class ArtifactObjects(proto.Message):
        r"""Files in the workspace to upload to Cloud Storage upon
        successful completion of all build steps.

        Attributes:
            location (str):
                Cloud Storage bucket and optional object path, in the form
                "gs://bucket/path/to/somewhere/". (see `Bucket Name
                Requirements <https://cloud.google.com/storage/docs/bucket-naming#requirements>`__).

                Files in the workspace matching any path pattern will be
                uploaded to Cloud Storage with this location as a prefix.
            paths (Sequence[str]):
                Path globs used to match files in the build's
                workspace.
            timing (google.events.cloud.cloudbuild_v1.types.TimeSpan):
                Stores timing information for pushing all
                artifact objects.
        """

        location = proto.Field(
            proto.STRING,
            number=1,
        )
        paths = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        timing = proto.Field(
            proto.MESSAGE,
            number=3,
            message="TimeSpan",
        )

    images = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    objects = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ArtifactObjects,
    )


class TimeSpan(proto.Message):
    r"""Start and end times for a build execution phase.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start of time span.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End of time span.
    """

    start_time = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class SourceProvenance(proto.Message):
    r"""Provenance of the source. Ways to find the original source,
    or verify that some source was used for this build.

    Attributes:
        resolved_storage_source (google.events.cloud.cloudbuild_v1.types.StorageSource):
            A copy of the build's ``source.storage_source``, if exists,
            with any generations resolved.
        resolved_repo_source (google.events.cloud.cloudbuild_v1.types.RepoSource):
            A copy of the build's ``source.repo_source``, if exists,
            with any revisions resolved.
        file_hashes (Mapping[str, google.events.cloud.cloudbuild_v1.types.FileHashes]):
            Hash(es) of the build source, which can be used to verify
            that the original source integrity was maintained in the
            build. Note that ``FileHashes`` will only be populated if
            ``BuildOptions`` has requested a ``SourceProvenanceHash``.

            The keys to this map are file paths used as build source and
            the values contain the hash values for those files.

            If the build source came in a single package such as a
            gzipped tarfile (``.tar.gz``), the ``FileHash`` will be for
            the single path to that file.
    """

    resolved_storage_source = proto.Field(
        proto.MESSAGE,
        number=3,
        message="StorageSource",
    )
    resolved_repo_source = proto.Field(
        proto.MESSAGE,
        number=6,
        message="RepoSource",
    )
    file_hashes = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=4,
        message="FileHashes",
    )


class FileHashes(proto.Message):
    r"""Container message for hashes of byte content of files, used
    in SourceProvenance messages to verify integrity of source input
    to the build.

    Attributes:
        file_hash (Sequence[google.events.cloud.cloudbuild_v1.types.Hash]):
            Collection of file hashes.
    """

    file_hash = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Hash",
    )


class Hash(proto.Message):
    r"""Container message for hash values.

    Attributes:
        type_ (google.events.cloud.cloudbuild_v1.types.Hash.HashType):
            The type of hash that was performed.
        value (bytes):
            The hash value.
    """

    class HashType(proto.Enum):
        r"""Specifies the hash algorithm, if any."""
        NONE = 0
        SHA256 = 1
        MD5 = 2

    type_ = proto.Field(
        proto.ENUM,
        number=1,
        enum=HashType,
    )
    value = proto.Field(
        proto.BYTES,
        number=2,
    )


class Secret(proto.Message):
    r"""Pairs a set of secret environment variables containing
    encrypted values with the Cloud KMS key to use to decrypt the
    value.

    Attributes:
        kms_key_name (str):
            Cloud KMS key name to use to decrypt these
            envs.
        secret_env (Mapping[str, bytes]):
            Map of environment variable name to its
            encrypted value.
            Secret environment variables must be unique
            across all of a build's secrets, and must be
            used by at least one build step. Values can be
            at most 64 KB in size. There can be at most 100
            secret values across all of a build's secrets.
    """

    kms_key_name = proto.Field(
        proto.STRING,
        number=1,
    )
    secret_env = proto.MapField(
        proto.STRING,
        proto.BYTES,
        number=3,
    )


class BuildOptions(proto.Message):
    r"""Optional arguments to enable specific features of builds.

    Attributes:
        source_provenance_hash (Sequence[google.events.cloud.cloudbuild_v1.types.Hash.HashType]):
            Requested hash for SourceProvenance.
        requested_verify_option (google.events.cloud.cloudbuild_v1.types.BuildOptions.VerifyOption):
            Requested verifiability options.
        machine_type (google.events.cloud.cloudbuild_v1.types.BuildOptions.MachineType):
            Compute Engine machine type on which to run
            the build.
        disk_size_gb (int):
            Requested disk size for the VM that runs the build. Note
            that this is *NOT* "disk free"; some of the space will be
            used by the operating system and build utilities. Also note
            that this is the minimum disk size that will be allocated
            for the build -- the build may run with a larger disk than
            requested. At present, the maximum disk size is 1000GB;
            builds that request more than the maximum are rejected with
            an error.
        substitution_option (google.events.cloud.cloudbuild_v1.types.BuildOptions.SubstitutionOption):
            Option to specify behavior when there is an
            error in the substitution checks.
        log_streaming_option (google.events.cloud.cloudbuild_v1.types.BuildOptions.LogStreamingOption):
            Option to define build log streaming behavior
            to Google Cloud Storage.
        worker_pool (str):
            Option to specify a ``WorkerPool`` for the build. Format:
            projects/{project}/locations/{location}/workerPools/{workerPool}
        logging (google.events.cloud.cloudbuild_v1.types.BuildOptions.LoggingMode):
            Option to specify the logging mode, which
            determines where the logs are stored.
        env (Sequence[str]):
            A list of global environment variable
            definitions that will exist for all build steps
            in this build. If a variable is defined in both
            globally and in a build step, the variable will
            use the build step value.
            The elements are of the form "KEY=VALUE" for the
            environment variable "KEY" being given the value
            "VALUE".
        secret_env (Sequence[str]):
            A list of global environment variables, which are encrypted
            using a Cloud Key Management Service crypto key. These
            values must be specified in the build's ``Secret``. These
            variables will be available to all build steps in this
            build.
        volumes (Sequence[google.events.cloud.cloudbuild_v1.types.Volume]):
            Global list of volumes to mount for ALL build
            steps
            Each volume is created as an empty volume prior
            to starting the build process. Upon completion
            of the build, volumes and their contents are
            discarded. Global volume names and paths cannot
            conflict with the volumes defined a build step.

            Using a global volume in a build with only one
            step is not valid as it is indicative of a build
            request with an incorrect configuration.
    """

    class VerifyOption(proto.Enum):
        r"""Specifies the manner in which the build should be verified,
        if at all.
        """
        NOT_VERIFIED = 0
        VERIFIED = 1

    class MachineType(proto.Enum):
        r"""Supported VM sizes."""
        UNSPECIFIED = 0
        N1_HIGHCPU_8 = 1
        N1_HIGHCPU_32 = 2

    class SubstitutionOption(proto.Enum):
        r"""Specifies the behavior when there is an error in the
        substitution checks.
        """
        MUST_MATCH = 0
        ALLOW_LOOSE = 1

    class LogStreamingOption(proto.Enum):
        r"""Specifies the behavior when writing build logs to Google
        Cloud Storage.
        """
        STREAM_DEFAULT = 0
        STREAM_ON = 1
        STREAM_OFF = 2

    class LoggingMode(proto.Enum):
        r"""Specifies the logging mode."""
        LOGGING_UNSPECIFIED = 0
        LEGACY = 1
        GCS_ONLY = 2

    source_provenance_hash = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum="Hash.HashType",
    )
    requested_verify_option = proto.Field(
        proto.ENUM,
        number=2,
        enum=VerifyOption,
    )
    machine_type = proto.Field(
        proto.ENUM,
        number=3,
        enum=MachineType,
    )
    disk_size_gb = proto.Field(
        proto.INT64,
        number=6,
    )
    substitution_option = proto.Field(
        proto.ENUM,
        number=4,
        enum=SubstitutionOption,
    )
    log_streaming_option = proto.Field(
        proto.ENUM,
        number=5,
        enum=LogStreamingOption,
    )
    worker_pool = proto.Field(
        proto.STRING,
        number=7,
    )
    logging = proto.Field(
        proto.ENUM,
        number=11,
        enum=LoggingMode,
    )
    env = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    secret_env = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    volumes = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="Volume",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
