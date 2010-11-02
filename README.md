# Detours Clone

This app is an idealogical clone of the [Detours](http://detoursapp.com/) app for Mac's created by Jerod Santo - [@sant0sk1](http://github.com/sant0sk1)

This only exists because I wanted to see if I could implement it, and play around with some Python bits I've never had the chance to use.

If you are on a Mac, I'd use the real thing.  If you are on Linux, you might give this a shot.

## How it works

This clone involves a client and a server, since on Linux the hosts file is protected we have to run our daemon with a privileged user.  The client and server communicate via TCP sockets with JSON.

Currently I have two clients.  One is an HTTP server and one is a GTK client.

Both allow you to add/remove/update any items in your hosts file __that have been set by this app__.  You can't edit all the entries, only ones created by Detours.

## Security Notice

In case you missed it, the gaping flaw here is that there is now a TCP server that is hooked up to your hosts file, with no authentication mechanism.

This means you should only run this on a single user system, and make sure it is not exposed to the external interface (it binds to 127.0.0.1 but you should verify)

## Install

Install is shaky at the moment, this is just a proof of concept.  If you want to try it, you can download and mangle the config file to use a fake hosts file (or the real one if you want).   Then fire up detoursd and a client to play with it.

Bug reports and fixes welcome!