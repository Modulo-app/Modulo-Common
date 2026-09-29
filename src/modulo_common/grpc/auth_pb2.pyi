from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppleUserBody(_message.Message):
    __slots__ = ("identityToken", "authorizationCode", "firstName")
    IDENTITYTOKEN_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATIONCODE_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    identityToken: str
    authorizationCode: str
    firstName: str
    def __init__(self, identityToken: _Optional[str] = ..., authorizationCode: _Optional[str] = ..., firstName: _Optional[str] = ...) -> None: ...

class AppleUserResponse(_message.Message):
    __slots__ = ("userId", "isNewAccount", "tokens")
    USERID_FIELD_NUMBER: _ClassVar[int]
    ISNEWACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    userId: str
    isNewAccount: bool
    tokens: TokenResponse
    def __init__(self, userId: _Optional[str] = ..., isNewAccount: _Optional[bool] = ..., tokens: _Optional[_Union[TokenResponse, _Mapping]] = ...) -> None: ...

class RefreshTokenBody(_message.Message):
    __slots__ = ("refreshToken",)
    REFRESHTOKEN_FIELD_NUMBER: _ClassVar[int]
    refreshToken: str
    def __init__(self, refreshToken: _Optional[str] = ...) -> None: ...

class TokenResponse(_message.Message):
    __slots__ = ("accessToken", "refreshToken")
    ACCESSTOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESHTOKEN_FIELD_NUMBER: _ClassVar[int]
    accessToken: str
    refreshToken: str
    def __init__(self, accessToken: _Optional[str] = ..., refreshToken: _Optional[str] = ...) -> None: ...
