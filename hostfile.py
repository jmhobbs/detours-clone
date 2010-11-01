# -*- coding: utf-8 -*-
import os

class HostFile:

	delimiter = "##### DO NOT EDIT BETWEEN THESE LINES - DETOURD #####\n"

	def __init__ ( self, path ):
		self.path = path

	def findSection ( self ):
		with open( self.path, 'r' ) as handle:
			index = 0
			for line in handle:
				index += 1
				if line == self.delimiter:
					return index
		return None

	def addSection ( self ):
		# TODO: This is bad. Should use a temp file and rename it.
		with open( self.path, 'w+' ) as handle:
			buffer = handle.read()
			handle.seek( 0 )
			handle.truncate()
			handle.write( self.delimiter )
			handle.write( "#\n" )
			handle.write( self.delimiter )
			handle.write( buffer )
