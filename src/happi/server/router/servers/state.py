# -*- coding: utf-8 -*-
"""
Server State Route

    Interface for happi.Client.get_servers_state
    API Server implementation.
"""
from typing import Optional

from ..resource import RouterResource


class State(RouterResource):
    """
    State Class.

    Implement happi.Client.get_servers_state API
    interface.

    Methods:
        GET: read backend information.
    """

    def get(self, backend: Optional[str] = ''):
        """
        HTTP GET Method.

        Args:
            backend (str, optional): HAProxy backend name.
                Defaults to empty string. When backend name is
                not provided then return information for all
                backends.

        Return:
            JSON Response with code 200 if succeed.
            JSON Response with code 404 if backend not found.
        """
        data = self.get_servers_state(backend)
        if data:
            return self.json_response(data, 200)
        return self.json_response([], 404, 200)

    # pylint: disable=W0613
    def put(self, backend: Optional[str] = None):
        """
        HTTP PUT Method.

        Note:
            Not implemented.

        Return:
            JSON Response with code 501 and error info.
        """
        return self.json_response('not implemented', 501, 200)

    # pylint: disable=W0613
    def post(self, backend: Optional[str] = None):
        """
        HTTP POST Method.

        Note:
            Not implemented.

        Return:
            JSON Response with code 501 and error info.
        """
        return self.json_response('not implemented', 501, 200)

    # pylint: disable=W0613
    def delete(self, backend: Optional[str] = None):
        """
        HTTP DELETE Method.

        Note:
            Not implemented.

        Return:
            JSON Response with code 501 and error info.
        """
        return self.json_response('not implemented', 501, 200)
