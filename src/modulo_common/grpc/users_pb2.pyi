import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_TYPE_UNSPECIFIED: _ClassVar[ProviderType]
    PROVIDER_TYPE_APPLE: _ClassVar[ProviderType]
    PROVIDER_TYPE_GOOGLE: _ClassVar[ProviderType]
    PROVIDER_TYPE_CLASSIC: _ClassVar[ProviderType]
PROVIDER_TYPE_UNSPECIFIED: ProviderType
PROVIDER_TYPE_APPLE: ProviderType
PROVIDER_TYPE_GOOGLE: ProviderType
PROVIDER_TYPE_CLASSIC: ProviderType

class UserBody(_message.Message):
    __slots__ = ("email", "firstName", "provider", "providerId")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    email: str
    firstName: str
    provider: ProviderType
    providerId: str
    def __init__(self, email: _Optional[str] = ..., firstName: _Optional[str] = ..., provider: _Optional[_Union[ProviderType, str]] = ..., providerId: _Optional[str] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ("id", "firstName", "email", "provider", "createdAt", "isNewUser")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    ISNEWUSER_FIELD_NUMBER: _ClassVar[int]
    id: str
    firstName: str
    email: str
    provider: ProviderType
    createdAt: _timestamp_pb2.Timestamp
    isNewUser: bool
    def __init__(self, id: _Optional[str] = ..., firstName: _Optional[str] = ..., email: _Optional[str] = ..., provider: _Optional[_Union[ProviderType, str]] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., isNewUser: _Optional[bool] = ...) -> None: ...
