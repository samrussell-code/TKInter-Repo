from tkinter import *
import random
from math import *
import time
class InitWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("DVD Bouncer")
        self.geometry("800x800+560+140")
        self.config(bg="#3C3744")
        self.x,self.y,self.width,self.height,self.size,self.magnitude =0,0,800,800,50,10

        self.box=Canvas(self, width=self.width,height=self.height,bg="#FBFFF1")
        #img=PhotoImage(file="converted.gif")
        self.object = self.box.create_rectangle(self.width/2-self.size,self.height/2-self.size,self.width/2+self.size,self.height/2+self.size,fill="#F49F0A")
        self.box.place(x=0,y=0)
        
        
        self.MoveObject(2,2,4)
    def Rotate(self,magnitude):
        hypotenuse=magnitude #this is the magnitude
        theta=random.uniform(-180,180) #this is the angle from x axis that the hypotenuse is aimed at
        x=hypotenuse*round(cos(theta),5)
        y=hypotenuse*round(sin(theta),5)
        isValid=False
        for coordinate in self.box.coords(self.object):
            if (coordinate+x<self.width and coordinate+x<self.height and coordinate+x>0) and (coordinate+y<self.width and coordinate+y<self.height and coordinate+y>0):
                isValid=True
        if isValid==True:
            self.MoveObject(x,y,magnitude)
        else:
            self.Rotate(magnitude)
        

    def MoveObject(self,x,y,magnitude):
        isValid=True
        for coordinate in self.box.coords(self.object):
            if (coordinate+x>=self.width or coordinate+x>=self.height or coordinate+x<=0) or (coordinate+y>=self.width or coordinate+y>=self.height or coordinate+y<=0):
                isValid=False
        if isValid==False:
            coords=self.box.coords(self.object)
            newrandom1=random.uniform(0,magnitude)
            newrandom2=random.uniform(0,magnitude)
            if coords[0]-magnitude<=0 and coords[1]-magnitude<=0:
                print("top left")
                x=(magnitude)+newrandom1;y=(magnitude)+newrandom2
                self.box.move(self.object, x, y)
                isValid=True
                self.box.after(10, self.MoveObject,x,y,magnitude)
            elif coords[2]+magnitude>=self.width and coords[1]-magnitude<=0:
                print("top right")
                x=(-magnitude)-newrandom1;y=(magnitude)+newrandom2
                self.box.move(self.object, x, y)
                isValid=True
                self.box.after(10, self.MoveObject,x,y,magnitude)
            elif coords[0]-magnitude<=0 and coords[2]+magnitude>=self.height:
                print("bottom left")
                x=(magnitude)+newrandom1;y=(-magnitude)-newrandom2
                self.box.move(self.object, x, y)
                isValid=True
                self.box.after(10, self.MoveObject,x,y,magnitude)
            elif coords[2]+magnitude>=self.width and coords[3]+magnitude>=self.height:
                print("bottom right")
                x=(-magnitude)-newrandom1;y=(-magnitude)-newrandom2
                self.box.move(self.object, x, y)
                isValid=True
                self.box.after(10, self.MoveObject,x,y,magnitude)
            else:
                time.sleep(0.01)
                self.Rotate(magnitude)
        else:
            self.box.move(self.object, x, y)
            self.box.after(10, self.MoveObject,x,y,magnitude) #calls movement after 10 milliseconds              
            

window=InitWindow()
window.mainloop()
