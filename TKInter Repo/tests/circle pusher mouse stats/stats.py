from tkinter import *
import random
from math import *
import threading
import time

class SimulationWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Circle Pusher")
        self.geometry("1500x1000+10+5")
        self.config(bg='#231B1B')
        mainfont=('Verdana',20)
        self.x,self.y,self.width,self.height,self.oldx,self.oldy,self.mX,self.mY,self.TIME=0,0,1000,1000,0.01,0.01,0.01,0.01,0.01
        self.canvas=self.box=Canvas(self,width=self.width-20,height=self.height-20,bg="#DDFFF7")
        self.canvas.place(x=10,y=10)
        bg_process=threading.Thread(target=self.CheckVelocity)
        while True:
            print("process1")
            self.update()
            self.canvas.bind('<Motion>',self.MouseMotion)
            bg_process.start()
            bg_process.join()



            self.CheckVelocity()
            #self.after(int((1/self.TIME)*10**3),self.CheckVelocity)
    def MouseMotion(self,event):
        self.mX,self.mY=event.x,event.y
    def CheckVelocity(self):
        print("process2")
        time.sleep(self.TIME)
        distance=sqrt(((self.mY-self.oldy)**2)+((self.mX-self.oldx)**2))
        velocity=distance/self.TIME
        self.oldy,self.oldx=self.mY,self.mX
        print(velocity)

window=SimulationWindow()
window.mainloop()
