from google.protobuf.json_format import ParseDict


from google.events.firebase.database.v1.events_pb2 import ReferenceCreatedEvent

from google.events.firebase.database.v1.events_pb2 import ReferenceDeletedEvent

from google.events.firebase.database.v1.events_pb2 import ReferenceUpdatedEvent

from google.events.firebase.database.v1.events_pb2 import ReferenceWrittenEvent

from google.events.firebase.auth.v1.events_pb2 import UserCreatedEvent

from google.events.firebase.auth.v1.events_pb2 import UserDeletedEvent

from google.events.firebase.remoteconfig.v1.events_pb2 import RemoteConfigUpdatedEvent

from google.events.firebase.analytics.v1.events_pb2 import AnalyticsLogWrittenEvent

from google.events.cloud.firestore.v1.events_pb2 import DocumentCreatedEvent

from google.events.cloud.firestore.v1.events_pb2 import DocumentDeletedEvent

from google.events.cloud.firestore.v1.events_pb2 import DocumentUpdatedEvent

from google.events.cloud.firestore.v1.events_pb2 import DocumentWrittenEvent

from google.events.cloud.scheduler.v1.events_pb2 import JobExecutedEvent

from google.events.cloud.storage.v1.events_pb2 import ObjectArchivedEvent

from google.events.cloud.storage.v1.events_pb2 import ObjectDeletedEvent

from google.events.cloud.storage.v1.events_pb2 import ObjectFinalizedEvent

from google.events.cloud.storage.v1.events_pb2 import ObjectMetadataUpdatedEvent

from google.events.cloud.audit.v1.events_pb2 import AuditLogWrittenEvent

from google.events.cloud.pubsub.v1.events_pb2 import MessagePublishedEvent


@classmethod
def from_dikt(cls, dikt):
    message = cls()
    dikt = { 'data': dikt }
    return ParseDict(dikt, message)


ReferenceCreatedEvent.from_dikt = from_dikt

ReferenceDeletedEvent.from_dikt = from_dikt

ReferenceUpdatedEvent.from_dikt = from_dikt

ReferenceWrittenEvent.from_dikt = from_dikt

UserCreatedEvent.from_dikt = from_dikt

UserDeletedEvent.from_dikt = from_dikt

RemoteConfigUpdatedEvent.from_dikt = from_dikt

AnalyticsLogWrittenEvent.from_dikt = from_dikt

DocumentCreatedEvent.from_dikt = from_dikt

DocumentDeletedEvent.from_dikt = from_dikt

DocumentUpdatedEvent.from_dikt = from_dikt

DocumentWrittenEvent.from_dikt = from_dikt

JobExecutedEvent.from_dikt = from_dikt

ObjectArchivedEvent.from_dikt = from_dikt

ObjectDeletedEvent.from_dikt = from_dikt

ObjectFinalizedEvent.from_dikt = from_dikt

ObjectMetadataUpdatedEvent.from_dikt = from_dikt

AuditLogWrittenEvent.from_dikt = from_dikt

MessagePublishedEvent.from_dikt = from_dikt
