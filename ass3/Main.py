import tkinter as tk
import Action
from ActionBox import ActionBox
from ActionButton import ActionButton


class Main:
    def __init__(self):
        self.screenWidth = 1000
        self.screenHeight = 750

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
                ActionBox(self.canvas, 100 + i * (self.screenWidth - 100) / 8, self.screenHeight / 2, 100, 125))

        # buttons to pick up an action
        self.buttons = [ActionButton(self.canvas, 75, 75, 100, 125, "#1568C5", 0, "Forward"), #blue
                        ActionButton(self.canvas, 175, 75, 100, 125, "#82C59E", 1, "Backward"), #green
                        ActionButton(self.canvas, 275, 75, 100, 125, "#ff0000", 2, "Left"),
                        ActionButton(self.canvas, 375, 75, 100, 125, "#82bfc5", 2, "Right")] #red
        #self.canvas.create_text(self.buttons[0].x, self.buttons[0].y, text="Forward")

        # the actions for the robot to execute
        self.actions = []

        # button to start sequence
        self.startButton = ActionButton(self.canvas, self.screenWidth / 2, self.screenHeight - 100, 100, 50,
                                        "#12FF1A", None, "Start")


    def run_program(self):
        for box in self.boxes:
            if box.action is not None:
                box.action.run()
        print()

    def mouse_pressed(self, event):
        for button in self.buttons:
            # check if the button has been clicked on
            if button.contains(event.x, event.y):
                if button.bType == 0:
                    action = Action.Action(self.canvas, button.x, button.y, 100, 125, button.color, button.textString)  # create new action
                elif button.bType == 1:
                    action = Action.MoveAction(self.canvas, button.x, button.y, 100, 125, button.color, button.textString)  # create new action
                elif button.bType == 2:
                    action = Action.MoveAction(self.canvas, button.x, button.y, 100, 125, button.color, button.textString)
                elif button.bType == 3:
                    action = Action.MoveAction(self.canvas, button.x, button.y, 100, 125, button.color, button.textString)  # create new action
                action.clicked = True  # set that the action has been clicked
                self.actions.append(action)  # add action to list

        for action in self.actions:
            # check if the action has been clicked on
            if action.contains(event.x, event.y):
                action.clicked = True  # set that the action is clicked

                for box in self.boxes:
                    # check if an action within the box has been clicked
                    if box.contains(event.x, event.y):
                        box.action = None  # set the box is no longer filled

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
                    self.canvas.delete(action.icon)  # delete action if not in box
                    self.canvas.delete(action.text)
                    self.actions.remove(action)
                action.clicked = False  # set that the action is no longer clicked


m = Main()
m.win.mainloop()
