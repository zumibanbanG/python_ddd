# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: todo.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'todo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\"A\n\x0e\x41\x64\x64TaskRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x10\n\x08\x64ue_date\x18\x03 \x01(\t\"\x1d\n\x0f\x41\x64\x64TaskResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x1c\n\x0eGetTaskRequest\x12\n\n\x02id\x18\x01 \x01(\t\"N\n\x0fGetTaskResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x10\n\x08\x64ue_date\x18\x04 \x01(\t\"\x1f\n\x11RemoveTaskRequest\x12\n\n\x02id\x18\x01 \x01(\t\" \n\x12RemoveTaskResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x14\n\x12ListAllTaskRequest\"6\n\x13ListAllTaskResponse\x12\x1f\n\x05tasks\x18\x01 \x03(\x0b\x32\x10.GetTaskResponse2\xd4\x01\n\x05Tasks\x12,\n\x07\x41\x64\x64Task\x12\x0f.AddTaskRequest\x1a\x10.AddTaskResponse\x12,\n\x07GetTask\x12\x0f.GetTaskRequest\x1a\x10.GetTaskResponse\x12\x35\n\nRemoveTask\x12\x12.RemoveTaskRequest\x1a\x13.RemoveTaskResponse\x12\x38\n\x0bListAllTask\x12\x13.ListAllTaskRequest\x1a\x14.ListAllTaskResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'todo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADDTASKREQUEST']._serialized_start=14
  _globals['_ADDTASKREQUEST']._serialized_end=79
  _globals['_ADDTASKRESPONSE']._serialized_start=81
  _globals['_ADDTASKRESPONSE']._serialized_end=110
  _globals['_GETTASKREQUEST']._serialized_start=112
  _globals['_GETTASKREQUEST']._serialized_end=140
  _globals['_GETTASKRESPONSE']._serialized_start=142
  _globals['_GETTASKRESPONSE']._serialized_end=220
  _globals['_REMOVETASKREQUEST']._serialized_start=222
  _globals['_REMOVETASKREQUEST']._serialized_end=253
  _globals['_REMOVETASKRESPONSE']._serialized_start=255
  _globals['_REMOVETASKRESPONSE']._serialized_end=287
  _globals['_LISTALLTASKREQUEST']._serialized_start=289
  _globals['_LISTALLTASKREQUEST']._serialized_end=309
  _globals['_LISTALLTASKRESPONSE']._serialized_start=311
  _globals['_LISTALLTASKRESPONSE']._serialized_end=365
  _globals['_TASKS']._serialized_start=368
  _globals['_TASKS']._serialized_end=580
# @@protoc_insertion_point(module_scope)
