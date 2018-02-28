# from Maestro import Controller
import time


class Action:
    def __init__(self, canvas, x, y, width, height, color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clicked = False  # if the action is currently clicked
        self.color = color  # color of action rectangle
        self.setting = 0  # how long or how many degrees to do action for
        self.settingStep = 0  # how much to decrease or increase setting per button press
        self.settingType = None  # duration or degrees
        self.settingMin = 0  # minimum setting
        self.settingMax = 0  # maximum setting

        self.icon = canvas.create_rectangle(self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2,
                                            self.y + self.height / 2, fill=color, width=5)
        self.text = canvas.create_text(self.x, self.y - 7, text=text)  # name of action
        self.label = None  # shows current setting
        self.buttonUp = canvas.create_polygon(self.x - 20, self.y - 20, self.x + 20, self.y - 20, self.x, self.y - 50,
                                              fill='black')  # up button for adjusting setting
        self.buttonDown = canvas.create_polygon(self.x - 20, self.y + 20, self.x + 20, self.y + 20, self.x, self.y + 50,
                                                fill='black')  # down button for adjusting setting
        # self.control = Controller()
        # self.control.setTarget(1,6000)

    # move the action to the specified location
    def move(self, canvas, x, y):
        canvas.move(self.icon, x - self.x, y - self.y)
        canvas.move(self.text, x - self.x, y - self.y)
        canvas.move(self.label, x - self.x, y - self.y)
        canvas.move(self.buttonUp, x - self.x, y - self.y)
        canvas.move(self.buttonDown, x - self.x, y - self.y)
        self.x = x
        self.y = y

    # return if and where the action was clicked
    # 0 = not clicked
    # 1 = up arrow
    # 2 = down arrow
    # 3 = rest of box
    def click_location(self, x, y):
        if self.x - 20 < x < self.x + 20 and self.y - 50 < y < self.y - 20:  # if up arrow clicked
            return 1
        elif self.x - 20 < x < self.x + 20 and self.y + 20 < y < self.y + 50:  # if down arrow clicked
            return 2
        elif self.x - self.width / 2 < x < self.x + self.width / 2 and \
                                        self.y - self.height / 2 < y < self.y + self.height / 2:  # if rest clicked
            return 3

        return 0  # if not clicked

    # change the setting for this action
    # if direction = 0 => decrease
    # if direction = 1 => increase
    def change_setting(self, direction, canvas):
        if direction == 0 and self.setting - self.settingStep >= self.settingMin:
            self.setting -= self.settingStep  # decrease setting
        elif direction == 1 and self.setting + self.settingStep <= self.settingMax:
            self.setting += self.settingStep  # increase setting

        canvas.delete(self.label)  # delete old label
        # create new label
        self.label = canvas.create_text(self.x, self.y + 7, text=str(self.setting) + " " + self.settingType)

    # set border color to yellow or black
    def set_active(self, canvas, flag):
        canvas.delete(self.icon)  # delete old icon
        # create new icon
        if flag:  # if active set border to yellow
            self.icon = canvas.create_rectangle(self.x - self.width / 2, self.y - self.height / 2,
                                                self.x + self.width / 2, self.y + self.height / 2,
                                                fill=self.color, outline="#ffd700", width=5)
        else:  # if inactive set border to black
            self.icon = canvas.create_rectangle(self.x - self.width / 2, self.y - self.height / 2,
                                                self.x + self.width / 2, self.y + self.height / 2,
                                                fill=self.color, outline="black", width=5)
        canvas.tag_raise(self.text)  # move other parts of action to top of icon
        canvas.tag_raise(self.label)
        canvas.tag_raise(self.buttonUp)
        canvas.tag_raise(self.buttonDown)
        canvas.update_idletasks()

    def destroy(self, canvas):
        canvas.delete(self.icon)  # delete action if not in box
        canvas.delete(self.text)
        canvas.delete(self.label)
        canvas.delete(self.buttonUp)
        canvas.delete(self.buttonDown)


class MoveAction(Action):
    def __init__(self, canvas, x, y, width, height, color, text):
        super().__init__(canvas, x, y, width, height, color, text)
        self.color = color
        self.namePlate = text  # had to be different from text otherwise it broke
        self.setting = 1.0
        self.settingStep = 0.25
        self.settingType = "seconds"
        self.settingMin = self.settingStep
        self.settingMax = 10
        self.label = canvas.create_text(self.x, self.y + 7, text=str(self.setting) + " " + self.settingType)

    def run(self):
        time.sleep(self.setting)
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
        self.namePlate = text  # had to be different from text otherwise it broke
        self.setting = 30
        self.settingStep = 5
        self.settingType = "degrees"
        self.settingMin = 0
        self.settingMax = 90
        self.label = canvas.create_text(self.x, self.y + 7, text=str(self.setting) + " " + self.settingType)

    def run(self):
        if self.namePlate == "Turn Body Right":
            print("Turn Body Right")
        elif self.namePlate == "Turn Body Left":
            print("Turn Body Left")


class HeadAction(Action):
    def __init__(self, canvas, x, y, width, height, color, text):
        super().__init__(canvas, x, y, width, height, color, text)
        self.color = color
        self.namePlate = text  # had to be different from text otherwise it broke
        self.setting = 30
        self.settingStep = 5
        self.settingType = "degrees"
        self.settingMin = 0
        self.settingMax = 90
        self.label = canvas.create_text(self.x, self.y + 7, text=str(self.setting) + " " + self.settingType)

    def run(self):
        if self.namePlate == "Turn Head Right":
            print("Turn Head Right")
        elif self.namePlate == "Turn Head Left":
            print("Turn Head Left")
        elif self.namePlate == "Tilt Head Up":
            print("Tilt Head Up")
        elif self.namePlate == "Tilt Head Down":
            print("Tilt Head Down")
