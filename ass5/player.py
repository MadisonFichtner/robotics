class Player:

    def __init__(self, node):
        self.node = node

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
