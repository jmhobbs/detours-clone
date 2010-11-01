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
		self.wfile.write( self.header )
		if self.path == '/':
			response = self.do_request( { 'method': 'list' } )
			if response['response'] == 'list':
				self.wfile.write( "<table><tr><th>Host</th><th>IP</th></tr>\n" )
				for pair in response['pairs']:
					self.wfile.write( "<tr><td>%s</td><td>%s</td></tr>\n" % ( pair['host'], pair['ip'] ) )
				self.wfile.write( "</table>\n" )
		self.wfile.write( self.footer )

httpd = SocketServer.ForkingTCPServer( ( '127.0.0.1', SERVE_PORT ), DetoursHandler )

print "serving at port", SERVE_PORT
httpd.serve_forever()