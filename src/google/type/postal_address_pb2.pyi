from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PostalAddress(_message.Message):
    __slots__ = [
        "address_lines",
        "administrative_area",
        "language_code",
        "locality",
        "organization",
        "postal_code",
        "recipients",
        "region_code",
        "revision",
        "sorting_code",
        "sublocality",
    ]
    ADDRESS_LINES_FIELD_NUMBER: ClassVar[int]
    ADMINISTRATIVE_AREA_FIELD_NUMBER: ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: ClassVar[int]
    LOCALITY_FIELD_NUMBER: ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: ClassVar[int]
    REGION_CODE_FIELD_NUMBER: ClassVar[int]
    REVISION_FIELD_NUMBER: ClassVar[int]
    SORTING_CODE_FIELD_NUMBER: ClassVar[int]
    SUBLOCALITY_FIELD_NUMBER: ClassVar[int]
    address_lines: _containers.RepeatedScalarFieldContainer[str]
    administrative_area: str
    language_code: str
    locality: str
    organization: str
    postal_code: str
    recipients: _containers.RepeatedScalarFieldContainer[str]
    region_code: str
    revision: int
    sorting_code: str
    sublocality: str
    def __init__(
        self,
        revision: Optional[int] = ...,
        region_code: Optional[str] = ...,
        language_code: Optional[str] = ...,
        postal_code: Optional[str] = ...,
        sorting_code: Optional[str] = ...,
        administrative_area: Optional[str] = ...,
        locality: Optional[str] = ...,
        sublocality: Optional[str] = ...,
        address_lines: Optional[Iterable[str]] = ...,
        recipients: Optional[Iterable[str]] = ...,
        organization: Optional[str] = ...,
    ) -> None: ...
