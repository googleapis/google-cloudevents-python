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
#     result = auth_event_data_from_dict(json.loads(json_string))

from typing import Optional, Dict, Any, List, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


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


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class CustomClaims:
    """User's custom claims, typically used to define user roles and propagated
    to an authenticated user's ID token.
    """
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields

    @staticmethod
    def from_dict(obj: Any) -> 'CustomClaims':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], obj.get("fields"))
        return CustomClaims(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_dict(lambda x: from_union([from_none, lambda x: from_dict(lambda x: x, x)], x), x), from_none], self.fields)
        return result


class Metadata:
    """Additional metadata about the user."""
    """The date the user was created."""
    created_at: Optional[datetime]
    """The date the user last signed in."""
    last_signed_in_at: Optional[datetime]

    def __init__(self, created_at: Optional[datetime], last_signed_in_at: Optional[datetime]) -> None:
        self.created_at = created_at
        self.last_signed_in_at = last_signed_in_at

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        assert isinstance(obj, dict)
        created_at = from_union([from_datetime, from_none], obj.get("createdAt"))
        last_signed_in_at = from_union([from_datetime, from_none], obj.get("lastSignedInAt"))
        return Metadata(created_at, last_signed_in_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["createdAt"] = from_union([lambda x: x.isoformat(), from_none], self.created_at)
        result["lastSignedInAt"] = from_union([lambda x: x.isoformat(), from_none], self.last_signed_in_at)
        return result


class ProviderDatum:
    """User's info at the identity provider"""
    """The display name for the linked provider."""
    display_name: Optional[str]
    """The email for the linked provider."""
    email: Optional[str]
    """The photo URL for the linked provider."""
    photo_url: Optional[str]
    """The linked provider ID (e.g. "google.com" for the Google provider)."""
    provider_id: Optional[str]
    """The user identifier for the linked provider."""
    uid: Optional[str]

    def __init__(self, display_name: Optional[str], email: Optional[str], photo_url: Optional[str], provider_id: Optional[str], uid: Optional[str]) -> None:
        self.display_name = display_name
        self.email = email
        self.photo_url = photo_url
        self.provider_id = provider_id
        self.uid = uid

    @staticmethod
    def from_dict(obj: Any) -> 'ProviderDatum':
        assert isinstance(obj, dict)
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        email = from_union([from_str, from_none], obj.get("email"))
        photo_url = from_union([from_str, from_none], obj.get("photoUrl"))
        provider_id = from_union([from_str, from_none], obj.get("providerId"))
        uid = from_union([from_str, from_none], obj.get("uid"))
        return ProviderDatum(display_name, email, photo_url, provider_id, uid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["displayName"] = from_union([from_str, from_none], self.display_name)
        result["email"] = from_union([from_str, from_none], self.email)
        result["photoUrl"] = from_union([from_str, from_none], self.photo_url)
        result["providerId"] = from_union([from_str, from_none], self.provider_id)
        result["uid"] = from_union([from_str, from_none], self.uid)
        return result


class AuthEventData:
    """The data within all Firebase Auth events."""
    """User's custom claims, typically used to define user roles and propagated
    to an authenticated user's ID token.
    """
    custom_claims: Optional[CustomClaims]
    """Whether the user is disabled."""
    disabled: Optional[bool]
    """The user's display name."""
    display_name: Optional[str]
    """The user's primary email, if set."""
    email: Optional[str]
    """Whether or not the user's primary email is verified."""
    email_verified: Optional[bool]
    """Additional metadata about the user."""
    metadata: Optional[Metadata]
    """The user's phone number."""
    phone_number: Optional[str]
    """The user's photo URL."""
    photo_url: Optional[str]
    """User's info at the providers"""
    provider_data: Optional[List[ProviderDatum]]
    """The user identifier in the Firebase app."""
    uid: Optional[str]

    def __init__(self, custom_claims: Optional[CustomClaims], disabled: Optional[bool], display_name: Optional[str], email: Optional[str], email_verified: Optional[bool], metadata: Optional[Metadata], phone_number: Optional[str], photo_url: Optional[str], provider_data: Optional[List[ProviderDatum]], uid: Optional[str]) -> None:
        self.custom_claims = custom_claims
        self.disabled = disabled
        self.display_name = display_name
        self.email = email
        self.email_verified = email_verified
        self.metadata = metadata
        self.phone_number = phone_number
        self.photo_url = photo_url
        self.provider_data = provider_data
        self.uid = uid

    @staticmethod
    def from_dict(obj: Any) -> 'AuthEventData':
        assert isinstance(obj, dict)
        custom_claims = from_union([CustomClaims.from_dict, from_none], obj.get("customClaims"))
        disabled = from_union([from_bool, from_none], obj.get("disabled"))
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        email = from_union([from_str, from_none], obj.get("email"))
        email_verified = from_union([from_bool, from_none], obj.get("emailVerified"))
        metadata = from_union([Metadata.from_dict, from_none], obj.get("metadata"))
        phone_number = from_union([from_str, from_none], obj.get("phoneNumber"))
        photo_url = from_union([from_str, from_none], obj.get("photoUrl"))
        provider_data = from_union([lambda x: from_list(ProviderDatum.from_dict, x), from_none], obj.get("providerData"))
        uid = from_union([from_str, from_none], obj.get("uid"))
        return AuthEventData(custom_claims, disabled, display_name, email, email_verified, metadata, phone_number, photo_url, provider_data, uid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["customClaims"] = from_union([lambda x: to_class(CustomClaims, x), from_none], self.custom_claims)
        result["disabled"] = from_union([from_bool, from_none], self.disabled)
        result["displayName"] = from_union([from_str, from_none], self.display_name)
        result["email"] = from_union([from_str, from_none], self.email)
        result["emailVerified"] = from_union([from_bool, from_none], self.email_verified)
        result["metadata"] = from_union([lambda x: to_class(Metadata, x), from_none], self.metadata)
        result["phoneNumber"] = from_union([from_str, from_none], self.phone_number)
        result["photoUrl"] = from_union([from_str, from_none], self.photo_url)
        result["providerData"] = from_union([lambda x: from_list(lambda x: to_class(ProviderDatum, x), x), from_none], self.provider_data)
        result["uid"] = from_union([from_str, from_none], self.uid)
        return result


def auth_event_data_from_dict(s: Any) -> AuthEventData:
    return AuthEventData.from_dict(s)


def auth_event_data_to_dict(x: AuthEventData) -> Any:
    return to_class(AuthEventData, x)
