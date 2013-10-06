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
    
    while True:
        tmp_data = conn.recv(1024)
        
        if not tmp_data:
            break
        
        data += tmp_data
    
    file = open("key_store", "a")
    file.write(data)
    file.close()
    
    print('data written to key_store')

conn.close()

