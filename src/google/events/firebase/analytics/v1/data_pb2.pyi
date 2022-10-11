from typing import ClassVar, Iterable, Mapping, Optional, Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class AnalyticsLogData(_message.Message):
    __slots__ = ["event_dim", "user_dim"]
    EVENT_DIM_FIELD_NUMBER: ClassVar[int]
    USER_DIM_FIELD_NUMBER: ClassVar[int]
    event_dim: _containers.RepeatedCompositeFieldContainer[EventDimensions]
    user_dim: UserDimensions
    def __init__(
        self,
        user_dim: Optional[Union[UserDimensions, Mapping]] = ...,
        event_dim: Optional[Iterable[Union[EventDimensions, Mapping]]] = ...,
    ) -> None: ...

class AnalyticsValue(_message.Message):
    __slots__ = ["double_value", "float_value", "int_value", "string_value"]
    DOUBLE_VALUE_FIELD_NUMBER: ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: ClassVar[int]
    INT_VALUE_FIELD_NUMBER: ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: ClassVar[int]
    double_value: float
    float_value: float
    int_value: int
    string_value: str
    def __init__(
        self,
        string_value: Optional[str] = ...,
        int_value: Optional[int] = ...,
        float_value: Optional[float] = ...,
        double_value: Optional[float] = ...,
    ) -> None: ...

class AppInfo(_message.Message):
    __slots__ = [
        "app_id",
        "app_instance_id",
        "app_platform",
        "app_store",
        "app_version",
    ]
    APP_ID_FIELD_NUMBER: ClassVar[int]
    APP_INSTANCE_ID_FIELD_NUMBER: ClassVar[int]
    APP_PLATFORM_FIELD_NUMBER: ClassVar[int]
    APP_STORE_FIELD_NUMBER: ClassVar[int]
    APP_VERSION_FIELD_NUMBER: ClassVar[int]
    app_id: str
    app_instance_id: str
    app_platform: str
    app_store: str
    app_version: str
    def __init__(
        self,
        app_version: Optional[str] = ...,
        app_instance_id: Optional[str] = ...,
        app_store: Optional[str] = ...,
        app_platform: Optional[str] = ...,
        app_id: Optional[str] = ...,
    ) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = [
        "device_category",
        "device_id",
        "device_model",
        "device_time_zone_offset_seconds",
        "limited_ad_tracking",
        "mobile_brand_name",
        "mobile_marketing_name",
        "mobile_model_name",
        "platform_version",
        "resettable_device_id",
        "user_default_language",
    ]
    DEVICE_CATEGORY_FIELD_NUMBER: ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: ClassVar[int]
    DEVICE_TIME_ZONE_OFFSET_SECONDS_FIELD_NUMBER: ClassVar[int]
    LIMITED_AD_TRACKING_FIELD_NUMBER: ClassVar[int]
    MOBILE_BRAND_NAME_FIELD_NUMBER: ClassVar[int]
    MOBILE_MARKETING_NAME_FIELD_NUMBER: ClassVar[int]
    MOBILE_MODEL_NAME_FIELD_NUMBER: ClassVar[int]
    PLATFORM_VERSION_FIELD_NUMBER: ClassVar[int]
    RESETTABLE_DEVICE_ID_FIELD_NUMBER: ClassVar[int]
    USER_DEFAULT_LANGUAGE_FIELD_NUMBER: ClassVar[int]
    device_category: str
    device_id: str
    device_model: str
    device_time_zone_offset_seconds: int
    limited_ad_tracking: bool
    mobile_brand_name: str
    mobile_marketing_name: str
    mobile_model_name: str
    platform_version: str
    resettable_device_id: str
    user_default_language: str
    def __init__(
        self,
        device_category: Optional[str] = ...,
        mobile_brand_name: Optional[str] = ...,
        mobile_model_name: Optional[str] = ...,
        mobile_marketing_name: Optional[str] = ...,
        device_model: Optional[str] = ...,
        platform_version: Optional[str] = ...,
        device_id: Optional[str] = ...,
        resettable_device_id: Optional[str] = ...,
        user_default_language: Optional[str] = ...,
        device_time_zone_offset_seconds: Optional[int] = ...,
        limited_ad_tracking: bool = ...,
    ) -> None: ...

class EventDimensions(_message.Message):
    __slots__ = [
        "date",
        "name",
        "params",
        "previous_timestamp_micros",
        "timestamp_micros",
        "value_in_usd",
    ]

    class ParamsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: AnalyticsValue
        def __init__(
            self,
            key: Optional[str] = ...,
            value: Optional[Union[AnalyticsValue, Mapping]] = ...,
        ) -> None: ...
    DATE_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    PARAMS_FIELD_NUMBER: ClassVar[int]
    PREVIOUS_TIMESTAMP_MICROS_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_MICROS_FIELD_NUMBER: ClassVar[int]
    VALUE_IN_USD_FIELD_NUMBER: ClassVar[int]
    date: str
    name: str
    params: _containers.MessageMap[str, AnalyticsValue]
    previous_timestamp_micros: int
    timestamp_micros: int
    value_in_usd: float
    def __init__(
        self,
        date: Optional[str] = ...,
        name: Optional[str] = ...,
        params: Optional[Mapping[str, AnalyticsValue]] = ...,
        timestamp_micros: Optional[int] = ...,
        previous_timestamp_micros: Optional[int] = ...,
        value_in_usd: Optional[float] = ...,
    ) -> None: ...

