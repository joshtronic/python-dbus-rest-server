#!/usr/bin/env python 

from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import dbus
import json

available_bus_types = ['Session', 'System']

class GetHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		parts = self.path.split('/')
		parts.pop(0)

		count = len(parts)

		code    = 403
		payload = {'status': 'error'}
		
		if count >= 5:
			bus_type = parts.pop(0).capitalize()

			if bool([x for x in available_bus_types if bus_type in x]) == True:
				try:
					func = getattr(dbus, bus_type + 'Bus')
				except AttributeError:
					payload = {'status': 'error'}
				else:
					bus = func()

					bus_name = parts.pop(0)

					parts.reverse()

					method      = parts.pop(0)
					interface   = parts.pop(0)

					parts.reverse()

					object_path = '/' + '/'.join(parts)

					bus_object    = bus.get_object(bus_name, object_path)
					bus_interface = dbus.Interface(bus_object, interface)
					
					try:
						func = getattr(bus_interface, method)
					except AttributeError:
						payload = {'status': 'error'}
					else:
						code    = 200
						payload = {
							'status':    'OK',
							'type':      bus_type,
							'name':      bus_name,
							'path':      object_path,
							'method':    method,
							'interface': interface,
							'output':    func()
						}

		self.send_response(code)
		self.send_header('Content-Type', 'application/json')
		self.end_headers()
		self.wfile.write(json.dumps(payload))
		return

if __name__ == '__main__':
	from BaseHTTPServer import HTTPServer
	server = HTTPServer(('', 3000), GetHandler)
	print 'Starting server, use <Ctrl-C> to stop'
	server.serve_forever()
