# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/events/cloud/cloudbuild/v1/data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/events/cloud/cloudbuild/v1/data.proto\x12!google.events.cloud.cloudbuild.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xec\n\n\x0e\x42uildEventData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x10 \x01(\t\x12H\n\x06status\x18\x02 \x01(\x0e\x32\x38.google.events.cloud.cloudbuild.v1.BuildEventData.Status\x12\x15\n\rstatus_detail\x18\x18 \x01(\t\x12\x39\n\x06source\x18\x03 \x01(\x0b\x32).google.events.cloud.cloudbuild.v1.Source\x12;\n\x05steps\x18\x0b \x03(\x0b\x32,.google.events.cloud.cloudbuild.v1.BuildStep\x12;\n\x07results\x18\n \x01(\x0b\x32*.google.events.cloud.cloudbuild.v1.Results\x12/\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inish_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x07timeout\x18\x0c \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0e\n\x06images\x18\r \x03(\t\x12,\n\tqueue_ttl\x18( \x01(\x0b\x32\x19.google.protobuf.Duration\x12?\n\tartifacts\x18% \x01(\x0b\x32,.google.events.cloud.cloudbuild.v1.Artifacts\x12\x13\n\x0blogs_bucket\x18\x13 \x01(\t\x12N\n\x11source_provenance\x18\x15 \x01(\x0b\x32\x33.google.events.cloud.cloudbuild.v1.SourceProvenance\x12\x18\n\x10\x62uild_trigger_id\x18\x16 \x01(\t\x12@\n\x07options\x18\x17 \x01(\x0b\x32/.google.events.cloud.cloudbuild.v1.BuildOptions\x12\x0f\n\x07log_url\x18\x19 \x01(\t\x12[\n\rsubstitutions\x18\x1d \x03(\x0b\x32\x44.google.events.cloud.cloudbuild.v1.BuildEventData.SubstitutionsEntry\x12\x0c\n\x04tags\x18\x1f \x03(\t\x12:\n\x07secrets\x18  \x03(\x0b\x32).google.events.cloud.cloudbuild.v1.Secret\x12M\n\x06timing\x18! \x03(\x0b\x32=.google.events.cloud.cloudbuild.v1.BuildEventData.TimingEntry\x1a\x34\n\x12SubstitutionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aZ\n\x0bTimingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.google.events.cloud.cloudbuild.v1.TimeSpan:\x02\x38\x01\"\x8c\x01\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\x0b\n\x07WORKING\x10\x02\x12\x0b\n\x07SUCCESS\x10\x03\x12\x0b\n\x07\x46\x41ILURE\x10\x04\x12\x12\n\x0eINTERNAL_ERROR\x10\x05\x12\x0b\n\x07TIMEOUT\x10\x06\x12\r\n\tCANCELLED\x10\x07\x12\x0b\n\x07\x45XPIRED\x10\t\"\xa4\x01\n\x06Source\x12J\n\x0estorage_source\x18\x02 \x01(\x0b\x32\x30.google.events.cloud.cloudbuild.v1.StorageSourceH\x00\x12\x44\n\x0brepo_source\x18\x03 \x01(\x0b\x32-.google.events.cloud.cloudbuild.v1.RepoSourceH\x00\x42\x08\n\x06source\"C\n\rStorageSource\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x0e\n\x06object\x18\x02 \x01(\t\x12\x12\n\ngeneration\x18\x03 \x01(\x03\"\xb2\x02\n\nRepoSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\trepo_name\x18\x02 \x01(\t\x12\x15\n\x0b\x62ranch_name\x18\x03 \x01(\tH\x00\x12\x12\n\x08tag_name\x18\x04 \x01(\tH\x00\x12\x14\n\ncommit_sha\x18\x05 \x01(\tH\x00\x12\x0b\n\x03\x64ir\x18\x07 \x01(\t\x12\x14\n\x0cinvert_regex\x18\x08 \x01(\x08\x12W\n\rsubstitutions\x18\t \x03(\x0b\x32@.google.events.cloud.cloudbuild.v1.RepoSource.SubstitutionsEntry\x1a\x34\n\x12SubstitutionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\n\n\x08revision\"\xb8\x03\n\tBuildStep\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x65nv\x18\x02 \x03(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x0b\n\x03\x64ir\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x10\n\x08wait_for\x18\x06 \x03(\t\x12\x12\n\nentrypoint\x18\x07 \x01(\t\x12\x12\n\nsecret_env\x18\x08 \x03(\t\x12:\n\x07volumes\x18\t \x03(\x0b\x32).google.events.cloud.cloudbuild.v1.Volume\x12;\n\x06timing\x18\n \x01(\x0b\x32+.google.events.cloud.cloudbuild.v1.TimeSpan\x12@\n\x0bpull_timing\x18\r \x01(\x0b\x32+.google.events.cloud.cloudbuild.v1.TimeSpan\x12*\n\x07timeout\x18\x0b \x01(\x0b\x32\x19.google.protobuf.Duration\x12H\n\x06status\x18\x0c \x01(\x0e\x32\x38.google.events.cloud.cloudbuild.v1.BuildEventData.Status\"$\n\x06Volume\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"\xf7\x01\n\x07Results\x12=\n\x06images\x18\x02 \x03(\x0b\x32-.google.events.cloud.cloudbuild.v1.BuiltImage\x12\x19\n\x11\x62uild_step_images\x18\x03 \x03(\t\x12\x19\n\x11\x61rtifact_manifest\x18\x04 \x01(\t\x12\x15\n\rnum_artifacts\x18\x05 \x01(\x03\x12\x1a\n\x12\x62uild_step_outputs\x18\x06 \x03(\x0c\x12\x44\n\x0f\x61rtifact_timing\x18\x07 \x01(\x0b\x32+.google.events.cloud.cloudbuild.v1.TimeSpan\"l\n\nBuiltImage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x64igest\x18\x03 \x01(\t\x12@\n\x0bpush_timing\x18\x04 \x01(\x0b\x32+.google.events.cloud.cloudbuild.v1.TimeSpan\"\xdb\x01\n\tArtifacts\x12\x0e\n\x06images\x18\x01 \x03(\t\x12M\n\x07objects\x18\x02 \x01(\x0b\x32<.google.events.cloud.cloudbuild.v1.Artifacts.ArtifactObjects\x1ao\n\x0f\x41rtifactObjects\x12\x10\n\x08location\x18\x01 \x01(\t\x12\r\n\x05paths\x18\x02 \x03(\t\x12;\n\x06timing\x18\x03 \x01(\x0b\x32+.google.events.cloud.cloudbuild.v1.TimeSpan\"h\n\x08TimeSpan\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xee\x02\n\x10SourceProvenance\x12Q\n\x17resolved_storage_source\x18\x03 \x01(\x0b\x32\x30.google.events.cloud.cloudbuild.v1.StorageSource\x12K\n\x14resolved_repo_source\x18\x06 \x01(\x0b\x32-.google.events.cloud.cloudbuild.v1.RepoSource\x12X\n\x0b\x66ile_hashes\x18\x04 \x03(\x0b\x32\x43.google.events.cloud.cloudbuild.v1.SourceProvenance.FileHashesEntry\x1a`\n\x0f\x46ileHashesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.google.events.cloud.cloudbuild.v1.FileHashes:\x02\x38\x01\"H\n\nFileHashes\x12:\n\tfile_hash\x18\x01 \x03(\x0b\x32\'.google.events.cloud.cloudbuild.v1.Hash\"\x80\x01\n\x04Hash\x12>\n\x04type\x18\x01 \x01(\x0e\x32\x30.google.events.cloud.cloudbuild.v1.Hash.HashType\x12\r\n\x05value\x18\x02 \x01(\x0c\")\n\x08HashType\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06SHA256\x10\x01\x12\x07\n\x03MD5\x10\x02\"\x9e\x01\n\x06Secret\x12\x14\n\x0ckms_key_name\x18\x01 \x01(\t\x12L\n\nsecret_env\x18\x03 \x03(\x0b\x32\x38.google.events.cloud.cloudbuild.v1.Secret.SecretEnvEntry\x1a\x30\n\x0eSecretEnvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xe2\x07\n\x0c\x42uildOptions\x12P\n\x16source_provenance_hash\x18\x01 \x03(\x0e\x32\x30.google.events.cloud.cloudbuild.v1.Hash.HashType\x12]\n\x17requested_verify_option\x18\x02 \x01(\x0e\x32<.google.events.cloud.cloudbuild.v1.BuildOptions.VerifyOption\x12Q\n\x0cmachine_type\x18\x03 \x01(\x0e\x32;.google.events.cloud.cloudbuild.v1.BuildOptions.MachineType\x12\x14\n\x0c\x64isk_size_gb\x18\x06 \x01(\x03\x12_\n\x13substitution_option\x18\x04 \x01(\x0e\x32\x42.google.events.cloud.cloudbuild.v1.BuildOptions.SubstitutionOption\x12`\n\x14log_streaming_option\x18\x05 \x01(\x0e\x32\x42.google.events.cloud.cloudbuild.v1.BuildOptions.LogStreamingOption\x12\x13\n\x0bworker_pool\x18\x07 \x01(\t\x12L\n\x07logging\x18\x0b \x01(\x0e\x32;.google.events.cloud.cloudbuild.v1.BuildOptions.LoggingMode\x12\x0b\n\x03\x65nv\x18\x0c \x03(\t\x12\x12\n\nsecret_env\x18\r \x03(\t\x12:\n\x07volumes\x18\x0e \x03(\x0b\x32).google.events.cloud.cloudbuild.v1.Volume\".\n\x0cVerifyOption\x12\x10\n\x0cNOT_VERIFIED\x10\x00\x12\x0c\n\x08VERIFIED\x10\x01\"C\n\x0bMachineType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x10\n\x0cN1_HIGHCPU_8\x10\x01\x12\x11\n\rN1_HIGHCPU_32\x10\x02\"5\n\x12SubstitutionOption\x12\x0e\n\nMUST_MATCH\x10\x00\x12\x0f\n\x0b\x41LLOW_LOOSE\x10\x01\"G\n\x12LogStreamingOption\x12\x12\n\x0eSTREAM_DEFAULT\x10\x00\x12\r\n\tSTREAM_ON\x10\x01\x12\x0e\n\nSTREAM_OFF\x10\x02\"@\n\x0bLoggingMode\x12\x17\n\x13LOGGING_UNSPECIFIED\x10\x00\x12\n\n\x06LEGACY\x10\x01\x12\x0c\n\x08GCS_ONLY\x10\x02\x42-\xaa\x02*Google.Events.Protobuf.Cloud.CloudBuild.V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.events.cloud.cloudbuild.v1.data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002*Google.Events.Protobuf.Cloud.CloudBuild.V1'
  _BUILDEVENTDATA_SUBSTITUTIONSENTRY._options = None
  _BUILDEVENTDATA_SUBSTITUTIONSENTRY._serialized_options = b'8\001'
  _BUILDEVENTDATA_TIMINGENTRY._options = None
  _BUILDEVENTDATA_TIMINGENTRY._serialized_options = b'8\001'
  _REPOSOURCE_SUBSTITUTIONSENTRY._options = None
  _REPOSOURCE_SUBSTITUTIONSENTRY._serialized_options = b'8\001'
  _SOURCEPROVENANCE_FILEHASHESENTRY._options = None
  _SOURCEPROVENANCE_FILEHASHESENTRY._serialized_options = b'8\001'
  _SECRET_SECRETENVENTRY._options = None
  _SECRET_SECRETENVENTRY._serialized_options = b'8\001'
  _BUILDEVENTDATA._serialized_start=149
  _BUILDEVENTDATA._serialized_end=1537
  _BUILDEVENTDATA_SUBSTITUTIONSENTRY._serialized_start=1250
  _BUILDEVENTDATA_SUBSTITUTIONSENTRY._serialized_end=1302
  _BUILDEVENTDATA_TIMINGENTRY._serialized_start=1304
  _BUILDEVENTDATA_TIMINGENTRY._serialized_end=1394
  _BUILDEVENTDATA_STATUS._serialized_start=1397
  _BUILDEVENTDATA_STATUS._serialized_end=1537
  _SOURCE._serialized_start=1540
  _SOURCE._serialized_end=1704
  _STORAGESOURCE._serialized_start=1706
  _STORAGESOURCE._serialized_end=1773
  _REPOSOURCE._serialized_start=1776
  _REPOSOURCE._serialized_end=2082
  _REPOSOURCE_SUBSTITUTIONSENTRY._serialized_start=1250
  _REPOSOURCE_SUBSTITUTIONSENTRY._serialized_end=1302
  _BUILDSTEP._serialized_start=2085
  _BUILDSTEP._serialized_end=2525
  _VOLUME._serialized_start=2527
  _VOLUME._serialized_end=2563
  _RESULTS._serialized_start=2566
  _RESULTS._serialized_end=2813
  _BUILTIMAGE._serialized_start=2815
  _BUILTIMAGE._serialized_end=2923
  _ARTIFACTS._serialized_start=2926
  _ARTIFACTS._serialized_end=3145
  _ARTIFACTS_ARTIFACTOBJECTS._serialized_start=3034
  _ARTIFACTS_ARTIFACTOBJECTS._serialized_end=3145
  _TIMESPAN._serialized_start=3147
  _TIMESPAN._serialized_end=3251
  _SOURCEPROVENANCE._serialized_start=3254
  _SOURCEPROVENANCE._serialized_end=3620
  _SOURCEPROVENANCE_FILEHASHESENTRY._serialized_start=3524
  _SOURCEPROVENANCE_FILEHASHESENTRY._serialized_end=3620
  _FILEHASHES._serialized_start=3622
  _FILEHASHES._serialized_end=3694
  _HASH._serialized_start=3697
  _HASH._serialized_end=3825
  _HASH_HASHTYPE._serialized_start=3784
  _HASH_HASHTYPE._serialized_end=3825
  _SECRET._serialized_start=3828
  _SECRET._serialized_end=3986
  _SECRET_SECRETENVENTRY._serialized_start=3938
  _SECRET_SECRETENVENTRY._serialized_end=3986
  _BUILDOPTIONS._serialized_start=3989
  _BUILDOPTIONS._serialized_end=4983
  _BUILDOPTIONS_VERIFYOPTION._serialized_start=4674
  _BUILDOPTIONS_VERIFYOPTION._serialized_end=4720
  _BUILDOPTIONS_MACHINETYPE._serialized_start=4722
  _BUILDOPTIONS_MACHINETYPE._serialized_end=4789
  _BUILDOPTIONS_SUBSTITUTIONOPTION._serialized_start=4791
  _BUILDOPTIONS_SUBSTITUTIONOPTION._serialized_end=4844
  _BUILDOPTIONS_LOGSTREAMINGOPTION._serialized_start=4846
  _BUILDOPTIONS_LOGSTREAMINGOPTION._serialized_end=4917
  _BUILDOPTIONS_LOGGINGMODE._serialized_start=4919
  _BUILDOPTIONS_LOGGINGMODE._serialized_end=4983
# @@protoc_insertion_point(module_scope)