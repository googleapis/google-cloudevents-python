# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.events.cloud.scheduler.v1',
    manifest={
        'HttpMethod',
        'SchedulerJobData',
        'HttpTarget',
        'AppEngineHttpTarget',
        'PubsubTarget',
        'AppEngineRouting',
        'OAuthToken',
        'OidcToken',
        'Job',
        'RetryConfig',
        'JobEventData',
    },
)


class HttpMethod(proto.Enum):
    r"""The HTTP method used to execute the job.

    Values:
        HTTP_METHOD_UNSPECIFIED (0):
            HTTP method unspecified. Defaults to POST.
        POST (1):
            HTTP POST
        GET (2):
            HTTP GET
        HEAD (3):
            HTTP HEAD
        PUT (4):
            HTTP PUT
        DELETE (5):
            HTTP DELETE
        PATCH (6):
            HTTP PATCH
        OPTIONS (7):
            HTTP OPTIONS
    """
    HTTP_METHOD_UNSPECIFIED = 0
    POST = 1
    GET = 2
    HEAD = 3
    PUT = 4
    DELETE = 5
    PATCH = 6
    OPTIONS = 7


class SchedulerJobData(proto.Message):
    r"""Scheduler job data.

    Attributes:
        custom_data (bytes):
            The custom data the user specified when
            creating the scheduler source.
    """

    custom_data: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )


