# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = events_from_dict(json.loads(json_string))

from dataclasses import dataclass
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


@dataclass
class Message:
    attributes: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    message_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        attributes = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("attributes"))
        message = from_union([from_str, from_none], obj.get("message"))
        message_id = from_union([from_str, from_none], obj.get("messageId"))
        return Message(attributes, message, message_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["attributes"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.attributes)
        result["message"] = from_union([from_str, from_none], self.message)
        result["messageId"] = from_union([from_str, from_none], self.message_id)
        return result


@dataclass
class MessagePublishedEvent:
    """This event is triggered when a new Cloud Pub/Sub event is published to a topic."""
    message: Optional[Message] = None
    subscription: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MessagePublishedEvent':
        assert isinstance(obj, dict)
        message = from_union([Message.from_dict, from_none], obj.get("message"))
        subscription = from_union([from_str, from_none], obj.get("subscription"))
        return MessagePublishedEvent(message, subscription)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message"] = from_union([lambda x: to_class(Message, x), from_none], self.message)
        result["subscription"] = from_union([from_str, from_none], self.subscription)
        return result


@dataclass
class Events:
    """This event is triggered when a new Cloud Pub/Sub event is published to a topic."""
    message_published_event: Optional[MessagePublishedEvent] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Events':
        assert isinstance(obj, dict)
        message_published_event = from_union([MessagePublishedEvent.from_dict, from_none], obj.get("MessagePublishedEvent"))
        return Events(message_published_event)

    def to_dict(self) -> dict:
        result: dict = {}
        result["MessagePublishedEvent"] = from_union([lambda x: to_class(MessagePublishedEvent, x), from_none], self.message_published_event)
        return result


def events_from_dict(s: Any) -> Events:
    return Events.from_dict(s)


def events_to_dict(x: Events) -> Any:
    return to_class(Events, x)
