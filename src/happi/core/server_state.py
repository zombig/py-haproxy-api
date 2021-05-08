# -*- coding: utf-8 -*-
"""
HAPPI Core

    Servers State Enumerate.
"""
from enum import Enum


class ServerState(bytes, Enum):
    """
    Meta class for handle servers statuses.
    For more info please view an official documentation:
    https://docs.python.org/3/library/enum.html#when-to-use-new-vs-init
    """
    def __new__(cls, value, label, desc):
        """
        Override enum.Enum.__new__() method.

        Extend it with additional enum keys:
            - label (str): enum item label.
            - desc (str): enum item description.

        Return:
            Enum object.
        """
        obj = bytes.__new__(cls, [value])
        obj._value_ = value
        obj.label = label.upper()
        obj.desc = desc
        return obj
