# Detours Clone

This app is an idealogical clone of the [Detours](http://detoursapp.com/) app for Mac's created by Jerod Santo - [@sant0sk1](http://github.com/sant0sk1)

This only exists because I wanted to see if I could implement it, and play around with some Python bits I've never had the chance to use.

If you are on a Mac, I'd use the real thing.  If you are on Linux, you might give this a shot.

## How it works

This app involves a client and a server, since on Linux the hosts file is protected we have to run our daemon with a privileged user.  The client and server communicate via TCP sockets with JSON.

Currently I have two clients.  One is an HTTP server and one is a GTK client.

Both allow you to add/remove/update any items in your hosts file __that have been set by this app__.  You can't edit all the entries, only ones created by Detours.

## Security Notice

In case you missed it, the gaping flaw here is that there is now a TCP server that is hooked up to your hosts file, with no authentication mechanism.

This means you should only run this on a single user system, and make sure it is not exposed to the external interface (it binds to 127.0.0.1 but you should verify)

## Install

Download this package, then, as root, run:

    # python setup.py install

That should drop an init script in for you as well as the two clients, detours-gtk and detours-http

Start detoursd like so:

    # /etc/init.d/detoursd start

Then a client, like so:

    $ detours-gtk

This has been tested on a Debian Sid machine, an Ubuntu machine, and nowhere else. Bug and install reports are coveted!

### Always-On Daemon

If you want the daemon to run on boot, you can set up the init script, as root, like so (Ubuntu)

    # update-rc.d detoursd defaults

## Upgrading

Same process as install, though I recommend stopping your detoursd before the upgrade, then starting it again after.

