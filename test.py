from socket import *
from threading import *


class Server(socket):

    def __init__(self, **kwargs):
        super(Server, self).__init__(**kwargs)
        self.conn = None
        self.addr = None

    def server_actions(self, server_address):
        self.bind(server_address)
        self.listen()
        while True:
            self.conn, self.addr = self.accept()
            self.conn.send('From server is connecting ..'.encode())
            print(
                self.conn.recv(5000)
            )
            self.conn.close()

    def start(self, server_address):
        thread = Thread(
            target=self.server_actions,
            args=(server_address,)
        )
        thread.daemon = False
        thread.start()


Server(family=AF_UNIX, type=SOCK_STREAM).start(server_address='127.0.0.1')
