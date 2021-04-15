from tkinter import *
from modules import Maths2
class GFG(Tk):
    def __init__(self):
        super().__init__()
        self.title("Real Box")
        self.geometry("800x800+560+140")
        self.config(bg="#262322")

        self.x,self.y,self.width,self.height,self.size =0,0,800,800,50
        self.canvas = Canvas(self,width=self.width,height=self.height, bg="#F6F6F4")
        self.rectangle = self.canvas.create_rectangle(self.width/2-self.size,self.height/2-self.size,self.width/2+self.size,self.height/2+self.size,fill="#F49F0A")
        self.rectangleData = Maths2.Physics()
        print(self.canvas.coords(self.rectangle))

        self.GRAVITY=9.81
        self.speed=100
        self.velocity=0
        self.canvas.pack()
        self.movement()
      
    def touchingEdge(self):
        self.x,self.y=0,0

    def movement(self):
        self.rectangleData.ModifyValues(time_change=0.01,acceleration=self.GRAVITY,initial_velocity=self.velocity)
        self.rectangleData.VelocityAccelerationTime("velocity")
        print(self.rectangleData.final_velocity)
        self.velocity=self.rectangleData.final_velocity
        self.canvas.move(self.rectangle, self.x/100, self.velocity/100) 
        self.rectangleData.PrintData()
        self.canvas.after(9, self.movement) #calls movement after 10 milliseconds
        for x in self.canvas.coords(self.rectangle):
            print(x)
            if x==self.width or x==self.height or x==0:
                self.touchingEdge()
      
    def left(self, event):
        self.x = -(self.speed)
        self.y = 0    

    def right(self, event):
        self.x = self.speed
        self.y = 0

    def up(self, event):
        self.x = 0
        self.y = -(self.speed)
      
    def down(self, event):
        self.x = 0
        self.y = self.speed
  

master = GFG()

master.bind("<KeyPress-Left>", lambda e: master.left(e))
master.bind("<KeyPress-Right>", lambda e: master.right(e))
master.bind("<KeyPress-Up>", lambda e: master.up(e))
master.bind("<KeyPress-Down>", lambda e: master.down(e))

master.mainloop()