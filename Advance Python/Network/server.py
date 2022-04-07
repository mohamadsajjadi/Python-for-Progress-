import socket
from socket import *

soc = socket(AF_INET, SOCK_STREAM)
port = 1234

soc.bind(('127.0.0.1', port))
soc.listen()
while True:
    client, address = soc.accept()
    print(type(client), address)
    client.sendall(b"hello\n")
    client.close()
