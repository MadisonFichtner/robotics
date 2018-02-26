#from Maestro import Controller
import time

class Action:
    def __init__(self, canvas, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clicked = False # if the action is currently clicked
        self.icon = canvas.create_rectangle(self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2,
                                            self.y + self.height / 2, fill=color)
        #self.control = Controller()
        #self.control.setTarget(1,6000)

    # move the action to the specified location
    def move(self, canvas, x, y):
        canvas.move(self.icon, x - self.x, y - self.y)
        self.x = x
        self.y = y


    # return if the given coordinates are within the action icon
    def contains(self, x, y):
        return self.x - self.width / 2 < x < self.x + self.width / 2 and \
               self.y - self.height / 2 < y < self.y + self.height / 2

    def run(self):  #blue/forward action
        #self.control.setTarget(1,6000)
        time.sleep(5)
        print("forward action")
        print("Blue action")


class MoveAction(Action):
    def __init__(self, canvas, x, y, width, height, color):
        super().__init__(canvas, x, y, width, height, color)

    def run(self):
        time.sleep(5)
        print("green action")
