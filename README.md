# Google CloudEvents - Python

This library provides classes of common event types used with Google services.
At this moment the following types are available:

| Package | Python Class | Description |
| ------------- | ------------- | ------------- |
| google.events.cloud.pubsub.v1 | MessagePublishedData | A message that is published by publishers and consumed by subscribers. |
| google.events.cloud.audit.v1 | LogEntryData | This event is triggered when a new audit log entry is written. |

## Installation and Usage

**Note**: This library requires Python 3.7+.

To install this package, run

``` sh
pip install --upgrade google-events
```

To use an event class, see the snippet below:

``` python
from google.events.cloud.pubsub.v1 import MessagePublishedEvent

# Parses a Dict into an event
# The Dict may be an argument in a background Cloud Function,
# or the payload of an HTTP request received by a Cloud Run service with event
# triggers.
event_data = "Some event data"
event = MessagePublishedData.from_dict(event_data)
print(event.message)
```
