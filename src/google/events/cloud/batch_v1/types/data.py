# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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

from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.events.cloud.batch.v1',
    manifest={
        'Volume',
        'NFS',
        'GCS',
        'ComputeResource',
        'StatusEvent',
        'TaskExecution',
        'TaskStatus',
        'Runnable',
        'TaskSpec',
        'LifecyclePolicy',
        'Environment',
        'Job',
        'LogsPolicy',
        'JobStatus',
        'JobNotification',
        'AllocationPolicy',
        'TaskGroup',
        'ServiceAccount',
        'JobEventData',
    },
)


class Volume(proto.Message):
    r"""Volume describes a volume and parameters for it to be mounted
    to a VM.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        nfs (google.events.cloud.batch_v1.types.NFS):
            A Network File System (NFS) volume. For
            example, a Filestore file share.

            This field is a member of `oneof`_ ``source``.
        gcs (google.events.cloud.batch_v1.types.GCS):
            A Google Cloud Storage (GCS) volume.

            This field is a member of `oneof`_ ``source``.
        device_name (str):
            Device name of an attached disk volume, which should align
            with a device_name specified by
            job.allocation_policy.instances[0].policy.disks[i].device_name
            or defined by the given instance template in
            job.allocation_policy.instances[0].instance_template.

            This field is a member of `oneof`_ ``source``.
        mount_path (str):
            The mount path for the volume, e.g.
            /mnt/disks/share.
        mount_options (MutableSequence[str]):
            For Google Cloud Storage (GCS), mount options
            are the options supported by the gcsfuse tool
            (https://github.com/GoogleCloudPlatform/gcsfuse).
            For existing persistent disks, mount options
            provided by the mount command
            (https://man7.org/linux/man-pages/man8/mount.8.html)
            except writing are supported. This is due to
            restrictions of multi-writer mode
            (https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms).
            For other attached disks and Network File System
            (NFS), mount options are these supported by the
            mount command
            (https://man7.org/linux/man-pages/man8/mount.8.html).
    """

    nfs: 'NFS' = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='source',
        message='NFS',
    )
    gcs: 'GCS' = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof='source',
        message='GCS',
    )
    device_name: str = proto.Field(
        proto.STRING,
        number=6,
        oneof='source',
    )
    mount_path: str = proto.Field(
        proto.STRING,
        number=4,
    )
    mount_options: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class NFS(proto.Message):
    r"""Represents an NFS volume.

    Attributes:
        server (str):
            The IP address of the NFS.
        remote_path (str):
            Remote source path exported from the NFS,
            e.g., "/share".
    """

    server: str = proto.Field(
        proto.STRING,
        number=1,
    )
    remote_path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GCS(proto.Message):
    r"""Represents a Google Cloud Storage volume.

    Attributes:
        remote_path (str):
            Remote path, either a bucket name or a subdirectory of a
            bucket, e.g.: bucket_name, bucket_name/subdirectory/
    """

    remote_path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ComputeResource(proto.Message):
    r"""Compute resource requirements

    Attributes:
        cpu_milli (int):
            The milliCPU count.
        memory_mib (int):
            Memory in MiB.
        boot_disk_mib (int):
            Extra boot disk size in MiB for each task.
    """

    cpu_milli: int = proto.Field(
        proto.INT64,
        number=1,
    )
    memory_mib: int = proto.Field(
        proto.INT64,
        number=2,
    )
    boot_disk_mib: int = proto.Field(
        proto.INT64,
        number=4,
    )


class StatusEvent(proto.Message):
    r"""Status event

    Attributes:
        type_ (str):
            Type of the event.
        description (str):
            Description of the event.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            The time this event occurred.
        task_execution (google.events.cloud.batch_v1.types.TaskExecution):
            Task Execution
        task_state (google.events.cloud.batch_v1.types.TaskStatus.State):
            Task State
    """

    type_: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    task_execution: 'TaskExecution' = proto.Field(
        proto.MESSAGE,
        number=4,
        message='TaskExecution',
    )
    task_state: 'TaskStatus.State' = proto.Field(
        proto.ENUM,
        number=5,
        enum='TaskStatus.State',
    )


class TaskExecution(proto.Message):
    r"""This Task Execution field includes detail information for
    task execution procedures, based on StatusEvent types.

    Attributes:
        exit_code (int):
            When task is completed as the status of
            FAILED or SUCCEEDED, exit code is for one task
            execution result, default is 0 as success.
    """

    exit_code: int = proto.Field(
        proto.INT32,
        number=1,
    )


class TaskStatus(proto.Message):
    r"""Status of a task
    """
    class State(proto.Enum):
        r"""Task states.

        Values:
            STATE_UNSPECIFIED (0):
                Unknown state.
            PENDING (1):
                The Task is created and waiting for
                resources.
            ASSIGNED (2):
                The Task is assigned to at least one VM.
            RUNNING (3):
                The Task is running.
            FAILED (4):
                The Task has failed.
            SUCCEEDED (5):
                The Task has succeeded.
            UNEXECUTED (6):
                The Task has not been executed when the Job
                finishes.
        """
        STATE_UNSPECIFIED = 0
        PENDING = 1
        ASSIGNED = 2
        RUNNING = 3
        FAILED = 4
        SUCCEEDED = 5
        UNEXECUTED = 6


