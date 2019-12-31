# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ComputeService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ComputeService.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x43omputeService.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\".\n\x16\x61reaOfRectangleRequest\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"$\n\x17\x61reaOfRectangleResponse\x12\t\n\x01z\x18\x01 \x01(\x05\x32\\\n\x0e\x43omputeService\x12J\n\x0f\x61reaOfRectangle\x12\x17.areaOfRectangleRequest\x1a\x18.areaOfRectangleResponse\"\x00(\x01\x30\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_AREAOFRECTANGLEREQUEST = _descriptor.Descriptor(
  name='areaOfRectangleRequest',
  full_name='areaOfRectangleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='areaOfRectangleRequest.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='areaOfRectangleRequest.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=162,
)


_AREAOFRECTANGLERESPONSE = _descriptor.Descriptor(
  name='areaOfRectangleResponse',
  full_name='areaOfRectangleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='z', full_name='areaOfRectangleResponse.z', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=200,
)

DESCRIPTOR.message_types_by_name['areaOfRectangleRequest'] = _AREAOFRECTANGLEREQUEST
DESCRIPTOR.message_types_by_name['areaOfRectangleResponse'] = _AREAOFRECTANGLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

areaOfRectangleRequest = _reflection.GeneratedProtocolMessageType('areaOfRectangleRequest', (_message.Message,), {
  'DESCRIPTOR' : _AREAOFRECTANGLEREQUEST,
  '__module__' : 'ComputeService_pb2'
  # @@protoc_insertion_point(class_scope:areaOfRectangleRequest)
  })
_sym_db.RegisterMessage(areaOfRectangleRequest)

areaOfRectangleResponse = _reflection.GeneratedProtocolMessageType('areaOfRectangleResponse', (_message.Message,), {
  'DESCRIPTOR' : _AREAOFRECTANGLERESPONSE,
  '__module__' : 'ComputeService_pb2'
  # @@protoc_insertion_point(class_scope:areaOfRectangleResponse)
  })
_sym_db.RegisterMessage(areaOfRectangleResponse)



_COMPUTESERVICE = _descriptor.ServiceDescriptor(
  name='ComputeService',
  full_name='ComputeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=202,
  serialized_end=294,
  methods=[
  _descriptor.MethodDescriptor(
    name='areaOfRectangle',
    full_name='ComputeService.areaOfRectangle',
    index=0,
    containing_service=None,
    input_type=_AREAOFRECTANGLEREQUEST,
    output_type=_AREAOFRECTANGLERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMPUTESERVICE)

DESCRIPTOR.services_by_name['ComputeService'] = _COMPUTESERVICE

# @@protoc_insertion_point(module_scope)
