# -*- coding: utf-8 -*-
"""
HAPPI Server Resources

    Implement different resources for API Server.
"""
import logging
from typing import Any, Optional, Union

from flask import jsonify, make_response
from flask_restful import Resource

from ...client import Client
from ...core import HTTPReturnCode

logger = logging.getLogger(__name__)


class RouterResource(Resource, Client):
    """
    Router Resource Class.
        This class is a default resource class for API Server
        implementation.

    Note:
        This class is extend Flask.Resource and HAPPI.Client
        classes.

    Methods:
        json_response: create json response.
    """
    @staticmethod
    def json_response(
        data: Union[dict, list, str],
        code: int,
        ret_code: Optional[int] = None,
    ) -> Any:
        """
        Create JSON Response.

        Args:
            data (Union[dict, list, str]): Data for response.
            code (int): API HTTP Code.
            ret_code (int, optional): Returned HTTP Code. Defaults to `code`.

        Return:
            Any
        """
        logger.debug('[response][%d]: %s', int(code), str(data))
        return make_response(
            jsonify({
                'code': code,
                'status': HTTPReturnCode(code).name,
                'data': data,
            }),
            ret_code or code,
        )
