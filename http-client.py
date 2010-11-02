# -*- coding: utf-8 -*-
import SimpleHTTPServer
import SocketServer

import socket
import json

PORT = 8551
SERVE_PORT = 8080

class DetoursHandler ( SimpleHTTPServer.SimpleHTTPRequestHandler ):

	header = """
<html>
	<head>
		<title>Detours</title>
		<style type="text/css">
			table { border-collapse: collapse; }
			th { background-color: #444; color: #EEE; }
			td, th { padding: 5px; border: 1px solid #777; }
			table.form th { text-align: right; }
		</style>
	</head>
	<body>
		<h1>Detours</h1>
"""

	footer = """
	</body>
</html>
"""

	def do_request ( self, request ):
		s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		s.connect( ( '127.0.0.1', PORT ) )
		s.send( json.dumps( request ) + "\n" )
		data = s.recv( 8192 )
		s.close()
		return json.loads( data )

	def do_GET ( self ):
		# Quick & dirty path handling!
		url = self.path.split( '?' )
		path = url[0]
		args = {}
		for pair in '?'.join( url[1:] ).split( '&' ):
			split = pair.split( '=' )
			if '' == split[0].strip():
				continue
			args[split[0]] = '='.join( split[1:] )

		# Send the default header
		self.wfile.write( self.header )

		# Now serve based on path
		if path == '/':
			response = self.do_request( { 'method': 'list' } )
			if response['response'] == 'list':
				self.wfile.write( """
<form action="/set" method="GET">
	<table class="form">
		<tr>
			<th>Host:</th>
			<td><input type="text" name="host" /></td>
		</tr>
		<tr>
			<th>IP:</th>
			<td><input type="text" name="ip" /></td>
		</tr>
		<tr>
			<th colspan="2"><input type="submit" value="Set" /></th>
		</tr>
	</table>
</form>

<table>
	<tr>
		<th>Host</th>
		<th>IP</th>
		<th>Delete</th>
	</tr>
"""
				)
				self.wfile.write( "\n" )
				for pair in response['pairs']:
					self.wfile.write( "<tr><td>%s</td><td>%s</td><td><a href=\"/delete?host=%s\">Delete</a></tr>\n" % ( pair['host'], pair['ip'],  pair['host'] ) )
				self.wfile.write( "</table>\n" )
		elif path == '/set':
			response = self.do_request( { 'method': 'set', 'pairs': [ { 'host': args['host'], 'ip': args['ip'] } ] } )
			if response['response'] == 'set':
				self.wfile.write( '<h2>Set %s to %s</h2>' % ( args['host'], args['ip'] ) )
				self.wfile.write( '<p><a href="/">Back</a></p>' )
		elif path == '/delete':
			response = self.do_request( { 'method': 'delete', 'hosts': [ args['host'] ] } )
			if response['response'] == 'deleted':
				self.wfile.write( '<h2>Deleted %s</h2>' % args['host'] )
				self.wfile.write( '<p><a href="/">Back</a></p>' )
		else:
			self.wfile.write( '<h1>404 - Not Found</h1>' )
			self.send_response( 404 )
			return
		self.wfile.write( self.footer )

httpd = SocketServer.ForkingTCPServer( ( '127.0.0.1', SERVE_PORT ), DetoursHandler )

print "serving at port", SERVE_PORT

httpd.serve_forever()