#!/usr/local/bin/python
import SocketServer
import pyDaemon
import os

pyDaemon.createDaemon()

class myUDPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print "Port connected. Going to shut down server";
		os.execl("/sbin/shutdown", "/sbin/shutdown", "-p", "now");

if __name__ == "__main__":
	HOST, PORT = "192.168.1.2", 9999
	server = SocketServer.UDPServer((HOST, PORT), myUDPHandler)
	server.serve_forever()
