# -*- coding: utf-8 -*-
"""
HAPPI Client Module

    Human-friendly interface for interact with
    HAProxy Stats API socket.

    Example:
        python -m happi.client get_servers_state \
            -p /path/to/stats/socket -l DEBUG
"""
import argparse
import inspect
import json
import logging
from typing import NoReturn

from ..core import LOGGER_FORMAT, ArgAutoName, LogLevel
from . import Client

logger = logging.getLogger(__name__)


def collect_methods() -> list:
    """
    Collect registered HAProxy Stats API
    methods.

    Return:
        list
    """
    methods = set()
    for method in inspect.getmembers(Client, predicate=inspect.isfunction):
        if '__' not in method[0]:
            methods.add(method)
    return [m[0] for m in methods]


def get_args() -> argparse.Namespace:
    """
    Collect user-provided CLI arguments.

    Return:
        argparse.Namespace
    """

    methods = ArgAutoName('Methods', ' '.join(collect_methods()))

    parser = argparse.ArgumentParser(
        prog='python3 -m haproxy_api.client',
        description='Simple client for communicate with HAProxy API.',
    )
    parser.add_argument(
        'method',
        type=methods,
        choices=list(methods),
    )   #: (str): HAProxy Stats API Method.
    parser.add_argument(
        '-p', '--path', required=True, type=str,
        help='Path to HAProxy stats socket file.',
    )
    parser.add_argument(
        '-d', '--data', default=None, type=str,
        help='Data JSON for send to HAProxy API.',
    )   #: (str, optional): JSON with data for send to HAProxy Stats API.
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

    if args.data:
        try:
            data = json.loads(args.data)
        except json.JSONDecodeError as e:
            logger.debug(
                'unable to parse data %s with error %s',
                str(args.data), str(e),
            )
            raise RuntimeError from e
    else:
        data = {}

    c = Client(args.path)

    print(getattr(c, args.method.name)(**data))


main()
