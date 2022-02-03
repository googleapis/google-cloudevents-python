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
#     result = document_event_data_from_dict(json.loads(json_string))

from typing import Optional, Any, Union, Dict, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


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


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class GeoPointValue:
    """A geo point value representing a point on the surface of Earth."""
    """The latitude in degrees. It must be in the range [-90.0, +90.0]."""
    latitude: Optional[float]
    """The longitude in degrees. It must be in the range [-180.0, +180.0]."""
    longitude: Optional[float]

    def __init__(self, latitude: Optional[float], longitude: Optional[float]) -> None:
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def from_dict(obj: Any) -> 'GeoPointValue':
        assert isinstance(obj, dict)
        latitude = from_union([from_float, from_none], obj.get("latitude"))
        longitude = from_union([from_float, from_none], obj.get("longitude"))
        return GeoPointValue(latitude, longitude)

    def to_dict(self) -> dict:
        result: dict = {}
        result["latitude"] = from_union([to_float, from_none], self.latitude)
        result["longitude"] = from_union([to_float, from_none], self.longitude)
        return result


class MapValueField:
    """A message that can hold any of the supported value types."""
    """An array value.
    
    Cannot directly contain another array value, though can contain an
    map which contains another array.
    """
    array_value: Optional['ArrayValue']
    """A boolean value."""
    boolean_value: Optional[bool]
    """A bytes value.
    
    Must not exceed 1 MiB - 89 bytes.
    Only the first 1,500 bytes are considered by queries.
    """
    bytes_value: Optional[str]
    """A double value."""
    double_value: Optional[float]
    """A geo point value representing a point on the surface of Earth."""
    geo_point_value: Optional[GeoPointValue]
    """An integer value."""
    integer_value: Optional[str]
    """A map value."""
    map_value: Optional['MapValue']
    """A null value."""
    null_value: Union[int, None, str]
    """A reference to a document. For example:
    `projects/{project_id}/databases/{database_id}/documents/{document_path}`.
    """
    reference_value: Optional[str]
    """A string value.
    
    The string, represented as UTF-8, must not exceed 1 MiB - 89 bytes.
    Only the first 1,500 bytes of the UTF-8 representation are considered by
    queries.
    """
    string_value: Optional[str]
    """A timestamp value.
    
    Precise only to microseconds. When stored, any additional precision is
    rounded down.
    """
    timestamp_value: Optional[datetime]

    def __init__(self, array_value: Optional['ArrayValue'], boolean_value: Optional[bool], bytes_value: Optional[str], double_value: Optional[float], geo_point_value: Optional[GeoPointValue], integer_value: Optional[str], map_value: Optional['MapValue'], null_value: Union[int, None, str], reference_value: Optional[str], string_value: Optional[str], timestamp_value: Optional[datetime]) -> None:
        self.array_value = array_value
        self.boolean_value = boolean_value
        self.bytes_value = bytes_value
        self.double_value = double_value
        self.geo_point_value = geo_point_value
        self.integer_value = integer_value
        self.map_value = map_value
        self.null_value = null_value
        self.reference_value = reference_value
        self.string_value = string_value
        self.timestamp_value = timestamp_value

    @staticmethod
    def from_dict(obj: Any) -> 'MapValueField':
        assert isinstance(obj, dict)
        array_value = from_union([ArrayValue.from_dict, from_none], obj.get("arrayValue"))
        boolean_value = from_union([from_bool, from_none], obj.get("booleanValue"))
        bytes_value = from_union([from_str, from_none], obj.get("bytesValue"))
        double_value = from_union([from_float, from_none], obj.get("doubleValue"))
        geo_point_value = from_union([GeoPointValue.from_dict, from_none], obj.get("geoPointValue"))
        integer_value = from_union([from_str, from_none], obj.get("integerValue"))
        map_value = from_union([MapValue.from_dict, from_none], obj.get("mapValue"))
        null_value = from_union([from_int, from_str, from_none], obj.get("nullValue"))
        reference_value = from_union([from_str, from_none], obj.get("referenceValue"))
        string_value = from_union([from_str, from_none], obj.get("stringValue"))
        timestamp_value = from_union([from_datetime, from_none], obj.get("timestampValue"))
        return MapValueField(array_value, boolean_value, bytes_value, double_value, geo_point_value, integer_value, map_value, null_value, reference_value, string_value, timestamp_value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["arrayValue"] = from_union([lambda x: to_class(ArrayValue, x), from_none], self.array_value)
        result["booleanValue"] = from_union([from_bool, from_none], self.boolean_value)
        result["bytesValue"] = from_union([from_str, from_none], self.bytes_value)
        result["doubleValue"] = from_union([to_float, from_none], self.double_value)
        result["geoPointValue"] = from_union([lambda x: to_class(GeoPointValue, x), from_none], self.geo_point_value)
        result["integerValue"] = from_union([from_str, from_none], self.integer_value)
        result["mapValue"] = from_union([lambda x: to_class(MapValue, x), from_none], self.map_value)
        result["nullValue"] = from_union([from_int, from_str, from_none], self.null_value)
        result["referenceValue"] = from_union([from_str, from_none], self.reference_value)
        result["stringValue"] = from_union([from_str, from_none], self.string_value)
        result["timestampValue"] = from_union([lambda x: x.isoformat(), from_none], self.timestamp_value)
        return result


class MapValue:
    """A map value."""
    """The map's fields.
    
    The map keys represent field names. Field names matching the regular
    expression `__.*__` are reserved. Reserved field names are forbidden except
    in certain documented contexts. The map keys, represented as UTF-8, must
    not exceed 1,500 bytes and cannot be empty.
    """
    fields: Optional[Dict[str, MapValueField]]

    def __init__(self, fields: Optional[Dict[str, MapValueField]]) -> None:
        self.fields = fields

    @staticmethod
    def from_dict(obj: Any) -> 'MapValue':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_dict(MapValueField.from_dict, x), from_none], obj.get("fields"))
        return MapValue(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_dict(lambda x: to_class(MapValueField, x), x), from_none], self.fields)
        return result


