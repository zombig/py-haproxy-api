# -*- coding: utf-8 -*-
"""
HAPPI Server Module

    Implements API Server CLI.
"""
import argparse
import logging
import os
from typing import NoReturn

from waitress import serve

from ..core import LOGGER_FORMAT, LogLevel
from . import api, app
from .router import routes

logger = logging.getLogger('werkzeug')


def get_args() -> argparse.Namespace:
    """
    Collect user-provided CLI arguments.

    Return:
        argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        prog='python3 -m haproxy_api.server',
        description='HAProxy API Server',
    )
    parser.add_argument(
        '-p', '--path', required=True, type=str,
        help='Path to HAProxy stats socket file.',
    )   #: (str): Path to unix socket file.
    parser.add_argument(
        '-l', '--loglevel', default='INFO', type=LogLevel,
        choices=list(LogLevel),
        help='Log level.',
    )   #: (str, optional): Logging level. Defaults to INFO.
    parser.add_argument(
        '--host', default='127.0.0.1', type=str,
        help='Binding ip address.',
    )   #: (str): Listen IP Address. Defaults to 127.0.0.1.
    parser.add_argument(
        '--port', default=5080, type=int,
        help='Port number for binding',
    )   #: (int): Listen port number. Defaults to 5080.
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

    app.config['SECRET_KEY'] = os.urandom(24)

    resource_class_kwargs = {
        'path': args.path,
    }

    for route in routes:
        api.add_resource(*route, resource_class_kwargs=resource_class_kwargs)

    serve(app, host=args.host, port=args.port)


main()
