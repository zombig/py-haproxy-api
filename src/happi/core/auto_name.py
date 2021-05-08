# -*- coding: utf-8 -*-
"""
HAPPI Core

    Enumerate overload for do auto name formation.
"""
from enum import Enum


class AutoName(Enum):
    """
    AutoName Class.

    Create Enum Class object with auto created variables names.
    """
    # For compatible with parent interface
    # pylint: disable=E0213 disable=W0613
    def _generate_next_value_(name, start, count, last_values):
        """
        Override enum.Enum._generate_next_value_() method.

        Return:
            str
        """
        return name


class ArgAutoName(AutoName):
    """
    ArgAutoName Class.

    Create string representation for AutoNamed Enum object.
    """

    def __str__(self):
        """
        Override enum.Enum.__str__() method.

        Return:
            str
        """
        # For compatible with parent interface
        # pylint: disable=E0307
        return self.value
