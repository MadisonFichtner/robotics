class Player:

    def __init__(self, node):
        self.node = node
        self.done = False
        self.hp = 100
        self.hasKey = False

    def move(self):
        valid = False
        while not valid:
            valid = True
            selection = input()
            if selection == "north":
                if self.node.north is not None:
                    self.node = self.node.north
                else:
                    valid = False
            elif selection == "east":
                if self.node.east is not None:
                    self.node = self.node.east
                else:
                    valid = False
            elif selection == "south":
                if self.node.south is not None:
                    self.node = self.node.south
                else:
                    valid = False
            elif selection == "west":
                if self.node.west is not None:
                    self.node = self.node.west
                else:
                    valid = False
            else:
                valid = False

            if not valid:
                print("I can't go that direction")

    def fight(self, enemyHp, enemyHasKey):
        print("\nFight!")
        enemyHp -= 50
        self.hp -= 50
        if self.hp <= 0:
            print("\nI am dead")
            self.done = True
        else:
            print("Enemy dead!")
            print("My hp is at " + str(self.hp))

            if enemyHasKey:
                print("I picked up a key")
                self.hasKey = True

    def heal(self):
        print("\nI found a healing station!")
        print("I have healed to full health")
        self.hp = 100

    def openChest(self):
        if self.hasKey:
            print("\nAll of the treasures are mine!")
            self.done = True
        else:
            print("\nI need a key to open this chest")