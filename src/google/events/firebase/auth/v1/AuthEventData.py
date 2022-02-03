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
from typing import Optional, Dict, Any, List
from datetime import datetime


class Metadata:
    """Additional metadata about the user."""
    """The date the user was created."""
    create_time: Optional[datetime]
    """The date the user last signed in."""
    last_sign_in_time: Optional[datetime]

    def __init__(self, create_time: Optional[datetime], last_sign_in_time: Optional[datetime]) -> None:
        self.create_time = create_time
        self.last_sign_in_time = last_sign_in_time


class UserInfo:
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


class AuthEventData:
    """The data within all Firebase Auth events."""
    """User's custom claims, typically used to define user roles and propagated
    to an authenticated user's ID token.
    """
    custom_claims: Optional[Dict[str, Any]]
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
    provider_data: Optional[List[UserInfo]]
    """The user identifier in the Firebase app."""
    uid: Optional[str]

    def __init__(self, custom_claims: Optional[Dict[str, Any]], disabled: Optional[bool], display_name: Optional[str], email: Optional[str], email_verified: Optional[bool], metadata: Optional[Metadata], phone_number: Optional[str], photo_url: Optional[str], provider_data: Optional[List[UserInfo]], uid: Optional[str]) -> None:
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
