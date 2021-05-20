from tkinter import *
import random
from math import *

class SimulationWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Circle Pusher")
        self.geometry("1500x1000+10+5")
        self.config(bg='#231B1B')
        mainfont=('Verdana',20)
        self.x,self.y,self.width,self.height,self.size,self.circle_count,self.range,self.friction,self.move_cache,self.power=0,0,1000,1000,20,50,1,1,{},800
        self.labeltext='Friction: '+str(round(int(self.friction),3))
        self.rangetext='Range: '+str(round(int(self.range)))
        self.friction_label=Label(text=self.labeltext,font=mainfont)
        self.friction=1+(int(self.friction)*10**-5)
        self.canvas=self.box=Canvas(self,width=self.width-20,height=self.height-20,bg="#DDFFF7")
        Scale(command=self.ChangeFriction,resolution=1, from_=1, to=2000,length=250,orient="horizontal").place(x=1155,y=105)
        self.range_label=Label(text=self.rangetext,font=mainfont)
        self.range_label.place(x=1198,y=165)
        Scale(command=self.ChangeRange,resolution=1, from_=1, to=250,length=250,orient="horizontal").place(x=1155,y=205)
        self.friction_label.place(x=1198,y=65)
        self.canvas.place(x=10,y=10)
        self.CreateCircles()

        while True:
            self.update()
            self.canvas.bind('<Motion>',self.MouseMotion)
            self.UpdateMovement()

    def ChangeFriction(self,event):
        self.friction=event
        print(self.friction)
        self.labeltext='Friction: '+str(round(int(self.friction),3))
        self.friction_label.configure(text=(self.labeltext))
        self.friction=1+(int(self.friction)*10**-5)    
    def ChangeRange(self,event):
        self.range=int(event)
        print(self.range)
        self.rangetext='Range: '+str(round(int(self.range)))
        self.range_label.configure(text=(self.rangetext))

        return

    def MouseMotion(self,event):
        self.mX,self.mY=event.x,event.y
        near_list=self.canvas.find_overlapping(self.mX-self.range,self.mY-self.range,self.mX+self.range,self.mY+self.range)
        for ID in near_list:
            x,y=self.CalculateDistance(ID,self.mX,self.mY)
            print(x,y)
            x=0.1 if x==0 else x
            y=0.1 if y==0 else y
            self.canvas.move(ID,x/1000,y/1000)
            self.move_cache[ID]=x,y
            print(x,y)
        self.UpdateMovement()

    def UpdateMovement(self):
        items_not_moving=[]
        for item in self.move_cache:
            x,y=self.move_cache.get(item)
            self.move_cache[item]=x/self.friction,y/self.friction
            if abs(x)<0.1 or abs(y)<0.1:
                items_not_moving.append(item)
            self.canvas.move(item,(x/1000),(y/1000))
        for item in items_not_moving:
            del self.move_cache[item]
        return

    def CalculateDistance(self,ID,mX,mY):
       coords=self.canvas.coords(ID)
       eX,eY=((coords[0]+coords[2])/2),((coords[1]+coords[3])/2)
       A,B=eX-mX,eY-mY
       C=sqrt((A**2)+(B**2))
       A=0.1 if A==0 else A
       B=0.1 if B==0 else B
       angle=atan(B/A)
       return A,B
      

    def CreateCircles(self):
        for x in range(0,self.circle_count):
            topx,topy=random.randint(0,self.width),random.randint(0,self.height)
            bottomx,bottomy=topx+self.size,topy+self.size
            self.canvas.create_oval(topx,topy,bottomx,bottomy,fill=("#"+("%06x"%random.randint(0,255**3))))
    def RandomPoint(self,canvas,point_list,width,height):
        generated_point=random.randint(0,width),random.randint(0,height)

window=SimulationWindow()
window.mainloop()
