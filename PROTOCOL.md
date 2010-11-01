# Method: Ping #

Get status of the daemon.

## Request ##
    {request: 'ping'}

## Response ##
    {response: 'pong'}

# Method: Set #

Ensure that a detour is set. Can be used to set or update.

## Request ##
    {request: 'set', pairs: [ { host: '[host]', ip: '[ip]' } ] }

## Response ##
    {response: 'set', pairs: [ { host: '[host]', ip: '[ip]' } ] }

# Method: Delete ##

Delete a host.

## Request ##
    {request: 'delete', hosts: [ '[host]' ] }

## Response ##
    {response: 'deleted', hosts: [ '[host]' ] }

# Method: List #

List all existing detours.

## Request ##
    {request: 'list'}
## Response ##
    {response: 'list', pairs: [ { host: '[host]', ip: '[ip]' } ] }
