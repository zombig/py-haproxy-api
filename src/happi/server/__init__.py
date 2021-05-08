# -*- coding: utf-8 -*-
"""
HAPPI: Server

    Implement HAPPI API Server.

    Note:
        Please note that API Server is always return results
        with code 200 if there is no any exceptions is appear
        and route exist. But in this case code in json would
        associated with result.
"""
import logging

from flask import Flask, request
from flask_restful import Api

from .router.resource import RouterResource

logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
# pylint: disable=W0613
def err404(e):
    """
    Processor for HTTP Code 404.

    Args:
        e (Any): Caught error.

    Return:
         Any
    """
    path = request.path
    logger.warning('404 Not Found: %s', str(path))
    return RouterResource.json_response(path, 404)
