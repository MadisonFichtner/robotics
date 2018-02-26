#from Maestro import Controller
import time

class Action:
    def __init__(self, canvas, x, y, width, height, color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clicked = False # if the action is currently clicked
        self.color = color
        self.icon = canvas.create_rectangle(self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2,
                                            self.y + self.height / 2, fill=color)
        #self.control = Controller()
        #self.control.setTarget(1,6000)
        self.text = canvas.create_text(self.x, self.y, text=text)

    # move the action to the specified location
    def move(self, canvas, x, y):
        canvas.move(self.icon, x - self.x, y - self.y)
        canvas.move(self.text, x - self.x, y - self.y)
        self.x = x
        self.y = y


    # return if the given coordinates are within the action icon
    def contains(self, x, y):
        return self.x - self.width / 2 < x < self.x + self.width / 2 and \
               self.y - self.height / 2 < y < self.y + self.height / 2

    #def run(self):  #blue/forward action
        #self.control.setTarget(1,6000)
        #time.sleep(5)
        #print("Forward Action")


class MoveAction(Action):
    def __init__(self, canvas, x, y, width, height, color, text):
        super().__init__(canvas, x, y, width, height, color, text)
        self.color = color
        self.namePlate = text #had to be different from text otherwise it broke

    def run(self):
        #time.sleep(5)
        if self.namePlate == "Move Forward":
            print("Move Forward")
        elif self.namePlate == "Move Backward":
            print("Move Backward")
        elif self.namePlate == "Turn Left":
            print("Turn Left")
        elif self.namePlate == "Turn Right":
            print("Turn Right")


class BodyAction(Action):
    def __init__(self, canvas, x, y, width, height, color, text):
        super().__init__(canvas, x, y, width, height, color, text)
        self.color = color
        self.namePlate = text #had to be different from text otherwise it broke

    def run(self):
        if self.namePlate == "Turn Body Right":
            print("Turn Body Right")
        elif self.namePlate == "Turn Body Left":
            print("Turn Body Left")

class HeadAction(Action):
    def __init__(self, canvas, x, y, width, height, color, text):
        super().__init__(canvas, x, y, width, height, color, text)
        self.color = color
        self.namePlate = text #had to be different from text otherwise it broke

    def run(self):
        if self.namePlate == "Turn Head Right":
            print ("Turn Head Right")
        elif self.namePlate == "Turn Head Left":
            print ("Turn Head Left")
        elif self.namePlate == "Tilt Head Up":
            print ("Tilt Head Up")
        elif self.namePlate == "Tilt Head Down":
            print ("Tile Head Down")
