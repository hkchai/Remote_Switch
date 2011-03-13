#!/usr/bin/env python
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
# The setsockopt line is very important or else
# python won't send to broadcast address
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1);
magic_packet = '\xff'*6+'\x00\x24\x1d\x8c\x91\x71'*16;
s.sendto(magic_packet, ('192.168.1.255', 80));
