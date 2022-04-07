from socket import *

host = '127.0.0.1'
port = 12345
soc = socket(AF_INET, SOCK_STREAM)
soc.connect((host, port))
while True:
    msg = input("Enter your msg\n")
    soc.sendall(msg.encode('ascii'))
    if msg == 'exit':
        break
    data = soc.recv(1024)
    print('Received from the server :', str(data.decode('ascii')), '\n')

    ans = input('Do you want to continue(y/n) :')
    if ans == 'y':
        continue
    else:
        soc.sendall(b'exit')
        break
soc.close()
