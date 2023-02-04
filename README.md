# Google CloudEvents - Python

[![PyPI version](https://badge.fury.io/py/google-events.svg)](https://badge.fury.io/py/google-events)

This library provides classes of common event types used with Google services,
as defined in the [Google Cloudevents repository](https://github.com/googleapis/google-cloudevents).

## Installation and Usage

**Note**: This library requires Python 3.7+.

To install this package, run

``` sh
pip install --upgrade google-events
```

To use an event class, see the snippet below:

``` python
from google.events.cloud import storage

# Parses a json string containing an event payload
# The json payload may be from an HTTP request received by a Cloud Run
# service with event triggers.

def handle_event_trigger(json_payload):
    event = storage.StorageObjectData.from_json(json_payload)
    print(f"{event.bucket}/{event.name} had event")
    return "OK"
```
