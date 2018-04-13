class Node:
    def __init__(self, game):
        self.game = game
        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def action(self):
        print("\nPaths:")
        if self.north is not None:
            print("\tNorth")
        if self.east is not None:
            print("\tEast")
        if self.south is not None:
            print("\tSouth")
        if self.west is not None:
            print("\tWest")


class EnemyNode(Node):
    def __init__(self, game, hasKey):
        super().__init__(game)
        self.alive = True
        self.hasKey = hasKey

    def action(self):
        if self.alive:
            self.game.player.fight(100, self.hasKey)

        if not self.game.player.done:
            self.alive = False
            super().action()


class HealthNode(Node):
    def __init__(self, game):
        super().__init__(game)

    def action(self):
        self.game.player.heal()
        super().action()


class ChestNode(Node):
    def __init__(self, game):
        super().__init__(game)

    def action(self):
        self.game.player.openChest()

        if not self.game.player.done:
            super().action()
