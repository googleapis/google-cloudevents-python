# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Parse and validate text-formatted Cloud Event payload data in a variety of
# google types.

import importlib
import os
import unittest

from util import make_test_case


class TestdataParsing(unittest.TestCase):
    """Load testdata files from $GOOGLE_EVENTS_TESTDATA directory and verify parsing."""

    def setUp(self) -> None:
        self.testdata_root = os.getenv("GOOGLE_EVENTS_TESTDATA", "")
        if self.testdata_root == "":
            self.skipTest("set GOOGLE_EVENTS_TESTDATA to run these tests")
        return super().setUp()

    # sorted the order files appear when running the following command in the testdata dir:
    # find . -type f -name '*.json' | sort
    def test_LogEntryData(self):
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/audit/v1/LogEntryData-bigqueryjobcompleted.json",
            ),
            "google.events.cloud.audit_v1",
            "LogEntryData",
        )()
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/audit/v1/LogEntryData-pubsubCreateTopic.json",
            ),
            "google.events.cloud.audit_v1",
            "LogEntryData",
        )()

    def test_BuildEventData(self):
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/cloudbuild/v1/BuildEventData-simple.json",
            ),
            "google.events.cloud.cloudbuild_v1",
            "BuildEventData",
        )()
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/cloudbuild/v1/BuildEventData-complex.json",
            ),
            "google.events.cloud.cloudbuild_v1",
            "BuildEventData",
        )()

    def test_DocumentEventData(self):
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/firestore/v1/DocumentEventData-simple.json",
            ),
            "google.events.cloud.firestore_v1",
            "DocumentEventData",
        )()
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/firestore/v1/DocumentEventData-complex.json",
            ),
            "google.events.cloud.firestore_v1",
            "DocumentEventData",
        )()

    def test_MessagePublishedData(self):
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/pubsub/v1/MessagePublishedData-text.json",
            ),
            "google.events.cloud.pubsub_v1",
            "MessagePublishedData",
        )()
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/pubsub/v1/MessagePublishedData-binary.json",
            ),
            "google.events.cloud.pubsub_v1",
            "MessagePublishedData",
        )()
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/pubsub/v1/MessagePublishedData-duplicatedFields.json",
            ),
            "google.events.cloud.pubsub_v1",
            "MessagePublishedData",
        )()

    def test_SchedulerJobData(self):
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/scheduler/v1/SchedulerJobData-simple.json",
            ),
            "google.events.cloud.scheduler_v1",
            "SchedulerJobData",
        )()

    def test_StorageObjectData(self):
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/storage/v1/StorageObjectData-simple.json",
            ),
            "google.events.cloud.storage_v1",
            "StorageObjectData",
        )()
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/cloud/storage/v1/StorageObjectData-complex.json",
            ),
            "google.events.cloud.storage_v1",
            "StorageObjectData",
        )()

    def test_AnalyticsLogData(self):
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/firebase/analytics/v1/AnalyticsLogData-complex.json",
            ),
            "google.events.firebase.analytics_v1",
            "AnalyticsLogData",
        )()

    def test_AuthEventData(self):
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/firebase/auth/v1/AuthEventData-complex.json",
            ),
            "google.events.firebase.auth_v1",
            "AuthEventData",
        )()

    def test_ReferenceEventData(self):
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/firebase/database/v1/ReferenceEventData-simple.json",
            ),
            "google.events.firebase.database_v1",
            "ReferenceEventData",
        )()

    def test_RemoteConfigEventData(self):
        make_test_case(
            os.path.join(
                self.testdata_root,
                "google/events/firebase/remoteconfig/v1/RemoteConfigEventData-simple.json",
            ),
            "google.events.firebase.remoteconfig_v1",
            "RemoteConfigEventData",
        )()


if __name__ == "__main__":
    unittest.main()
