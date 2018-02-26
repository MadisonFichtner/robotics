# from Maestro import Controller
import tkinter as tk


class Move:
    def __init__(self):
        self.win = tk.Tk()
        self.win.bind('<Left>', self.move)
        self.win.bind('<Right>', self.move)
        self.win.bind('<KeyRelease-Left>', self.move)
        self.win.bind('<KeyRelease-Right>', self.move)
        self.win.bind('<Up>', self.move)
        self.win.bind('<Down>', self.move)
        self.win.bind('<KeyRelease-Up>', self.move)
        self.win.bind('<KeyRelease-Down>', self.move)

        self.moving = False
        self.turning = False

        # self.control = Controller()

        self.win.mainloop()

    def move(self, event):
        if str(event.type) == "KeyPress":
            if event.keysym == "Left" and not self.turning:
                self.turning = True
                print("Pressed Left")
            elif event.keysym == "Right" and not self.turning:
                self.turning = True
                print("Pressed Right")
            elif event.keysym == "Up" and not self.moving:
                self.moving = True
                print("Pressed Up")
            elif event.keysym == "Down" and not self.moving:
                self.moving = True
                print("Pressed Down")

        if str(event.type) == "KeyRelease":
            if event.keysym == "Left":
                self.turning = False
                print("Released Left")
            elif event.keysym == "Right":
                self.turning = False
                print("Released Right")
            elif event.keysym == "Up":
                self.moving = False
                print("Released Up")
            elif event.keysym == "Down":
                self.moving = False
                print("Released Down")

move = Move()
