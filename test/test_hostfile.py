# -*- coding: utf-8 -*-
import unittest

# Fix it so we import the dev version before anything else
lib_path = os.path.abspath( os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), '..', 'lib' ) )
sys.path.insert( 0, lib_path )
import hostfile
del sys.path[0]

import os.path

# Set the path to our data directory
DATA_PATH = "%s/data" % os.path.dirname( __file__ )

class TestHostFile ( unittest.TestCase ):

	def test_get_detours_exist ( self ):
		hf = hostfile.HostFile( DATA_PATH + '/has-detours-section' )
		self.assertEquals( hf.getDetours(), [ {'ip': '127.0.0.1', 'host': 'localhost'}, {'ip': '127.0.0.1', 'host': 'www.google.com'}] )

	def test_get_detours_dont_exist ( self ):
		hf = hostfile.HostFile( DATA_PATH + '/no-detours-section' )
		self.assertEquals( hf.getDetours(), [] )

	def test_get_detour_exist ( self ):
		hf = hostfile.HostFile( DATA_PATH + '/has-detours-section' )
		self.assertEquals( hf.findDetour( 'www.google.com' ), {'ip': '127.0.0.1', 'host': 'www.google.com'} )

	def test_get_detour_doesnt_exist ( self ):
		hf = hostfile.HostFile( DATA_PATH + '/has-detours-section' )
		self.assertEquals( hf.findDetour( 'google.com' ), None )

		hf = hostfile.HostFile( DATA_PATH + '/no-detours-section' )
		self.assertEquals( hf.findDetour( 'google.com' ), None )

if __name__ == '__main__':
	unitest.main()
