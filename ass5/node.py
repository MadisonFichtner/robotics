import time

class Node:
    def __init__(self, game, server):
        self.game = game
        self.server = server
        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def action(self):
        directions = []
        string = ""
        if self.north is not None:
            directions.append("north")
        if self.east is not None:
            directions.append("east")
        if self.south is not None:
            directions.append("south")
        if self.west is not None:
            directions.append("west")

        if len(directions) is 1:
            string = "I see a path to the " + directions[0]
        elif len(directions) is 2:
            string = "I see paths to the " + directions[0] + " and " + directions[1]
            time.sleep(1)
        elif len(directions) is 3:
            string = "I see paths to the " + directions[0] + " " + directions[1] + " and " + directions[2]
            time.sleep(1)
        elif len(directions) is 4:
            string = "I see paths to the " + directions[0] + " " + directions[1] + " " + directions[2] + " and " + \
                     directions[3]

        print(string)
        self.server.write_message(string)
        time.sleep(3)
        self.server.write_message("Where should I go?")
        time.sleep(1.5)


class EnemyNode(Node):
    def __init__(self, game, hasKey, server):
        super().__init__(game, server)
        self.alive = True
        self.hasKey = hasKey

    def action(self):
        if self.alive:
            self.game.player.fight(100, self.hasKey)

        if not self.game.player.done:
            self.alive = False
            super().action()


class HealthNode(Node):
    def __init__(self, game, server):
        self.used = False
        super().__init__(game, server)

    def action(self):
        if not self.used:
            self.game.player.heal()
            self.used = True
        super().action()


class ChestNode(Node):
    def __init__(self, game, server):
        super().__init__(game, server)

    def action(self):
        self.game.player.openChest()

        if not self.game.player.done:
            super().action()
