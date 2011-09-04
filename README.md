# Client-side REST Server for interfacing with D-Bus

## What's it do?

Creates a RESTful interface to D-Bus that lives on port 3000 and can be utlized to build client side web applications that interact with D-Bus (e.g. web-based controls for Rhythmbox)

## How do I run it?

Assuming you already have Python (and any additional libraries) on your system and are running Ubuntu (Only OS I'll be testing this one) then all you need to do is run:

	./dbus-rest.py

## How do I talk to it?

Communicating with the server can be done by pointing your web browser to something like: http://localhost:3000/Session/com.ubuntuone.SyncDaemon/status/com.ubuntuone.SyncDaemon.Status/current_status or http://localhost:3000/Session/com.Gwibber.Accounts/com/gwibber/Accounts/com.Gwibber.Accounts/List

The format of the URI is /type/object/path/interface/method

The data is returned as JSON but the output of the D-Bus response will be varied (seems that return data is not standardized)

## What's the future hold?

* Documentation page when calling the server with no path
* Support for the root object path's methods (connect, disconnect, et cetera)
* POST methods to push as well as pull data
