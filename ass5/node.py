class Node:

    def __init__(self):
        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def action(self):
        print("Paths:")
        if self.north is not None:
            print("\tNorth")
        if self.east is not None:
            print("\tEast")
        if self.south is not None:
            print("\tSouth")
        if self.west is not None:
            print("\tWest")
