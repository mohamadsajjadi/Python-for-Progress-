import socket, json


class Network:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = None

    def start(self):
        self.soc.connect((self.host, self.port))
        data = self.soc.recv(1024).decode('ascii')
        json_data = json.loads(data)
        self.id = json_data['id']
        with open("config.json", 'w') as f:
            f.write(data)

    def send_data(self, keys):
        if len(keys) == 0:
            key = f"no_key"
        else:
            key = keys[0]
        string = "{" + f'"keys": ["snake_{self.id}_{key}], "dead": false' + '}'
        self.soc.sendall(string.encode('ascii'))

    def get_data(self):
        data = self.soc.recv(1024).decode('ascii')
        data = list(data)
        return data
