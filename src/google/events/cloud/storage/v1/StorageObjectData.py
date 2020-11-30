# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Optional, Union, Dict
from datetime import datetime


class CustomerEncryption:
    """Metadata of customer-supplied encryption key, if the object is encrypted by
    such a key.
    """
    """The encryption algorithm."""
    encryption_algorithm: Optional[str]
    """SHA256 hash value of the encryption key."""
    key_sha256: Optional[str]

    def __init__(self, encryption_algorithm: Optional[str], key_sha256: Optional[str]) -> None:
        self.encryption_algorithm = encryption_algorithm
        self.key_sha256 = key_sha256


class StorageObjectData:
    """An object within Google Cloud Storage."""
    """The name of the bucket containing this object."""
    bucket: Optional[str]
    """Cache-Control directive for the object data, matching
    [https://tools.ietf.org/html/rfc7234#section-5.2"][RFC 7234 §5.2].
    """
    cache_control: Optional[str]
    """Number of underlying components that make up this object. Components are
    accumulated by compose operations.
    Attempting to set this field will result in an error.
    """
    component_count: Optional[int]
    """Content-Disposition of the object data, matching
    [https://tools.ietf.org/html/rfc6266][RFC 6266].
    """
    content_disposition: Optional[str]
    """Content-Encoding of the object data, matching
    [https://tools.ietf.org/html/rfc7231#section-3.1.2.2][RFC 7231 §3.1.2.2]
    """
    content_encoding: Optional[str]
    """Content-Language of the object data, matching
    [https://tools.ietf.org/html/rfc7231#section-3.1.3.2][RFC 7231 §3.1.3.2].
    """
    content_language: Optional[str]
    """Content-Type of the object data, matching
    [https://tools.ietf.org/html/rfc7231#section-3.1.1.5][RFC 7231 §3.1.1.5].
    If an object is stored without a Content-Type, it is served as
    `application/octet-stream`.
    """
    content_type: Optional[str]
    """CRC32c checksum. For more information about using the CRC32c
    checksum, see
    [https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI][Hashes and
    ETags: Best Practices].
    """
    crc32_c: Optional[str]
    """Metadata of customer-supplied encryption key, if the object is encrypted by
    such a key.
    """
    customer_encryption: Optional[CustomerEncryption]
    """HTTP 1.1 Entity tag for the object. See
    [https://tools.ietf.org/html/rfc7232#section-2.3][RFC 7232 §2.3].
    """
    etag: Optional[str]
    """Whether an object is under event-based hold."""
    event_based_hold: Optional[bool]
    """The content generation of this object. Used for object versioning.
    Attempting to set this field will result in an error.
    """
    generation: Union[int, None, str]
    """The ID of the object, including the bucket name, object name, and
    generation number.
    """
    id: Optional[str]
    """The kind of item this is. For objects, this is always "storage#object"."""
    kind: Optional[str]
    """Cloud KMS Key used to encrypt this object, if the object is encrypted by
    such a key.
    """
    kms_key_name: Optional[str]
    """MD5 hash of the data; encoded using base64 as per
    [https://tools.ietf.org/html/rfc4648#section-4][RFC 4648 §4]. For more
    information about using the MD5 hash, see
    [https://cloud.google.com/storage/docs/hashes-etags#_JSONAPI][Hashes and
    ETags: Best Practices].
    """
    md5_hash: Optional[str]
    """Media download link."""
    media_link: Optional[str]
    """User-provided metadata, in key/value pairs."""
    metadata: Optional[Dict[str, str]]
    """The version of the metadata for this object at this generation. Used for
    preconditions and for detecting changes in metadata. A metageneration
    number is only meaningful in the context of a particular generation of a
    particular object.
    """
    metageneration: Union[int, None, str]
    """The name of the object."""
    name: Optional[str]
    """A server-determined value that specifies the earliest time that the
    object's retention period expires.
    """
    retention_expiration_time: Optional[datetime]
    """The link to this object."""
    self_link: Optional[str]
    """Content-Length of the object data in bytes, matching
    [https://tools.ietf.org/html/rfc7230#section-3.3.2][RFC 7230 §3.3.2].
    """
    size: Union[int, None, str]
    """Storage class of the object."""
    storage_class: Optional[str]
    """Whether an object is under temporary hold."""
    temporary_hold: Optional[bool]
    """The creation time of the object.
    Attempting to set this field will result in an error.
    """
    time_created: Optional[datetime]
    """The deletion time of the object. Will be returned if and only if this
    version of the object has been deleted.
    """
    time_deleted: Optional[datetime]
    """The time at which the object's storage class was last changed."""
    time_storage_class_updated: Optional[datetime]
    """The modification time of the object metadata."""
    updated: Optional[datetime]

    def __init__(self, bucket: Optional[str], cache_control: Optional[str], component_count: Optional[int], content_disposition: Optional[str], content_encoding: Optional[str], content_language: Optional[str], content_type: Optional[str], crc32_c: Optional[str], customer_encryption: Optional[CustomerEncryption], etag: Optional[str], event_based_hold: Optional[bool], generation: Union[int, None, str], id: Optional[str], kind: Optional[str], kms_key_name: Optional[str], md5_hash: Optional[str], media_link: Optional[str], metadata: Optional[Dict[str, str]], metageneration: Union[int, None, str], name: Optional[str], retention_expiration_time: Optional[datetime], self_link: Optional[str], size: Union[int, None, str], storage_class: Optional[str], temporary_hold: Optional[bool], time_created: Optional[datetime], time_deleted: Optional[datetime], time_storage_class_updated: Optional[datetime], updated: Optional[datetime]) -> None:
        self.bucket = bucket
        self.cache_control = cache_control
        self.component_count = component_count
        self.content_disposition = content_disposition
        self.content_encoding = content_encoding
        self.content_language = content_language
        self.content_type = content_type
        self.crc32_c = crc32_c
        self.customer_encryption = customer_encryption
        self.etag = etag
        self.event_based_hold = event_based_hold
        self.generation = generation
        self.id = id
        self.kind = kind
        self.kms_key_name = kms_key_name
        self.md5_hash = md5_hash
        self.media_link = media_link
        self.metadata = metadata
        self.metageneration = metageneration
        self.name = name
        self.retention_expiration_time = retention_expiration_time
        self.self_link = self_link
        self.size = size
        self.storage_class = storage_class
        self.temporary_hold = temporary_hold
        self.time_created = time_created
        self.time_deleted = time_deleted
        self.time_storage_class_updated = time_storage_class_updated
        self.updated = updated
