from socket import *

soc = socket(AF_INET, SOCK_STREAM)
port = 1234

soc.connect(('127.0.0.1', port))
print(soc.recv(1024).decode('ascii'))
soc.close()
