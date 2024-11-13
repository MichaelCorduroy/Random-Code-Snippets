#simple implementation of a decentralized network client

import socket
import sys
import time

if len(sys.argv) != 3:
    print("usage: python decen1.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    s.send("hello".encode())
    print(s.recv(1024).decode())
    time.sleep(1)

s.close()




