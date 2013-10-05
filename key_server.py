import socket
import os
import sys

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 9337               # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while 1:
    conn, addr = s.accept()
    print('client connected')
    data = conn.recv(1024 * 16)
    if not data:
        print('data broken')
        continue
    file = open("key_store", "a")
    file.write(data)
    file.close()
    print('data written to key_store')

conn.close()

