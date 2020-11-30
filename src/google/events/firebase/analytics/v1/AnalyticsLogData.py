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
from typing import Optional, Union, Dict, List


class AnalyticsValue:
    """Value for Event Params and UserProperty can be of type string or int or
    float or double.
    """
    double_value: Optional[float]
    float_value: Optional[float]
    int_value: Union[int, None, str]
    string_value: Optional[str]

    def __init__(self, double_value: Optional[float], float_value: Optional[float], int_value: Union[int, None, str], string_value: Optional[str]) -> None:
        self.double_value = double_value
        self.float_value = float_value
        self.int_value = int_value
        self.string_value = string_value


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
    previous_timestamp_micros: Union[int, None, str]
    """UTC client time when the event happened."""
    timestamp_micros: Union[int, None, str]
    """Value param in USD."""
    value_in_usd: Optional[float]

    def __init__(self, date: Optional[str], name: Optional[str], params: Optional[Dict[str, AnalyticsValue]], previous_timestamp_micros: Union[int, None, str], timestamp_micros: Union[int, None, str], value_in_usd: Optional[float]) -> None:
        self.date = date
        self.name = name
        self.params = params
        self.previous_timestamp_micros = previous_timestamp_micros
        self.timestamp_micros = timestamp_micros
        self.value_in_usd = value_in_usd


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


class BundleInfo:
    """Information regarding the bundle in which these events were uploaded."""
    """Monotonically increasing index for each bundle set by SDK."""
    bundle_sequence_id: Optional[int]
    """Timestamp offset between collection time and upload time."""
    server_timestamp_offset_micros: Union[int, None, str]

    def __init__(self, bundle_sequence_id: Optional[int], server_timestamp_offset_micros: Union[int, None, str]) -> None:
        self.bundle_sequence_id = bundle_sequence_id
        self.server_timestamp_offset_micros = server_timestamp_offset_micros


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


class LtvInfo:
    """Lifetime Value information about this user."""
    """The currency corresponding to the revenue."""
    currency: Optional[str]
    """The Lifetime Value revenue of this user."""
    revenue: Optional[float]

    def __init__(self, currency: Optional[str], revenue: Optional[float]) -> None:
        self.currency = currency
        self.revenue = revenue


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


class Value:
    """Last set value of user property.
    
    Value for Event Params and UserProperty can be of type string or int or
    float or double.
    """
    double_value: Optional[float]
    float_value: Optional[float]
    int_value: Union[int, None, str]
    string_value: Optional[str]

    def __init__(self, double_value: Optional[float], float_value: Optional[float], int_value: Union[int, None, str], string_value: Optional[str]) -> None:
        self.double_value = double_value
        self.float_value = float_value
        self.int_value = int_value
        self.string_value = string_value


class UserProperty:
    """Index for user property (one-based)."""
    index: Optional[int]
    """UTC client time when user property was last set."""
    set_timestamp_usec: Union[int, None, str]
    """Last set value of user property."""
    value: Optional[Value]

    def __init__(self, index: Optional[int], set_timestamp_usec: Union[int, None, str], value: Optional[Value]) -> None:
        self.index = index
        self.set_timestamp_usec = set_timestamp_usec
        self.value = value


class UserDim:
    """User related dimensions."""
    """App information."""
    app_info: Optional[AppInfo]
    """Information regarding the bundle in which these events were uploaded."""
    bundle_info: Optional[BundleInfo]
    """Device information."""
    device_info: Optional[DeviceInfo]
    """The time (in microseconds) at which the user first opened the app."""
    first_open_timestamp_micros: Union[int, None, str]
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

    def __init__(self, app_info: Optional[AppInfo], bundle_info: Optional[BundleInfo], device_info: Optional[DeviceInfo], first_open_timestamp_micros: Union[int, None, str], geo_info: Optional[GeoInfo], ltv_info: Optional[LtvInfo], traffic_source: Optional[TrafficSource], user_id: Optional[str], user_properties: Optional[Dict[str, UserProperty]]) -> None:
        self.app_info = app_info
        self.bundle_info = bundle_info
        self.device_info = device_info
        self.first_open_timestamp_micros = first_open_timestamp_micros
        self.geo_info = geo_info
        self.ltv_info = ltv_info
        self.traffic_source = traffic_source
        self.user_id = user_id
        self.user_properties = user_properties


class AnalyticsLogData:
    """The data within Firebase Analytics log events."""
    """A repeated record of event related dimensions."""
    event_dim: Optional[List[EventDim]]
    """User related dimensions."""
    user_dim: Optional[UserDim]

    def __init__(self, event_dim: Optional[List[EventDim]], user_dim: Optional[UserDim]) -> None:
        self.event_dim = event_dim
        self.user_dim = user_dim
