# -*- coding: utf-8 -*-
import os

class HostFile:

	delimiter = "##### DO NOT EDIT BETWEEN THESE LINES - DETOURD #####\n"

	def __init__ ( self, path ):
		self.path = path

	def canWrite ( self ):
		try:
			f = open( self.path, 'r+' )
			f.close()
			return True
		except IOError:
			return False

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
						try:
							detours.append( self.parseDetour( line ) )
						except IndexError, e:
							pass

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
				handle.write( "%s\t%s\n" % ( detour['ip'], detour['host'].lower() ) )
			handle.write( self.delimiter )
			handle.write( buffer )

	def parseDetour ( self, line ):
		split = line.strip().split()
		return { 'ip': split[0], 'host': split[1] }

	def findDetour ( self, host ):
		for detour in self.getDetours():
			if detour['host'] == host.lower():
				return detour
		return None

