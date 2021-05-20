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
        self.update()      
        self.start_threads() #must start in a function

    def start_threads(self):
        t1 = threading.Thread(target=self.Process1,daemon=True);t1.start()#t1.start is important
        t2 = threading.Thread(target=self.Process2,daemon=True);t2.start()



    def Process1(self):
        while True:
            print("process1")
            self.update()
            self.canvas.bind('<Motion>',self.MouseMotion)

    def MouseMotion(self,event):
        self.mX,self.mY=event.x,event.y

    def Process2(self):
        while True:
            print("process2")
            time.sleep(self.TIME)
            distance=sqrt(((self.mY-self.oldy)**2)+((self.mX-self.oldx)**2))
            velocity=distance/self.TIME
            self.oldy,self.oldx=self.mY,self.mX
            print(velocity)

    


window=SimulationWindow()
window.mainloop()