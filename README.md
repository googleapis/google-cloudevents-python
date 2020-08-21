# Google CloudEvents - Python

This library provides classes of common event types used with Google services.
At this moment the following types are available:

| Package | Python Class | Description |
| ------------- | ------------- | ------------- |
| google.events.cloud.audit.v1 | AuditLogWrittenEvent | The event is triggered when a new Cloud Audit Log entry is written. |
| google.events.cloud.pubsub.v1 | MessagePublishedEvent | This event is triggered when a new Cloud Pub/Sub event is published to a topic. |


## Installation and Usage

**Note**: This library requires Python 3.7+.

To install this package, run

``` sh
pip install --upgrade google-events
```

To use an event class, see the snippet below:

``` python
from google.events import MessagePublishedEvent

# Parses a Dict into an event
# The Dict may be an argument in a background Cloud Function,
# or the payload of an HTTP request received by a Cloud Run service with event
# triggers.
event = MessagePublishedEvent.from_dict(event_data)
print(event.message)
```

## Generation

**Note**: Before generating the package, install and set up
[quicktype](https://quicktype.io/) and Python 3.7+.

To generate this package, run

``` sh
chmod +x gen.sh
./gen.sh
```