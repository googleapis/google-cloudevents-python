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
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = analytics_log_data_from_dict(json.loads(json_string))

from typing import Optional, Any, Dict, List, TypeVar, Callable, Type, cast


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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class AnalyticsValue:
    """Value for Event Params and UserProperty can be of type string or int or
    float or double.
    """
    double_value: Optional[float]
    float_value: Optional[float]
    int_value: Optional[str]
    string_value: Optional[str]

    def __init__(self, double_value: Optional[float], float_value: Optional[float], int_value: Optional[str], string_value: Optional[str]) -> None:
        self.double_value = double_value
        self.float_value = float_value
        self.int_value = int_value
        self.string_value = string_value

    @staticmethod
    def from_dict(obj: Any) -> 'AnalyticsValue':
        assert isinstance(obj, dict)
        double_value = from_union([from_float, from_none], obj.get("doubleValue"))
        float_value = from_union([from_float, from_none], obj.get("floatValue"))
        int_value = from_union([from_str, from_none], obj.get("intValue"))
        string_value = from_union([from_str, from_none], obj.get("stringValue"))
        return AnalyticsValue(double_value, float_value, int_value, string_value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["doubleValue"] = from_union([to_float, from_none], self.double_value)
        result["floatValue"] = from_union([to_float, from_none], self.float_value)
        result["intValue"] = from_union([from_str, from_none], self.int_value)
        result["stringValue"] = from_union([from_str, from_none], self.string_value)
        return result


class EventDim:
    """Message containing information pertaining to the event."""
    """The date on which this event was logged.
    (YYYYMMDD format in the registered timezone of your app.)
    """
    date: Optional[str]
    """The name of this event."""
    name: Optional[str]
    """A repeated record of the parameters associated with this event."""
    params: Optional[Dict[str, AnalyticsValue]]
    """UTC client time when the previous event happened."""
    previous_timestamp_micros: Optional[str]
    """UTC client time when the event happened."""
    timestamp_micros: Optional[str]
    """Value param in USD."""
    value_in_usd: Optional[float]

    def __init__(self, date: Optional[str], name: Optional[str], params: Optional[Dict[str, AnalyticsValue]], previous_timestamp_micros: Optional[str], timestamp_micros: Optional[str], value_in_usd: Optional[float]) -> None:
        self.date = date
        self.name = name
        self.params = params
        self.previous_timestamp_micros = previous_timestamp_micros
        self.timestamp_micros = timestamp_micros
        self.value_in_usd = value_in_usd

    @staticmethod
    def from_dict(obj: Any) -> 'EventDim':
        assert isinstance(obj, dict)
        date = from_union([from_str, from_none], obj.get("date"))
        name = from_union([from_str, from_none], obj.get("name"))
        params = from_union([lambda x: from_dict(AnalyticsValue.from_dict, x), from_none], obj.get("params"))
        previous_timestamp_micros = from_union([from_str, from_none], obj.get("previousTimestampMicros"))
        timestamp_micros = from_union([from_str, from_none], obj.get("timestampMicros"))
        value_in_usd = from_union([from_float, from_none], obj.get("valueInUsd"))
        return EventDim(date, name, params, previous_timestamp_micros, timestamp_micros, value_in_usd)

    def to_dict(self) -> dict:
        result: dict = {}
        result["date"] = from_union([from_str, from_none], self.date)
        result["name"] = from_union([from_str, from_none], self.name)
        result["params"] = from_union([lambda x: from_dict(lambda x: to_class(AnalyticsValue, x), x), from_none], self.params)
        result["previousTimestampMicros"] = from_union([from_str, from_none], self.previous_timestamp_micros)
        result["timestampMicros"] = from_union([from_str, from_none], self.timestamp_micros)
        result["valueInUsd"] = from_union([to_float, from_none], self.value_in_usd)
        return result


class AppInfo:
    """App information."""
    """Unique application identifier within an app store."""
    app_id: Optional[str]
    """Unique id for this instance of the app.
    Example: "71683BF9FA3B4B0D9535A1F05188BAF3"
    """
    app_instance_id: Optional[str]
    """The app platform.
    Eg "ANDROID", "IOS".
    """
    app_platform: Optional[str]
    """The identifier of the store that installed the app.
    Eg. "com.sec.android.app.samsungapps", "com.amazon.venezia",
    "com.nokia.nstore"
    """
    app_store: Optional[str]
    """The app's version name
    Examples: "1.0", "4.3.1.1.213361", "2.3 (1824253)", "v1.8b22p6"
    """
    app_version: Optional[str]

    def __init__(self, app_id: Optional[str], app_instance_id: Optional[str], app_platform: Optional[str], app_store: Optional[str], app_version: Optional[str]) -> None:
        self.app_id = app_id
        self.app_instance_id = app_instance_id
        self.app_platform = app_platform
        self.app_store = app_store
        self.app_version = app_version

    @staticmethod
    def from_dict(obj: Any) -> 'AppInfo':
        assert isinstance(obj, dict)
        app_id = from_union([from_str, from_none], obj.get("appId"))
        app_instance_id = from_union([from_str, from_none], obj.get("appInstanceId"))
        app_platform = from_union([from_str, from_none], obj.get("appPlatform"))
        app_store = from_union([from_str, from_none], obj.get("appStore"))
        app_version = from_union([from_str, from_none], obj.get("appVersion"))
        return AppInfo(app_id, app_instance_id, app_platform, app_store, app_version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["appId"] = from_union([from_str, from_none], self.app_id)
        result["appInstanceId"] = from_union([from_str, from_none], self.app_instance_id)
        result["appPlatform"] = from_union([from_str, from_none], self.app_platform)
        result["appStore"] = from_union([from_str, from_none], self.app_store)
        result["appVersion"] = from_union([from_str, from_none], self.app_version)
        return result


class BundleInfo:
    """Information regarding the bundle in which these events were uploaded."""
    """Monotonically increasing index for each bundle set by SDK."""
    bundle_sequence_id: Optional[int]
    """Timestamp offset between collection time and upload time."""
    server_timestamp_offset_micros: Optional[str]

    def __init__(self, bundle_sequence_id: Optional[int], server_timestamp_offset_micros: Optional[str]) -> None:
        self.bundle_sequence_id = bundle_sequence_id
        self.server_timestamp_offset_micros = server_timestamp_offset_micros

    @staticmethod
    def from_dict(obj: Any) -> 'BundleInfo':
        assert isinstance(obj, dict)
        bundle_sequence_id = from_union([from_int, from_none], obj.get("bundleSequenceId"))
        server_timestamp_offset_micros = from_union([from_str, from_none], obj.get("serverTimestampOffsetMicros"))
        return BundleInfo(bundle_sequence_id, server_timestamp_offset_micros)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bundleSequenceId"] = from_union([from_int, from_none], self.bundle_sequence_id)
        result["serverTimestampOffsetMicros"] = from_union([from_str, from_none], self.server_timestamp_offset_micros)
        return result


class DeviceInfo:
    """Device information."""
    """Device category.
    Eg. tablet or mobile.
    """
    device_category: Optional[str]
    """Vendor specific device identifier. This is IDFV on iOS. Not used for
    Android.
    Example: "599F9C00-92DC-4B5C-9464-7971F01F8370"
    """
    device_id: Optional[str]
    """Device model.
    Eg. GT-I9192
    """
    device_model: Optional[str]
    """The timezone of the device when data was uploaded as seconds skew from UTC."""
    device_time_zone_offset_seconds: Optional[int]
    """The device's Limit Ad Tracking setting.
    When true, we cannot use device_id for remarketing, demographics or
    influencing ads serving behaviour. However, we can use device_id for
    conversion tracking and campaign attribution.
    """
    limited_ad_tracking: Optional[bool]
    """Device brand name.
    Eg. Samsung, HTC, etc.
    """
    mobile_brand_name: Optional[str]
    """Device marketing name.
    Eg. Galaxy S4 Mini
    """
    mobile_marketing_name: Optional[str]
    """Device model name.
    Eg. GT-I9192
    """
    mobile_model_name: Optional[str]
    """Device OS version when data capture ended.
    Eg. 4.4.2
    """
    platform_version: Optional[str]
    """The type of the resettable_device_id is always IDFA on iOS and AdId
    on Android.
    Example: "71683BF9-FA3B-4B0D-9535-A1F05188BAF3"
    """
    resettable_device_id: Optional[str]
    """The user language.
    Eg. "en-us", "en-za", "zh-tw", "jp"
    """
    user_default_language: Optional[str]

    def __init__(self, device_category: Optional[str], device_id: Optional[str], device_model: Optional[str], device_time_zone_offset_seconds: Optional[int], limited_ad_tracking: Optional[bool], mobile_brand_name: Optional[str], mobile_marketing_name: Optional[str], mobile_model_name: Optional[str], platform_version: Optional[str], resettable_device_id: Optional[str], user_default_language: Optional[str]) -> None:
        self.device_category = device_category
        self.device_id = device_id
        self.device_model = device_model
        self.device_time_zone_offset_seconds = device_time_zone_offset_seconds
        self.limited_ad_tracking = limited_ad_tracking
        self.mobile_brand_name = mobile_brand_name
        self.mobile_marketing_name = mobile_marketing_name
        self.mobile_model_name = mobile_model_name
        self.platform_version = platform_version
        self.resettable_device_id = resettable_device_id
        self.user_default_language = user_default_language

    @staticmethod
    def from_dict(obj: Any) -> 'DeviceInfo':
        assert isinstance(obj, dict)
        device_category = from_union([from_str, from_none], obj.get("deviceCategory"))
        device_id = from_union([from_str, from_none], obj.get("deviceId"))
        device_model = from_union([from_str, from_none], obj.get("deviceModel"))
        device_time_zone_offset_seconds = from_union([from_int, from_none], obj.get("deviceTimeZoneOffsetSeconds"))
        limited_ad_tracking = from_union([from_bool, from_none], obj.get("limitedAdTracking"))
        mobile_brand_name = from_union([from_str, from_none], obj.get("mobileBrandName"))
        mobile_marketing_name = from_union([from_str, from_none], obj.get("mobileMarketingName"))
        mobile_model_name = from_union([from_str, from_none], obj.get("mobileModelName"))
        platform_version = from_union([from_str, from_none], obj.get("platformVersion"))
        resettable_device_id = from_union([from_str, from_none], obj.get("resettableDeviceId"))
        user_default_language = from_union([from_str, from_none], obj.get("userDefaultLanguage"))
        return DeviceInfo(device_category, device_id, device_model, device_time_zone_offset_seconds, limited_ad_tracking, mobile_brand_name, mobile_marketing_name, mobile_model_name, platform_version, resettable_device_id, user_default_language)

    def to_dict(self) -> dict:
        result: dict = {}
        result["deviceCategory"] = from_union([from_str, from_none], self.device_category)
        result["deviceId"] = from_union([from_str, from_none], self.device_id)
        result["deviceModel"] = from_union([from_str, from_none], self.device_model)
        result["deviceTimeZoneOffsetSeconds"] = from_union([from_int, from_none], self.device_time_zone_offset_seconds)
        result["limitedAdTracking"] = from_union([from_bool, from_none], self.limited_ad_tracking)
        result["mobileBrandName"] = from_union([from_str, from_none], self.mobile_brand_name)
        result["mobileMarketingName"] = from_union([from_str, from_none], self.mobile_marketing_name)
        result["mobileModelName"] = from_union([from_str, from_none], self.mobile_model_name)
        result["platformVersion"] = from_union([from_str, from_none], self.platform_version)
        result["resettableDeviceId"] = from_union([from_str, from_none], self.resettable_device_id)
        result["userDefaultLanguage"] = from_union([from_str, from_none], self.user_default_language)
        return result


class GeoInfo:
    """User's geographic information."""
    """The geographic city.
    Eg. Sao Paulo
    """
    city: Optional[str]
    """The geographic continent.
    Eg. Americas
    """
    continent: Optional[str]
    """The geographic country.
    Eg. Brazil
    """
    country: Optional[str]
    """The geographic region.
    Eg. State of Sao Paulo
    """
    region: Optional[str]

    def __init__(self, city: Optional[str], continent: Optional[str], country: Optional[str], region: Optional[str]) -> None:
        self.city = city
        self.continent = continent
        self.country = country
        self.region = region

    @staticmethod
    def from_dict(obj: Any) -> 'GeoInfo':
        assert isinstance(obj, dict)
        city = from_union([from_str, from_none], obj.get("city"))
        continent = from_union([from_str, from_none], obj.get("continent"))
        country = from_union([from_str, from_none], obj.get("country"))
        region = from_union([from_str, from_none], obj.get("region"))
        return GeoInfo(city, continent, country, region)

    def to_dict(self) -> dict:
        result: dict = {}
        result["city"] = from_union([from_str, from_none], self.city)
        result["continent"] = from_union([from_str, from_none], self.continent)
        result["country"] = from_union([from_str, from_none], self.country)
        result["region"] = from_union([from_str, from_none], self.region)
        return result


class LtvInfo:
    """Lifetime Value information about this user."""
    """The currency corresponding to the revenue."""
    currency: Optional[str]
    """The Lifetime Value revenue of this user."""
    revenue: Optional[float]

    def __init__(self, currency: Optional[str], revenue: Optional[float]) -> None:
        self.currency = currency
        self.revenue = revenue

    @staticmethod
    def from_dict(obj: Any) -> 'LtvInfo':
        assert isinstance(obj, dict)
        currency = from_union([from_str, from_none], obj.get("currency"))
        revenue = from_union([from_float, from_none], obj.get("revenue"))
        return LtvInfo(currency, revenue)

    def to_dict(self) -> dict:
        result: dict = {}
        result["currency"] = from_union([from_str, from_none], self.currency)
        result["revenue"] = from_union([to_float, from_none], self.revenue)
        return result


class TrafficSource:
    """Information about marketing campaign which acquired the user."""
    """The name of the campaign which acquired the user."""
    user_acquired_campaign: Optional[str]
    """The name of the medium which acquired the user."""
    user_acquired_medium: Optional[str]
    """The name of the network which acquired the user."""
    user_acquired_source: Optional[str]

    def __init__(self, user_acquired_campaign: Optional[str], user_acquired_medium: Optional[str], user_acquired_source: Optional[str]) -> None:
        self.user_acquired_campaign = user_acquired_campaign
        self.user_acquired_medium = user_acquired_medium
        self.user_acquired_source = user_acquired_source

    @staticmethod
    def from_dict(obj: Any) -> 'TrafficSource':
        assert isinstance(obj, dict)
        user_acquired_campaign = from_union([from_str, from_none], obj.get("userAcquiredCampaign"))
        user_acquired_medium = from_union([from_str, from_none], obj.get("userAcquiredMedium"))
        user_acquired_source = from_union([from_str, from_none], obj.get("userAcquiredSource"))
        return TrafficSource(user_acquired_campaign, user_acquired_medium, user_acquired_source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["userAcquiredCampaign"] = from_union([from_str, from_none], self.user_acquired_campaign)
        result["userAcquiredMedium"] = from_union([from_str, from_none], self.user_acquired_medium)
        result["userAcquiredSource"] = from_union([from_str, from_none], self.user_acquired_source)
        return result


class Value:
    """Last set value of user property.
    
    Value for Event Params and UserProperty can be of type string or int or
    float or double.
    """
    double_value: Optional[float]
    float_value: Optional[float]
    int_value: Optional[str]
    string_value: Optional[str]

    def __init__(self, double_value: Optional[float], float_value: Optional[float], int_value: Optional[str], string_value: Optional[str]) -> None:
        self.double_value = double_value
        self.float_value = float_value
        self.int_value = int_value
        self.string_value = string_value

    @staticmethod
    def from_dict(obj: Any) -> 'Value':
        assert isinstance(obj, dict)
        double_value = from_union([from_float, from_none], obj.get("doubleValue"))
        float_value = from_union([from_float, from_none], obj.get("floatValue"))
        int_value = from_union([from_str, from_none], obj.get("intValue"))
        string_value = from_union([from_str, from_none], obj.get("stringValue"))
        return Value(double_value, float_value, int_value, string_value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["doubleValue"] = from_union([to_float, from_none], self.double_value)
        result["floatValue"] = from_union([to_float, from_none], self.float_value)
        result["intValue"] = from_union([from_str, from_none], self.int_value)
        result["stringValue"] = from_union([from_str, from_none], self.string_value)
        return result


class UserProperty:
    """Index for user property (one-based)."""
    index: Optional[int]
    """UTC client time when user property was last set."""
    set_timestamp_usec: Optional[str]
    """Last set value of user property."""
    value: Optional[Value]

    def __init__(self, index: Optional[int], set_timestamp_usec: Optional[str], value: Optional[Value]) -> None:
        self.index = index
        self.set_timestamp_usec = set_timestamp_usec
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'UserProperty':
        assert isinstance(obj, dict)
        index = from_union([from_int, from_none], obj.get("index"))
        set_timestamp_usec = from_union([from_str, from_none], obj.get("setTimestampUsec"))
        value = from_union([Value.from_dict, from_none], obj.get("value"))
        return UserProperty(index, set_timestamp_usec, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["index"] = from_union([from_int, from_none], self.index)
        result["setTimestampUsec"] = from_union([from_str, from_none], self.set_timestamp_usec)
        result["value"] = from_union([lambda x: to_class(Value, x), from_none], self.value)
        return result


class UserDim:
    """User related dimensions."""
    """App information."""
    app_info: Optional[AppInfo]
    """Information regarding the bundle in which these events were uploaded."""
    bundle_info: Optional[BundleInfo]
    """Device information."""
    device_info: Optional[DeviceInfo]
    """The time (in microseconds) at which the user first opened the app."""
    first_open_timestamp_micros: Optional[str]
    """User's geographic information."""
    geo_info: Optional[GeoInfo]
    """Lifetime Value information about this user."""
    ltv_info: Optional[LtvInfo]
    """Information about marketing campaign which acquired the user."""
    traffic_source: Optional[TrafficSource]
    """The user ID set via the setUserId API."""
    user_id: Optional[str]
    """A repeated record of user properties set with the setUserProperty API.
    https://firebase.google.com/docs/analytics/android/properties
    """
    user_properties: Optional[Dict[str, UserProperty]]

    def __init__(self, app_info: Optional[AppInfo], bundle_info: Optional[BundleInfo], device_info: Optional[DeviceInfo], first_open_timestamp_micros: Optional[str], geo_info: Optional[GeoInfo], ltv_info: Optional[LtvInfo], traffic_source: Optional[TrafficSource], user_id: Optional[str], user_properties: Optional[Dict[str, UserProperty]]) -> None:
        self.app_info = app_info
        self.bundle_info = bundle_info
        self.device_info = device_info
        self.first_open_timestamp_micros = first_open_timestamp_micros
        self.geo_info = geo_info
        self.ltv_info = ltv_info
        self.traffic_source = traffic_source
        self.user_id = user_id
        self.user_properties = user_properties

    @staticmethod
    def from_dict(obj: Any) -> 'UserDim':
        assert isinstance(obj, dict)
        app_info = from_union([AppInfo.from_dict, from_none], obj.get("appInfo"))
        bundle_info = from_union([BundleInfo.from_dict, from_none], obj.get("bundleInfo"))
        device_info = from_union([DeviceInfo.from_dict, from_none], obj.get("deviceInfo"))
        first_open_timestamp_micros = from_union([from_str, from_none], obj.get("firstOpenTimestampMicros"))
        geo_info = from_union([GeoInfo.from_dict, from_none], obj.get("geoInfo"))
        ltv_info = from_union([LtvInfo.from_dict, from_none], obj.get("ltvInfo"))
        traffic_source = from_union([TrafficSource.from_dict, from_none], obj.get("trafficSource"))
        user_id = from_union([from_str, from_none], obj.get("userId"))
        user_properties = from_union([lambda x: from_dict(UserProperty.from_dict, x), from_none], obj.get("userProperties"))
        return UserDim(app_info, bundle_info, device_info, first_open_timestamp_micros, geo_info, ltv_info, traffic_source, user_id, user_properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["appInfo"] = from_union([lambda x: to_class(AppInfo, x), from_none], self.app_info)
        result["bundleInfo"] = from_union([lambda x: to_class(BundleInfo, x), from_none], self.bundle_info)
        result["deviceInfo"] = from_union([lambda x: to_class(DeviceInfo, x), from_none], self.device_info)
        result["firstOpenTimestampMicros"] = from_union([from_str, from_none], self.first_open_timestamp_micros)
        result["geoInfo"] = from_union([lambda x: to_class(GeoInfo, x), from_none], self.geo_info)
        result["ltvInfo"] = from_union([lambda x: to_class(LtvInfo, x), from_none], self.ltv_info)
        result["trafficSource"] = from_union([lambda x: to_class(TrafficSource, x), from_none], self.traffic_source)
        result["userId"] = from_union([from_str, from_none], self.user_id)
        result["userProperties"] = from_union([lambda x: from_dict(lambda x: to_class(UserProperty, x), x), from_none], self.user_properties)
        return result


class AnalyticsLogData:
    """The data within Firebase Analytics log events."""
    """A repeated record of event related dimensions."""
    event_dim: Optional[List[EventDim]]
    """User related dimensions."""
    user_dim: Optional[UserDim]

    def __init__(self, event_dim: Optional[List[EventDim]], user_dim: Optional[UserDim]) -> None:
        self.event_dim = event_dim
        self.user_dim = user_dim

    @staticmethod
    def from_dict(obj: Any) -> 'AnalyticsLogData':
        assert isinstance(obj, dict)
        event_dim = from_union([lambda x: from_list(EventDim.from_dict, x), from_none], obj.get("eventDim"))
        user_dim = from_union([UserDim.from_dict, from_none], obj.get("userDim"))
        return AnalyticsLogData(event_dim, user_dim)

    def to_dict(self) -> dict:
        result: dict = {}
        result["eventDim"] = from_union([lambda x: from_list(lambda x: to_class(EventDim, x), x), from_none], self.event_dim)
        result["userDim"] = from_union([lambda x: to_class(UserDim, x), from_none], self.user_dim)
        return result


def analytics_log_data_from_dict(s: Any) -> AnalyticsLogData:
    return AnalyticsLogData.from_dict(s)


def analytics_log_data_to_dict(x: AnalyticsLogData) -> Any:
    return to_class(AnalyticsLogData, x)