class HttpTarget(proto.Message):
    r"""Http target. The job will be pushed to the job handler by means of
    an HTTP request via an
    [http_method][google.cloud.scheduler.v1.HttpTarget.http_method] such
    as HTTP POST, HTTP GET, etc. The job is acknowledged by means of an
    HTTP response code in the range [200 - 299]. A failure to receive a
    response constitutes a failed execution. For a redirected request,
    the response returned by the redirected request is considered.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uri (str):
            Required. The full URI path that the request will be sent
            to. This string must begin with either "http://" or
            "https://". Some examples of valid values for
            [uri][google.cloud.scheduler.v1.HttpTarget.uri] are:
            ``http://acme.com`` and ``https://acme.com/sales:8080``.
            Cloud Scheduler will encode some characters for safety and
            compatibility. The maximum allowed URL length is 2083
            characters after encoding.
        http_method (google.events.cloud.scheduler_v1.types.HttpMethod):
            Which HTTP method to use for the request.
        headers (MutableMapping[str, str]):
            HTTP request headers.

            This map contains the header field names and values.

            The user can specify HTTP request headers to send with the
            job's HTTP request. Repeated headers are not supported, but
            a header value can contain commas.

            The following headers represent a subset of the headers that
            accompany the job's HTTP request. Some HTTP request headers
            are ignored or replaced. A partial list of headers that are
            ignored or replaced is below:

            -  Host: This will be computed by Cloud Scheduler and
               derived from
               [uri][google.cloud.scheduler.v1.HttpTarget.uri].
            -  ``Content-Length``: This will be computed by Cloud
               Scheduler.
            -  ``User-Agent``: This will be set to
               ``"Google-Cloud-Scheduler"``.
            -  ``X-Google-*``: Google internal use only.
            -  ``X-AppEngine-*``: Google internal use only.
            -  ``X-CloudScheduler``: This header will be set to true.
            -  ``X-CloudScheduler-JobName``: This header will contain
               the job name.
            -  ``X-CloudScheduler-ScheduleTime``: For Cloud Scheduler
               jobs specified in the unix-cron format, this header will
               contain the job schedule as an offset of UTC parsed
               according to RFC3339.

            If the job has a
            [body][google.cloud.scheduler.v1.HttpTarget.body] and the
            following headers are not set by the user, Cloud Scheduler
            sets default values:

            -  ``Content-Type``: This will be set to
               ``"application/octet-stream"``. You can override this
               default by explicitly setting ``Content-Type`` to a
               particular media type when creating the job. For example,
               you can set ``Content-Type`` to ``"application/json"``.

            The total size of headers must be less than 80KB.
        body (bytes):
            HTTP request body. A request body is allowed only if the
            HTTP method is POST, PUT, or PATCH. It is an error to set
            body on a job with an incompatible
            [HttpMethod][google.cloud.scheduler.v1.HttpMethod].
        oauth_token (google.events.cloud.scheduler_v1.types.OAuthToken):
            If specified, an `OAuth
            token <https://developers.google.com/identity/protocols/OAuth2>`__
            will be generated and attached as an ``Authorization``
            header in the HTTP request.

            This type of authorization should generally only be used
            when calling Google APIs hosted on \*.googleapis.com.

            This field is a member of `oneof`_ ``authorization_header``.
        oidc_token (google.events.cloud.scheduler_v1.types.OidcToken):
            If specified, an
            `OIDC <https://developers.google.com/identity/protocols/OpenIDConnect>`__
            token will be generated and attached as an ``Authorization``
            header in the HTTP request.

            This type of authorization can be used for many scenarios,
            including calling Cloud Run, or endpoints where you intend
            to validate the token yourself.

            This field is a member of `oneof`_ ``authorization_header``.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    http_method: 'HttpMethod' = proto.Field(
        proto.ENUM,
        number=2,
        enum='HttpMethod',
    )
    headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    body: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    oauth_token: 'OAuthToken' = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof='authorization_header',
        message='OAuthToken',
    )
    oidc_token: 'OidcToken' = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof='authorization_header',
        message='OidcToken',
    )


class AppEngineHttpTarget(proto.Message):
    r"""App Engine target. The job will be pushed to a job handler by means
    of an HTTP request via an
    [http_method][google.cloud.scheduler.v1.AppEngineHttpTarget.http_method]
    such as HTTP POST, HTTP GET, etc. The job is acknowledged by means
    of an HTTP response code in the range [200 - 299]. Error 503 is
    considered an App Engine system error instead of an application
    error. Requests returning error 503 will be retried regardless of
    retry configuration and not counted against retry counts. Any other
    response code, or a failure to receive a response before the
    deadline, constitutes a failed attempt.

    Attributes:
        http_method (google.events.cloud.scheduler_v1.types.HttpMethod):
            The HTTP method to use for the request. PATCH
            and OPTIONS are not permitted.
        app_engine_routing (google.events.cloud.scheduler_v1.types.AppEngineRouting):
            App Engine Routing setting for the job.
        relative_uri (str):
            The relative URI.

            The relative URL must begin with "/" and must be a valid
            HTTP relative URL. It can contain a path, query string
            arguments, and ``#`` fragments. If the relative URL is
            empty, then the root path "/" will be used. No spaces are
            allowed, and the maximum length allowed is 2083 characters.
        headers (MutableMapping[str, str]):
            HTTP request headers.

            This map contains the header field names and values. Headers
            can be set when the job is created.

            Cloud Scheduler sets some headers to default values:

            -  ``User-Agent``: By default, this header is
               ``"AppEngine-Google; (+http://code.google.com/appengine)"``.
               This header can be modified, but Cloud Scheduler will
               append
               ``"AppEngine-Google; (+http://code.google.com/appengine)"``
               to the modified ``User-Agent``.
            -  ``X-CloudScheduler``: This header will be set to true.
            -  ``X-CloudScheduler-JobName``: This header will contain
               the job name.
            -  ``X-CloudScheduler-ScheduleTime``: For Cloud Scheduler
               jobs specified in the unix-cron format, this header will
               contain the job schedule as an offset of UTC parsed
               according to RFC3339.

            If the job has a
            [body][google.cloud.scheduler.v1.AppEngineHttpTarget.body]
            and the following headers are not set by the user, Cloud
            Scheduler sets default values:

            -  ``Content-Type``: This will be set to
               ``"application/octet-stream"``. You can override this
               default by explicitly setting ``Content-Type`` to a
               particular media type when creating the job. For example,
               you can set ``Content-Type`` to ``"application/json"``.

            The headers below are output only. They cannot be set or
            overridden:

            -  ``Content-Length``: This is computed by Cloud Scheduler.
            -  ``X-Google-*``: For Google internal use only.
            -  ``X-AppEngine-*``: For Google internal use only.

            In addition, some App Engine headers, which contain
            job-specific information, are also be sent to the job
            handler.
        body (bytes):
            Body.

            HTTP request body. A request body is allowed only if the
            HTTP method is POST or PUT. It will result in invalid
            argument error to set a body on a job with an incompatible
            [HttpMethod][google.cloud.scheduler.v1.HttpMethod].
    """

    http_method: 'HttpMethod' = proto.Field(
        proto.ENUM,
        number=1,
        enum='HttpMethod',
    )
    app_engine_routing: 'AppEngineRouting' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='AppEngineRouting',
    )
    relative_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    body: bytes = proto.Field(
        proto.BYTES,
        number=5,
    )


class PubsubTarget(proto.Message):
    r"""Pub/Sub target. The job will be delivered by publishing a
    message to the given Pub/Sub topic.

    Attributes:
        topic_name (str):
            Required. The name of the Cloud Pub/Sub topic to which
            messages will be published when a job is delivered. The
            topic name must be in the same format as required by
            Pub/Sub's
            `PublishRequest.name <https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#publishrequest>`__,
            for example ``projects/PROJECT_ID/topics/TOPIC_ID``.

            The topic must be in the same project as the Cloud Scheduler
            job.
        data (bytes):
            The message payload for PubsubMessage.

            Pubsub message must contain either non-empty
            data, or at least one attribute.
        attributes (MutableMapping[str, str]):
            Attributes for PubsubMessage.

            Pubsub message must contain either non-empty
            data, or at least one attribute.
    """

    topic_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


class AppEngineRouting(proto.Message):
    r"""App Engine Routing.

    For more information about services, versions, and instances see `An
    Overview of App
    Engine <https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine>`__,
    `Microservices Architecture on Google App
    Engine <https://cloud.google.com/appengine/docs/python/microservices-on-app-engine>`__,
    `App Engine Standard request
    routing <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__,
    and `App Engine Flex request
    routing <https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed>`__.

    Attributes:
        service (str):
            App service.

            By default, the job is sent to the service which
            is the default service when the job is
            attempted.
        version (str):
            App version.

            By default, the job is sent to the version which
            is the default version when the job is
            attempted.
        instance (str):
            App instance.

            By default, the job is sent to an instance which is
            available when the job is attempted.

            Requests can only be sent to a specific instance if `manual
            scaling is used in App Engine
            Standard <https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine?#scaling_types_and_instance_classes>`__.
            App Engine Flex does not support instances. For more
            information, see `App Engine Standard request
            routing <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__
            and `App Engine Flex request
            routing <https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed>`__.
        host (str):
            Output only. The host that the job is sent to.

            For more information about how App Engine requests are
            routed, see
            `here <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__.

            The host is constructed as:

            -  ``host = [application_domain_name]``\
               ``| [service] + '.' + [application_domain_name]``\
               ``| [version] + '.' + [application_domain_name]``\
               ``| [version_dot_service]+ '.' + [application_domain_name]``\
               ``| [instance] + '.' + [application_domain_name]``\
               ``| [instance_dot_service] + '.' + [application_domain_name]``\
               ``| [instance_dot_version] + '.' + [application_domain_name]``\
               ``| [instance_dot_version_dot_service] + '.' + [application_domain_name]``

            -  ``application_domain_name`` = The domain name of the app,
               for example .appspot.com, which is associated with the
               job's project ID.

            -  ``service =``
               [service][google.cloud.scheduler.v1.AppEngineRouting.service]

            -  ``version =``
               [version][google.cloud.scheduler.v1.AppEngineRouting.version]

            -  ``version_dot_service =``
               [version][google.cloud.scheduler.v1.AppEngineRouting.version]
               ``+ '.' +``
               [service][google.cloud.scheduler.v1.AppEngineRouting.service]

            -  ``instance =``
               [instance][google.cloud.scheduler.v1.AppEngineRouting.instance]

            -  ``instance_dot_service =``
               [instance][google.cloud.scheduler.v1.AppEngineRouting.instance]
               ``+ '.' +``
               [service][google.cloud.scheduler.v1.AppEngineRouting.service]

            -  ``instance_dot_version =``
               [instance][google.cloud.scheduler.v1.AppEngineRouting.instance]
               ``+ '.' +``
               [version][google.cloud.scheduler.v1.AppEngineRouting.version]

            -  ``instance_dot_version_dot_service =``
               [instance][google.cloud.scheduler.v1.AppEngineRouting.instance]
               ``+ '.' +``
               [version][google.cloud.scheduler.v1.AppEngineRouting.version]
               ``+ '.' +``
               [service][google.cloud.scheduler.v1.AppEngineRouting.service]

            If
            [service][google.cloud.scheduler.v1.AppEngineRouting.service]
            is empty, then the job will be sent to the service which is
            the default service when the job is attempted.

            If
            [version][google.cloud.scheduler.v1.AppEngineRouting.version]
            is empty, then the job will be sent to the version which is
            the default version when the job is attempted.

            If
            [instance][google.cloud.scheduler.v1.AppEngineRouting.instance]
            is empty, then the job will be sent to an instance which is
            available when the job is attempted.

            If
            [service][google.cloud.scheduler.v1.AppEngineRouting.service],
            [version][google.cloud.scheduler.v1.AppEngineRouting.version],
            or
            [instance][google.cloud.scheduler.v1.AppEngineRouting.instance]
            is invalid, then the job will be sent to the default version
            of the default service when the job is attempted.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=3,
    )
    host: str = proto.Field(
        proto.STRING,
        number=4,
    )


