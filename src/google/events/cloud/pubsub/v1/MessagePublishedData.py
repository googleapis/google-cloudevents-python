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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class PubsubMessage:
    """The message that was published.
    
    A message published to a topic.
    """
    """Attributes for this message. If this field is empty, the message must contain non-empty
    data. This can be used to filter messages on the subscription.
    """
    attributes: Optional[Dict[str, Any]]
    """The message data field. If this field is empty, the message must contain at least one
    attribute. A base64-encoded string.
    """
    data: Optional[str]
    """ID of this message, assigned by the server when the message is published. Guaranteed to
    be unique within the topic. This value may be read by a subscriber that receives a
    PubsubMessage via a subscriptions.pull call or a push delivery. It must not be populated
    by the publisher in a topics.publish call.
    """
    message_id: Optional[str]

    def __init__(self, attributes: Optional[Dict[str, Any]], data: Optional[str], message_id: Optional[str]) -> None:
        self.attributes = attributes
        self.data = data
        self.message_id = message_id

    @staticmethod
    def from_dict(obj: Any) -> 'PubsubMessage':
        assert isinstance(obj, dict)
        attributes = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("attributes"))
        data = from_union([from_str, from_none], obj.get("data"))
        message_id = from_union([from_str, from_none], obj.get("messageId"))
        return PubsubMessage(attributes, data, message_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["attributes"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.attributes)
        result["data"] = from_union([from_str, from_none], self.data)
        result["messageId"] = from_union([from_str, from_none], self.message_id)
        return result


class MessagePublishedData:
    """A message that is published by publishers and consumed by subscribers."""
    """The message that was published."""
    message: Optional[PubsubMessage]
    """The resource name of the subscription for which this event was generated. The format of
    the value is `projects/{project-id}/subscriptions/{subscription-id}`.
    """
    subscription: Optional[str]

    def __init__(self, message: Optional[PubsubMessage], subscription: Optional[str]) -> None:
        self.message = message
        self.subscription = subscription

    @staticmethod
    def from_dict(obj: Any) -> 'MessagePublishedData':
        assert isinstance(obj, dict)
        message = from_union([PubsubMessage.from_dict, from_none], obj.get("message"))
        subscription = from_union([from_str, from_none], obj.get("subscription"))
        return MessagePublishedData(message, subscription)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message"] = from_union([lambda x: to_class(PubsubMessage, x), from_none], self.message)
        result["subscription"] = from_union([from_str, from_none], self.subscription)
        return result


def message_published_data_from_dict(s: Any) -> MessagePublishedData:
    return MessagePublishedData.from_dict(s)


def message_published_data_to_dict(x: MessagePublishedData) -> Any:
    return to_class(MessagePublishedData, x)
