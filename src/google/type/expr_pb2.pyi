from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Expr(_message.Message):
    __slots__ = ["description", "expression", "location", "title"]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    EXPRESSION_FIELD_NUMBER: ClassVar[int]
    LOCATION_FIELD_NUMBER: ClassVar[int]
    TITLE_FIELD_NUMBER: ClassVar[int]
    description: str
    expression: str
    location: str
    title: str
    def __init__(
        self,
        expression: Optional[str] = ...,
        title: Optional[str] = ...,
        description: Optional[str] = ...,
        location: Optional[str] = ...,
    ) -> None: ...
