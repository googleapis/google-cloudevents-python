# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = event_from_dict(json.loads(json_string))

from typing import Optional, Dict, Any, List, Union, TypeVar, Callable, Type, cast


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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


class PubsubMessage:
    attributes: Optional[Dict[str, Any]]
    data: Optional[str]
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


class MessagePublishedEvent:
    """This event is triggered when a Pub/Sub message is published."""
    message: Optional[PubsubMessage]
    subscription: Optional[str]

    def __init__(self, message: Optional[PubsubMessage], subscription: Optional[str]) -> None:
        self.message = message
        self.subscription = subscription

    @staticmethod
    def from_dict(obj: Any) -> 'MessagePublishedEvent':
        assert isinstance(obj, dict)
        message = from_union([PubsubMessage.from_dict, from_none], obj.get("message"))
        subscription = from_union([from_str, from_none], obj.get("subscription"))
        return MessagePublishedEvent(message, subscription)

    def to_dict(self) -> dict:
        result: dict = {}
        result["message"] = from_union([lambda x: to_class(PubsubMessage, x), from_none], self.message)
        result["subscription"] = from_union([from_str, from_none], self.subscription)
        return result


class EventClass:
    """This event is triggered when a Pub/Sub message is published."""
    message_published_event: Optional[MessagePublishedEvent]

    def __init__(self, message_published_event: Optional[MessagePublishedEvent]) -> None:
        self.message_published_event = message_published_event

    @staticmethod
    def from_dict(obj: Any) -> 'EventClass':
        assert isinstance(obj, dict)
        message_published_event = from_union([MessagePublishedEvent.from_dict, from_none], obj.get("MessagePublishedEvent"))
        return EventClass(message_published_event)

    def to_dict(self) -> dict:
        result: dict = {}
        result["MessagePublishedEvent"] = from_union([lambda x: to_class(MessagePublishedEvent, x), from_none], self.message_published_event)
        return result


def event_from_dict(s: Any) -> Union[List[Any], bool, EventClass, float, int, None, str]:
    return from_union([from_none, from_float, from_int, from_bool, from_str, lambda x: from_list(lambda x: x, x), EventClass.from_dict], s)


def event_to_dict(x: Union[List[Any], bool, EventClass, float, int, None, str]) -> Any:
    return from_union([from_none, to_float, from_int, from_bool, from_str, lambda x: from_list(lambda x: x, x), lambda x: to_class(EventClass, x)], x)
