# -*- coding: utf-8 -*-
"""
HAPPI Core

    HTTP Response Codes.
"""
from enum import Enum, unique

from .quiet_enum_meta import QuietEnumMeta


@unique
class HTTPReturnCode(Enum, metaclass=QuietEnumMeta):
    """
    Enum representation for provide HTTP Return Codes.
    """
    SUCCESS = 200
    ERROR = 500 | 503
    NOT_IMPLEMENTED = 501
    NOT_FOUND = 404
    WRONG_REQUEST = 400
