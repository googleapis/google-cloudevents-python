from typing import Optional, Union, Dict, List
from datetime import datetime


class GeoPointValue:
    """A geo point value representing a point on the surface of Earth."""
    """The latitude in degrees. It must be in the range [-90.0, +90.0]."""
    latitude: Optional[float]
    """The longitude in degrees. It must be in the range [-180.0, +180.0]."""
    longitude: Optional[float]

    def __init__(self, latitude: Optional[float], longitude: Optional[float]) -> None:
        self.latitude = latitude
        self.longitude = longitude


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
    integer_value: Union[int, None, str]
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

    def __init__(self, array_value: Optional['ArrayValue'], boolean_value: Optional[bool], bytes_value: Optional[str], double_value: Optional[float], geo_point_value: Optional[GeoPointValue], integer_value: Union[int, None, str], map_value: Optional['MapValue'], null_value: Union[int, None, str], reference_value: Optional[str], string_value: Optional[str], timestamp_value: Optional[datetime]) -> None:
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
    integer_value: Union[int, None, str]
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

    def __init__(self, array_value: Optional['ArrayValue'], boolean_value: Optional[bool], bytes_value: Optional[str], double_value: Optional[float], geo_point_value: Optional[GeoPointValue], integer_value: Union[int, None, str], map_value: Optional[MapValue], null_value: Union[int, None, str], reference_value: Optional[str], string_value: Optional[str], timestamp_value: Optional[datetime]) -> None:
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


class ArrayValue:
    """An array value.
    
    Cannot directly contain another array value, though can contain an
    map which contains another array.
    """
    """Values in the array."""
    values: Optional[List[ValueElement]]

    def __init__(self, values: Optional[List[ValueElement]]) -> None:
        self.values = values


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
    integer_value: Union[int, None, str]
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

    def __init__(self, array_value: Optional[ArrayValue], boolean_value: Optional[bool], bytes_value: Optional[str], double_value: Optional[float], geo_point_value: Optional[GeoPointValue], integer_value: Union[int, None, str], map_value: Optional[MapValue], null_value: Union[int, None, str], reference_value: Optional[str], string_value: Optional[str], timestamp_value: Optional[datetime]) -> None:
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
