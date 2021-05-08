# -*- coding: utf-8 -*-
"""
HAPPI Core

    Logger tools.
"""
from enum import Enum, unique

# Unified logger format string.
LOGGER_FORMAT = \
    '[%(asctime)s][%(name)s][%(process)d][%(levelname)s]: %(message)s'


@unique
class LogLevel(Enum):
    """
    Enum representations for provide logger log levels.
    """
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

    # For compatible with parent interface
    # pylint: disable=E0307
    def __str__(self) -> str:
        """
        Override enum.Enum.__str__() method.

        Return:
            str
        """
        return self.value
