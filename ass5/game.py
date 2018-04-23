from threading import Thread
import socket
import sys

from node import *
from player import Player


class Game:
    def __init__(self, server):
        self.nodes = [Node(self, server), EnemyNode(self, True, server), EnemyNode(self, False, server), ChestNode(self, server), HealthNode(self, server)]
        self.server = server

        #      0
        #    1 2 3
        #      4

        self.nodes[0].south = self.nodes[2]

        self.nodes[1].east = self.nodes[2]

        self.nodes[2].north = self.nodes[0]
        self.nodes[2].east = self.nodes[3]
        self.nodes[2].south = self.nodes[4]
        self.nodes[2].west = self.nodes[1]

        self.nodes[3].west = self.nodes[2]

        self.nodes[4].north = self.nodes[2]

        self.player = Player(self.nodes[0], server)

    def play(self):
        while self.server.connection is None:
            pass
        time.sleep(1)
        self.server.write_message("say start to begin")
        time.sleep(1)

        self.listenFor("start")

        self.player.node.action()
        while not self.player.done:
            self.player.move()
            self.player.node.action()

        sys.exit()

    def listenFor(self, word):
        self.server.write_message("%listen")
        done = False
        while not done:
            if word in self.server.received:
                done = True
                self.server.received = ""
            elif self.server.received != "":
                self.server.write_message("%listen")
                self.server.received = ""


class Main:
    def __init__(self):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port
        server_address = ('192.168.0.165', 2000)
        ('starting up on {} port {}'.format(*server_address))
        self.sock.bind(server_address)
        self.connection = None

        # Listen for incoming connections
        self.sock.listen(1)
        self.received = ""

    def create_gui(self):
        game = Game(self)
        game.play()

    def write_message(self, message):
        self.message = message

    def write(self):
        try:
            while True:
                if self.message != "":
                    self.connection.send((self.message + '\n').encode())
                    self.message = ""
        finally:
            self.connection.close()

    def read(self):
        try:
            while True:
                self.received = self.connection.recv(256).decode()

        finally:
            self.connection.close()

    def run(self):
        # Wait for a connection
        guiThread = Thread(target=self.create_gui)
        guiThread.start()
        print('waiting for a connection')
        self.connection, self.client_address = self.sock.accept()
        self.message = 'goodbye'
        try:
            print('connection from', self.client_address)
            readThread = Thread(target=self.read)
            writeThread = Thread(target=self.write)

            readThread.start()
            writeThread.start()

            readThread.join()
            writeThread.join()

        finally:
            # Clean up the connection
            self.connection.close()


main = Main()
main.run()
