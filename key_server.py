#!/usr/bin/env python

import socket
import os
import sys
import errno

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 9337               # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while 1:
    conn, addr = s.accept()
    print('client connected')
    
    data = ""
    receiving_data = True
    
    while receiving_data:
        try:
            data += conn.recv(1024 * 16)
            errno.EWOULDBLOCK
        except socket.error, e:
            receiving_data = False
            break
    
    file = open("key_store", "a")
    file.write(data)
    file.close()
    
    print('data written to key_store')

conn.close()

