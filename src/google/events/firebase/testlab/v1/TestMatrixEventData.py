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
from typing import Optional, Dict, Union
from enum import Enum
from datetime import datetime


class ClientInfo:
    """Information provided by the client that created the test matrix.
    
    Information about the client which invoked the test.
    """
    """Client name, such as "gcloud"."""
    client: Optional[str]
    """Map of detailed information about the client."""
    details: Optional[Dict[str, str]]

    def __init__(self, client: Optional[str], details: Optional[Dict[str, str]]) -> None:
        self.client = client
        self.details = details


class OutcomeSummaryEnum(Enum):
    FAILURE = "FAILURE"
    INCONCLUSIVE = "INCONCLUSIVE"
    OUTCOME_SUMMARY_UNSPECIFIED = "OUTCOME_SUMMARY_UNSPECIFIED"
    SKIPPED = "SKIPPED"
    SUCCESS = "SUCCESS"


class ResultStorage:
    """Locations where test results are stored."""
    """Location in Google Cloud Storage where test results are written to.
    In the form "gs://bucket/path/to/somewhere".
    """
    gcs_path: Optional[str]
    """URI to the test results in the Firebase Web Console."""
    results_uri: Optional[str]
    """Tool Results execution resource containing test results. Format is
    `projects/{project_id}/histories/{history_id}/executions/{execution_id}`.
    Optional, can be omitted in erroneous test states.
    See https://firebase.google.com/docs/test-lab/reference/toolresults/rest
    for more information.
    """
    tool_results_execution: Optional[str]
    """Tool Results history resource containing test results. Format is
    `projects/{project_id}/histories/{history_id}`.
    See https://firebase.google.com/docs/test-lab/reference/toolresults/rest
    for more information.
    """
    tool_results_history: Optional[str]

    def __init__(self, gcs_path: Optional[str], results_uri: Optional[str], tool_results_execution: Optional[str], tool_results_history: Optional[str]) -> None:
        self.gcs_path = gcs_path
        self.results_uri = results_uri
        self.tool_results_execution = tool_results_execution
        self.tool_results_history = tool_results_history


class StateEnum(Enum):
    ERROR = "ERROR"
    FINISHED = "FINISHED"
    INVALID = "INVALID"
    PENDING = "PENDING"
    TEST_STATE_UNSPECIFIED = "TEST_STATE_UNSPECIFIED"
    VALIDATING = "VALIDATING"


class TestMatrixEventData:
    """The data within all Firebase test matrix events."""
    """Information provided by the client that created the test matrix."""
    client_info: Optional[ClientInfo]
    """Time the test matrix was created."""
    create_time: Optional[datetime]
    """Code that describes why the test matrix is considered invalid. Only set for
    matrices in the INVALID state.
    """
    invalid_matrix_details: Optional[str]
    """Outcome summary of the test matrix."""
    outcome_summary: Union[OutcomeSummaryEnum, int, None]
    """Locations where test results are stored."""
    result_storage: Optional[ResultStorage]
    """State of the test matrix."""
    state: Union[StateEnum, int, None]
    """ID of the test matrix this event belongs to."""
    test_matrix_id: Optional[str]

    def __init__(self, client_info: Optional[ClientInfo], create_time: Optional[datetime], invalid_matrix_details: Optional[str], outcome_summary: Union[OutcomeSummaryEnum, int, None], result_storage: Optional[ResultStorage], state: Union[StateEnum, int, None], test_matrix_id: Optional[str]) -> None:
        self.client_info = client_info
        self.create_time = create_time
        self.invalid_matrix_details = invalid_matrix_details
        self.outcome_summary = outcome_summary
        self.result_storage = result_storage
        self.state = state
        self.test_matrix_id = test_matrix_id
