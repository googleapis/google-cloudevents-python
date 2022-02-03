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
from typing import Optional, Dict
from datetime import datetime


class Message:
    """The message that was published.
    
    A message published to a topic.
    """
    """Attributes for this message."""
    attributes: Optional[Dict[str, str]]
    """The binary data in the message."""
    data: Optional[str]
    """ID of this message, assigned by the server when the message is published.
    Guaranteed to be unique within the topic.
    """
    message_id: Optional[str]
    """If non-empty, identifies related messages for which publish order should be
    respected.
    """
    ordering_key: Optional[str]
    """The time at which the message was published, populated by the server when
    it receives the `Publish` call.
    """
    publish_time: Optional[datetime]

    def __init__(self, attributes: Optional[Dict[str, str]], data: Optional[str], message_id: Optional[str], ordering_key: Optional[str], publish_time: Optional[datetime]) -> None:
        self.attributes = attributes
        self.data = data
        self.message_id = message_id
        self.ordering_key = ordering_key
        self.publish_time = publish_time


class MessagePublishedData:
    """The event data when a message is published to a topic."""
    """The message that was published."""
    message: Optional[Message]
    """The resource name of the subscription for which this event was
    generated. The format of the value is
    `projects/{project-id}/subscriptions/{subscription-id}`.
    """
    subscription: Optional[str]

    def __init__(self, message: Optional[Message], subscription: Optional[str]) -> None:
        self.message = message
        self.subscription = subscription
