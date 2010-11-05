# -*- coding: utf-8 -*-
import unittest
import hostfile

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