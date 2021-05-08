# -*- coding: utf-8 -*-
"""
HAPPI Router

    API Server Routes.
"""
from .servers.state import State as ServersState

# A list with supported routes in
#   flask_restful.Api.add_resource format.
routes = [
    [
        ServersState,
        '/api/v1/servers/state',
        '/api/v1/servers/state/',
        '/api/v1/servers/state/<string:backend>',
    ],
]
