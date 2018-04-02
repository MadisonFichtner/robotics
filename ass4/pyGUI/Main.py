import tkinter as tk
import Action
from ActionBox import ActionBox
from ActionButton import ActionButton


class Main:
    def __init__(self):
        self.screenWidth = 770
        self.screenHeight = 460

        self.win = tk.Tk()
        self.canvas = tk.Canvas(self.win, bg="#333333", width=str(self.screenWidth), height=str(self.screenHeight))
        self.canvas.bind('<B1-Motion>', self.mouse_dragged)
        self.canvas.bind('<ButtonPress-1>', self.mouse_pressed)
        self.canvas.bind('<ButtonRelease-1>', self.mouse_release)

        self.canvas.pack()

        # the boxes in which actions are placed
        self.boxes = []
        for i in range(8):
            self.boxes.append(
                ActionBox(self.canvas, 50 + i * (self.screenWidth / 8), self.screenHeight / 1.5, 100, 125))

        buttonWidth = ((self.screenWidth) / 10)
        # buttons to pick up an action
        self.buttons = [ActionButton(self.canvas, buttonWidth / 2, 100, buttonWidth, 125, "#1568C5", 0, "Move Forward"),
                        ActionButton(self.canvas, buttonWidth / 2 + buttonWidth, 100, buttonWidth, 125, "#1568C5", 0, "Move Backward"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 2), 0, buttonWidth, 125, "#ff0000", 0, "Turn Left"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 3), 0, buttonWidth, 125, "#ff0000", 0, "Turn Right"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 4), 0, buttonWidth, 125, "#ffffff", 1, "Turn Body Left"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 5), 0, buttonWidth, 125, "#ffffff", 1, "Turn Body Right"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 6), 0, buttonWidth, 125, "#cc0099", 2, "Turn Head Left"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 7), 0, buttonWidth, 125, "#cc0099", 2, "Turn Head Right"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 8), 0, buttonWidth, 125, "#ffff00", 2, "Tilt Head Up"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 9), 0, buttonWidth, 125, "#ffff00", 2, "Tilt Head Down"),
                        ActionButton(self.canvas, buttonWidth / 2, 150, buttonWidth, 125, "#ffffff", 3, "Hello"),
                        ActionButton(self.canvas, buttonWidth / 2 + buttonWidth, 150, buttonWidth, 125, "#ffffff", 3, "Beep Boop Beep"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 2), 150, buttonWidth, 125, "#cc0099", 3, "What is Life"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 3), 150, buttonWidth, 125, "#cc0099", 3, "Goodbye"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 4), 150, buttonWidth, 125, "#ffff00", 3, "Destroy all Humans"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 5), 150, buttonWidth, 125, "#ffffff", 4, "Listen: Start"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 6), 150, buttonWidth, 125, "#ffffff", 4, "Listen: Continue"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 7), 150, buttonWidth, 125, "#cc0099", 4, "Listen: Go Home"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 8), 150, buttonWidth, 125, "#cc0099", 4, "Listen: Fuck Off"),
                        ActionButton(self.canvas, buttonWidth / 2 + (buttonWidth * 9), 150, buttonWidth, 125, "#ffff00", 4, "Listen: Shit")]
        # self.canvas.create_text(self.buttons[0].x, self.buttons[0].y, text="Forward")

        # the actions for the robot to execute
        self.actions = []

        # button to start sequence
        self.startButton = ActionButton(self.canvas, self.screenWidth / 2, self.screenHeight - 50, 100, 50,
                                        "#12FF1A", None, "Start")

    def run_program(self):
        for box in self.boxes:
            if box.action is not None:
                box.action.set_active(self.canvas, True)  # set the action to be active
                box.action.run()        # run action

        for box in self.boxes:
            if box.action is not None:
                box.action.set_active(self.canvas, False)  # set all actions to inactive
        print()

    def mouse_pressed(self, event):
        for button in self.buttons:
            # check if the button has been clicked on
            if button.contains(event.x, event.y):
                if button.bType == 0:
                    action = Action.MoveAction(self.canvas, button.x, button.y, 100, 125, button.color,
                                               button.textString)  # create new action
                elif button.bType == 1:
                    action = Action.BodyAction(self.canvas, button.x, button.y, 100, 125, button.color,
                                               button.textString)
                elif button.bType == 2:
                    action = Action.HeadAction(self.canvas, button.x, button.y, 100, 125, button.color,
                                               button.textString)
                elif button.bType == 3:
                    action = Action.VoiceAction(self.canvas, button.x, button.y, 100, 125, button.color, button.textString)

                elif button.bType == 4:
                    action = Action.ListenAction(self.canvas, button.x, button.y, 100, 125, button.color, button.textString)

                action.clicked = True  # set that the action has been clicked
                self.actions.append(action)  # add action to list

        for action in self.actions:
            # check if the action has been clicked on
            click_location = action.click_location(event.x, event.y)
            if click_location == 3:
                action.clicked = True  # set that the action is clicked

                for box in self.boxes:
                    # check if an action within the box has been clicked
                    if box.contains(event.x, event.y):
                        box.action = None  # set the box is no longer filled
            elif click_location == 1 and not action.clicked:   # if the up button is clicked
                action.change_setting(1, self.canvas)
            elif click_location == 2 and not action.clicked:   # if the down button is clicked
                action.change_setting(0, self.canvas)

        # if the play button was pressed
        if self.startButton.contains(event.x, event.y):
            self.run_program()

    def mouse_dragged(self, event):
        for action in self.actions:  # iterate through all actions
            if action.clicked:
                action.move(self.canvas, event.x, event.y)  # move the action if it is being dragged

    def mouse_release(self, event):
        for action in self.actions:
            if action.clicked:  # if an action has been clicked
                placed = False  # if the action was placed in a box
                for box in self.boxes:
                    # check if the action was released within a box
                    if box.x - box.width / 2 < event.x < box.x + box.width / 2 and \
                                                    box.y - box.height / 2 < event.y < box.y + box.height / 2 and box.action is None:
                        action.move(self.canvas, box.x, box.y)  # move the action to the center of the box
                        box.action = action  # set that the box is now filled
                        placed = True

                if not placed:
                    action.destroy(self.canvas)  # delete action if not in box
                    self.actions.remove(action)
                action.clicked = False  # set that the action is no longer clicked


m = Main()
m.win.mainloop()
