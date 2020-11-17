from typing import Optional, Dict, Any, List
from datetime import datetime


class CustomClaims:
    """User's custom claims, typically used to define user roles and propagated
    to an authenticated user's ID token.
    """
    """Unordered map of dynamically typed values."""
    fields: Optional[Dict[str, Optional[Dict[str, Any]]]]

    def __init__(self, fields: Optional[Dict[str, Optional[Dict[str, Any]]]]) -> None:
        self.fields = fields


class Metadata:
    """Additional metadata about the user."""
    """The date the user was created."""
    created_at: Optional[datetime]
    """The date the user last signed in."""
    last_signed_in_at: Optional[datetime]

    def __init__(self, created_at: Optional[datetime], last_signed_in_at: Optional[datetime]) -> None:
        self.created_at = created_at
        self.last_signed_in_at = last_signed_in_at


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


class AuthEventData:
    """The data within all Firebase Auth events"""
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
