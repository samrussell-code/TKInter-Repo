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
        self.x,self.y,self.width,self.height,self.oldx,self.oldy,self.mX,self.mY,self.TIME=0,0,1000,1000,0.01,0.01,0.01,0.01,0.1
        self.canvas=self.box=Canvas(self,width=self.width-20,height=self.height-20,bg="#DDFFF7")
        self.canvas.place(x=10,y=10)
        self.update()      
        self.start_threads() #must start in a function

    def start_threads(self):
        t1 = threading.Thread(target=self.Process1,daemon=True);t1.start()#t1.start is important
        t2 = threading.Thread(target=self.Process2,args=[True],daemon=True);t2.start()



    def Process1(self):
        while True:
            self.update()
            self.canvas.bind('<Motion>',self.MouseMotion)

    def MouseMotion(self,event):
        self.mX,self.mY=event.x,event.y

    def Process2(self,debug_mode=False):
        velocity=0
        momentum=0
        mass=5
        while True:
            oldvelocity=velocity
            oldmomentum=momentum
            time.sleep(self.TIME)
            distance=(sqrt(((self.mY-self.oldy)**2)+((self.mX-self.oldx)**2)))/1000
            #1m is 100px
            velocity=distance/self.TIME
            acceleration=(velocity-oldvelocity)/self.TIME
            force=mass*acceleration
            momentum=mass*velocity
            impulse=momentum-oldmomentum
            self.oldy,self.oldx=self.mY,self.mX
            if debug_mode==True:
                print(f'''
                Distance={round(distance,2)}m
                Velocity={round(velocity,2)}ms^-1
                Acceleration={round(acceleration,2)}ms^-2
                Force={round(force,2)}N
                Momentum={round(momentum,2)}kgms^-1
                Impulse={round(impulse,2)}Ns
                ''')

    


window=SimulationWindow()
window.mainloop()