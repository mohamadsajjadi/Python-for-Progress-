import threading
from socket import *


def threaded(client, address):
    while True:
        data = client.recv(1024)
        print(data)
        if data == b'exit':
            print(f"connection{address[0]}:{address[1]} lost ")
            break
        data = data[::-1]
        client.sendall(data)
    client.close


host = ''
port = 12345
soc = socket(AF_INET, SOCK_STREAM)
soc.bind((host, port))
soc.listen(2)
print("socket is listening...")
for i in range(2):
    client, address = soc.accept()
    print(f"connected to {address[0]} : {address[1]}")
    threading.Thread(target=threaded, args=(client, address)).start()
soc.close()
