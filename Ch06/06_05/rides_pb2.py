# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rides.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rides.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z\ngateway/pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0brides.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"$\n\x08Location\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lng\x18\x02 \x01(\x01\"\xa8\x01\n\x0cStartRequest\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x03\x12\x11\n\tdriver_id\x18\x02 \x01(\t\x12\x15\n\rpassenger_ids\x18\x03 \x03(\t\x12\x17\n\x04type\x18\x04 \x01(\x0e\x32\t.RideType\x12\x1b\n\x08location\x18\x05 \x01(\x0b\x32\t.Location\x12(\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1b\n\rStartResponse\x12\n\n\x02id\x18\x01 \x01(\t\"e\n\x0cTrackRequest\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x03\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x08location\x18\x03 \x01(\x0b\x32\t.Location\"\x1e\n\rTrackResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x04*!\n\x08RideType\x12\x0b\n\x07REGULAR\x10\x00\x12\x08\n\x04POOL\x10\x01\x32n\n\x05Rides\x12\x39\n\x05Start\x12\r.StartRequest\x1a\x0e.StartResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\"\x06/start:\x01*\x12*\n\x05Track\x12\r.TrackRequest\x1a\x0e.TrackResponse\"\x00(\x01\x42\x0cZ\ngateway/pbb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_RIDETYPE = _descriptor.EnumDescriptor(
  name='RideType',
  full_name='RideType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REGULAR', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POOL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=451,
  serialized_end=484,
)
_sym_db.RegisterEnumDescriptor(_RIDETYPE)

RideType = enum_type_wrapper.EnumTypeWrapper(_RIDETYPE)
REGULAR = 0
POOL = 1



_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='Location.lat', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lng', full_name='Location.lng', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=78,
  serialized_end=114,
)


_STARTREQUEST = _descriptor.Descriptor(
  name='StartRequest',
  full_name='StartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='car_id', full_name='StartRequest.car_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='driver_id', full_name='StartRequest.driver_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passenger_ids', full_name='StartRequest.passenger_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='StartRequest.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='StartRequest.location', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='StartRequest.time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=117,
  serialized_end=285,
)


_STARTRESPONSE = _descriptor.Descriptor(
  name='StartResponse',
  full_name='StartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='StartResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=314,
)


_TRACKREQUEST = _descriptor.Descriptor(
  name='TrackRequest',
  full_name='TrackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='car_id', full_name='TrackRequest.car_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='TrackRequest.time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='TrackRequest.location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=316,
  serialized_end=417,
)


_TRACKRESPONSE = _descriptor.Descriptor(
  name='TrackResponse',
  full_name='TrackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='TrackResponse.count', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=419,
  serialized_end=449,
)

_STARTREQUEST.fields_by_name['type'].enum_type = _RIDETYPE
_STARTREQUEST.fields_by_name['location'].message_type = _LOCATION
_STARTREQUEST.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRACKREQUEST.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRACKREQUEST.fields_by_name['location'].message_type = _LOCATION
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['StartRequest'] = _STARTREQUEST
DESCRIPTOR.message_types_by_name['StartResponse'] = _STARTRESPONSE
DESCRIPTOR.message_types_by_name['TrackRequest'] = _TRACKREQUEST
DESCRIPTOR.message_types_by_name['TrackResponse'] = _TRACKRESPONSE
DESCRIPTOR.enum_types_by_name['RideType'] = _RIDETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'rides_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  })
_sym_db.RegisterMessage(Location)

StartRequest = _reflection.GeneratedProtocolMessageType('StartRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTREQUEST,
  '__module__' : 'rides_pb2'
  # @@protoc_insertion_point(class_scope:StartRequest)
  })
_sym_db.RegisterMessage(StartRequest)

StartResponse = _reflection.GeneratedProtocolMessageType('StartResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTRESPONSE,
  '__module__' : 'rides_pb2'
  # @@protoc_insertion_point(class_scope:StartResponse)
  })
_sym_db.RegisterMessage(StartResponse)

TrackRequest = _reflection.GeneratedProtocolMessageType('TrackRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRACKREQUEST,
  '__module__' : 'rides_pb2'
  # @@protoc_insertion_point(class_scope:TrackRequest)
  })
_sym_db.RegisterMessage(TrackRequest)

TrackResponse = _reflection.GeneratedProtocolMessageType('TrackResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRACKRESPONSE,
  '__module__' : 'rides_pb2'
  # @@protoc_insertion_point(class_scope:TrackResponse)
  })
_sym_db.RegisterMessage(TrackResponse)


DESCRIPTOR._options = None

_RIDES = _descriptor.ServiceDescriptor(
  name='Rides',
  full_name='Rides',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=486,
  serialized_end=596,
  methods=[
  _descriptor.MethodDescriptor(
    name='Start',
    full_name='Rides.Start',
    index=0,
    containing_service=None,
    input_type=_STARTREQUEST,
    output_type=_STARTRESPONSE,
    serialized_options=b'\202\323\344\223\002\013\"\006/start:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Track',
    full_name='Rides.Track',
    index=1,
    containing_service=None,
    input_type=_TRACKREQUEST,
    output_type=_TRACKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RIDES)

DESCRIPTOR.services_by_name['Rides'] = _RIDES

# @@protoc_insertion_point(module_scope)
