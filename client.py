# -*- coding: utf-8 -*-
import asyncore, socket

class detour_client ( asyncore.dispatcher ):

	def __init__( self, command ):
		asyncore.dispatcher.__init__( self )
		self.create_socket( socket.AF_INET, socket.SOCK_STREAM )
		self.connect( ( 'localhost', 8552 ) )
		self.command = command

	def handle_connect ( self ):
		pass

	def handle_close( self ):
		self.close()

	def handle_read( self ):
		data = self.recv( 8192 )
		if len( data ) > 2: # Skip newlines
			print data

	#def writable( self ):
		#return ( len( self.buffer ) > 0 )

	def handle_write ( self ):
		sent = self.send( self.command + "\n")

c = detour_client( 'ping' )
c = detour_client( 'pong' )

asyncore.loop()
