from typing import Optional, Dict


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


class MessagePublishedData:
    """The data received in an event when a message is published to a topic."""
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
