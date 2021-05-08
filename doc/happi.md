# HAProxy API Server

HAProxy API Server or HAPPI implement json API for
HAProxy Stats API via HTTP protocol for provide easy-to-use
stats collect and management.

HAPPI include few modules: socket, client and server. Each
module provides a short functionality for communicate with
HAProxy stats on different levels.

<!-- toc -->

- [HAPPI: Socket Module](#happi-socket-module)
- [HAPPI: Client Module](#happi-client-module)
- [HAPPI: Server Module](#happi-server-module)
- [Tests](#tests)
- [Tips](#tips)

<!-- tocstop -->

## HAPPI: Socket Module

The HAPPI Socket module implement low-level communication
protocol for interact with HAProxy Stats API unix socket.

Example:

```shell
python -m happi.socket \
  -p /path/to/stats/socket \
  -d 'show servers state' \
  -l DEBUG
```

This example will collect servers state data from HAProxy
Stats API unix socket and print it with debug information.

Moreover, you can use this module directly from your python
program for communicate with any unix socket file.

Example:

```python
from happi import Socket

s = Socket('/path/to/haproxy/stats/socket')
print(s.send('show servers state'))
```

## HAPPI: Client Module

The HAPPI Client module implement human-friendly interface
for happi.socket with pre-defined methods.

Example:

```shell
python -m happi.client get_servers_state \
  -p /path/to/stats/socket -l DEBUG
```

This example will show servers state from HAProxy Stats API
as a python dict object.

Or you can use this module direct from your code.

Example:

```python
from happi import Client

c = Client('/path/to/haproxy/stats/socket')
print(c.get_servers_state())
```

## HAPPI: Server Module

Implement API Server. For run server just run:

```shell
python -m happi.server \
  -p /path/to/haproxy/stats/socket -l DEBUG
```

## Tests

We haven't any automated tests for now, but you can test
server by hands after run.

Example:

```shell
curl http://127.0.0.1:5080/api/v1/servers/state/
```

## Tips

If you want to do some tests locally but have not installed
haproxy you can use ssh proxy for pin HAProxy Stats API
socket to your local machine.

Example:

```shell
ssh -nNT \
  -L /tmp/haproxy:/var/lib/haproxy/stats \
  user@example.com sleep 10
```
