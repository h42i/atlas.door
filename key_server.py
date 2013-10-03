#!/usr/bin/env python2

import socket

HOST = '127.0.0.1' # Symbolic name meaning the local host
PORT = 9337 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)

conn, addr = s.accept()

while True:
	conn, addr = s.accept()
	
	print("accepted client.")
	
	data = conn.recv(2**14)
	
	if not data:
		break
	
	print("wrote public key to keystore.")
	
	file = open("keystore", "w")
	file.write(data)
	file.close()
	
	conn.close()

