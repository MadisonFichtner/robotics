import tkinter as tk
import _thread
import time

class DrawingStuff():
    def __init__(self, r, c=None):
        self.client = c
        self.root = r
        self.flag = True
        self.speed = .8
        r.title("TangoBot")
        self.canvasW = 800
        self.canvasH = 410
        self.c = tk.Canvas(self.root, width = self.canvasW, height=self.canvasH)
        self.c.pack()
        
    def changeFlag(self):
        for i in range(100):
            #print (i)
        while(i != "Stop"):
            i = input("Stop, up or down Eyeballs?")
            if i == "up":
                #print('down')
                self.speed += .2
            elif i == "up":
                self.speed -= .2
                
        self.flag = False
        
    def drawEyes(self):
        midRow = int(self.canvasH/2)
        midCol = int(self.canvasW/2)
        while(self.flag):
            self.c.create_oval(5, 5, midCol-5, self.canvasH-40, fill="#000000")
            self.c.create_oval(midCol+5, 5, self.canvasW, self.canvasH-40, fill="#000000")
            leftRow = int(midRow/2)+100
            leftCol = int(midCol/2)
            #start pupils
            self.c.create_oval(leftRow, leftCol, leftRow+100, leftCol+100, fill="#ffffff")
            self.c.create_oval(700, 220, 600, 320, fill="#ffffff")
            self.root.update()
            time.sleep(self.speed)

            self.c.create_oval(5, 5, midCol-5, self.canvasH-40, fill="#000000")
            self.c.create_oval(midCol+5, 5, self.canvasW, self.canvasH-40, fill="#000000")
            self.c.create_oval(leftRow, leftCol, leftRow-100, leftCol+100, fill="#ffffff")
            self.c.create_oval(500, 220, 600, 320, fill="#ffffff")
            self.root.update()
            time.sleep(self.speed)
           
  
def __main__():

    root = tk.Tk()
    paint = DrawingStuff(root)
    ######Start a new Thread
    try:
        _thread.start_new_thread(paint.changeFlag,())
    except:
       #print ("Error: unable to start thread")

    ####Continue with new Thread   
    paint.drawEyes()
    #print("Goodbye")
    root.mainloop()
  
__main__()
