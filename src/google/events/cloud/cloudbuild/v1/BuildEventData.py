# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = build_event_data_from_dict(json.loads(json_string))

from typing import Optional, Any, List, Union, Dict, TypeVar, Callable, Type, cast
from datetime import datetime
from enum import Enum
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class ObjectsTiming:
    """Stores timing information for pushing all artifact objects.
    
    Start and end times for a build execution phase.
    """
    """End of time span."""
    end_time: Optional[datetime]
    """Start of time span."""
    start_time: Optional[datetime]

    def __init__(self, end_time: Optional[datetime], start_time: Optional[datetime]) -> None:
        self.end_time = end_time
        self.start_time = start_time

    @staticmethod
    def from_dict(obj: Any) -> 'ObjectsTiming':
        assert isinstance(obj, dict)
        end_time = from_union([from_datetime, from_none], obj.get("endTime"))
        start_time = from_union([from_datetime, from_none], obj.get("startTime"))
        return ObjectsTiming(end_time, start_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["endTime"] = from_union([lambda x: x.isoformat(), from_none], self.end_time)
        result["startTime"] = from_union([lambda x: x.isoformat(), from_none], self.start_time)
        return result


class Objects:
    """A list of objects to be uploaded to Cloud Storage upon successful
    completion of all build steps.
    
    Files in the workspace matching specified paths globs will be uploaded to
    the specified Cloud Storage location using the builder service account's
    credentials.
    
    The location and generation of the uploaded objects will be stored in the
    Build resource's results field.
    
    If any objects fail to be pushed, the build is marked FAILURE.
    """
    """Cloud Storage bucket and optional object path, in the form
    "gs://bucket/path/to/somewhere/". (see [Bucket Name
    Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)).
    
    Files in the workspace matching any path pattern will be uploaded to
    Cloud Storage with this location as a prefix.
    """
    location: Optional[str]
    """Path globs used to match files in the build's workspace."""
    paths: Optional[List[str]]
    """Stores timing information for pushing all artifact objects."""
    timing: Optional[ObjectsTiming]

    def __init__(self, location: Optional[str], paths: Optional[List[str]], timing: Optional[ObjectsTiming]) -> None:
        self.location = location
        self.paths = paths
        self.timing = timing

    @staticmethod
    def from_dict(obj: Any) -> 'Objects':
        assert isinstance(obj, dict)
        location = from_union([from_str, from_none], obj.get("location"))
        paths = from_union([lambda x: from_list(from_str, x), from_none], obj.get("paths"))
        timing = from_union([ObjectsTiming.from_dict, from_none], obj.get("timing"))
        return Objects(location, paths, timing)

    def to_dict(self) -> dict:
        result: dict = {}
        result["location"] = from_union([from_str, from_none], self.location)
        result["paths"] = from_union([lambda x: from_list(from_str, x), from_none], self.paths)
        result["timing"] = from_union([lambda x: to_class(ObjectsTiming, x), from_none], self.timing)
        return result


class Artifacts:
    """Artifacts produced by the build that should be uploaded upon
    successful completion of all build steps.
    """
    """A list of images to be pushed upon the successful completion of all build
    steps.
    
    The images will be pushed using the builder service account's credentials.
    
    The digests of the pushed images will be stored in the Build resource's
    results field.
    
    If any of the images fail to be pushed, the build is marked FAILURE.
    """
    images: Optional[List[str]]
    """A list of objects to be uploaded to Cloud Storage upon successful
    completion of all build steps.
    
    Files in the workspace matching specified paths globs will be uploaded to
    the specified Cloud Storage location using the builder service account's
    credentials.
    
    The location and generation of the uploaded objects will be stored in the
    Build resource's results field.
    
    If any objects fail to be pushed, the build is marked FAILURE.
    """
    objects: Optional[Objects]

    def __init__(self, images: Optional[List[str]], objects: Optional[Objects]) -> None:
        self.images = images
        self.objects = objects

    @staticmethod
    def from_dict(obj: Any) -> 'Artifacts':
        assert isinstance(obj, dict)
        images = from_union([lambda x: from_list(from_str, x), from_none], obj.get("images"))
        objects = from_union([Objects.from_dict, from_none], obj.get("objects"))
        return Artifacts(images, objects)

    def to_dict(self) -> dict:
        result: dict = {}
        result["images"] = from_union([lambda x: from_list(from_str, x), from_none], self.images)
        result["objects"] = from_union([lambda x: to_class(Objects, x), from_none], self.objects)
        return result


class LogStreamingOptionEnum(Enum):
    STREAM_DEFAULT = "STREAM_DEFAULT"
    STREAM_OFF = "STREAM_OFF"
    STREAM_ON = "STREAM_ON"


class LoggingEnum(Enum):
    GCS_ONLY = "GCS_ONLY"
    LEGACY = "LEGACY"
    LOGGING_UNSPECIFIED = "LOGGING_UNSPECIFIED"


class MachineTypeEnum(Enum):
    N1_HIGHCPU_32 = "N1_HIGHCPU_32"
    N1_HIGHCPU_8 = "N1_HIGHCPU_8"
    UNSPECIFIED = "UNSPECIFIED"


class RequestedVerifyOptionEnum(Enum):
    NOT_VERIFIED = "NOT_VERIFIED"
    VERIFIED = "VERIFIED"


class SubstitutionOptionEnum(Enum):
    ALLOW_LOOSE = "ALLOW_LOOSE"
    MUST_MATCH = "MUST_MATCH"


class Volume:
    """Volume describes a Docker container volume which is mounted into build steps
    in order to persist files across build step execution.
    """
    """Name of the volume to mount.
    
    Volume names must be unique per build step and must be valid names for
    Docker volumes. Each named volume must be used by at least two build steps.
    """
    name: Optional[str]
    """Path at which to mount the volume.
    
    Paths must be absolute and cannot conflict with other volume paths on the
    same build step or with certain reserved volume paths.
    """
    path: Optional[str]

    def __init__(self, name: Optional[str], path: Optional[str]) -> None:
        self.name = name
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'Volume':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        path = from_union([from_str, from_none], obj.get("path"))
        return Volume(name, path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["path"] = from_union([from_str, from_none], self.path)
        return result


class Options:
    """Special options for this build."""
    """Requested disk size for the VM that runs the build. Note that this is *NOT*
    "disk free"; some of the space will be used by the operating system and
    build utilities. Also note that this is the minimum disk size that will be
    allocated for the build -- the build may run with a larger disk than
    requested. At present, the maximum disk size is 1000GB; builds that request
    more than the maximum are rejected with an error.
    """
    disk_size_gb: Optional[str]
    """A list of global environment variable definitions that will exist for all
    build steps in this build. If a variable is defined in both globally and in
    a build step, the variable will use the build step value.
    
    The elements are of the form "KEY=VALUE" for the environment variable "KEY"
    being given the value "VALUE".
    """
    env: Optional[List[str]]
    """Option to specify the logging mode, which determines where the logs are
    stored.
    """
    logging: Union[LoggingEnum, int, None]
    """Option to define build log streaming behavior to Google Cloud
    Storage.
    """
    log_streaming_option: Union[LogStreamingOptionEnum, int, None]
    """Compute Engine machine type on which to run the build."""
    machine_type: Union[MachineTypeEnum, int, None]
    """Requested verifiability options."""
    requested_verify_option: Union[RequestedVerifyOptionEnum, int, None]
    """A list of global environment variables, which are encrypted using a Cloud
    Key Management Service crypto key. These values must be specified in the
    build's `Secret`. These variables will be available to all build steps
    in this build.
    """
    secret_env: Optional[List[str]]
    """Requested hash for SourceProvenance."""
    source_provenance_hash: Optional[List[Union[int, str]]]
    """Option to specify behavior when there is an error in the substitution
    checks.
    """
    substitution_option: Union[SubstitutionOptionEnum, int, None]
    """Global list of volumes to mount for ALL build steps
    
    Each volume is created as an empty volume prior to starting the build
    process. Upon completion of the build, volumes and their contents are
    discarded. Global volume names and paths cannot conflict with the volumes
    defined a build step.
    
    Using a global volume in a build with only one step is not valid as
    it is indicative of a build request with an incorrect configuration.
    """
    volumes: Optional[List[Volume]]
    """Option to specify a `WorkerPool` for the build.
    Format: projects/{project}/locations/{location}/workerPools/{workerPool}
    """
    worker_pool: Optional[str]

    def __init__(self, disk_size_gb: Optional[str], env: Optional[List[str]], logging: Union[LoggingEnum, int, None], log_streaming_option: Union[LogStreamingOptionEnum, int, None], machine_type: Union[MachineTypeEnum, int, None], requested_verify_option: Union[RequestedVerifyOptionEnum, int, None], secret_env: Optional[List[str]], source_provenance_hash: Optional[List[Union[int, str]]], substitution_option: Union[SubstitutionOptionEnum, int, None], volumes: Optional[List[Volume]], worker_pool: Optional[str]) -> None:
        self.disk_size_gb = disk_size_gb
        self.env = env
        self.logging = logging
        self.log_streaming_option = log_streaming_option
        self.machine_type = machine_type
        self.requested_verify_option = requested_verify_option
        self.secret_env = secret_env
        self.source_provenance_hash = source_provenance_hash
        self.substitution_option = substitution_option
        self.volumes = volumes
        self.worker_pool = worker_pool

    @staticmethod
    def from_dict(obj: Any) -> 'Options':
        assert isinstance(obj, dict)
        disk_size_gb = from_union([from_str, from_none], obj.get("diskSizeGb"))
        env = from_union([lambda x: from_list(from_str, x), from_none], obj.get("env"))
        logging = from_union([from_int, LoggingEnum, from_none], obj.get("logging"))
        log_streaming_option = from_union([from_int, LogStreamingOptionEnum, from_none], obj.get("logStreamingOption"))
        machine_type = from_union([from_int, MachineTypeEnum, from_none], obj.get("machineType"))
        requested_verify_option = from_union([from_int, RequestedVerifyOptionEnum, from_none], obj.get("requestedVerifyOption"))
        secret_env = from_union([lambda x: from_list(from_str, x), from_none], obj.get("secretEnv"))
        source_provenance_hash = from_union([lambda x: from_list(lambda x: from_union([from_int, from_str], x), x), from_none], obj.get("sourceProvenanceHash"))
        substitution_option = from_union([from_int, SubstitutionOptionEnum, from_none], obj.get("substitutionOption"))
        volumes = from_union([lambda x: from_list(Volume.from_dict, x), from_none], obj.get("volumes"))
        worker_pool = from_union([from_str, from_none], obj.get("workerPool"))
        return Options(disk_size_gb, env, logging, log_streaming_option, machine_type, requested_verify_option, secret_env, source_provenance_hash, substitution_option, volumes, worker_pool)

    def to_dict(self) -> dict:
        result: dict = {}
        result["diskSizeGb"] = from_union([from_str, from_none], self.disk_size_gb)
        result["env"] = from_union([lambda x: from_list(from_str, x), from_none], self.env)
        result["logging"] = from_union([from_int, lambda x: to_enum(LoggingEnum, x), from_none], self.logging)
        result["logStreamingOption"] = from_union([from_int, lambda x: to_enum(LogStreamingOptionEnum, x), from_none], self.log_streaming_option)
        result["machineType"] = from_union([from_int, lambda x: to_enum(MachineTypeEnum, x), from_none], self.machine_type)
        result["requestedVerifyOption"] = from_union([from_int, lambda x: to_enum(RequestedVerifyOptionEnum, x), from_none], self.requested_verify_option)
        result["secretEnv"] = from_union([lambda x: from_list(from_str, x), from_none], self.secret_env)
        result["sourceProvenanceHash"] = from_union([lambda x: from_list(lambda x: from_union([from_int, from_str], x), x), from_none], self.source_provenance_hash)
        result["substitutionOption"] = from_union([from_int, lambda x: to_enum(SubstitutionOptionEnum, x), from_none], self.substitution_option)
        result["volumes"] = from_union([lambda x: from_list(lambda x: to_class(Volume, x), x), from_none], self.volumes)
        result["workerPool"] = from_union([from_str, from_none], self.worker_pool)
        return result


class QueueTTL:
    """TTL in queue for this build. If provided and the build is enqueued longer
    than this value, the build will expire and the build status will be
    `EXPIRED`.
    
    The TTL starts ticking from create_time.
    """
    """Signed fractions of a second at nanosecond resolution of the span
    of time. Durations less than one second are represented with a 0
    `seconds` field and a positive or negative `nanos` field. For durations
    of one second or more, a non-zero value for the `nanos` field must be
    of the same sign as the `seconds` field. Must be from -999,999,999
    to +999,999,999 inclusive.
    """
    nanos: Optional[int]
    """Signed seconds of the span of time. Must be from -315,576,000,000
    to +315,576,000,000 inclusive. Note: these bounds are computed from:
    60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years
    """
    seconds: Optional[str]

    def __init__(self, nanos: Optional[int], seconds: Optional[str]) -> None:
        self.nanos = nanos
        self.seconds = seconds

    @staticmethod
    def from_dict(obj: Any) -> 'QueueTTL':
        assert isinstance(obj, dict)
        nanos = from_union([from_int, from_none], obj.get("nanos"))
        seconds = from_union([from_str, from_none], obj.get("seconds"))
        return QueueTTL(nanos, seconds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nanos"] = from_union([from_int, from_none], self.nanos)
        result["seconds"] = from_union([from_str, from_none], self.seconds)
        return result


class ArtifactTiming:
    """Time to push all non-container artifacts.
    
    Stores timing information for pushing all artifact objects.
    
    Start and end times for a build execution phase.
    """
    """End of time span."""
    end_time: Optional[datetime]
    """Start of time span."""
    start_time: Optional[datetime]

    def __init__(self, end_time: Optional[datetime], start_time: Optional[datetime]) -> None:
        self.end_time = end_time
        self.start_time = start_time

    @staticmethod
    def from_dict(obj: Any) -> 'ArtifactTiming':
        assert isinstance(obj, dict)
        end_time = from_union([from_datetime, from_none], obj.get("endTime"))
        start_time = from_union([from_datetime, from_none], obj.get("startTime"))
        return ArtifactTiming(end_time, start_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["endTime"] = from_union([lambda x: x.isoformat(), from_none], self.end_time)
        result["startTime"] = from_union([lambda x: x.isoformat(), from_none], self.start_time)
        return result


class PushTiming:
    """Stores timing information for pushing the specified image.
    
    Stores timing information for pushing all artifact objects.
    
    Start and end times for a build execution phase.
    """
    """End of time span."""
    end_time: Optional[datetime]
    """Start of time span."""
    start_time: Optional[datetime]

    def __init__(self, end_time: Optional[datetime], start_time: Optional[datetime]) -> None:
        self.end_time = end_time
        self.start_time = start_time

    @staticmethod
    def from_dict(obj: Any) -> 'PushTiming':
        assert isinstance(obj, dict)
        end_time = from_union([from_datetime, from_none], obj.get("endTime"))
        start_time = from_union([from_datetime, from_none], obj.get("startTime"))
        return PushTiming(end_time, start_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["endTime"] = from_union([lambda x: x.isoformat(), from_none], self.end_time)
        result["startTime"] = from_union([lambda x: x.isoformat(), from_none], self.start_time)
        return result


class Image:
    """An image built by the pipeline."""
    """Docker Registry 2.0 digest."""
    digest: Optional[str]
    """Name used to push the container image to Google Container Registry, as
    presented to `docker push`.
    """
    name: Optional[str]
    """Stores timing information for pushing the specified image."""
    push_timing: Optional[PushTiming]

    def __init__(self, digest: Optional[str], name: Optional[str], push_timing: Optional[PushTiming]) -> None:
        self.digest = digest
        self.name = name
        self.push_timing = push_timing

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        digest = from_union([from_str, from_none], obj.get("digest"))
        name = from_union([from_str, from_none], obj.get("name"))
        push_timing = from_union([PushTiming.from_dict, from_none], obj.get("pushTiming"))
        return Image(digest, name, push_timing)

    def to_dict(self) -> dict:
        result: dict = {}
        result["digest"] = from_union([from_str, from_none], self.digest)
        result["name"] = from_union([from_str, from_none], self.name)
        result["pushTiming"] = from_union([lambda x: to_class(PushTiming, x), from_none], self.push_timing)
        return result


class Results:
    """Results of the build."""
    """Path to the artifact manifest. Only populated when artifacts are uploaded."""
    artifact_manifest: Optional[str]
    """Time to push all non-container artifacts."""
    artifact_timing: Optional[ArtifactTiming]
    """List of build step digests, in the order corresponding to build step
    indices.
    """
    build_step_images: Optional[List[str]]
    """List of build step outputs, produced by builder images, in the order
    corresponding to build step indices.
    
    [Cloud Builders](https://cloud.google.com/cloud-build/docs/cloud-builders)
    can produce this output by writing to `$BUILDER_OUTPUT/output`.
    Only the first 4KB of data is stored.
    """
    build_step_outputs: Optional[List[str]]
    """Container images that were built as a part of the build."""
    images: Optional[List[Image]]
    """Number of artifacts uploaded. Only populated when artifacts are uploaded."""
    num_artifacts: Optional[str]

    def __init__(self, artifact_manifest: Optional[str], artifact_timing: Optional[ArtifactTiming], build_step_images: Optional[List[str]], build_step_outputs: Optional[List[str]], images: Optional[List[Image]], num_artifacts: Optional[str]) -> None:
        self.artifact_manifest = artifact_manifest
        self.artifact_timing = artifact_timing
        self.build_step_images = build_step_images
        self.build_step_outputs = build_step_outputs
        self.images = images
        self.num_artifacts = num_artifacts

    @staticmethod
    def from_dict(obj: Any) -> 'Results':
        assert isinstance(obj, dict)
        artifact_manifest = from_union([from_str, from_none], obj.get("artifactManifest"))
        artifact_timing = from_union([ArtifactTiming.from_dict, from_none], obj.get("artifactTiming"))
        build_step_images = from_union([lambda x: from_list(from_str, x), from_none], obj.get("buildStepImages"))
        build_step_outputs = from_union([lambda x: from_list(from_str, x), from_none], obj.get("buildStepOutputs"))
        images = from_union([lambda x: from_list(Image.from_dict, x), from_none], obj.get("images"))
        num_artifacts = from_union([from_str, from_none], obj.get("numArtifacts"))
        return Results(artifact_manifest, artifact_timing, build_step_images, build_step_outputs, images, num_artifacts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["artifactManifest"] = from_union([from_str, from_none], self.artifact_manifest)
        result["artifactTiming"] = from_union([lambda x: to_class(ArtifactTiming, x), from_none], self.artifact_timing)
        result["buildStepImages"] = from_union([lambda x: from_list(from_str, x), from_none], self.build_step_images)
        result["buildStepOutputs"] = from_union([lambda x: from_list(from_str, x), from_none], self.build_step_outputs)
        result["images"] = from_union([lambda x: from_list(lambda x: to_class(Image, x), x), from_none], self.images)
        result["numArtifacts"] = from_union([from_str, from_none], self.num_artifacts)
        return result


class Secret:
    """Pairs a set of secret environment variables containing encrypted
    values with the Cloud KMS key to use to decrypt the value.
    """
    """Cloud KMS key name to use to decrypt these envs."""
    kms_key_name: Optional[str]
    """Map of environment variable name to its encrypted value.
    
    Secret environment variables must be unique across all of a build's
    secrets, and must be used by at least one build step. Values can be at most
    64 KB in size. There can be at most 100 secret values across all of a
    build's secrets.
    """
    secret_env: Optional[Dict[str, str]]

    def __init__(self, kms_key_name: Optional[str], secret_env: Optional[Dict[str, str]]) -> None:
        self.kms_key_name = kms_key_name
        self.secret_env = secret_env

    @staticmethod
    def from_dict(obj: Any) -> 'Secret':
        assert isinstance(obj, dict)
        kms_key_name = from_union([from_str, from_none], obj.get("kmsKeyName"))
        secret_env = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("secretEnv"))
        return Secret(kms_key_name, secret_env)

    def to_dict(self) -> dict:
        result: dict = {}
        result["kmsKeyName"] = from_union([from_str, from_none], self.kms_key_name)
        result["secretEnv"] = from_union([lambda x: from_dict(from_str, x), from_none], self.secret_env)
        return result


class RepoSourceClass:
    """If provided, get the source from this location in a Cloud Source
    Repository.
    
    Location of the source in a Google Cloud Source Repository.
    """
    """Regex matching branches to build.
    
    The syntax of the regular expressions accepted is the syntax accepted by
    RE2 and described at https://github.com/google/re2/wiki/Syntax
    """
    branch_name: Optional[str]
    """Explicit commit SHA to build."""
    commit_sha: Optional[str]
    """Directory, relative to the source root, in which to run the build.
    
    This must be a relative path. If a step's `dir` is specified and is an
    absolute path, this value is ignored for that step's execution.
    """
    dir: Optional[str]
    """Only trigger a build if the revision regex does NOT match the revision
    regex.
    """
    invert_regex: Optional[bool]
    """ID of the project that owns the Cloud Source Repository."""
    project_id: Optional[str]
    """Name of the Cloud Source Repository."""
    repo_name: Optional[str]
    """Substitutions to use in a triggered build.
    Should only be used with RunBuildTrigger
    """
    substitutions: Optional[Dict[str, str]]
    """Regex matching tags to build.
    
    The syntax of the regular expressions accepted is the syntax accepted by
    RE2 and described at https://github.com/google/re2/wiki/Syntax
    """
    tag_name: Optional[str]

    def __init__(self, branch_name: Optional[str], commit_sha: Optional[str], dir: Optional[str], invert_regex: Optional[bool], project_id: Optional[str], repo_name: Optional[str], substitutions: Optional[Dict[str, str]], tag_name: Optional[str]) -> None:
        self.branch_name = branch_name
        self.commit_sha = commit_sha
        self.dir = dir
        self.invert_regex = invert_regex
        self.project_id = project_id
        self.repo_name = repo_name
        self.substitutions = substitutions
        self.tag_name = tag_name

    @staticmethod
    def from_dict(obj: Any) -> 'RepoSourceClass':
        assert isinstance(obj, dict)
        branch_name = from_union([from_str, from_none], obj.get("branchName"))
        commit_sha = from_union([from_str, from_none], obj.get("commitSha"))
        dir = from_union([from_str, from_none], obj.get("dir"))
        invert_regex = from_union([from_bool, from_none], obj.get("invertRegex"))
        project_id = from_union([from_str, from_none], obj.get("projectId"))
        repo_name = from_union([from_str, from_none], obj.get("repoName"))
        substitutions = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("substitutions"))
        tag_name = from_union([from_str, from_none], obj.get("tagName"))
        return RepoSourceClass(branch_name, commit_sha, dir, invert_regex, project_id, repo_name, substitutions, tag_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["branchName"] = from_union([from_str, from_none], self.branch_name)
        result["commitSha"] = from_union([from_str, from_none], self.commit_sha)
        result["dir"] = from_union([from_str, from_none], self.dir)
        result["invertRegex"] = from_union([from_bool, from_none], self.invert_regex)
        result["projectId"] = from_union([from_str, from_none], self.project_id)
        result["repoName"] = from_union([from_str, from_none], self.repo_name)
        result["substitutions"] = from_union([lambda x: from_dict(from_str, x), from_none], self.substitutions)
        result["tagName"] = from_union([from_str, from_none], self.tag_name)
        return result


class StorageSourceClass:
    """If provided, get the source from this location in Google Cloud Storage.
    
    Location of the source in an archive file in Google Cloud Storage.
    """
    """Google Cloud Storage bucket containing the source (see
    [Bucket Name
    Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)).
    """
    bucket: Optional[str]
    """Google Cloud Storage generation for the object. If the generation is
    omitted, the latest generation will be used.
    """
    generation: Optional[str]
    """Google Cloud Storage object containing the source."""
    object: Optional[str]

    def __init__(self, bucket: Optional[str], generation: Optional[str], object: Optional[str]) -> None:
        self.bucket = bucket
        self.generation = generation
        self.object = object

    @staticmethod
    def from_dict(obj: Any) -> 'StorageSourceClass':
        assert isinstance(obj, dict)
        bucket = from_union([from_str, from_none], obj.get("bucket"))
        generation = from_union([from_str, from_none], obj.get("generation"))
        object = from_union([from_str, from_none], obj.get("object"))
        return StorageSourceClass(bucket, generation, object)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bucket"] = from_union([from_str, from_none], self.bucket)
        result["generation"] = from_union([from_str, from_none], self.generation)
        result["object"] = from_union([from_str, from_none], self.object)
        return result


class Source:
    """The location of the source files to build."""
    """If provided, get the source from this location in a Cloud Source
    Repository.
    """
    repo_source: Optional[RepoSourceClass]
    """If provided, get the source from this location in Google Cloud Storage."""
    storage_source: Optional[StorageSourceClass]

    def __init__(self, repo_source: Optional[RepoSourceClass], storage_source: Optional[StorageSourceClass]) -> None:
        self.repo_source = repo_source
        self.storage_source = storage_source

    @staticmethod
    def from_dict(obj: Any) -> 'Source':
        assert isinstance(obj, dict)
        repo_source = from_union([RepoSourceClass.from_dict, from_none], obj.get("repoSource"))
        storage_source = from_union([StorageSourceClass.from_dict, from_none], obj.get("storageSource"))
        return Source(repo_source, storage_source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repoSource"] = from_union([lambda x: to_class(RepoSourceClass, x), from_none], self.repo_source)
        result["storageSource"] = from_union([lambda x: to_class(StorageSourceClass, x), from_none], self.storage_source)
        return result


class TypeEnum(Enum):
    MD5 = "MD5"
    NONE = "NONE"
    SHA256 = "SHA256"


class FileHashElement:
    """Container message for hash values."""
    """The type of hash that was performed."""
    type: Union[TypeEnum, int, None]
    """The hash value."""
    value: Optional[str]

    def __init__(self, type: Union[TypeEnum, int, None], value: Optional[str]) -> None:
        self.type = type
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'FileHashElement':
        assert isinstance(obj, dict)
        type = from_union([from_int, TypeEnum, from_none], obj.get("type"))
        value = from_union([from_str, from_none], obj.get("value"))
        return FileHashElement(type, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_int, lambda x: to_enum(TypeEnum, x), from_none], self.type)
        result["value"] = from_union([from_str, from_none], self.value)
        return result


class FileHashValue:
    """Collection of file hashes."""
    file_hash: Optional[List[FileHashElement]]

    def __init__(self, file_hash: Optional[List[FileHashElement]]) -> None:
        self.file_hash = file_hash

    @staticmethod
    def from_dict(obj: Any) -> 'FileHashValue':
        assert isinstance(obj, dict)
        file_hash = from_union([lambda x: from_list(FileHashElement.from_dict, x), from_none], obj.get("fileHash"))
        return FileHashValue(file_hash)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fileHash"] = from_union([lambda x: from_list(lambda x: to_class(FileHashElement, x), x), from_none], self.file_hash)
        return result


class ResolvedRepoSourceClass:
    """A copy of the build's `source.repo_source`, if exists, with any
    revisions resolved.
    
    If provided, get the source from this location in a Cloud Source
    Repository.
    
    Location of the source in a Google Cloud Source Repository.
    """
    """Regex matching branches to build.
    
    The syntax of the regular expressions accepted is the syntax accepted by
    RE2 and described at https://github.com/google/re2/wiki/Syntax
    """
    branch_name: Optional[str]
    """Explicit commit SHA to build."""
    commit_sha: Optional[str]
    """Directory, relative to the source root, in which to run the build.
    
    This must be a relative path. If a step's `dir` is specified and is an
    absolute path, this value is ignored for that step's execution.
    """
    dir: Optional[str]
    """Only trigger a build if the revision regex does NOT match the revision
    regex.
    """
    invert_regex: Optional[bool]
    """ID of the project that owns the Cloud Source Repository."""
    project_id: Optional[str]
    """Name of the Cloud Source Repository."""
    repo_name: Optional[str]
    """Substitutions to use in a triggered build.
    Should only be used with RunBuildTrigger
    """
    substitutions: Optional[Dict[str, str]]
    """Regex matching tags to build.
    
    The syntax of the regular expressions accepted is the syntax accepted by
    RE2 and described at https://github.com/google/re2/wiki/Syntax
    """
    tag_name: Optional[str]

    def __init__(self, branch_name: Optional[str], commit_sha: Optional[str], dir: Optional[str], invert_regex: Optional[bool], project_id: Optional[str], repo_name: Optional[str], substitutions: Optional[Dict[str, str]], tag_name: Optional[str]) -> None:
        self.branch_name = branch_name
        self.commit_sha = commit_sha
        self.dir = dir
        self.invert_regex = invert_regex
        self.project_id = project_id
        self.repo_name = repo_name
        self.substitutions = substitutions
        self.tag_name = tag_name

    @staticmethod
    def from_dict(obj: Any) -> 'ResolvedRepoSourceClass':
        assert isinstance(obj, dict)
        branch_name = from_union([from_str, from_none], obj.get("branchName"))
        commit_sha = from_union([from_str, from_none], obj.get("commitSha"))
        dir = from_union([from_str, from_none], obj.get("dir"))
        invert_regex = from_union([from_bool, from_none], obj.get("invertRegex"))
        project_id = from_union([from_str, from_none], obj.get("projectId"))
        repo_name = from_union([from_str, from_none], obj.get("repoName"))
        substitutions = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("substitutions"))
        tag_name = from_union([from_str, from_none], obj.get("tagName"))
        return ResolvedRepoSourceClass(branch_name, commit_sha, dir, invert_regex, project_id, repo_name, substitutions, tag_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["branchName"] = from_union([from_str, from_none], self.branch_name)
        result["commitSha"] = from_union([from_str, from_none], self.commit_sha)
        result["dir"] = from_union([from_str, from_none], self.dir)
        result["invertRegex"] = from_union([from_bool, from_none], self.invert_regex)
        result["projectId"] = from_union([from_str, from_none], self.project_id)
        result["repoName"] = from_union([from_str, from_none], self.repo_name)
        result["substitutions"] = from_union([lambda x: from_dict(from_str, x), from_none], self.substitutions)
        result["tagName"] = from_union([from_str, from_none], self.tag_name)
        return result


class ResolvedStorageSourceClass:
    """A copy of the build's `source.storage_source`, if exists, with any
    generations resolved.
    
    If provided, get the source from this location in Google Cloud Storage.
    
    Location of the source in an archive file in Google Cloud Storage.
    """
    """Google Cloud Storage bucket containing the source (see
    [Bucket Name
    Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)).
    """
    bucket: Optional[str]
    """Google Cloud Storage generation for the object. If the generation is
    omitted, the latest generation will be used.
    """
    generation: Optional[str]
    """Google Cloud Storage object containing the source."""
    object: Optional[str]

    def __init__(self, bucket: Optional[str], generation: Optional[str], object: Optional[str]) -> None:
        self.bucket = bucket
        self.generation = generation
        self.object = object

    @staticmethod
    def from_dict(obj: Any) -> 'ResolvedStorageSourceClass':
        assert isinstance(obj, dict)
        bucket = from_union([from_str, from_none], obj.get("bucket"))
        generation = from_union([from_str, from_none], obj.get("generation"))
        object = from_union([from_str, from_none], obj.get("object"))
        return ResolvedStorageSourceClass(bucket, generation, object)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bucket"] = from_union([from_str, from_none], self.bucket)
        result["generation"] = from_union([from_str, from_none], self.generation)
        result["object"] = from_union([from_str, from_none], self.object)
        return result


class SourceProvenance:
    """A permanent fixed identifier for source."""
    """Hash(es) of the build source, which can be used to verify that
    the original source integrity was maintained in the build. Note that
    `FileHashes` will only be populated if `BuildOptions` has requested a
    `SourceProvenanceHash`.
    
    The keys to this map are file paths used as build source and the values
    contain the hash values for those files.
    
    If the build source came in a single package such as a gzipped tarfile
    (`.tar.gz`), the `FileHash` will be for the single path to that file.
    """
    file_hashes: Optional[Dict[str, FileHashValue]]
    """A copy of the build's `source.repo_source`, if exists, with any
    revisions resolved.
    """
    resolved_repo_source: Optional[ResolvedRepoSourceClass]
    """A copy of the build's `source.storage_source`, if exists, with any
    generations resolved.
    """
    resolved_storage_source: Optional[ResolvedStorageSourceClass]

    def __init__(self, file_hashes: Optional[Dict[str, FileHashValue]], resolved_repo_source: Optional[ResolvedRepoSourceClass], resolved_storage_source: Optional[ResolvedStorageSourceClass]) -> None:
        self.file_hashes = file_hashes
        self.resolved_repo_source = resolved_repo_source
        self.resolved_storage_source = resolved_storage_source

    @staticmethod
    def from_dict(obj: Any) -> 'SourceProvenance':
        assert isinstance(obj, dict)
        file_hashes = from_union([lambda x: from_dict(FileHashValue.from_dict, x), from_none], obj.get("fileHashes"))
        resolved_repo_source = from_union([ResolvedRepoSourceClass.from_dict, from_none], obj.get("resolvedRepoSource"))
        resolved_storage_source = from_union([ResolvedStorageSourceClass.from_dict, from_none], obj.get("resolvedStorageSource"))
        return SourceProvenance(file_hashes, resolved_repo_source, resolved_storage_source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fileHashes"] = from_union([lambda x: from_dict(lambda x: to_class(FileHashValue, x), x), from_none], self.file_hashes)
        result["resolvedRepoSource"] = from_union([lambda x: to_class(ResolvedRepoSourceClass, x), from_none], self.resolved_repo_source)
        result["resolvedStorageSource"] = from_union([lambda x: to_class(ResolvedStorageSourceClass, x), from_none], self.resolved_storage_source)
        return result


class StatusEnum(Enum):
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"
    FAILURE = "FAILURE"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    QUEUED = "QUEUED"
    STATUS_UNKNOWN = "STATUS_UNKNOWN"
    SUCCESS = "SUCCESS"
    TIMEOUT = "TIMEOUT"
    WORKING = "WORKING"


class PullTiming:
    """Stores timing information for pulling this build step's
    builder image only.
    
    Stores timing information for pushing all artifact objects.
    
    Start and end times for a build execution phase.
    """
    """End of time span."""
    end_time: Optional[datetime]
    """Start of time span."""
    start_time: Optional[datetime]

    def __init__(self, end_time: Optional[datetime], start_time: Optional[datetime]) -> None:
        self.end_time = end_time
        self.start_time = start_time

    @staticmethod
    def from_dict(obj: Any) -> 'PullTiming':
        assert isinstance(obj, dict)
        end_time = from_union([from_datetime, from_none], obj.get("endTime"))
        start_time = from_union([from_datetime, from_none], obj.get("startTime"))
        return PullTiming(end_time, start_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["endTime"] = from_union([lambda x: x.isoformat(), from_none], self.end_time)
        result["startTime"] = from_union([lambda x: x.isoformat(), from_none], self.start_time)
        return result


class StepTimeout:
    """Time limit for executing this build step. If not defined, the step has no
    time limit and will be allowed to continue to run until either it completes
    or the build itself times out.
    """
    """Signed fractions of a second at nanosecond resolution of the span
    of time. Durations less than one second are represented with a 0
    `seconds` field and a positive or negative `nanos` field. For durations
    of one second or more, a non-zero value for the `nanos` field must be
    of the same sign as the `seconds` field. Must be from -999,999,999
    to +999,999,999 inclusive.
    """
    nanos: Optional[int]
    """Signed seconds of the span of time. Must be from -315,576,000,000
    to +315,576,000,000 inclusive. Note: these bounds are computed from:
    60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years
    """
    seconds: Optional[str]

    def __init__(self, nanos: Optional[int], seconds: Optional[str]) -> None:
        self.nanos = nanos
        self.seconds = seconds

    @staticmethod
    def from_dict(obj: Any) -> 'StepTimeout':
        assert isinstance(obj, dict)
        nanos = from_union([from_int, from_none], obj.get("nanos"))
        seconds = from_union([from_str, from_none], obj.get("seconds"))
        return StepTimeout(nanos, seconds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nanos"] = from_union([from_int, from_none], self.nanos)
        result["seconds"] = from_union([from_str, from_none], self.seconds)
        return result


class StepTiming:
    """Stores timing information for executing this build step.
    
    Stores timing information for pushing all artifact objects.
    
    Start and end times for a build execution phase.
    """
    """End of time span."""
    end_time: Optional[datetime]
    """Start of time span."""
    start_time: Optional[datetime]

    def __init__(self, end_time: Optional[datetime], start_time: Optional[datetime]) -> None:
        self.end_time = end_time
        self.start_time = start_time

    @staticmethod
    def from_dict(obj: Any) -> 'StepTiming':
        assert isinstance(obj, dict)
        end_time = from_union([from_datetime, from_none], obj.get("endTime"))
        start_time = from_union([from_datetime, from_none], obj.get("startTime"))
        return StepTiming(end_time, start_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["endTime"] = from_union([lambda x: x.isoformat(), from_none], self.end_time)
        result["startTime"] = from_union([lambda x: x.isoformat(), from_none], self.start_time)
        return result


class Step:
    """A step in the build pipeline."""
    """A list of arguments that will be presented to the step when it is started.
    
    If the image used to run the step's container has an entrypoint, the `args`
    are used as arguments to that entrypoint. If the image does not define
    an entrypoint, the first element in args is used as the entrypoint,
    and the remainder will be used as arguments.
    """
    args: Optional[List[str]]
    """Working directory to use when running this step's container.
    
    If this value is a relative path, it is relative to the build's working
    directory. If this value is absolute, it may be outside the build's working
    directory, in which case the contents of the path may not be persisted
    across build step executions, unless a `volume` for that path is specified.
    
    If the build specifies a `RepoSource` with `dir` and a step with a `dir`,
    which specifies an absolute path, the `RepoSource` `dir` is ignored for
    the step's execution.
    """
    dir: Optional[str]
    """Entrypoint to be used instead of the build step image's default entrypoint.
    If unset, the image's default entrypoint is used.
    """
    entrypoint: Optional[str]
    """A list of environment variable definitions to be used when running a step.
    
    The elements are of the form "KEY=VALUE" for the environment variable "KEY"
    being given the value "VALUE".
    """
    env: Optional[List[str]]
    """Unique identifier for this build step, used in `wait_for` to
    reference this build step as a dependency.
    """
    id: Optional[str]
    """The name of the container image that will run this particular
    build step.
    
    If the image is available in the host's Docker daemon's cache, it
    will be run directly. If not, the host will attempt to pull the image
    first, using the builder service account's credentials if necessary.
    
    The Docker daemon's cache will already have the latest versions of all of
    the officially supported build steps
    
    ([https://github.com/GoogleCloudPlatform/cloud-builders](https://github.com/GoogleCloudPlatform/cloud-builders)).
    The Docker daemon will also have cached many of the layers for some popular
    images, like "ubuntu", "debian", but they will be refreshed at the time you
    attempt to use them.
    
    If you built an image in a previous build step, it will be stored in the
    host's Docker daemon's cache and is available to use as the name for a
    later build step.
    """
    name: Optional[str]
    """Stores timing information for pulling this build step's
    builder image only.
    """
    pull_timing: Optional[PullTiming]
    """A list of environment variables which are encrypted using a Cloud Key
    Management Service crypto key. These values must be specified in the
    build's `Secret`.
    """
    secret_env: Optional[List[str]]
    """Status of the build step. At this time, build step status is
    only updated on build completion; step status is not updated in real-time
    as the build progresses.
    """
    status: Union[int, None, str]
    """Time limit for executing this build step. If not defined, the step has no
    time limit and will be allowed to continue to run until either it completes
    or the build itself times out.
    """
    timeout: Optional[StepTimeout]
    """Stores timing information for executing this build step."""
    timing: Optional[StepTiming]
    """List of volumes to mount into the build step.
    
    Each volume is created as an empty volume prior to execution of the
    build step. Upon completion of the build, volumes and their contents are
    discarded.
    
    Using a named volume in only one step is not valid as it is indicative
    of a build request with an incorrect configuration.
    """
    volumes: Optional[List[Volume]]
    """The ID(s) of the step(s) that this build step depends on.
    This build step will not start until all the build steps in `wait_for`
    have completed successfully. If `wait_for` is empty, this build step will
    start when all previous build steps in the `Build.Steps` list have
    completed successfully.
    """
    wait_for: Optional[List[str]]

    def __init__(self, args: Optional[List[str]], dir: Optional[str], entrypoint: Optional[str], env: Optional[List[str]], id: Optional[str], name: Optional[str], pull_timing: Optional[PullTiming], secret_env: Optional[List[str]], status: Union[int, None, str], timeout: Optional[StepTimeout], timing: Optional[StepTiming], volumes: Optional[List[Volume]], wait_for: Optional[List[str]]) -> None:
        self.args = args
        self.dir = dir
        self.entrypoint = entrypoint
        self.env = env
        self.id = id
        self.name = name
        self.pull_timing = pull_timing
        self.secret_env = secret_env
        self.status = status
        self.timeout = timeout
        self.timing = timing
        self.volumes = volumes
        self.wait_for = wait_for

    @staticmethod
    def from_dict(obj: Any) -> 'Step':
        assert isinstance(obj, dict)
        args = from_union([lambda x: from_list(from_str, x), from_none], obj.get("args"))
        dir = from_union([from_str, from_none], obj.get("dir"))
        entrypoint = from_union([from_str, from_none], obj.get("entrypoint"))
        env = from_union([lambda x: from_list(from_str, x), from_none], obj.get("env"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        pull_timing = from_union([PullTiming.from_dict, from_none], obj.get("pullTiming"))
        secret_env = from_union([lambda x: from_list(from_str, x), from_none], obj.get("secretEnv"))
        status = from_union([from_int, from_str, from_none], obj.get("status"))
        timeout = from_union([StepTimeout.from_dict, from_none], obj.get("timeout"))
        timing = from_union([StepTiming.from_dict, from_none], obj.get("timing"))
        volumes = from_union([lambda x: from_list(Volume.from_dict, x), from_none], obj.get("volumes"))
        wait_for = from_union([lambda x: from_list(from_str, x), from_none], obj.get("waitFor"))
        return Step(args, dir, entrypoint, env, id, name, pull_timing, secret_env, status, timeout, timing, volumes, wait_for)

    def to_dict(self) -> dict:
        result: dict = {}
        result["args"] = from_union([lambda x: from_list(from_str, x), from_none], self.args)
        result["dir"] = from_union([from_str, from_none], self.dir)
        result["entrypoint"] = from_union([from_str, from_none], self.entrypoint)
        result["env"] = from_union([lambda x: from_list(from_str, x), from_none], self.env)
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["pullTiming"] = from_union([lambda x: to_class(PullTiming, x), from_none], self.pull_timing)
        result["secretEnv"] = from_union([lambda x: from_list(from_str, x), from_none], self.secret_env)
        result["status"] = from_union([from_int, from_str, from_none], self.status)
        result["timeout"] = from_union([lambda x: to_class(StepTimeout, x), from_none], self.timeout)
        result["timing"] = from_union([lambda x: to_class(StepTiming, x), from_none], self.timing)
        result["volumes"] = from_union([lambda x: from_list(lambda x: to_class(Volume, x), x), from_none], self.volumes)
        result["waitFor"] = from_union([lambda x: from_list(from_str, x), from_none], self.wait_for)
        return result


class BuildEventDataTimeout:
    """Amount of time that this build should be allowed to run, to second
    granularity. If this amount of time elapses, work on the build will cease
    and the build status will be `TIMEOUT`.
    """
    """Signed fractions of a second at nanosecond resolution of the span
    of time. Durations less than one second are represented with a 0
    `seconds` field and a positive or negative `nanos` field. For durations
    of one second or more, a non-zero value for the `nanos` field must be
    of the same sign as the `seconds` field. Must be from -999,999,999
    to +999,999,999 inclusive.
    """
    nanos: Optional[int]
    """Signed seconds of the span of time. Must be from -315,576,000,000
    to +315,576,000,000 inclusive. Note: these bounds are computed from:
    60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years
    """
    seconds: Optional[str]

    def __init__(self, nanos: Optional[int], seconds: Optional[str]) -> None:
        self.nanos = nanos
        self.seconds = seconds

    @staticmethod
    def from_dict(obj: Any) -> 'BuildEventDataTimeout':
        assert isinstance(obj, dict)
        nanos = from_union([from_int, from_none], obj.get("nanos"))
        seconds = from_union([from_str, from_none], obj.get("seconds"))
        return BuildEventDataTimeout(nanos, seconds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nanos"] = from_union([from_int, from_none], self.nanos)
        result["seconds"] = from_union([from_str, from_none], self.seconds)
        return result


class TimeSpan:
    """Stores timing information for pushing all artifact objects.
    
    Start and end times for a build execution phase.
    """
    """End of time span."""
    end_time: Optional[datetime]
    """Start of time span."""
    start_time: Optional[datetime]

    def __init__(self, end_time: Optional[datetime], start_time: Optional[datetime]) -> None:
        self.end_time = end_time
        self.start_time = start_time

    @staticmethod
    def from_dict(obj: Any) -> 'TimeSpan':
        assert isinstance(obj, dict)
        end_time = from_union([from_datetime, from_none], obj.get("endTime"))
        start_time = from_union([from_datetime, from_none], obj.get("startTime"))
        return TimeSpan(end_time, start_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["endTime"] = from_union([lambda x: x.isoformat(), from_none], self.end_time)
        result["startTime"] = from_union([lambda x: x.isoformat(), from_none], self.start_time)
        return result


class BuildEventData:
    """Build event data for Google Cloud Platform API operations."""
    """Artifacts produced by the build that should be uploaded upon
    successful completion of all build steps.
    """
    artifacts: Optional[Artifacts]
    """The ID of the `BuildTrigger` that triggered this build, if it
    was triggered automatically.
    """
    build_trigger_id: Optional[str]
    """Time at which the request to create the build was received."""
    create_time: Optional[datetime]
    """Time at which execution of the build was finished.
    
    The difference between finish_time and start_time is the duration of the
    build's execution.
    """
    finish_time: Optional[datetime]
    """Unique identifier of the build."""
    id: Optional[str]
    """A list of images to be pushed upon the successful completion of all build
    steps.
    
    The images are pushed using the builder service account's credentials.
    
    The digests of the pushed images will be stored in the `Build` resource's
    results field.
    
    If any of the images fail to be pushed, the build status is marked
    `FAILURE`.
    """
    images: Optional[List[str]]
    """Google Cloud Storage bucket where logs should be written (see
    [Bucket Name
    Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)).
    Logs file names will be of the format `${logs_bucket}/log-${build_id}.txt`.
    """
    logs_bucket: Optional[str]
    """URL to logs for this build in Google Cloud Console."""
    log_url: Optional[str]
    """Special options for this build."""
    options: Optional[Options]
    """ID of the project."""
    project_id: Optional[str]
    """TTL in queue for this build. If provided and the build is enqueued longer
    than this value, the build will expire and the build status will be
    `EXPIRED`.
    
    The TTL starts ticking from create_time.
    """
    queue_ttl: Optional[QueueTTL]
    """Results of the build."""
    results: Optional[Results]
    """Secrets to decrypt using Cloud Key Management Service."""
    secrets: Optional[List[Secret]]
    """The location of the source files to build."""
    source: Optional[Source]
    """A permanent fixed identifier for source."""
    source_provenance: Optional[SourceProvenance]
    """Time at which execution of the build was started."""
    start_time: Optional[datetime]
    """Status of the build."""
    status: Union[StatusEnum, int, None]
    """Customer-readable message about the current status."""
    status_detail: Optional[str]
    """The operations to be performed on the workspace."""
    steps: Optional[List[Step]]
    """Substitutions data for `Build` resource."""
    substitutions: Optional[Dict[str, str]]
    """Tags for annotation of a `Build`. These are not docker tags."""
    tags: Optional[List[str]]
    """Amount of time that this build should be allowed to run, to second
    granularity. If this amount of time elapses, work on the build will cease
    and the build status will be `TIMEOUT`.
    """
    timeout: Optional[BuildEventDataTimeout]
    """Stores timing information for phases of the build. Valid keys
    are:
    
    * BUILD: time to execute all build steps
    * PUSH: time to push all specified images.
    * FETCHSOURCE: time to fetch source.
    
    If the build does not specify source or images,
    these keys will not be included.
    """
    timing: Optional[Dict[str, TimeSpan]]

    def __init__(self, artifacts: Optional[Artifacts], build_trigger_id: Optional[str], create_time: Optional[datetime], finish_time: Optional[datetime], id: Optional[str], images: Optional[List[str]], logs_bucket: Optional[str], log_url: Optional[str], options: Optional[Options], project_id: Optional[str], queue_ttl: Optional[QueueTTL], results: Optional[Results], secrets: Optional[List[Secret]], source: Optional[Source], source_provenance: Optional[SourceProvenance], start_time: Optional[datetime], status: Union[StatusEnum, int, None], status_detail: Optional[str], steps: Optional[List[Step]], substitutions: Optional[Dict[str, str]], tags: Optional[List[str]], timeout: Optional[BuildEventDataTimeout], timing: Optional[Dict[str, TimeSpan]]) -> None:
        self.artifacts = artifacts
        self.build_trigger_id = build_trigger_id
        self.create_time = create_time
        self.finish_time = finish_time
        self.id = id
        self.images = images
        self.logs_bucket = logs_bucket
        self.log_url = log_url
        self.options = options
        self.project_id = project_id
        self.queue_ttl = queue_ttl
        self.results = results
        self.secrets = secrets
        self.source = source
        self.source_provenance = source_provenance
        self.start_time = start_time
        self.status = status
        self.status_detail = status_detail
        self.steps = steps
        self.substitutions = substitutions
        self.tags = tags
        self.timeout = timeout
        self.timing = timing

    @staticmethod
    def from_dict(obj: Any) -> 'BuildEventData':
        assert isinstance(obj, dict)
        artifacts = from_union([Artifacts.from_dict, from_none], obj.get("artifacts"))
        build_trigger_id = from_union([from_str, from_none], obj.get("buildTriggerId"))
        create_time = from_union([from_datetime, from_none], obj.get("createTime"))
        finish_time = from_union([from_datetime, from_none], obj.get("finishTime"))
        id = from_union([from_str, from_none], obj.get("id"))
        images = from_union([lambda x: from_list(from_str, x), from_none], obj.get("images"))
        logs_bucket = from_union([from_str, from_none], obj.get("logsBucket"))
        log_url = from_union([from_str, from_none], obj.get("logUrl"))
        options = from_union([Options.from_dict, from_none], obj.get("options"))
        project_id = from_union([from_str, from_none], obj.get("projectId"))
        queue_ttl = from_union([QueueTTL.from_dict, from_none], obj.get("queueTtl"))
        results = from_union([Results.from_dict, from_none], obj.get("results"))
        secrets = from_union([lambda x: from_list(Secret.from_dict, x), from_none], obj.get("secrets"))
        source = from_union([Source.from_dict, from_none], obj.get("source"))
        source_provenance = from_union([SourceProvenance.from_dict, from_none], obj.get("sourceProvenance"))
        start_time = from_union([from_datetime, from_none], obj.get("startTime"))
        status = from_union([from_int, StatusEnum, from_none], obj.get("status"))
        status_detail = from_union([from_str, from_none], obj.get("statusDetail"))
        steps = from_union([lambda x: from_list(Step.from_dict, x), from_none], obj.get("steps"))
        substitutions = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("substitutions"))
        tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("tags"))
        timeout = from_union([BuildEventDataTimeout.from_dict, from_none], obj.get("timeout"))
        timing = from_union([lambda x: from_dict(TimeSpan.from_dict, x), from_none], obj.get("timing"))
        return BuildEventData(artifacts, build_trigger_id, create_time, finish_time, id, images, logs_bucket, log_url, options, project_id, queue_ttl, results, secrets, source, source_provenance, start_time, status, status_detail, steps, substitutions, tags, timeout, timing)

    def to_dict(self) -> dict:
        result: dict = {}
        result["artifacts"] = from_union([lambda x: to_class(Artifacts, x), from_none], self.artifacts)
        result["buildTriggerId"] = from_union([from_str, from_none], self.build_trigger_id)
        result["createTime"] = from_union([lambda x: x.isoformat(), from_none], self.create_time)
        result["finishTime"] = from_union([lambda x: x.isoformat(), from_none], self.finish_time)
        result["id"] = from_union([from_str, from_none], self.id)
        result["images"] = from_union([lambda x: from_list(from_str, x), from_none], self.images)
        result["logsBucket"] = from_union([from_str, from_none], self.logs_bucket)
        result["logUrl"] = from_union([from_str, from_none], self.log_url)
        result["options"] = from_union([lambda x: to_class(Options, x), from_none], self.options)
        result["projectId"] = from_union([from_str, from_none], self.project_id)
        result["queueTtl"] = from_union([lambda x: to_class(QueueTTL, x), from_none], self.queue_ttl)
        result["results"] = from_union([lambda x: to_class(Results, x), from_none], self.results)
        result["secrets"] = from_union([lambda x: from_list(lambda x: to_class(Secret, x), x), from_none], self.secrets)
        result["source"] = from_union([lambda x: to_class(Source, x), from_none], self.source)
        result["sourceProvenance"] = from_union([lambda x: to_class(SourceProvenance, x), from_none], self.source_provenance)
        result["startTime"] = from_union([lambda x: x.isoformat(), from_none], self.start_time)
        result["status"] = from_union([from_int, lambda x: to_enum(StatusEnum, x), from_none], self.status)
        result["statusDetail"] = from_union([from_str, from_none], self.status_detail)
        result["steps"] = from_union([lambda x: from_list(lambda x: to_class(Step, x), x), from_none], self.steps)
        result["substitutions"] = from_union([lambda x: from_dict(from_str, x), from_none], self.substitutions)
        result["tags"] = from_union([lambda x: from_list(from_str, x), from_none], self.tags)
        result["timeout"] = from_union([lambda x: to_class(BuildEventDataTimeout, x), from_none], self.timeout)
        result["timing"] = from_union([lambda x: from_dict(lambda x: to_class(TimeSpan, x), x), from_none], self.timing)
        return result


def build_event_data_from_dict(s: Any) -> BuildEventData:
    return BuildEventData.from_dict(s)


def build_event_data_to_dict(x: BuildEventData) -> Any:
    return to_class(BuildEventData, x)