class ExportBundleInfo(_message.Message):
    __slots__ = ["bundle_sequence_id", "server_timestamp_offset_micros"]
    BUNDLE_SEQUENCE_ID_FIELD_NUMBER: ClassVar[int]
    SERVER_TIMESTAMP_OFFSET_MICROS_FIELD_NUMBER: ClassVar[int]
    bundle_sequence_id: int
    server_timestamp_offset_micros: int
    def __init__(
        self,
        bundle_sequence_id: Optional[int] = ...,
        server_timestamp_offset_micros: Optional[int] = ...,
    ) -> None: ...

class GeoInfo(_message.Message):
    __slots__ = ["city", "continent", "country", "region"]
    CITY_FIELD_NUMBER: ClassVar[int]
    CONTINENT_FIELD_NUMBER: ClassVar[int]
    COUNTRY_FIELD_NUMBER: ClassVar[int]
    REGION_FIELD_NUMBER: ClassVar[int]
    city: str
    continent: str
    country: str
    region: str
    def __init__(
        self,
        continent: Optional[str] = ...,
        country: Optional[str] = ...,
        region: Optional[str] = ...,
        city: Optional[str] = ...,
    ) -> None: ...

class LtvInfo(_message.Message):
    __slots__ = ["currency", "revenue"]
    CURRENCY_FIELD_NUMBER: ClassVar[int]
    REVENUE_FIELD_NUMBER: ClassVar[int]
    currency: str
    revenue: float
    def __init__(
        self, revenue: Optional[float] = ..., currency: Optional[str] = ...
    ) -> None: ...

class TrafficSource(_message.Message):
    __slots__ = [
        "user_acquired_campaign",
        "user_acquired_medium",
        "user_acquired_source",
    ]
    USER_ACQUIRED_CAMPAIGN_FIELD_NUMBER: ClassVar[int]
    USER_ACQUIRED_MEDIUM_FIELD_NUMBER: ClassVar[int]
    USER_ACQUIRED_SOURCE_FIELD_NUMBER: ClassVar[int]
    user_acquired_campaign: str
    user_acquired_medium: str
    user_acquired_source: str
    def __init__(
        self,
        user_acquired_campaign: Optional[str] = ...,
        user_acquired_source: Optional[str] = ...,
        user_acquired_medium: Optional[str] = ...,
    ) -> None: ...

class UserDimensions(_message.Message):
    __slots__ = [
        "app_info",
        "bundle_info",
        "device_info",
        "first_open_timestamp_micros",
        "geo_info",
        "ltv_info",
        "traffic_source",
        "user_id",
        "user_properties",
    ]

    class UserPropertiesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: UserPropertyValue
        def __init__(
            self,
            key: Optional[str] = ...,
            value: Optional[Union[UserPropertyValue, Mapping]] = ...,
        ) -> None: ...
    APP_INFO_FIELD_NUMBER: ClassVar[int]
    BUNDLE_INFO_FIELD_NUMBER: ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: ClassVar[int]
    FIRST_OPEN_TIMESTAMP_MICROS_FIELD_NUMBER: ClassVar[int]
    GEO_INFO_FIELD_NUMBER: ClassVar[int]
    LTV_INFO_FIELD_NUMBER: ClassVar[int]
    TRAFFIC_SOURCE_FIELD_NUMBER: ClassVar[int]
    USER_ID_FIELD_NUMBER: ClassVar[int]
    USER_PROPERTIES_FIELD_NUMBER: ClassVar[int]
    app_info: AppInfo
    bundle_info: ExportBundleInfo
    device_info: DeviceInfo
    first_open_timestamp_micros: int
    geo_info: GeoInfo
    ltv_info: LtvInfo
    traffic_source: TrafficSource
    user_id: str
    user_properties: _containers.MessageMap[str, UserPropertyValue]
    def __init__(
        self,
        user_id: Optional[str] = ...,
        first_open_timestamp_micros: Optional[int] = ...,
        user_properties: Optional[Mapping[str, UserPropertyValue]] = ...,
        device_info: Optional[Union[DeviceInfo, Mapping]] = ...,
        geo_info: Optional[Union[GeoInfo, Mapping]] = ...,
        app_info: Optional[Union[AppInfo, Mapping]] = ...,
        traffic_source: Optional[Union[TrafficSource, Mapping]] = ...,
        bundle_info: Optional[Union[ExportBundleInfo, Mapping]] = ...,
        ltv_info: Optional[Union[LtvInfo, Mapping]] = ...,
    ) -> None: ...

class UserPropertyValue(_message.Message):
    __slots__ = ["index", "set_timestamp_usec", "value"]
    INDEX_FIELD_NUMBER: ClassVar[int]
    SET_TIMESTAMP_USEC_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    index: int
    set_timestamp_usec: int
    value: AnalyticsValue
    def __init__(
        self,
        value: Optional[Union[AnalyticsValue, Mapping]] = ...,
        set_timestamp_usec: Optional[int] = ...,
        index: Optional[int] = ...,
    ) -> None: ...