class ValueElement:
    """A message that can hold any of the supported value types."""
    """An array value.
    
    Cannot directly contain another array value, though can contain an
    map which contains another array.
    """
    array_value: Optional['ArrayValue']
    """A boolean value."""
    boolean_value: Optional[bool]
    """A bytes value.
    
    Must not exceed 1 MiB - 89 bytes.
    Only the first 1,500 bytes are considered by queries.
    """
    bytes_value: Optional[str]
    """A double value."""
    double_value: Optional[float]
    """A geo point value representing a point on the surface of Earth."""
    geo_point_value: Optional[GeoPointValue]
    """An integer value."""
    integer_value: Optional[str]
    """A map value."""
    map_value: Optional[MapValue]
    """A null value."""
    null_value: Union[int, None, str]
    """A reference to a document. For example:
    `projects/{project_id}/databases/{database_id}/documents/{document_path}`.
    """
    reference_value: Optional[str]
    """A string value.
    
    The string, represented as UTF-8, must not exceed 1 MiB - 89 bytes.
    Only the first 1,500 bytes of the UTF-8 representation are considered by
    queries.
    """
    string_value: Optional[str]
    """A timestamp value.
    
    Precise only to microseconds. When stored, any additional precision is
    rounded down.
    """
    timestamp_value: Optional[datetime]

    def __init__(self, array_value: Optional['ArrayValue'], boolean_value: Optional[bool], bytes_value: Optional[str], double_value: Optional[float], geo_point_value: Optional[GeoPointValue], integer_value: Optional[str], map_value: Optional[MapValue], null_value: Union[int, None, str], reference_value: Optional[str], string_value: Optional[str], timestamp_value: Optional[datetime]) -> None:
        self.array_value = array_value
        self.boolean_value = boolean_value
        self.bytes_value = bytes_value
        self.double_value = double_value
        self.geo_point_value = geo_point_value
        self.integer_value = integer_value
        self.map_value = map_value
        self.null_value = null_value
        self.reference_value = reference_value
        self.string_value = string_value
        self.timestamp_value = timestamp_value

    @staticmethod
    def from_dict(obj: Any) -> 'ValueElement':
        assert isinstance(obj, dict)
        array_value = from_union([ArrayValue.from_dict, from_none], obj.get("arrayValue"))
        boolean_value = from_union([from_bool, from_none], obj.get("booleanValue"))
        bytes_value = from_union([from_str, from_none], obj.get("bytesValue"))
        double_value = from_union([from_float, from_none], obj.get("doubleValue"))
        geo_point_value = from_union([GeoPointValue.from_dict, from_none], obj.get("geoPointValue"))
        integer_value = from_union([from_str, from_none], obj.get("integerValue"))
        map_value = from_union([MapValue.from_dict, from_none], obj.get("mapValue"))
        null_value = from_union([from_int, from_str, from_none], obj.get("nullValue"))
        reference_value = from_union([from_str, from_none], obj.get("referenceValue"))
        string_value = from_union([from_str, from_none], obj.get("stringValue"))
        timestamp_value = from_union([from_datetime, from_none], obj.get("timestampValue"))
        return ValueElement(array_value, boolean_value, bytes_value, double_value, geo_point_value, integer_value, map_value, null_value, reference_value, string_value, timestamp_value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["arrayValue"] = from_union([lambda x: to_class(ArrayValue, x), from_none], self.array_value)
        result["booleanValue"] = from_union([from_bool, from_none], self.boolean_value)
        result["bytesValue"] = from_union([from_str, from_none], self.bytes_value)
        result["doubleValue"] = from_union([to_float, from_none], self.double_value)
        result["geoPointValue"] = from_union([lambda x: to_class(GeoPointValue, x), from_none], self.geo_point_value)
        result["integerValue"] = from_union([from_str, from_none], self.integer_value)
        result["mapValue"] = from_union([lambda x: to_class(MapValue, x), from_none], self.map_value)
        result["nullValue"] = from_union([from_int, from_str, from_none], self.null_value)
        result["referenceValue"] = from_union([from_str, from_none], self.reference_value)
        result["stringValue"] = from_union([from_str, from_none], self.string_value)
        result["timestampValue"] = from_union([lambda x: x.isoformat(), from_none], self.timestamp_value)
        return result


class ArrayValue:
    """An array value.
    
    Cannot directly contain another array value, though can contain an
    map which contains another array.
    """
    """Values in the array."""
    values: Optional[List[ValueElement]]

    def __init__(self, values: Optional[List[ValueElement]]) -> None:
        self.values = values

    @staticmethod
    def from_dict(obj: Any) -> 'ArrayValue':
        assert isinstance(obj, dict)
        values = from_union([lambda x: from_list(ValueElement.from_dict, x), from_none], obj.get("values"))
        return ArrayValue(values)

    def to_dict(self) -> dict:
        result: dict = {}
        result["values"] = from_union([lambda x: from_list(lambda x: to_class(ValueElement, x), x), from_none], self.values)
        return result


class OldValueField:
    """A message that can hold any of the supported value types."""
    """An array value.
    
    Cannot directly contain another array value, though can contain an
    map which contains another array.
    """
    array_value: Optional[ArrayValue]
    """A boolean value."""
    boolean_value: Optional[bool]
    """A bytes value.
    
    Must not exceed 1 MiB - 89 bytes.
    Only the first 1,500 bytes are considered by queries.
    """
    bytes_value: Optional[str]
    """A double value."""
    double_value: Optional[float]
    """A geo point value representing a point on the surface of Earth."""
    geo_point_value: Optional[GeoPointValue]
    """An integer value."""
    integer_value: Optional[str]
    """A map value."""
    map_value: Optional[MapValue]
    """A null value."""
    null_value: Union[int, None, str]
    """A reference to a document. For example:
    `projects/{project_id}/databases/{database_id}/documents/{document_path}`.
    """
    reference_value: Optional[str]
    """A string value.
    
    The string, represented as UTF-8, must not exceed 1 MiB - 89 bytes.
    Only the first 1,500 bytes of the UTF-8 representation are considered by
    queries.
    """
    string_value: Optional[str]
    """A timestamp value.
    
    Precise only to microseconds. When stored, any additional precision is
    rounded down.
    """
    timestamp_value: Optional[datetime]

    def __init__(self, array_value: Optional[ArrayValue], boolean_value: Optional[bool], bytes_value: Optional[str], double_value: Optional[float], geo_point_value: Optional[GeoPointValue], integer_value: Optional[str], map_value: Optional[MapValue], null_value: Union[int, None, str], reference_value: Optional[str], string_value: Optional[str], timestamp_value: Optional[datetime]) -> None:
        self.array_value = array_value
        self.boolean_value = boolean_value
        self.bytes_value = bytes_value
        self.double_value = double_value
        self.geo_point_value = geo_point_value
        self.integer_value = integer_value
        self.map_value = map_value
        self.null_value = null_value
        self.reference_value = reference_value
        self.string_value = string_value
        self.timestamp_value = timestamp_value

    @staticmethod
    def from_dict(obj: Any) -> 'OldValueField':
        assert isinstance(obj, dict)
        array_value = from_union([ArrayValue.from_dict, from_none], obj.get("arrayValue"))
        boolean_value = from_union([from_bool, from_none], obj.get("booleanValue"))
        bytes_value = from_union([from_str, from_none], obj.get("bytesValue"))
        double_value = from_union([from_float, from_none], obj.get("doubleValue"))
        geo_point_value = from_union([GeoPointValue.from_dict, from_none], obj.get("geoPointValue"))
        integer_value = from_union([from_str, from_none], obj.get("integerValue"))
        map_value = from_union([MapValue.from_dict, from_none], obj.get("mapValue"))
        null_value = from_union([from_int, from_str, from_none], obj.get("nullValue"))
        reference_value = from_union([from_str, from_none], obj.get("referenceValue"))
        string_value = from_union([from_str, from_none], obj.get("stringValue"))
        timestamp_value = from_union([from_datetime, from_none], obj.get("timestampValue"))
        return OldValueField(array_value, boolean_value, bytes_value, double_value, geo_point_value, integer_value, map_value, null_value, reference_value, string_value, timestamp_value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["arrayValue"] = from_union([lambda x: to_class(ArrayValue, x), from_none], self.array_value)
        result["booleanValue"] = from_union([from_bool, from_none], self.boolean_value)
        result["bytesValue"] = from_union([from_str, from_none], self.bytes_value)
        result["doubleValue"] = from_union([to_float, from_none], self.double_value)
        result["geoPointValue"] = from_union([lambda x: to_class(GeoPointValue, x), from_none], self.geo_point_value)
        result["integerValue"] = from_union([from_str, from_none], self.integer_value)
        result["mapValue"] = from_union([lambda x: to_class(MapValue, x), from_none], self.map_value)
        result["nullValue"] = from_union([from_int, from_str, from_none], self.null_value)
        result["referenceValue"] = from_union([from_str, from_none], self.reference_value)
        result["stringValue"] = from_union([from_str, from_none], self.string_value)
        result["timestampValue"] = from_union([lambda x: x.isoformat(), from_none], self.timestamp_value)
        return result


class OldValue:
    """A Document object containing a pre-operation document snapshot.
    This is only populated for update and delete events.
    
    A Firestore document.
    """
    """The time at which the document was created.
    
    This value increases monotonically when a document is deleted then
    recreated. It can also be compared to values from other documents and
    the `read_time` of a query.
    """
    create_time: Optional[datetime]
    """The document's fields.
    
    The map keys represent field names.
    
    A simple field name contains only characters `a` to `z`, `A` to `Z`,
    `0` to `9`, or `_`, and must not start with `0` to `9`. For example,
    `foo_bar_17`.
    
    Field names matching the regular expression `__.*__` are reserved. Reserved
    field names are forbidden except in certain documented contexts. The map
    keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be
    empty.
    
    Field paths may be used in other contexts to refer to structured fields
    defined here. For `map_value`, the field path is represented by the simple
    or quoted field names of the containing fields, delimited by `.`. For
    example, the structured field
    `"foo" : { map_value: { "x&y" : { string_value: "hello" }}}` would be
    represented by the field path `foo.x&y`.
    
    Within a field path, a quoted field name starts and ends with `` ` `` and
    may contain any character. Some characters, including `` ` ``, must be
    escaped using a `\`. For example, `` `x&y` `` represents `x&y` and
    `` `bak\`tik` `` represents `` bak`tik ``.
    """
    fields: Optional[Dict[str, OldValueField]]
    """The resource name of the document, for example
    `projects/{project_id}/databases/{database_id}/documents/{document_path}`.
    """
    name: Optional[str]
    """The time at which the document was last changed.
    
    This value is initially set to the `create_time` then increases
    monotonically with each change to the document. It can also be
    compared to values from other documents and the `read_time` of a query.
    """
    update_time: Optional[datetime]

    def __init__(self, create_time: Optional[datetime], fields: Optional[Dict[str, OldValueField]], name: Optional[str], update_time: Optional[datetime]) -> None:
        self.create_time = create_time
        self.fields = fields
        self.name = name
        self.update_time = update_time

    @staticmethod
    def from_dict(obj: Any) -> 'OldValue':
        assert isinstance(obj, dict)
        create_time = from_union([from_datetime, from_none], obj.get("createTime"))
        fields = from_union([lambda x: from_dict(OldValueField.from_dict, x), from_none], obj.get("fields"))
        name = from_union([from_str, from_none], obj.get("name"))
        update_time = from_union([from_datetime, from_none], obj.get("updateTime"))
        return OldValue(create_time, fields, name, update_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["createTime"] = from_union([lambda x: x.isoformat(), from_none], self.create_time)
        result["fields"] = from_union([lambda x: from_dict(lambda x: to_class(OldValueField, x), x), from_none], self.fields)
        result["name"] = from_union([from_str, from_none], self.name)
        result["updateTime"] = from_union([lambda x: x.isoformat(), from_none], self.update_time)
        return result


class UpdateMask:
    """A DocumentMask object that lists changed fields.
    This is only populated for update events.
    """
    """The list of field paths in the mask.
    See [Document.fields][google.cloud.firestore.v1.events.Document.fields]
    for a field path syntax reference.
    """
    field_paths: Optional[List[str]]

    def __init__(self, field_paths: Optional[List[str]]) -> None:
        self.field_paths = field_paths

    @staticmethod
    def from_dict(obj: Any) -> 'UpdateMask':
        assert isinstance(obj, dict)
        field_paths = from_union([lambda x: from_list(from_str, x), from_none], obj.get("fieldPaths"))
        return UpdateMask(field_paths)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fieldPaths"] = from_union([lambda x: from_list(from_str, x), from_none], self.field_paths)
        return result


class Value:
    """A Document object containing a post-operation document snapshot.
    This is not populated for delete events. (TODO: check this!)
    
    A Document object containing a pre-operation document snapshot.
    This is only populated for update and delete events.
    
    A Firestore document.
    """
    """The time at which the document was created.
    
    This value increases monotonically when a document is deleted then
    recreated. It can also be compared to values from other documents and
    the `read_time` of a query.
    """
    create_time: Optional[datetime]
    """The document's fields.
    
    The map keys represent field names.
    
    A simple field name contains only characters `a` to `z`, `A` to `Z`,
    `0` to `9`, or `_`, and must not start with `0` to `9`. For example,
    `foo_bar_17`.
    
    Field names matching the regular expression `__.*__` are reserved. Reserved
    field names are forbidden except in certain documented contexts. The map
    keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be
    empty.
    
    Field paths may be used in other contexts to refer to structured fields
    defined here. For `map_value`, the field path is represented by the simple
    or quoted field names of the containing fields, delimited by `.`. For
    example, the structured field
    `"foo" : { map_value: { "x&y" : { string_value: "hello" }}}` would be
    represented by the field path `foo.x&y`.
    
    Within a field path, a quoted field name starts and ends with `` ` `` and
    may contain any character. Some characters, including `` ` ``, must be
    escaped using a `\`. For example, `` `x&y` `` represents `x&y` and
    `` `bak\`tik` `` represents `` bak`tik ``.
    """
    fields: Optional[Dict[str, OldValueField]]
    """The resource name of the document, for example
    `projects/{project_id}/databases/{database_id}/documents/{document_path}`.
    """
    name: Optional[str]
    """The time at which the document was last changed.
    
    This value is initially set to the `create_time` then increases
    monotonically with each change to the document. It can also be
    compared to values from other documents and the `read_time` of a query.
    """
    update_time: Optional[datetime]

    def __init__(self, create_time: Optional[datetime], fields: Optional[Dict[str, OldValueField]], name: Optional[str], update_time: Optional[datetime]) -> None:
        self.create_time = create_time
        self.fields = fields
        self.name = name
        self.update_time = update_time

    @staticmethod
    def from_dict(obj: Any) -> 'Value':
        assert isinstance(obj, dict)
        create_time = from_union([from_datetime, from_none], obj.get("createTime"))
        fields = from_union([lambda x: from_dict(OldValueField.from_dict, x), from_none], obj.get("fields"))
        name = from_union([from_str, from_none], obj.get("name"))
        update_time = from_union([from_datetime, from_none], obj.get("updateTime"))
        return Value(create_time, fields, name, update_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["createTime"] = from_union([lambda x: x.isoformat(), from_none], self.create_time)
        result["fields"] = from_union([lambda x: from_dict(lambda x: to_class(OldValueField, x), x), from_none], self.fields)
        result["name"] = from_union([from_str, from_none], self.name)
        result["updateTime"] = from_union([lambda x: x.isoformat(), from_none], self.update_time)
        return result


class DocumentEventData:
    """The data within all Firestore document events."""
    """A Document object containing a pre-operation document snapshot.
    This is only populated for update and delete events.
    """
    old_value: Optional[OldValue]
    """A DocumentMask object that lists changed fields.
    This is only populated for update events.
    """
    update_mask: Optional[UpdateMask]
    """A Document object containing a post-operation document snapshot.
    This is not populated for delete events. (TODO: check this!)
    """
    value: Optional[Value]

    def __init__(self, old_value: Optional[OldValue], update_mask: Optional[UpdateMask], value: Optional[Value]) -> None:
        self.old_value = old_value
        self.update_mask = update_mask
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'DocumentEventData':
        assert isinstance(obj, dict)
        old_value = from_union([OldValue.from_dict, from_none], obj.get("oldValue"))
        update_mask = from_union([UpdateMask.from_dict, from_none], obj.get("updateMask"))
        value = from_union([Value.from_dict, from_none], obj.get("value"))
        return DocumentEventData(old_value, update_mask, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["oldValue"] = from_union([lambda x: to_class(OldValue, x), from_none], self.old_value)
        result["updateMask"] = from_union([lambda x: to_class(UpdateMask, x), from_none], self.update_mask)
        result["value"] = from_union([lambda x: to_class(Value, x), from_none], self.value)
        return result


def document_event_data_from_dict(s: Any) -> DocumentEventData:
    return DocumentEventData.from_dict(s)


def document_event_data_to_dict(x: DocumentEventData) -> Any:
    return to_class(DocumentEventData, x)
