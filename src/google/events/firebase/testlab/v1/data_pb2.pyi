from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor
ERROR: TestState
FAILURE: OutcomeSummary
FINISHED: TestState
INCONCLUSIVE: OutcomeSummary
INVALID: TestState
OUTCOME_SUMMARY_UNSPECIFIED: OutcomeSummary
PENDING: TestState
SKIPPED: OutcomeSummary
SUCCESS: OutcomeSummary
TEST_STATE_UNSPECIFIED: TestState
VALIDATING: TestState

class ClientInfo(_message.Message):
    __slots__ = ["client", "details"]
    class DetailsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(self, key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...
    CLIENT_FIELD_NUMBER: ClassVar[int]
    DETAILS_FIELD_NUMBER: ClassVar[int]
    client: str
    details: _containers.ScalarMap[str, str]
    def __init__(self, client: Optional[str] = ..., details: Optional[Mapping[str, str]] = ...) -> None: ...

class ResultStorage(_message.Message):
    __slots__ = ["gcs_path", "results_uri", "tool_results_execution", "tool_results_history"]
    GCS_PATH_FIELD_NUMBER: ClassVar[int]
    RESULTS_URI_FIELD_NUMBER: ClassVar[int]
    TOOL_RESULTS_EXECUTION_FIELD_NUMBER: ClassVar[int]
    TOOL_RESULTS_HISTORY_FIELD_NUMBER: ClassVar[int]
    gcs_path: str
    results_uri: str
    tool_results_execution: str
    tool_results_history: str
    def __init__(self, tool_results_history: Optional[str] = ..., tool_results_execution: Optional[str] = ..., results_uri: Optional[str] = ..., gcs_path: Optional[str] = ...) -> None: ...

class TestMatrixEventData(_message.Message):
    __slots__ = ["client_info", "create_time", "invalid_matrix_details", "outcome_summary", "result_storage", "state", "test_matrix_id"]
    CLIENT_INFO_FIELD_NUMBER: ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: ClassVar[int]
    INVALID_MATRIX_DETAILS_FIELD_NUMBER: ClassVar[int]
    OUTCOME_SUMMARY_FIELD_NUMBER: ClassVar[int]
    RESULT_STORAGE_FIELD_NUMBER: ClassVar[int]
    STATE_FIELD_NUMBER: ClassVar[int]
    TEST_MATRIX_ID_FIELD_NUMBER: ClassVar[int]
    client_info: ClientInfo
    create_time: _timestamp_pb2.Timestamp
    invalid_matrix_details: str
    outcome_summary: OutcomeSummary
    result_storage: ResultStorage
    state: TestState
    test_matrix_id: str
    def __init__(self, create_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., state: Optional[Union[TestState, str]] = ..., invalid_matrix_details: Optional[str] = ..., outcome_summary: Optional[Union[OutcomeSummary, str]] = ..., result_storage: Optional[Union[ResultStorage, Mapping]] = ..., client_info: Optional[Union[ClientInfo, Mapping]] = ..., test_matrix_id: Optional[str] = ...) -> None: ...

class TestState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class OutcomeSummary(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
