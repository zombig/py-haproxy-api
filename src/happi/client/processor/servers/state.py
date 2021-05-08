# -*- coding: utf-8 -*-
"""
HAPPI Client Processor Servers State

    Process response from servers state HAProxy
    API call.
"""
import logging
from enum import Enum, unique

from ....core import ServerState

logger = logging.getLogger(__name__)


@unique
class OpState(ServerState):
    """
    Server Operational State Flags.
    For more info please view an official HAProxy documentation:
    https://cbonte.github.io/haproxy-dconv/1.8/management.html#9.3-show%20servers%20state
    """
    SRV_ST_STOPPED = (0, 'DOWN', 'The server is down.')
    SRV_ST_STARTING = (
        1, 'STARTED', 'The server is warming up (up but throttled).',
    )
    SRV_ST_RUNNING = (2, 'RUNNING', 'The server is fully up.')
    SRV_ST_STOPPING = (
        3, 'STOPPING', 'The server is up but soft-stopping (eg: 404).',
    )


@unique
class AdminState(ServerState):
    """
    Server Admin State Flags.
    For more info please view an official HAProxy documentation:
    https://cbonte.github.io/haproxy-dconv/1.8/management.html#9.3-show%20servers%20state
    """
    SRV_ADMF_EMPTY = (
        0x00, 'EMPTY',
        'The server\'s admin state is not set.',
    )
    SRV_ADMF_FMAINT = (
        0x01, 'MAINTENANCE',
        'The server was explicitly forced into maintenance.',
    )
    SRV_ADMF_IMAINT = (
        0x02, 'MAINTENANCE',
        'The server has inherited the maintenance status from a '
        'tracked server.',
    )
    SRV_ADMF_CMAINT = (
        0x04, 'MAINTENANCE',
        'The server is in maintenance because of the configuration.',
    )
    SRV_ADMF_FDRAIN = (
        0x08, 'DRAIN',
        'The server was explicitly forced into drain state.',
    )
    SRV_ADMF_IDRAIN = (
        0x10, 'DRAIN',
        'The server has inherited the drain status from a tracked server.',
    )
    SRV_ADMF_RMAINT = (
        0x20, 'MAINTENANCE',
        'The server is in maintenance because of an IP address '
        'resolution failure.',
    )
    SRV_ADMF_HMAINT = (
        0x40, 'MAINTENANCE',
        'The server FQDN was set from stats socket.',
    )


@unique
class CheckResult(ServerState):
    """
    Server Check Result Flags.
    For more info please view an official HAProxy documentation:
    https://cbonte.github.io/haproxy-dconv/1.8/management.html#9.3-show%20servers%20state
    """
    CHK_RES_UNKNOWN = (0, 'UNKNOWN', 'Initialized to this by default.')
    CHK_RES_NEUTRAL = (1, 'NEUTRAL', 'Valid check but no status information.')
    CHK_RES_FAILED = (2, 'FAILED', 'Check failed.')
    CHK_RES_PASSED = (
        3, 'PASSED', 'Check succeeded and server is fully up again.',
    )
    CHK_RES_CONDPASS = (
        4, 'CONDPASS', 'Check reports the server doesn\'t want new sessions.',
    )


@unique
class ServerStatus(ServerState):
    """
    Server Status Flags.
    For more info please view an official HAProxy documentation:
    https://cbonte.github.io/haproxy-dconv/1.8/management.html#9.3-show%20servers%20state
    """
    be_id = (0, 'BACKEND_ID', 'Backend unique id.')
    be_name = (1, 'BACKEND_NAME', 'Backend label.')
    srv_id = (2, 'SERVER_ID', 'Server unique id (in the backend).')
    srv_name = (3, 'SERVER_NAME', 'Server label.')
    srv_addr = (4, 'ADDRESS', 'Server IP address.')
    srv_op_state = (5, 'STATE', 'Server operational state (UP/DOWN/...).')
    srv_admin_state = (
        6, 'STATE', 'Server administrative state (MAINT/DRAIN/...).',
    )
    srv_uweight = (7, 'WEIGHT', 'User visible server\'s weight.')
    srv_iweight = (8, 'WEIGHT', 'Server\'s initial weight.')
    srv_time_since_last_change = (
        9, 'TIME', 'Time since last operational change.',
    )
    srv_check_status = (10, 'CHECK', 'Last health check status.')
    srv_check_result = (11, 'CHECK', 'Last check result (FAILED/PASSED/...).')
    srv_check_health = (12, 'CHECK', 'Checks rise / fall current counter.')
    srv_check_state = (13, 'CHECK', 'State of the check (ENABLED/PAUSED/...).')
    srv_agent_state = (
        14, 'AGENT', 'State of the agent check (ENABLED/PAUSED/...).',
    )
    bk_f_forced_id = (
        15, 'BACKEND_ID',
        'Flag to know if the backend ID is forced by configuration.',
    )
    srv_f_forced_id = (
        16, 'SERVER_ID',
        'Flag to know if the server\'s ID is forced by configuration.',
    )
    srv_fqdn = (17, 'FQDN', 'Server FQDN.')
    srv_port = (18, 'PORT', 'Server port.')
    srvrecord = (19, 'DSNSRV', 'DNS SRV record associated to this SRV.')


def parse_servers_state(data: list) -> dict:
    """
    Parse response from HAProxy Stats API call.

    Args:
        data (list): Data from HAProxy Stats API call.

    Return:
        dict
    """

    logger.debug('data: %s', str(data))

    known_states = {
        'srv_op_state': OpState,
        'srv_admin_state': AdminState,
        'srv_check_result': CheckResult,
    }

    supported_stats_versions = [1]

    logger.debug('registered states: %s', str(known_states))
    logger.debug(
        'supported protocol versions: %s',
        str(supported_stats_versions),
    )

    servers_state = dict()
    try:
        servers_state['version'] = int(data[0])
        logger.debug('protocol version is: %d', int(servers_state['version']))
    except ValueError:
        logger.warning('can\'t find protocol version')
        return data  # Fixme "data":["Can't find backend."]

    if servers_state['version'] not in supported_stats_versions:
        logger.critical('Unsupported stats version')
        raise RuntimeError('Unsupported stats version')

    servers_state['servers'] = list()
    for line in data[2:]:
        server = dict()
        for index, value in enumerate(line.split(' ')):
            # pylint: disable=E1120
            state = ServerStatus(index)
            info = known_states[state.name](int(value)) \
                if known_states.get(state.name, False) \
                else value
            if isinstance(info, Enum):
                info = info.name
            server[state.label] = info
        servers_state['servers'].append(server)
    logger.debug('processed %d lines', len(data[2:]))
    return servers_state
