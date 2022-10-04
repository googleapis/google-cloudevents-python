import base64

class PubsubMessage():
    def __init__(self, from_dict=None):
        self._data = None
        self._attributes = None
        self._message_id = None
        self._publish_time = None
        self._ordering_key = None

        if from_dict is not None:
            self._data = base64.b64decode(from_dict.get("data", None))
            self._attributes = from_dict.get("attributes", None)
            self._message_id = from_dict.get("messageId", None)
            self._publish_time = from_dict.get("publishTime", None)
            self._ordering_key = from_dict.get("orderingKey", None)


    @property
    def data(self):
        return base64.b64decode(self._data)

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value

    @property
    def publish_time(self):
        return self._publish_time

    @publish_time.setter
    def publish_time(self, value):
        self._publish_time = value

    @property
    def ordering_key(self):
        return self._ordering_key

    @ordering_key.setter
    def ordering_key(self, value):
        self._ordering_key = value



class MessagePublishedData():
    def __init__(self, from_dict=None):
        self._message = None
        self._subscription = None

        if from_dict is not None:
            self._message = PubsubMessage(from_dict=from_dict["message"])
            self._subscription = from_dict["subscription"]

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = _value

    @property
    def subscription(self):
        return self._subscription

    @subscription.setter
    def subscription(self, value):
        self._subscription = value
