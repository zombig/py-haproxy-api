# -*- coding: utf-8 -*-
"""
HTTPI Core

    QuietEnumMeta implementation.
"""
from enum import Enum, EnumMeta


class QuietEnumMeta(EnumMeta):
    """
    QuietEnumMeta Meta Class.

    Implement quiet enum interface. This may be helpful for
    create enum objects with weak keys policy. In other words if
    you try to access to some unexciting value the program will not
    fail but return `UNKNOWN`.
    """
    def __call__(
        cls,
        value,
        names=None, *,
        module=None,
        qualname=None,
        # For compatible with parent interface
        # pylint: disable=W0622
        type=None,
        start=1
    ):
        """
        Override enum.EnumMeta.__call__() method.

        Return:
            Any value if it found.
            `UNKNOWN` string if name was not found.
        """
        if names is not None:
            return super().__call__(
                value,
                names=names,
                module=module,
                qualname=qualname,
                type=type,
                start=start,
            )
        try:
            # attempt to get an enum member
            return super().__call__(
                value,
                names=names,
                module=module,
                qualname=qualname,
                type=type,
                start=start,
            )
        except ValueError:
            # no such member exists, but we don't care
            return Enum('UNKNOWN', 'UNKNOWN', start=value)
