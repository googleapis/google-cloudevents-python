from typing import Optional, Union
from datetime import datetime


class UpdateUser:
    """Aggregation of all metadata fields about the account that performed the update."""
    """Email address."""
    email: Optional[str]
    """Image URL."""
    image_url: Optional[str]
    """Display name."""
    name: Optional[str]

    def __init__(self, email: Optional[str], image_url: Optional[str], name: Optional[str]) -> None:
        self.email = email
        self.image_url = image_url
        self.name = name


class RemoteConfigEventData:
    """The data within all Firebase Remote Config events."""
    """The user-provided description of the corresponding Remote Config template."""
    description: Optional[str]
    """Only present if this version is the result of a rollback, and will be the
    version number of the Remote Config template that was rolled-back to.
    """
    rollback_source: Union[int, None, str]
    """Where the update action originated."""
    update_origin: Union[int, None, str]
    """When the Remote Config template was written to the Remote Config server."""
    update_time: Optional[datetime]
    """What type of update was made."""
    update_type: Union[int, None, str]
    """Aggregation of all metadata fields about the account that performed the update."""
    update_user: Optional[UpdateUser]
    """The version number of the version's corresponding Remote Config template."""
    version_number: Union[int, None, str]

    def __init__(self, description: Optional[str], rollback_source: Union[int, None, str], update_origin: Union[int, None, str], update_time: Optional[datetime], update_type: Union[int, None, str], update_user: Optional[UpdateUser], version_number: Union[int, None, str]) -> None:
        self.description = description
        self.rollback_source = rollback_source
        self.update_origin = update_origin
        self.update_time = update_time
        self.update_type = update_type
        self.update_user = update_user
        self.version_number = version_number