class Runnable(proto.Message):
    r"""Runnable describes instructions for executing a specific
    script or container as part of a Task.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        container (google.events.cloud.batch_v1.types.Runnable.Container):
            Container runnable.

            This field is a member of `oneof`_ ``executable``.
        script (google.events.cloud.batch_v1.types.Runnable.Script):
            Script runnable.

            This field is a member of `oneof`_ ``executable``.
        barrier (google.events.cloud.batch_v1.types.Runnable.Barrier):
            Barrier runnable.

            This field is a member of `oneof`_ ``executable``.
        ignore_exit_status (bool):
            Normally, a non-zero exit status causes the
            Task to fail. This flag allows execution of
            other Runnables to continue instead.
        background (bool):
            This flag allows a Runnable to continue
            running in the background while the Task
            executes subsequent Runnables. This is useful to
            provide services to other Runnables (or to
            provide debugging support tools like SSH
            servers).
        always_run (bool):
            By default, after a Runnable fails, no further Runnable are
            executed. This flag indicates that this Runnable must be run
            even if the Task has already failed. This is useful for
            Runnables that copy output files off of the VM or for
            debugging.

            The always_run flag does not override the Task's overall
            max_run_duration. If the max_run_duration has expired then
            no further Runnables will execute, not even always_run
            Runnables.
        environment (google.events.cloud.batch_v1.types.Environment):
            Environment variables for this Runnable
            (overrides variables set for the whole Task or
            TaskGroup).
        timeout (google.protobuf.duration_pb2.Duration):
            Timeout for this Runnable.
        labels (MutableMapping[str, str]):
            Labels for this Runnable.
    """

    class Container(proto.Message):
        r"""Container runnable.

        Attributes:
            image_uri (str):
                The URI to pull the container image from.
            commands (MutableSequence[str]):
                Overrides the ``CMD`` specified in the container. If there
                is an ENTRYPOINT (either in the container image or with the
                entrypoint field below) then commands are appended as
                arguments to the ENTRYPOINT.
            entrypoint (str):
                Overrides the ``ENTRYPOINT`` specified in the container.
            volumes (MutableSequence[str]):
                Volumes to mount (bind mount) from the host
                machine files or directories into the container,
                formatted to match docker run's --volume option,
                e.g. /foo:/bar, or /foo:/bar:ro
            options (str):
                Arbitrary additional options to include in
                the "docker run" command when running this
                container, e.g. "--network host".
            block_external_network (bool):
                If set to true, external network access to and from
                container will be blocked, containers that are with
                block_external_network as true can still communicate with
                each other, network cannot be specified in the
                ``container.options`` field.
            username (str):
                Optional username for logging in to a docker registry. If
                username matches ``projects/*/secrets/*/versions/*`` then
                Batch will read the username from the Secret Manager.
            password (str):
                Optional password for logging in to a docker registry. If
                password matches ``projects/*/secrets/*/versions/*`` then
                Batch will read the password from the Secret Manager;
        """

        image_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        commands: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        entrypoint: str = proto.Field(
            proto.STRING,
            number=3,
        )
        volumes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=7,
        )
        options: str = proto.Field(
            proto.STRING,
            number=8,
        )
        block_external_network: bool = proto.Field(
            proto.BOOL,
            number=9,
        )
        username: str = proto.Field(
            proto.STRING,
            number=10,
        )
        password: str = proto.Field(
            proto.STRING,
            number=11,
        )

    class Script(proto.Message):
        r"""Script runnable.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            path (str):
                Script file path on the host VM.

                To specify an interpreter, please add a
                ``#!<interpreter>``\ (also known as `shebang
                line <https://en.wikipedia.org/wiki/Shebang_(Unix)>`__) as
                the first line of the file.(For example, to execute the
                script using bash, ``#!/bin/bash`` should be the first line
                of the file. To execute the script using\ ``Python3``,
                ``#!/usr/bin/env python3`` should be the first line of the
                file.) Otherwise, the file will by default be excuted by
                ``/bin/sh``.

                This field is a member of `oneof`_ ``command``.
            text (str):
                Shell script text.

                To specify an interpreter, please add a
                ``#!<interpreter>\n`` at the beginning of the text.(For
                example, to execute the script using bash, ``#!/bin/bash\n``
                should be added. To execute the script using\ ``Python3``,
                ``#!/usr/bin/env python3\n`` should be added.) Otherwise,
                the script will by default be excuted by ``/bin/sh``.

                This field is a member of `oneof`_ ``command``.
        """

        path: str = proto.Field(
            proto.STRING,
            number=1,
            oneof='command',
        )
        text: str = proto.Field(
            proto.STRING,
            number=2,
            oneof='command',
        )

    class Barrier(proto.Message):
        r"""Barrier runnable blocks until all tasks in a taskgroup reach
        it.

        Attributes:
            name (str):
                Barriers are identified by their index in
                runnable list. Names are not required, but if
                present should be an identifier.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    container: Container = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='executable',
        message=Container,
    )
    script: Script = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='executable',
        message=Script,
    )
    barrier: Barrier = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof='executable',
        message=Barrier,
    )
    ignore_exit_status: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    background: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    always_run: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    environment: 'Environment' = proto.Field(
        proto.MESSAGE,
        number=7,
        message='Environment',
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )


class TaskSpec(proto.Message):
    r"""Spec of a task

    Attributes:
        runnables (MutableSequence[google.events.cloud.batch_v1.types.Runnable]):
            The sequence of scripts or containers to run for this Task.
            Each Task using this TaskSpec executes its list of runnables
            in order. The Task succeeds if all of its runnables either
            exit with a zero status or any that exit with a non-zero
            status have the ignore_exit_status flag.

            Background runnables are killed automatically (if they have
            not already exited) a short time after all foreground
            runnables have completed. Even though this is likely to
            result in a non-zero exit status for the background
            runnable, these automatic kills are not treated as Task
            failures.
        compute_resource (google.events.cloud.batch_v1.types.ComputeResource):
            ComputeResource requirements.
        max_run_duration (google.protobuf.duration_pb2.Duration):
            Maximum duration the task should run.
            The task will be killed and marked as FAILED if
            over this limit.
        max_retry_count (int):
            Maximum number of retries on failures. The default, 0, which
            means never retry. The valid value range is [0, 10].
        lifecycle_policies (MutableSequence[google.events.cloud.batch_v1.types.LifecyclePolicy]):
            Lifecycle management schema when any task in a task group is
            failed. Currently we only support one lifecycle policy. When
            the lifecycle policy condition is met, the action in the
            policy will execute. If task execution result does not meet
            with the defined lifecycle policy, we consider it as the
            default policy. Default policy means if the exit code is 0,
            exit task. If task ends with non-zero exit code, retry the
            task with max_retry_count.
        environments (MutableMapping[str, str]):
            Deprecated: please use
            environment(non-plural) instead.
        volumes (MutableSequence[google.events.cloud.batch_v1.types.Volume]):
            Volumes to mount before running Tasks using
            this TaskSpec.
        environment (google.events.cloud.batch_v1.types.Environment):
            Environment variables to set before running
            the Task.
    """

    runnables: MutableSequence['Runnable'] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message='Runnable',
    )
    compute_resource: 'ComputeResource' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='ComputeResource',
    )
    max_run_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    max_retry_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    lifecycle_policies: MutableSequence['LifecyclePolicy'] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message='LifecyclePolicy',
    )
    environments: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    volumes: MutableSequence['Volume'] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message='Volume',
    )
    environment: 'Environment' = proto.Field(
        proto.MESSAGE,
        number=10,
        message='Environment',
    )


class LifecyclePolicy(proto.Message):
    r"""LifecyclePolicy describes how to deal with task failures
    based on different conditions.

    Attributes:
        action (google.events.cloud.batch_v1.types.LifecyclePolicy.Action):
            Action to execute when ActionCondition is true. When
            RETRY_TASK is specified, we will retry failed tasks if we
            notice any exit code match and fail tasks if no match is
            found. Likewise, when FAIL_TASK is specified, we will fail
            tasks if we notice any exit code match and retry tasks if no
            match is found.
        action_condition (google.events.cloud.batch_v1.types.LifecyclePolicy.ActionCondition):
            Conditions that decide why a task failure is
            dealt with a specific action.
    """
    class Action(proto.Enum):
        r"""Action on task failures based on different conditions.

        Values:
            ACTION_UNSPECIFIED (0):
                Action unspecified.
            RETRY_TASK (1):
                Action that tasks in the group will be
                scheduled to re-execute.
            FAIL_TASK (2):
                Action that tasks in the group will be
                stopped immediately.
        """
        ACTION_UNSPECIFIED = 0
        RETRY_TASK = 1
        FAIL_TASK = 2

    class ActionCondition(proto.Message):
        r"""Conditions for actions to deal with task failures.

        Attributes:
            exit_codes (MutableSequence[int]):
                Exit codes of a task execution.
                If there are more than 1 exit codes,
                when task executes with any of the exit code in
                the list, the condition is met and the action
                will be executed.
        """

        exit_codes: MutableSequence[int] = proto.RepeatedField(
            proto.INT32,
            number=1,
        )

    action: Action = proto.Field(
        proto.ENUM,
        number=1,
        enum=Action,
    )
    action_condition: ActionCondition = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ActionCondition,
    )


class Environment(proto.Message):
    r"""An Environment describes a collection of environment
    variables to set when executing Tasks.

    Attributes:
        variables (MutableMapping[str, str]):
            A map of environment variable names to
            values.
        secret_variables (MutableMapping[str, str]):
            A map of environment variable names to Secret
            Manager secret names. The VM will access the
            named secrets to set the value of each
            environment variable.
        encrypted_variables (google.events.cloud.batch_v1.types.Environment.KMSEnvMap):
            An encrypted JSON dictionary where the
            key/value pairs correspond to environment
            variable names and their values.
    """

    class KMSEnvMap(proto.Message):
        r"""

        Attributes:
            key_name (str):
                The name of the KMS key that will be used to
                decrypt the cipher text.
            cipher_text (str):
                The value of the cipherText response from the ``encrypt``
                method.
        """

        key_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        cipher_text: str = proto.Field(
            proto.STRING,
            number=2,
        )

    variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    secret_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    encrypted_variables: KMSEnvMap = proto.Field(
        proto.MESSAGE,
        number=3,
        message=KMSEnvMap,
    )


class Job(proto.Message):
    r"""The Cloud Batch Job description.

    Attributes:
        name (str):
            Output only. Job name.
            For example:
            "projects/123456/locations/us-central1/jobs/job01".
        uid (str):
            Output only. A system generated unique ID (in
            UUID4 format) for the Job.
        priority (int):
            Priority of the Job. The valid value range is [0, 100).
            Default value is 0. Higher value indicates higher priority.
            A job with higher priority value is more likely to run
            earlier if all other requirements are satisfied.
        task_groups (MutableSequence[google.events.cloud.batch_v1.types.TaskGroup]):
            Required. TaskGroups in the Job. Only one
            TaskGroup is supported now.
        allocation_policy (google.events.cloud.batch_v1.types.AllocationPolicy):
            Compute resource allocation for all
            TaskGroups in the Job.
        labels (MutableMapping[str, str]):
            Labels for the Job. Labels could be user provided or system
            generated. For example, "labels": { "department": "finance",
            "environment": "test" } You can assign up to 64 labels.
            `Google Compute Engine label
            restrictions <https://cloud.google.com/compute/docs/labeling-resources#restrictions>`__
            apply. Label names that start with "goog-" or "google-" are
            reserved.
        status (google.events.cloud.batch_v1.types.JobStatus):
            Output only. Job status. It is read only for
            users.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the Job was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time the Job was
            updated.
        logs_policy (google.events.cloud.batch_v1.types.LogsPolicy):
            Log preservation policy for the Job.
        notifications (MutableSequence[google.events.cloud.batch_v1.types.JobNotification]):
            Notification configurations.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    priority: int = proto.Field(
        proto.INT64,
        number=3,
    )
    task_groups: MutableSequence['TaskGroup'] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message='TaskGroup',
    )
    allocation_policy: 'AllocationPolicy' = proto.Field(
        proto.MESSAGE,
        number=7,
        message='AllocationPolicy',
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    status: 'JobStatus' = proto.Field(
        proto.MESSAGE,
        number=9,
        message='JobStatus',
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    logs_policy: 'LogsPolicy' = proto.Field(
        proto.MESSAGE,
        number=13,
        message='LogsPolicy',
    )
    notifications: MutableSequence['JobNotification'] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message='JobNotification',
    )


class LogsPolicy(proto.Message):
    r"""LogsPolicy describes how outputs from a Job's Tasks
    (stdout/stderr) will be preserved.

    Attributes:
        destination (google.events.cloud.batch_v1.types.LogsPolicy.Destination):
            Where logs should be saved.
        logs_path (str):
            The path to which logs are saved when the
            destination = PATH. This can be a local file
            path on the VM, or under the mount point of a
            Persistent Disk or Filestore, or a Cloud Storage
            path.
    """
    class Destination(proto.Enum):
        r"""The destination (if any) for logs.

        Values:
            DESTINATION_UNSPECIFIED (0):
                Logs are not preserved.
            CLOUD_LOGGING (1):
                Logs are streamed to Cloud Logging.
            PATH (2):
                Logs are saved to a file path.
        """
        DESTINATION_UNSPECIFIED = 0
        CLOUD_LOGGING = 1
        PATH = 2

    destination: Destination = proto.Field(
        proto.ENUM,
        number=1,
        enum=Destination,
    )
    logs_path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class JobStatus(proto.Message):
    r"""Job status.

    Attributes:
        state (google.events.cloud.batch_v1.types.JobStatus.State):
            Job state
        status_events (MutableSequence[google.events.cloud.batch_v1.types.StatusEvent]):
            Job status events
        task_groups (MutableMapping[str, google.events.cloud.batch_v1.types.JobStatus.TaskGroupStatus]):
            Aggregated task status for each TaskGroup in
            the Job. The map key is TaskGroup ID.
        run_duration (google.protobuf.duration_pb2.Duration):
            The duration of time that the Job spent in
            status RUNNING.
    """
    class State(proto.Enum):
        r"""Valid Job states.

        Values:
            STATE_UNSPECIFIED (0):
                Job state unspecified.
            QUEUED (1):
                Job is admitted (validated and persisted) and
                waiting for resources.
            SCHEDULED (2):
                Job is scheduled to run as soon as resource
                allocation is ready. The resource allocation may
                happen at a later time but with a high chance to
                succeed.
            RUNNING (3):
                Resource allocation has been successful. At
                least one Task in the Job is RUNNING.
            SUCCEEDED (4):
                All Tasks in the Job have finished
                successfully.
            FAILED (5):
                At least one Task in the Job has failed.
            DELETION_IN_PROGRESS (6):
                The Job will be deleted, but has not been
                deleted yet. Typically this is because resources
                used by the Job are still being cleaned up.
        """
        STATE_UNSPECIFIED = 0
        QUEUED = 1
        SCHEDULED = 2
        RUNNING = 3
        SUCCEEDED = 4
        FAILED = 5
        DELETION_IN_PROGRESS = 6

    class InstanceStatus(proto.Message):
        r"""VM instance status.

        Attributes:
            machine_type (str):
                The Compute Engine machine type.
            provisioning_model (google.events.cloud.batch_v1.types.AllocationPolicy.ProvisioningModel):
                The VM instance provisioning model.
            task_pack (int):
                The max number of tasks can be assigned to
                this instance type.
            boot_disk (google.events.cloud.batch_v1.types.AllocationPolicy.Disk):
                The VM boot disk.
        """

        machine_type: str = proto.Field(
            proto.STRING,
            number=1,
        )
        provisioning_model: 'AllocationPolicy.ProvisioningModel' = proto.Field(
            proto.ENUM,
            number=2,
            enum='AllocationPolicy.ProvisioningModel',
        )
        task_pack: int = proto.Field(
            proto.INT64,
            number=3,
        )
        boot_disk: 'AllocationPolicy.Disk' = proto.Field(
            proto.MESSAGE,
            number=4,
            message='AllocationPolicy.Disk',
        )

    class TaskGroupStatus(proto.Message):
        r"""Aggregated task status for a TaskGroup.

        Attributes:
            counts (MutableMapping[str, int]):
                Count of task in each state in the TaskGroup.
                The map key is task state name.
            instances (MutableSequence[google.events.cloud.batch_v1.types.JobStatus.InstanceStatus]):
                Status of instances allocated for the
                TaskGroup.
        """

        counts: MutableMapping[str, int] = proto.MapField(
            proto.STRING,
            proto.INT64,
            number=1,
        )
        instances: MutableSequence['JobStatus.InstanceStatus'] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message='JobStatus.InstanceStatus',
        )

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    status_events: MutableSequence['StatusEvent'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='StatusEvent',
    )
    task_groups: MutableMapping[str, TaskGroupStatus] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=4,
        message=TaskGroupStatus,
    )
    run_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )


