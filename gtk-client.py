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

		# Build the "menu"
		buttons = gtk.HBox()

		image = gtk.Image()
		image.set_from_stock( gtk.STOCK_ADD, gtk.ICON_SIZE_SMALL_TOOLBAR )
		button = gtk.Button()
		button.set_image( image )
		button.set_label( "Add" )
		button.connect( "clicked", self.show_add_dialog )
		buttons.pack_start( button, False, False )

		image = gtk.Image()
		image.set_from_stock( gtk.STOCK_REFRESH, gtk.ICON_SIZE_SMALL_TOOLBAR )
		button = gtk.Button()
		button.set_image( image )
		button.set_label( "Refresh" )
		button.connect( "clicked", self.do_refresh )
		buttons.pack_start( button, False, False )

		base.pack_start( buttons, False, False, 5 )

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
		self.status.push( self.status.get_context_id( 'welcome' ), 'Welcome to Detours - Loading...' )

		self.window.show_all()

		self.do_refresh()

	def show_add_dialog ( self, menuitem=None ):
		dialog = gtk.Dialog(
			"Set Detour",
			None,
			gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
			(
				"Set", gtk.RESPONSE_ACCEPT,
				"Cancel", gtk.RESPONSE_CLOSE
			)
		)

		label = gtk.Label( "<b>Host</b>" )
		label.set_alignment( 0, 0 )
		label.set_use_markup( True )
		label.show()
		dialog.vbox.pack_start( label )

		host = gtk.Entry()
		host.show()
		dialog.vbox.pack_start( host )

		label = gtk.Label( "<b>IP</b>" )
		label.set_alignment( 0, 0 )
		label.set_use_markup( True )
		label.show()
		dialog.vbox.pack_start( label )

		ip = gtk.Entry()
		ip.set_text( '127.0.0.1' )
		ip.show()
		dialog.vbox.pack_start( ip )

		response = dialog.run()
		dialog.hide()

		if response == gtk.RESPONSE_ACCEPT:
			self.do_set( host.get_text(), ip.get_text() )

	def do_request ( self, request ):
		s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		s.connect( ( 'localhost', PORT ) )
		s.send( json.dumps( request ) + "\n" )
		data = s.recv( 8192 )
		s.close()
		return json.loads( data )

	def do_refresh ( self, clickignore=None ):
		self.set_status( 'Loading Detours...' )
		response = self.do_request( { 'method': 'list' } )
		if 'list' == response['response']:
			self.detours.clear()
			for pair in response['pairs']:
				self.detours.append( None, [ pair['host'], pair['ip'] ] )
			self.set_status( 'Loaded Detours' )
		else:
			self.set_status( 'Could Not Load Detours!' )

	def do_set ( self, host, ip ):
		self.set_status( 'Setting Detour...' )
		response = self.do_request( { 'method': 'set', 'pairs': [ { 'host': host, 'ip': ip } ] } )
		if 'set' == response['response']:
			self.do_refresh()
			self.set_status( 'Set Detour' )
		else:
			self.set_status( 'Could Not Set Detour!' )

	def set_status ( self, message ):
		context = self.status.get_context_id( 'welcome' )
		self.status.pop( context )
		self.status.push( context, message )

	def main( self ):
		gtk.main()

if __name__ == "__main__":
	app = Detours()
	app.main()
