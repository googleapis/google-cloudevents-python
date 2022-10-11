from typing import ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DAY_OF_WEEK_UNSPECIFIED: DayOfWeek
DESCRIPTOR: _descriptor.FileDescriptor
FRIDAY: DayOfWeek
MONDAY: DayOfWeek
SATURDAY: DayOfWeek
SUNDAY: DayOfWeek
THURSDAY: DayOfWeek
TUESDAY: DayOfWeek
WEDNESDAY: DayOfWeek

class DayOfWeek(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