class JobNotification(proto.Message):
    r"""Notification configurations.

    Attributes:
        pubsub_topic (str):
            The Pub/Sub topic where notifications like the job state
            changes will be published. This topic exist in the same
            project as the job and billings will be charged to this
            project. If not specified, no Pub/Sub messages will be sent.
            Topic format: ``projects/{project}/topics/{topic}``.
        message (google.events.cloud.batch_v1.types.JobNotification.Message):
            The attribute requirements of messages to be
            sent to this Pub/Sub topic. Without this field,
            no message will be sent.
    """
    class Type(proto.Enum):
        r"""The message type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified.
            JOB_STATE_CHANGED (1):
                Notify users that the job state has changed.
            TASK_STATE_CHANGED (2):
                Notify users that the task state has changed.
        """
        TYPE_UNSPECIFIED = 0
        JOB_STATE_CHANGED = 1
        TASK_STATE_CHANGED = 2

    class Message(proto.Message):
        r"""Message details.
        Describe the attribute that a message should have.
        Without specified message attributes, no message will be sent by
        default.

        Attributes:
            type_ (google.events.cloud.batch_v1.types.JobNotification.Type):
                The message type.
            new_job_state (google.events.cloud.batch_v1.types.JobStatus.State):
                The new job state.
            new_task_state (google.events.cloud.batch_v1.types.TaskStatus.State):
                The new task state.
        """

        type_: 'JobNotification.Type' = proto.Field(
            proto.ENUM,
            number=1,
            enum='JobNotification.Type',
        )
        new_job_state: 'JobStatus.State' = proto.Field(
            proto.ENUM,
            number=2,
            enum='JobStatus.State',
        )
        new_task_state: 'TaskStatus.State' = proto.Field(
            proto.ENUM,
            number=3,
            enum='TaskStatus.State',
        )

    pubsub_topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message: Message = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Message,
    )


