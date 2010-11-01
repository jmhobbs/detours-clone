# -*- coding: utf-8 -*-

import pygtk
pygtk.require( '2.0' )
import gtk, gobject

import socket
import json

PORT = 8551

class Detours:

	def __init__ ( self ):
		self.window = gtk.Window( gtk.WINDOW_TOPLEVEL )
		self.window.connect( "destroy", lambda w: gtk.main_quit() )
		self.window.set_title( "Detours" )
		self.window.set_size_request( 350, 200 )

		# Build the layout
		base = gtk.VBox()
		self.window.add( base )

		# This is where we store the detours
		self.detours = gtk.TreeStore( str, str )

		# Build the tree view
		scrolled_window = gtk.ScrolledWindow()
		scrolled_window.set_policy( gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC )
		tree_view = gtk.TreeView( self.detours )
		cell = gtk.CellRendererText()
		column = gtk.TreeViewColumn( "Host", cell, text=0 )
		tree_view.append_column( column )
		cell = gtk.CellRendererText()
		column = gtk.TreeViewColumn( "IP", cell, text=1 )
		tree_view.append_column( column )
		scrolled_window.add( tree_view )
		base.pack_start( scrolled_window )

		# Build the status bar
		self.status = gtk.Statusbar()
		base.pack_end( self.status, False, False, 0 )
		self.status.push( self.status.get_context_id( 'welcome' ), 'Welcome to Detours - Connecting...' )

		self.window.show_all()

		self.do_refresh()

	def do_request ( self, request ):
		s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		s.connect( ( 'localhost', PORT ) )
		s.send( json.dumps( request ) + "\n" )
		data = s.recv( 8192 )
		s.close()
		return json.loads( data )

	def do_refresh ( self ):
		response = self.do_request( { 'method': 'list' } )
		if 'list' == response['response']:
			for pair in response['pairs']:
				self.detours.append( None, [ pair['host'], pair['ip'] ] )
			self.set_status( 'Loaded Detours' )
		else:
			self.set_status( 'Could Not Load Detours!' )

	def set_status ( self, message ):
		context = self.status.get_context_id( 'welcome' )
		self.status.pop( context )
		self.status.push( context, message )

	def main( self ):
		gtk.main()

if __name__ == "__main__":
	app = Detours()
	app.main()
