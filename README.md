# Google CloudEvents - Python

This library provides classes of common event types used with Google services.
At this moment the following types are available:

| Package | Python Class | Description |
| ------------- | ------------- | ------------- |
| google.events.cloud.scheduler.v1 | SchedulerJobData | Scheduler job data. |
| google.events.firebase.database.v1 | ReferenceEventData | The data within all Firebase Real Time Database reference events. |
| google.events.cloud.pubsub.v1 | MessagePublishedData | The event data when a message is published to a topic. |
| google.events.firebase.remoteconfig.v1 | RemoteConfigEventData | The data within all Firebase Remote Config events. |
| google.events.firebase.auth.v1 | AuthEventData | The data within all Firebase Auth events. |
| google.events.cloud.storage.v1 | StorageObjectData | An object within Google Cloud Storage. |
| google.events.cloud.firestore.v1 | DocumentEventData | The data within all Firestore document events. |
| google.events.firebase.analytics.v1 | AnalyticsLogData | The data within Firebase Analytics log events. |
| google.events.cloud.audit.v1 | LogEntryData | The data within all Cloud Audit Logs log entry events. |
| google.events.cloud.cloudbuild.v1 | BuildEventData | Build event data for Google Cloud Platform API operations. |

## Installation and Usage

**Note**: This library requires Python 3.7+.

To install this package, run

``` sh
pip install --upgrade google-events
```

To use an event class, see the snippet below:

``` python
from google.events.cloud.pubsub.v1 import MessagePublishedData

# Parses a Dict into an event
# The Dict may be an argument in a background Cloud Function,
# or the payload of an HTTP request received by a Cloud Run service with event
# triggers.
event_data = "Some event data"
event = MessagePublishedData.from_dict(event_data)
print(event.message)
```