class OAuthToken(proto.Message):
    r"""Contains information needed for generating an `OAuth
    token <https://developers.google.com/identity/protocols/OAuth2>`__.
    This type of authorization should generally only be used when
    calling Google APIs hosted on \*.googleapis.com.

    Attributes:
        service_account_email (str):
            `Service account
            email <https://cloud.google.com/iam/docs/service-accounts>`__
            to be used for generating OAuth token. The service account
            must be within the same project as the job. The caller must
            have iam.serviceAccounts.actAs permission for the service
            account.
        scope (str):
            OAuth scope to be used for generating OAuth
            access token. If not specified,
            "https://www.googleapis.com/auth/cloud-platform"
            will be used.
    """

    service_account_email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OidcToken(proto.Message):
    r"""Contains information needed for generating an `OpenID Connect
    token <https://developers.google.com/identity/protocols/OpenIDConnect>`__.
    This type of authorization can be used for many scenarios, including
    calling Cloud Run, or endpoints where you intend to validate the
    token yourself.

    Attributes:
        service_account_email (str):
            `Service account
            email <https://cloud.google.com/iam/docs/service-accounts>`__
            to be used for generating OIDC token. The service account
            must be within the same project as the job. The caller must
            have iam.serviceAccounts.actAs permission for the service
            account.
        audience (str):
            Audience to be used when generating OIDC
            token. If not specified, the URI specified in
            target will be used.
    """

    service_account_email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    audience: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Job(proto.Message):
    r"""Configuration for a job.
    The maximum allowed size for a job is 1MB.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Optionally caller-specified in
            [CreateJob][google.cloud.scheduler.v1.CloudScheduler.CreateJob],
            after which it becomes output only.

            The job name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.

            -  ``PROJECT_ID`` can contain letters ([A-Za-z]), numbers
               ([0-9]), hyphens (-), colons (:), or periods (.). For
               more information, see `Identifying
               projects <https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects>`__
            -  ``LOCATION_ID`` is the canonical ID for the job's
               location. The list of available locations can be obtained
               by calling
               [ListLocations][google.cloud.location.Locations.ListLocations].
               For more information, see
               https://cloud.google.com/about/locations/.
            -  ``JOB_ID`` can contain only letters ([A-Za-z]), numbers
               ([0-9]), hyphens (-), or underscores (_). The maximum
               length is 500 characters.
        description (str):
            Optionally caller-specified in
            [CreateJob][google.cloud.scheduler.v1.CloudScheduler.CreateJob]
            or
            [UpdateJob][google.cloud.scheduler.v1.CloudScheduler.UpdateJob].

            A human-readable description for the job. This string must
            not contain more than 500 characters.
        pubsub_target (google.events.cloud.scheduler_v1.types.PubsubTarget):
            Pub/Sub target.

            This field is a member of `oneof`_ ``target``.
        app_engine_http_target (google.events.cloud.scheduler_v1.types.AppEngineHttpTarget):
            App Engine HTTP target.

            This field is a member of `oneof`_ ``target``.
        http_target (google.events.cloud.scheduler_v1.types.HttpTarget):
            HTTP target.

            This field is a member of `oneof`_ ``target``.
        schedule (str):
            Required, except when used with
            [UpdateJob][google.cloud.scheduler.v1.CloudScheduler.UpdateJob].

            Describes the schedule on which the job will be executed.

            The schedule can be either of the following types:

            -  `Crontab <https://en.wikipedia.org/wiki/Cron#Overview>`__
            -  English-like
               `schedule <https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules>`__

            As a general rule, execution ``n + 1`` of a job will not
            begin until execution ``n`` has finished. Cloud Scheduler
            will never allow two simultaneously outstanding executions.
            For example, this implies that if the ``n+1``\ th execution
            is scheduled to run at 16:00 but the ``n``\ th execution
            takes until 16:15, the ``n+1``\ th execution will not start
            until ``16:15``. A scheduled start time will be delayed if
            the previous execution has not ended when its scheduled time
            occurs.

            If
            [retry_count][google.cloud.scheduler.v1.RetryConfig.retry_count]
            > 0 and a job attempt fails, the job will be tried a total
            of
            [retry_count][google.cloud.scheduler.v1.RetryConfig.retry_count]
            times, with exponential backoff, until the next scheduled
            start time. If retry_count is 0, a job attempt will not be
            retried if it fails. Instead the Cloud Scheduler system will
            wait for the next scheduled execution time. Setting
            retry_count to 0 does not prevent failed jobs from running
            according to schedule after the failure.
        time_zone (str):
            Specifies the time zone to be used in interpreting
            [schedule][google.cloud.scheduler.v1.Job.schedule]. The
            value of this field must be a time zone name from the `tz
            database <http://en.wikipedia.org/wiki/Tz_database>`__.

            Note that some time zones include a provision for daylight
            savings time. The rules for daylight saving time are
            determined by the chosen tz. For UTC use the string "utc".
            If a time zone is not specified, the default will be in UTC
            (also known as GMT).
        user_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the job.
        state (google.events.cloud.scheduler_v1.types.Job.State):
            Output only. State of the job.
        status (google.rpc.status_pb2.Status):
            Output only. The response from the target for
            the last attempted execution.
        schedule_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The next time the job is
            scheduled. Note that this may be a retry of a
            previously failed attempt or the next execution
            time according to the schedule.
        last_attempt_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the last job attempt
            started.
        retry_config (google.events.cloud.scheduler_v1.types.RetryConfig):
            Settings that determine the retry behavior.
        attempt_deadline (google.protobuf.duration_pb2.Duration):
            The deadline for job attempts. If the request handler does
            not respond by this deadline then the request is cancelled
            and the attempt is marked as a ``DEADLINE_EXCEEDED``
            failure. The failed attempt can be viewed in execution logs.
            Cloud Scheduler will retry the job according to the
            [RetryConfig][google.cloud.scheduler.v1.RetryConfig].

            The default and the allowed values depend on the type of
            target:

            -  For [HTTP
               targets][google.cloud.scheduler.v1.Job.http_target], the
               default is 3 minutes. The deadline must be in the
               interval [15 seconds, 30 minutes].

            -  For [App Engine HTTP
               targets][google.cloud.scheduler.v1.Job.app_engine_http_target],
               0 indicates that the request has the default deadline.
               The default deadline depends on the scaling type of the
               service: 10 minutes for standard apps with automatic
               scaling, 24 hours for standard apps with manual and basic
               scaling, and 60 minutes for flex apps. If the request
               deadline is set, it must be in the interval [15 seconds,
               24 hours 15 seconds].

            -  For [Pub/Sub
               targets][google.cloud.scheduler.v1.Job.pubsub_target],
               this field is ignored.
    """
    class State(proto.Enum):
        r"""State of the job.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            ENABLED (1):
                The job is executing normally.
            PAUSED (2):
                The job is paused by the user. It will not execute. A user
                can intentionally pause the job using
                [PauseJobRequest][google.cloud.scheduler.v1.PauseJobRequest].
            DISABLED (3):
                The job is disabled by the system due to
                error. The user cannot directly set a job to be
                disabled.
            UPDATE_FAILED (4):
                The job state resulting from a failed
                [CloudScheduler.UpdateJob][google.cloud.scheduler.v1.CloudScheduler.UpdateJob]
                operation. To recover a job from this state, retry
                [CloudScheduler.UpdateJob][google.cloud.scheduler.v1.CloudScheduler.UpdateJob]
                until a successful response is received.
        """
        STATE_UNSPECIFIED = 0
        ENABLED = 1
        PAUSED = 2
        DISABLED = 3
        UPDATE_FAILED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    pubsub_target: 'PubsubTarget' = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof='target',
        message='PubsubTarget',
    )
    app_engine_http_target: 'AppEngineHttpTarget' = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof='target',
        message='AppEngineHttpTarget',
    )
    http_target: 'HttpTarget' = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof='target',
        message='HttpTarget',
    )
    schedule: str = proto.Field(
        proto.STRING,
        number=20,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=21,
    )
    user_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=11,
        message=status_pb2.Status,
    )
    schedule_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=17,
        message=timestamp_pb2.Timestamp,
    )
    last_attempt_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=18,
        message=timestamp_pb2.Timestamp,
    )
    retry_config: 'RetryConfig' = proto.Field(
        proto.MESSAGE,
        number=19,
        message='RetryConfig',
    )
    attempt_deadline: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=22,
        message=duration_pb2.Duration,
    )


