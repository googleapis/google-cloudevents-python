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
#     result = message_published_data_from_dict(json.loads(json_string))

from typing import Optional, Dict, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Message:
    """The message that was published."""
    """Attributes for this message."""
    attributes: Optional[Dict[str, str]]
    """The binary data in the message."""
    data: Optional[str]
    """ID of this message, assigned by the server when the message is published.
    Guaranteed to be unique within the topic.
    """
    message_id: Optional[str]

    def __init__(self, attributes: Optional[Dict[str, str]], data: Optional[str], message_id: Optional[str]) -> None:
        self.attributes = attributes
        self.data = data
        self.message_id = message_id

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        attributes = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("attributes"))
        data = from_union([from_str, from_none], obj.get("data"))
        message_id = from_union([from_str, from_none], obj.get("messageId"))
        return Message(attributes, data, message_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["attributes"] = from_union([lambda x: from_dict(from_str, x), from_none], self.attributes)
        result["data"] = from_union([from_str, from_none], self.data)
        result["messageId"] = from_union([from_str, from_none], self.message_id)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'MessagePublishedData':
        assert isinstance(obj, dict)
        message = from_union([Message.from_dict, from_none], obj.get("message"))
        subscription = from_union([from_str, from_none], obj.get("subscription"))
        return MessagePublishedData(message, subscription)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message"] = from_union([lambda x: to_class(Message, x), from_none], self.message)
        result["subscription"] = from_union([from_str, from_none], self.subscription)
        return result


def message_published_data_from_dict(s: Any) -> MessagePublishedData:
    return MessagePublishedData.from_dict(s)


def message_published_data_to_dict(x: MessagePublishedData) -> Any:
    return to_class(MessagePublishedData, x)
