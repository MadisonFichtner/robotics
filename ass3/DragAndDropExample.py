import tkinter as tk
from Action import Action
from ActionBox import ActionBox
from ActionButton import ActionButton


class MouseMovement:
    def __init__(self):
        self.win = tk.Tk()
        self.canvas = tk.Canvas(self.win, bg="#333333", width="1000", height="750")
        self.canvas.bind('<B1-Motion>', self.mouse_dragged)
        self.canvas.bind('<ButtonPress-1>', self.mouse_pressed)
        self.canvas.bind('<ButtonRelease-1>', self.mouse_release)

        self.canvas.pack()

        # the boxes in which actions are placed
        self.boxes = [ActionBox(self.canvas, 300, 350, 100, 100),
                      ActionBox(self.canvas, 450, 350, 100, 100),
                      ActionBox(self.canvas, 600, 350, 100, 100),
                      ActionBox(self.canvas, 750, 350, 100, 100)]

        # buttons to pick up an action
        self.buttons = [ActionButton(self.canvas, 50, 50, 50, 50, "#1568C5"),
                        ActionButton(self.canvas, 50, 125, 50, 50, "#82C59E")]

        # the actions for the robot to execute
        self.actions = []

    def mouse_pressed(self, event):
        for button in self.buttons:
            # check if the button has been clicked on
            if button.contains(event.x, event.y):
                action = Action(self.canvas, button.x, button.y, 50, 50, button.color)  # create new action
                action.clicked = True  # set that the action has been clicked
                self.actions.append(action)  # add action to list

        for action in self.actions:
            # check if the aciton has been clicked on
            if action.contains(event.x, event.y):
                action.clicked = True  # set that the action is clicked

                for box in self.boxes:
                    # check if an action within the box has been clicked
                    if box.contains(event.x, event.y):
                        box.filled = False  # set the box is no longer filled

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
                                                    box.y - box.height / 2 < event.y < box.y + box.height / 2 and not box.filled:
                        action.move(self.canvas, box.x, box.y)  # move the action to the center of the box
                        box.filled = True  # set that the box is now filled
                        placed = True

                if not placed:
                    self.canvas.delete(action.icon)  # delete action if not in box
                action.clicked = False  # set that the action is no longer clicked


m = MouseMovement()
m.win.mainloop()
