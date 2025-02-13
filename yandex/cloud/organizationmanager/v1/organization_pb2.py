# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/organizationmanager/v1/organization.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/organizationmanager/v1/organization.proto',
  package='yandex.cloud.organizationmanager.v1',
  syntax='proto3',
  serialized_options=b'\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanager',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6yandex/cloud/organizationmanager/v1/organization.proto\x12#yandex.cloud.organizationmanager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfa\x01\n\x0cOrganization\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\r\n\x05title\x18\x06 \x01(\t\x12M\n\x06labels\x18\x07 \x03(\x0b\x32=.yandex.cloud.organizationmanager.v1.Organization.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x86\x01\n\'yandex.cloud.api.organizationmanager.v1Z[github.com/yandex-cloud/go-genproto/yandex/cloud/organizationmanager/v1;organizationmanagerb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_ORGANIZATION_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.organizationmanager.v1.Organization.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.organizationmanager.v1.Organization.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.organizationmanager.v1.Organization.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=379,
)

_ORGANIZATION = _descriptor.Descriptor(
  name='Organization',
  full_name='yandex.cloud.organizationmanager.v1.Organization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.organizationmanager.v1.Organization.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.organizationmanager.v1.Organization.created_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.organizationmanager.v1.Organization.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.organizationmanager.v1.Organization.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='yandex.cloud.organizationmanager.v1.Organization.title', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.organizationmanager.v1.Organization.labels', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ORGANIZATION_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=379,
)

_ORGANIZATION_LABELSENTRY.containing_type = _ORGANIZATION
_ORGANIZATION.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ORGANIZATION.fields_by_name['labels'].message_type = _ORGANIZATION_LABELSENTRY
DESCRIPTOR.message_types_by_name['Organization'] = _ORGANIZATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Organization = _reflection.GeneratedProtocolMessageType('Organization', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ORGANIZATION_LABELSENTRY,
    '__module__' : 'yandex.cloud.organizationmanager.v1.organization_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.Organization.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _ORGANIZATION,
  '__module__' : 'yandex.cloud.organizationmanager.v1.organization_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.organizationmanager.v1.Organization)
  })
_sym_db.RegisterMessage(Organization)
_sym_db.RegisterMessage(Organization.LabelsEntry)


DESCRIPTOR._options = None
_ORGANIZATION_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
