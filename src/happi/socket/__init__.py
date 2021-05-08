# -*- coding: utf-8 -*-
"""
HAPPI: Socket

    Implement low-level interface for communicate
    with unix socket file.
"""
import logging
import os
import socket
from typing import List

logger = logging.getLogger(__name__)


class Socket:
    """
    Socket Class

    Methods:
        send: Communicate with unix socket file.
    """

    def __init__(self, path: str, timeout: int = 10):
        """
        Socket Class Constructor.

        Args:
            path (str): Path to unix socket file.
            timeout (int, optional): Data collect timeout. Defaults to 10.

        Return:
            NoReturn
        """
        self.path = path
        self.timeout = timeout

    def send(self, data: str) -> List[str]:
        """
        Send some data to unix socket and collect results.

        Args:
            data (str): Data sting for send to unix socket file.

        Return:
            List[str]
        """
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)
        if os.path.exists(self.path):
            try:
                sock.connect(self.path)
                logger.debug('[conn]: connection %s is open', str(self.path))
            except OSError as e:
                logger.critical(
                    '[conn]: unable to connect to %s with error %s',
                    self.path, str(e),
                )
                raise ConnectionError from e
        else:
            logger.critical(
                "[conn]: socket %s doesn't exist or unavailable",
                self.path,
            )
            raise ConnectionError
        try:
            logger.debug('[send]: %s', str(data))
            sock.send((data + '\n').encode('utf-8'))
        except OSError as e:
            logger.critical(
                '[send]: unable to send data with error %s', str(e),
            )
            raise ConnectionError from e
        logger.debug('[read]: reading response')
        fh = sock.makefile()
        try:
            data = fh.read().strip().splitlines()
        except OSError as e:
            logger.critical(
                '[read]: unable to read data from socket with error %s',
                str(e),
            )
            raise ConnectionError from e
        finally:
            sock.close()
            logger.debug('[conn]: connection to %s is closed', str(self.path))
        return data
