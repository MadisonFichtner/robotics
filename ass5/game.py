import sys

from node import *
from player import Player


class Game:
    def __init__(self):
        self.nodes = [Node(self), EnemyNode(self, True), EnemyNode(self, False), ChestNode(self), HealthNode(self)]

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

        self.player = Player(self.nodes[0])

    def play(self):
        self.player.node.action()
        while not self.player.done:
            self.player.move()
            self.player.node.action()

        sys.exit()

game = Game()
game.play()
