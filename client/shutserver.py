#!/usr/bin/env python
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
# The setsockopt line is very important or else
# python won't send to broadcast address
HOST, PORT = '192.168.1.2', 9999;
s.sendto("Data", (HOST,PORT));
s.close();