class RetryConfig(proto.Message):
    r"""Settings that determine the retry behavior.

    By default, if a job does not complete successfully (meaning that an
    acknowledgement is not received from the handler, then it will be
    retried with exponential backoff according to the settings in
    [RetryConfig][google.cloud.scheduler.v1.RetryConfig].

    Attributes:
        retry_count (int):
            The number of attempts that the system will make to run a
            job using the exponential backoff procedure described by
            [max_doublings][google.cloud.scheduler.v1.RetryConfig.max_doublings].

            The default value of retry_count is zero.

            If retry_count is 0, a job attempt will not be retried if it
            fails. Instead the Cloud Scheduler system will wait for the
            next scheduled execution time. Setting retry_count to 0 does
            not prevent failed jobs from running according to schedule
            after the failure.

            If retry_count is set to a non-zero number then Cloud
            Scheduler will retry failed attempts, using exponential
            backoff, retry_count times, or until the next scheduled
            execution time, whichever comes first.

            Values greater than 5 and negative values are not allowed.
        max_retry_duration (google.protobuf.duration_pb2.Duration):
            The time limit for retrying a failed job, measured from time
            when an execution was first attempted. If specified with
            [retry_count][google.cloud.scheduler.v1.RetryConfig.retry_count],
            the job will be retried until both limits are reached.

            The default value for max_retry_duration is zero, which
            means retry duration is unlimited.
        min_backoff_duration (google.protobuf.duration_pb2.Duration):
            The minimum amount of time to wait before
            retrying a job after it fails.

            The default value of this field is 5 seconds.
        max_backoff_duration (google.protobuf.duration_pb2.Duration):
            The maximum amount of time to wait before
            retrying a job after it fails.

            The default value of this field is 1 hour.
        max_doublings (int):
            The time between retries will double ``max_doublings``
            times.

            A job's retry interval starts at
            [min_backoff_duration][google.cloud.scheduler.v1.RetryConfig.min_backoff_duration],
            then doubles ``max_doublings`` times, then increases
            linearly, and finally retries at intervals of
            [max_backoff_duration][google.cloud.scheduler.v1.RetryConfig.max_backoff_duration]
            up to
            [retry_count][google.cloud.scheduler.v1.RetryConfig.retry_count]
            times.

            For example, if
            [min_backoff_duration][google.cloud.scheduler.v1.RetryConfig.min_backoff_duration]
            is 10s,
            [max_backoff_duration][google.cloud.scheduler.v1.RetryConfig.max_backoff_duration]
            is 300s, and ``max_doublings`` is 3, then the job will first
            be retried in 10s. The retry interval will double three
            times, and then increase linearly by 2^3 \* 10s. Finally,
            the job will retry at intervals of
            [max_backoff_duration][google.cloud.scheduler.v1.RetryConfig.max_backoff_duration]
            until the job has been attempted
            [retry_count][google.cloud.scheduler.v1.RetryConfig.retry_count]
            times. Thus, the requests will retry at 10s, 20s, 40s, 80s,
            160s, 240s, 300s, 300s, ....

            The default value of this field is 5.
    """

    retry_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    max_retry_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    min_backoff_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    max_backoff_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    max_doublings: int = proto.Field(
        proto.INT32,
        number=5,
    )


class JobEventData(proto.Message):
    r"""The data within all Job events.

    Attributes:
        payload (google.events.cloud.scheduler_v1.types.Job):
            Optional. The Job event payload. Unset for
            deletion events.
    """

    payload: 'Job' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Job',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
