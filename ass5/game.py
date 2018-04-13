from node import Node
from player import Player

nodes = [Node(), Node(), Node(), Node(), Node()]

#      0
#    1 2 3
#      4

nodes[0].south = nodes[2]

nodes[1].east = nodes[2]

nodes[2].north = nodes[0]
nodes[2].east = nodes[3]
nodes[2].south = nodes[4]
nodes[2].west = nodes[1]

nodes[3].west = nodes[2]

nodes[4].north = nodes[2]

player = Player(nodes[0])

while (True):
    player.node.action()
    player.move()
