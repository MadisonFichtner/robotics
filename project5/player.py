import time
from Maestro import Controller

class Player:

    def __init__(self, node, server):
        self.node = node
        self.server = server
        self.done = False
        self.hp = 100
        self.hasKey = False
        self.direction = "South"
        self.control = Controller()
        self.control.setTarget(1,6000)

    def move(self):
        valid = False
        while not valid:
            valid = True

            self.server.write_message("%listen")
            self.server.received = ""

            while self.server.received == "":
                pass

            selection = self.server.received

            if selection == "North":
                if self.node.north is not None:
                    self.node = self.node.north
                    if self.direction == "South":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 5000)
                        time.sleep(3)
                        self.control.setTarget(2, 6000)
                    elif self.direction == "East":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 7000)
                        time.sleep(1.5)
                        self.control.setTarget(2, 6000)
                    elif self.direction == "West":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 5000)
                        time.sleep(1.5)
                        self.control.setTarget(2, 6000)
                else:
                    valid = False
            elif selection == "East":
                if self.node.east is not None:
                    self.node = self.node.east
                    if self.direction == "South":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 7000)
                        time.sleep(1.5)
                        self.control.setTarget(2, 6000)
                    elif self.direction == "North":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 5000)
                        time.sleep(1.5)
                        self.control.setTarget(2, 6000)
                    elif self.direction == "West":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 5000)
                        time.sleep(3)
                        self.control.setTarget(2, 6000)
                else:
                    valid = False
            elif selection == "South" or selection == "self":
                if self.node.south is not None:
                    self.node = self.node.south
                    if self.direction == "North":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 5000)
                        time.sleep(3)
                        self.control.setTarget(2, 6000)
                    elif self.direction == "East":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 5000)
                        time.sleep(1.5)
                        self.control.setTarget(2, 6000)
                    elif self.direction == "West":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 7000)
                        time.sleep(1.5)
                        self.control.setTarget(2, 6000)
                else:
                    valid = False
            elif selection == "West":
                if self.node.west is not None:
                    self.node = self.node.west
                    if self.direction == "South":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 5000)
                        time.sleep(1.5)
                        self.control.setTarget(2, 6000)
                    elif self.direction == "East":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 5000)
                        time.sleep(3)
                        self.control.setTarget(2, 6000)
                    elif self.direction == "North":
                        self.control.setTarget(1, 6000)
                        self.control.setTarget(2, 7000)
                        time.sleep(1.5)
                        self.control.setTarget(2, 6000)
                else:
                    valid = False
            else:
                valid = False

            if valid:
                self.control.setTarget(1, 4500)
                time.sleep(0.65)
                self.control.setTarget(1, 6000)
                self.direction = selection
            if not valid:
                print("I can't go that direction")
                self.server.write_message("I can't go that direction")
                time.sleep(1)

    def fight(self, enemyHp, enemyHasKey):
        print("\nFight!")
        self.server.write_message("Fight!")
        time.sleep(1)

        enemyHp -= 50
        self.hp -= 50
        if self.hp <= 0:
            print("\nI am dead")
            self.server.write_message("I am dead")
            time.sleep(1)

            self.done = True
        else:
            print("Enemy dead!")
            self.server.write_message("Enemy dead!")
            time.sleep(1)

            print("My hp is at " + str(self.hp))
            self.server.write_message("My hp is at " + str(self.hp))
            time.sleep(1.5)

            if enemyHasKey:
                print("I picked up a key")
                self.server.write_message("I picked up a key")
                time.sleep(1)

                self.hasKey = True

    def heal(self):
        print("\nI found a healing station!")
        self.server.write_message("I found a healing station!")
        time.sleep(1.5)

        print("I have healed to full health")
        self.server.write_message("I have healed to full health")
        time.sleep(1.5)

        self.hp = 100

    def openChest(self):
        if self.hasKey:
            print("\nAll of the treasures are mine!")
            self.server.write_message("All of the treasures are mine!")
            time.sleep(1.5)

            self.done = True
        else:
            print("\nI need a key to open this chest")
            self.server.write_message("I need a key to open this chest")
            time.sleep(2.0)