class AllocationPolicy(proto.Message):
    r"""A Job's resource allocation policy describes when, where, and
    how compute resources should be allocated for the Job.

    Attributes:
        location (google.events.cloud.batch_v1.types.AllocationPolicy.LocationPolicy):
            Location where compute resources should be
            allocated for the Job.
        instances (MutableSequence[google.events.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate]):
            Describe instances that can be created by this
            AllocationPolicy. Only instances[0] is supported now.
        service_account (google.events.cloud.batch_v1.types.ServiceAccount):
            Service account that VMs will run as.
        labels (MutableMapping[str, str]):
            Labels applied to all VM instances and other resources
            created by AllocationPolicy. Labels could be user provided
            or system generated. You can assign up to 64 labels. `Google
            Compute Engine label
            restrictions <https://cloud.google.com/compute/docs/labeling-resources#restrictions>`__
            apply. Label names that start with "goog-" or "google-" are
            reserved.
        network (google.events.cloud.batch_v1.types.AllocationPolicy.NetworkPolicy):
            The network policy.
        placement (google.events.cloud.batch_v1.types.AllocationPolicy.PlacementPolicy):
            The placement policy.
    """
    class ProvisioningModel(proto.Enum):
        r"""Compute Engine VM instance provisioning model.

        Values:
            PROVISIONING_MODEL_UNSPECIFIED (0):
                Unspecified.
            STANDARD (1):
                Standard VM.
            SPOT (2):
                SPOT VM.
            PREEMPTIBLE (3):
                Preemptible VM (PVM).

                Above SPOT VM is the preferable model for
                preemptible VM instances: the old preemptible VM
                model (indicated by this field) is the older
                model, and has been migrated to use the SPOT
                model as the underlying technology. This old
                model will still be supported.
        """
        PROVISIONING_MODEL_UNSPECIFIED = 0
        STANDARD = 1
        SPOT = 2
        PREEMPTIBLE = 3

    class LocationPolicy(proto.Message):
        r"""

        Attributes:
            allowed_locations (MutableSequence[str]):
                A list of allowed location names represented by internal
                URLs.

                Each location can be a region or a zone. Only one region or
                multiple zones in one region is supported now. For example,
                ["regions/us-central1"] allow VMs in any zones in region
                us-central1. ["zones/us-central1-a", "zones/us-central1-c"]
                only allow VMs in zones us-central1-a and us-central1-c.

                All locations end up in different regions would cause
                errors. For example, ["regions/us-central1",
                "zones/us-central1-a", "zones/us-central1-b",
                "zones/us-west1-a"] contains 2 regions "us-central1" and
                "us-west1". An error is expected in this case.
        """

        allowed_locations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class Disk(proto.Message):
        r"""A new persistent disk or a local ssd.
        A VM can only have one local SSD setting but multiple local SSD
        partitions. See
        https://cloud.google.com/compute/docs/disks#pdspecs and
        https://cloud.google.com/compute/docs/disks#localssds.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            image (str):
                Name of a public or custom image used as the data source.
                For example, the following are all valid URLs:

                -  Specify the image by its family name:
                   projects/{project}/global/images/family/{image_family}
                -  Specify the image version:
                   projects/{project}/global/images/{image_version}

                You can also use Batch customized image in short names. The
                following image values are supported for a boot disk:

                -  "batch-debian": use Batch Debian images.
                -  "batch-centos": use Batch CentOS images.
                -  "batch-cos": use Batch Container-Optimized images.
                -  "batch-hpc-centos": use Batch HPC CentOS images.

                This field is a member of `oneof`_ ``data_source``.
            snapshot (str):
                Name of a snapshot used as the data source.
                Snapshot is not supported as boot disk now.

                This field is a member of `oneof`_ ``data_source``.
            type_ (str):
                Disk type as shown in ``gcloud compute disk-types list``.
                For example, local SSD uses type "local-ssd". Persistent
                disks and boot disks use "pd-balanced", "pd-extreme",
                "pd-ssd" or "pd-standard".
            size_gb (int):
                Disk size in GB.

                For persistent disk, this field is ignored if
                ``data_source`` is ``image`` or ``snapshot``. For local SSD,
                size_gb should be a multiple of 375GB, otherwise, the final
                size will be the next greater multiple of 375 GB. For boot
                disk, Batch will calculate the boot disk size based on
                source image and task requirements if you do not speicify
                the size. If both this field and the boot_disk_mib field in
                task spec's compute_resource are defined, Batch will only
                honor this field.
            disk_interface (str):
                Local SSDs are available through both "SCSI"
                and "NVMe" interfaces. If not indicated, "NVMe"
                will be the default one for local ssds. We only
                support "SCSI" for persistent disks now.
        """

        image: str = proto.Field(
            proto.STRING,
            number=4,
            oneof='data_source',
        )
        snapshot: str = proto.Field(
            proto.STRING,
            number=5,
            oneof='data_source',
        )
        type_: str = proto.Field(
            proto.STRING,
            number=1,
        )
        size_gb: int = proto.Field(
            proto.INT64,
            number=2,
        )
        disk_interface: str = proto.Field(
            proto.STRING,
            number=6,
        )

    class AttachedDisk(proto.Message):
        r"""A new or an existing persistent disk (PD) or a local ssd
        attached to a VM instance.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            new_disk (google.events.cloud.batch_v1.types.AllocationPolicy.Disk):

                This field is a member of `oneof`_ ``attached``.
            existing_disk (str):
                Name of an existing PD.

                This field is a member of `oneof`_ ``attached``.
            device_name (str):
                Device name that the guest operating system will see. It is
                used by Runnable.volumes field to mount disks. So please
                specify the device_name if you want Batch to help mount the
                disk, and it should match the device_name field in volumes.
        """

        new_disk: 'AllocationPolicy.Disk' = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof='attached',
            message='AllocationPolicy.Disk',
        )
        existing_disk: str = proto.Field(
            proto.STRING,
            number=2,
            oneof='attached',
        )
        device_name: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class Accelerator(proto.Message):
        r"""Accelerator describes Compute Engine accelerators to be
        attached to the VM.

        Attributes:
            type_ (str):
                The accelerator type. For example, "nvidia-tesla-t4". See
                ``gcloud compute accelerator-types list``.
            count (int):
                The number of accelerators of this type.
            install_gpu_drivers (bool):
                Deprecated: please use instances[0].install_gpu_drivers
                instead.
        """

        type_: str = proto.Field(
            proto.STRING,
            number=1,
        )
        count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        install_gpu_drivers: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class InstancePolicy(proto.Message):
        r"""InstancePolicy describes an instance type and resources
        attached to each VM created by this InstancePolicy.

        Attributes:
            machine_type (str):
                The Compute Engine machine type.
            min_cpu_platform (str):
                The minimum CPU platform.
                See
                https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform.
            provisioning_model (google.events.cloud.batch_v1.types.AllocationPolicy.ProvisioningModel):
                The provisioning model.
            accelerators (MutableSequence[google.events.cloud.batch_v1.types.AllocationPolicy.Accelerator]):
                The accelerators attached to each VM
                instance.
            boot_disk (google.events.cloud.batch_v1.types.AllocationPolicy.Disk):
                Boot disk to be created and attached to each
                VM by this InstancePolicy. Boot disk will be
                deleted when the VM is deleted. Batch API now
                only supports booting from image.
            disks (MutableSequence[google.events.cloud.batch_v1.types.AllocationPolicy.AttachedDisk]):
                Non-boot disks to be attached for each VM
                created by this InstancePolicy. New disks will
                be deleted when the VM is deleted.
        """

        machine_type: str = proto.Field(
            proto.STRING,
            number=2,
        )
        min_cpu_platform: str = proto.Field(
            proto.STRING,
            number=3,
        )
        provisioning_model: 'AllocationPolicy.ProvisioningModel' = proto.Field(
            proto.ENUM,
            number=4,
            enum='AllocationPolicy.ProvisioningModel',
        )
        accelerators: MutableSequence['AllocationPolicy.Accelerator'] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message='AllocationPolicy.Accelerator',
        )
        boot_disk: 'AllocationPolicy.Disk' = proto.Field(
            proto.MESSAGE,
            number=8,
            message='AllocationPolicy.Disk',
        )
        disks: MutableSequence['AllocationPolicy.AttachedDisk'] = proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message='AllocationPolicy.AttachedDisk',
        )

    class InstancePolicyOrTemplate(proto.Message):
        r"""Either an InstancePolicy or an instance template.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            policy (google.events.cloud.batch_v1.types.AllocationPolicy.InstancePolicy):
                InstancePolicy.

                This field is a member of `oneof`_ ``policy_template``.
            instance_template (str):
                Name of an instance template used to create VMs. Named the
                field as 'instance_template' instead of 'template' to avoid
                c++ keyword conflict.

                This field is a member of `oneof`_ ``policy_template``.
            install_gpu_drivers (bool):
                Set this field true if users want Batch to help fetch
                drivers from a third party location and install them for
                GPUs specified in policy.accelerators or instance_template
                on their behalf. Default is false.
        """

        policy: 'AllocationPolicy.InstancePolicy' = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof='policy_template',
            message='AllocationPolicy.InstancePolicy',
        )
        instance_template: str = proto.Field(
            proto.STRING,
            number=2,
            oneof='policy_template',
        )
        install_gpu_drivers: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class NetworkInterface(proto.Message):
        r"""A network interface.

        Attributes:
            network (str):
                The URL of an existing network resource. You can specify the
                network as a full or partial URL.

                For example, the following are all valid URLs:

                -  https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}
                -  projects/{project}/global/networks/{network}
                -  global/networks/{network}
            subnetwork (str):
                The URL of an existing subnetwork resource in the network.
                You can specify the subnetwork as a full or partial URL.

                For example, the following are all valid URLs:

                -  https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/subnetworks/{subnetwork}
                -  projects/{project}/regions/{region}/subnetworks/{subnetwork}
                -  regions/{region}/subnetworks/{subnetwork}
            no_external_ip_address (bool):
                Default is false (with an external IP
                address). Required if no external public IP
                address is attached to the VM. If no external
                public IP address, additional configuration is
                required to allow the VM to access Google
                Services. See
                https://cloud.google.com/vpc/docs/configure-private-google-access
                and
                https://cloud.google.com/nat/docs/gce-example#create-nat
                for more information.
        """

        network: str = proto.Field(
            proto.STRING,
            number=1,
        )
        subnetwork: str = proto.Field(
            proto.STRING,
            number=2,
        )
        no_external_ip_address: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class NetworkPolicy(proto.Message):
        r"""NetworkPolicy describes VM instance network configurations.

        Attributes:
            network_interfaces (MutableSequence[google.events.cloud.batch_v1.types.AllocationPolicy.NetworkInterface]):
                Network configurations.
        """

        network_interfaces: MutableSequence['AllocationPolicy.NetworkInterface'] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message='AllocationPolicy.NetworkInterface',
        )

    class PlacementPolicy(proto.Message):
        r"""PlacementPolicy describes a group placement policy for the
        VMs controlled by this AllocationPolicy.

        Attributes:
            collocation (str):
                UNSPECIFIED vs. COLLOCATED (default
                UNSPECIFIED). Use COLLOCATED when you want VMs
                to be located close to each other for low
                network latency between the VMs. No placement
                policy will be generated when collocation is
                UNSPECIFIED.
            max_distance (int):
                When specified, causes the job to fail if more than
                max_distance logical switches are required between VMs.
                Batch uses the most compact possible placement of VMs even
                when max_distance is not specified. An explicit max_distance
                makes that level of compactness a strict requirement. Not
                yet implemented
        """

        collocation: str = proto.Field(
            proto.STRING,
            number=1,
        )
        max_distance: int = proto.Field(
            proto.INT64,
            number=2,
        )

    location: LocationPolicy = proto.Field(
        proto.MESSAGE,
        number=1,
        message=LocationPolicy,
    )
    instances: MutableSequence[InstancePolicyOrTemplate] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=InstancePolicyOrTemplate,
    )
    service_account: 'ServiceAccount' = proto.Field(
        proto.MESSAGE,
        number=9,
        message='ServiceAccount',
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    network: NetworkPolicy = proto.Field(
        proto.MESSAGE,
        number=7,
        message=NetworkPolicy,
    )
    placement: PlacementPolicy = proto.Field(
        proto.MESSAGE,
        number=10,
        message=PlacementPolicy,
    )


class TaskGroup(proto.Message):
    r"""A TaskGroup defines one or more Tasks that all share the same
    TaskSpec.

    Attributes:
        name (str):
            Output only. TaskGroup name.
            The system generates this field based on parent
            Job name. For example:

            "projects/123456/locations/us-west1/jobs/job01/taskGroups/group01".
        task_spec (google.events.cloud.batch_v1.types.TaskSpec):
            Required. Tasks in the group share the same
            task spec.
        task_count (int):
            Number of Tasks in the TaskGroup.
            Default is 1.
        parallelism (int):
            Max number of tasks that can run in parallel. Default to
            min(task_count, 1000). Field parallelism must be 1 if the
            scheduling_policy is IN_ORDER.
        scheduling_policy (google.events.cloud.batch_v1.types.TaskGroup.SchedulingPolicy):
            Scheduling policy for Tasks in the TaskGroup. The default
            value is AS_SOON_AS_POSSIBLE.
        task_environments (MutableSequence[google.events.cloud.batch_v1.types.Environment]):
            An array of environment variable mappings, which are passed
            to Tasks with matching indices. If task_environments is used
            then task_count should not be specified in the request (and
            will be ignored). Task count will be the length of
            task_environments.

            Tasks get a BATCH_TASK_INDEX and BATCH_TASK_COUNT
            environment variable, in addition to any environment
            variables set in task_environments, specifying the number of
            Tasks in the Task's parent TaskGroup, and the specific
            Task's index in the TaskGroup (0 through BATCH_TASK_COUNT -
            1).
        task_count_per_node (int):
            Max number of tasks that can be run on a VM
            at the same time. If not specified, the system
            will decide a value based on available compute
            resources on a VM and task requirements.
        require_hosts_file (bool):
            When true, Batch will populate a file with a list of all VMs
            assigned to the TaskGroup and set the BATCH_HOSTS_FILE
            environment variable to the path of that file. Defaults to
            false.
        permissive_ssh (bool):
            When true, Batch will configure SSH to allow
            passwordless login between VMs running the Batch
            tasks in the same TaskGroup.
    """
    class SchedulingPolicy(proto.Enum):
        r"""How Tasks in the TaskGroup should be scheduled relative to
        each other.

        Values:
            SCHEDULING_POLICY_UNSPECIFIED (0):
                Unspecified.
            AS_SOON_AS_POSSIBLE (1):
                Run Tasks as soon as resources are available.

                Tasks might be executed in parallel depending on parallelism
                and task_count values.
            IN_ORDER (2):
                Run Tasks sequentially with increased task
                index.
        """
        SCHEDULING_POLICY_UNSPECIFIED = 0
        AS_SOON_AS_POSSIBLE = 1
        IN_ORDER = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    task_spec: 'TaskSpec' = proto.Field(
        proto.MESSAGE,
        number=3,
        message='TaskSpec',
    )
    task_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    parallelism: int = proto.Field(
        proto.INT64,
        number=5,
    )
    scheduling_policy: SchedulingPolicy = proto.Field(
        proto.ENUM,
        number=6,
        enum=SchedulingPolicy,
    )
    task_environments: MutableSequence['Environment'] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message='Environment',
    )
    task_count_per_node: int = proto.Field(
        proto.INT64,
        number=10,
    )
    require_hosts_file: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    permissive_ssh: bool = proto.Field(
        proto.BOOL,
        number=12,
    )


class ServiceAccount(proto.Message):
    r"""Carries information about a Google Cloud service account.

    Attributes:
        email (str):
            Email address of the service account. If not
            specified, the default Compute Engine service
            account for the project will be used. If
            instance template is being used, the service
            account has to be specified in the instance
            template and it has to match the email field
            here.
        scopes (MutableSequence[str]):
            List of scopes to be enabled for this service
            account on the VM, in addition to the
            cloud-platform API scope that will be added by
            default.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class JobEventData(proto.Message):
    r"""The data within all Job events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        payload (google.events.cloud.batch_v1.types.Job):
            Optional. The Job event payload. Unset for
            deletion events.

            This field is a member of `oneof`_ ``_payload``.
    """

    payload: 'Job' = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message='Job',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
