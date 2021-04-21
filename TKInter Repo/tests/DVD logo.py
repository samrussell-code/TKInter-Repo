from tkinter import *
import random
from math import *
class InitWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("DVD Bouncer")
        self.geometry("1000x1000+0+0")
        self.config(bg="#3C3744")
        self.x,self.y,self.width,self.height,self.size,self.magnitude =0,0,1000,1000,50,10
        self.jack=PhotoImage(file="assets\\dvd\\mald.png")


        self.colour_list=["cigar","cyan","grey","megapurple","pale","purple","sunflower","sunset","teal","tommy_rgb","turq","violet","yellow"]
        self.image_list=[]
        load_percent=0
        self.box=Canvas(self, width=self.width,height=self.height,bg="#121113")
        self.box.place(x=0,y=0)
        self.load_label=Label(self,text="Loading Assets... "+str(round(load_percent))+"%",font="Verdana",relief="groove")
        self.load_label.place(x=10,y=10)
        self.load_label.update_idletasks()
        for colour in self.colour_list:
            path='assets\\dvd\\' + colour +'.png' 
            self.image_list.append(PhotoImage(file=path).subsample(10,10))
            load_percent+=100/len(self.colour_list)
            self.load_label['text'] = "Loading Assets... "+str(round(load_percent))+"%"
            self.load_label.update_idletasks()
        self.load_label.destroy()


        self.photo_image=random.choice(self.image_list)
        self.object=self.box.create_image(self.width/2,self.height/2,image=self.photo_image)
        self.Rotate(4)

    def ChangeColour(self,coords):
        self.photo_image=random.choice(self.image_list)
        self.box.itemconfig(self.object,image=self.photo_image)

    def GetCoords(self,initCoords):
        #i think the image coordinates are 0,0,160,74
        finalCoords=[]
        half_width=73
        half_height=33
        finalCoords.append(initCoords[0]-half_width) 
        finalCoords.append(initCoords[1]-half_height)
        finalCoords.append(initCoords[0]+half_width)
        finalCoords.append(initCoords[1]+half_height)
        return finalCoords
        
    def Rotate(self,magnitude):

        hypotenuse=magnitude #this is the magnitude
        theta=random.uniform(40,50) #this is the angle from x axis that the hypotenuse is aimed at
        x=hypotenuse*round(cos(theta),5)
        y=hypotenuse*round(sin(theta),5)
        isValid=False
        for coordinate in self.GetCoords(self.box.coords(self.object)):
            if (coordinate+x<self.width and coordinate+x<self.height and coordinate+x>0) and (coordinate+y<self.width and coordinate+y<self.height and coordinate+y>0):
                isValid=True
        if isValid==True:
            self.ChangeColour(self.box.coords(self.object))
            self.MoveObject(x,y,magnitude)
        else:
            self.Rotate(magnitude)
        

    def MoveObject(self,x,y,magnitude):
        isValid=True
        for coordinate in self.GetCoords(self.box.coords(self.object)):
            if (coordinate+x>=self.width or coordinate+x>=self.height or coordinate+x<=0) or (coordinate+y>=self.width or coordinate+y>=self.height or coordinate+y<=0):
                isValid=False
        if isValid==False:
            coords=self.GetCoords(self.box.coords(self.object))
            newrandom1=random.uniform(0,sqrt(magnitude))
            newrandom2=random.uniform(0,sqrt(magnitude))
            if coords[0]-magnitude<=0 and coords[1]-magnitude<=0:
                #print("top left")
                self.box.move(self.object, newrandom1,newrandom2)
                isValid=True
                self.box.after(10, self.MoveObject,x,y,magnitude)
                self.ChangeColour(self.box.coords(self.object))
                self.box.itemconfig(self.object,image=self.jack)
            elif coords[2]+magnitude>=self.width and coords[1]-magnitude<=0:
                #print("top right")
                x=(-magnitude)-newrandom1;y=(magnitude)+newrandom2
                self.box.move(self.object, x, y)
                isValid=True
                self.box.after(10, self.MoveObject,x,y,magnitude)
                self.ChangeColour(self.box.coords(self.object))
                self.box.itemconfig(self.object,image=self.jack)
            elif coords[0]-magnitude<=0 and coords[3]+magnitude>=self.height:
                #print("bottom left")
                x=(magnitude)+newrandom1;y=(-magnitude)-newrandom2
                self.box.move(self.object, x, y)
                isValid=True
                self.box.after(10, self.MoveObject,x,y,magnitude)
                self.ChangeColour(self.box.coords(self.object))
                self.box.itemconfig(self.object,image=self.jack)
            elif coords[2]+magnitude>=self.width and coords[3]+magnitude>=self.height:
               #print("bottom right")
                x=(-magnitude)-newrandom1;y=(-magnitude)-newrandom2
                self.box.move(self.object, x, y)
                isValid=True
                self.box.after(10, self.MoveObject,x,y,magnitude)
                self.ChangeColour(self.box.coords(self.object))
                self.box.itemconfig(self.object,image=self.jack)
            else:
                self.Rotate(magnitude)
        else:
            self.box.move(self.object, x, y)
            self.box.after(10, self.MoveObject,x,y,magnitude) #calls movement after 10 milliseconds              
            

window=InitWindow()
window.mainloop()
