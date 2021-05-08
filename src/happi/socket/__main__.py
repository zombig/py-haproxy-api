# -*- coding: utf-8 -*-
"""
HAPPI Socket Module.

    This module provides CLI interface for Socket Class.

    Example:
        python -m happi.socket \
            -p /path/to/stats/socket \
            -d 'show servers state' \
            -l DEBUG
"""
import argparse
import logging
from typing import NoReturn

from ..core import LOGGER_FORMAT, LogLevel
from . import Socket


def get_args() -> argparse.Namespace:
    """
    Collect user-provided CLI arguments.

    Return:
        argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        prog='python3 -m happi.socket',
        description='Simple client for communicate with Unix sockets.',
    )
    parser.add_argument(
        '-p', '--path', required=True, type=str,
        help='Path to HAProxy stats socket file.',
    )   #: (str): Path to unix socket file.
    parser.add_argument(
        '-d', '--data', required=True, type=str,
        help='Data sting for send to HAProxy stat socket.',
    )   #: (str): Data to send to unix socket file.
    parser.add_argument(
        '-l', '--loglevel', default='INFO', type=LogLevel,
        choices=list(LogLevel),
        help='Log level.',
    )   #: (str, optional): Logging level. Defaults to INFO.
    return parser.parse_args()


def main() -> NoReturn:
    """
    Run CLI Interface.

    Return:
        NoReturn
    """
    args = get_args()
    logging.basicConfig(
        format=LOGGER_FORMAT,
        level=getattr(logging, args.loglevel.name),
    )
    s = Socket(args.path)
    print(s.send(args.data))


main()
