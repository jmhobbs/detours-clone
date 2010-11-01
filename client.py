# -*- coding: utf-8 -*-
import socket
import json

PORT = 8551

def do_request ( request ):
	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	s.connect( ( 'localhost', PORT ) )
	s.send( json.dumps( request ) + "\n" )
	data = s.recv( 8192 )
	s.close()
	return json.loads( data )

print do_request( { 'method': 'ping' } )
print do_request( { 'method': 'list' } )
print do_request( { 'method': 'set', 'pairs': [ {'ip': '127.0.0.1', 'host': 'google.com'} ] } )
print do_request( { 'method': 'list' } )
print do_request( { 'method': 'delete', 'hosts': [ 'google.com' ] } )
print do_request( { 'method': 'list' } )