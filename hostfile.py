# -*- coding: utf-8 -*-
import os

class HostFile:

	delimiter = "##### DO NOT EDIT BETWEEN THESE LINES - DETOURD #####\n"

	def __init__ ( self, path ):
		self.path = path

	def getDetours ( self ):
		with open( self.path, 'r' ) as handle:
			detours = []
			opened = False
			for line in handle:
				if line == self.delimiter:
					if opened:
						break
					else:
						opened = True
				else:
					if opened:
						detours.append( self.parseDetour( line ) )
		return detours

	def writeDetours ( self, detours ):
		with open( self.path, 'r+' ) as handle:
			buffer = ''
			opened = False
			for line in handle:
				if line == self.delimiter:
					opened = not opened
					continue
				if opened:
					continue
				buffer += line
			handle.seek( 0 )
			handle.truncate()
			handle.write( self.delimiter )
			for detour in detours:
				handle.write( "%s\t%s\n" % ( detour[0], detour[1].lower() ) )
			handle.write( self.delimiter )
			handle.write( buffer )

	def parseDetour ( self, line ):
		return line.strip().split()

	def findDetour ( self, domain ):
		for detour in self.getDetours():
			if detour[1] == domain.lower():
				return detour
		return None
