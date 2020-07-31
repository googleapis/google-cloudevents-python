import json

from google.cloud import storage
from google.events import DocumentUpdatedEvent

BUCKET = 'firestore-change-events'

def firestore_data_change(data, context):
    DocumentUpdatedEvent.from_dikt(data)

    print(DocumentUpdatedEvent.data.value)
    print(DocumentUpdatedEvent.data.old_value)
