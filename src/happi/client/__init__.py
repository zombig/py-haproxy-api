# -*- coding: utf-8 -*-
"""
HAPPI Client

    Implement Client human-friendly interface.
"""
import logging
from functools import wraps
from ipaddress import IPv4Address, IPv6Address
from typing import Any, Union

from ..socket import Socket
from .processor.servers.state import parse_servers_state

logger = logging.getLogger(__name__)


def log_func(function):
    """
    Decorator for log executed functions.
    """
    @wraps(function)
    def do(*args, **kwargs):
        logger.debug('[%s]: ', str(function.__name__))
        return function(*args, **kwargs)
    return do


class Client:
    """
    Client Class.

        Implement human-friendly interface for interact with
        HAProxy Stats API.
    """

    def __init__(self, path: str):
        """
        Client Class.

        Args:
            path (str): Path to HAProxy Stats API unix socket file.

        Return:
            NoReturn
        """
        self.soc = Socket(path)

    @log_func
    def get_servers_state(self, backend: str = '') -> Any:
        """
        Implement `show servers state [backend]` HAProxy Stats API
        method.

        Args:
            backend (str): HAProxy backend name. Defaults to
                empty string.

        Return:
            Any
        """
        command = f'show servers state {backend}'
        logger.info('process command: %s', command)
        output = self.soc.send(command)
        return parse_servers_state(output)

    # temporary disabled
    def __set_server_state(self, backend: str, server: str, state: str) -> list:
        """NOT IMPLEMENTED"""
        command = f'set server {backend}/{server} state {state}'
        logger.info(command)
        return self.soc.send(command)

    # temporary disabled
    def __set_server_address(
            self, backend: str,
            server: str,
            address: Union[IPv4Address, IPv6Address],
    ) -> list:
        """NOT IMPLEMENTED"""
        command = f'set server {backend}/{server} addr {address}'
        logger.info(command)
        return self.soc.send(command)
