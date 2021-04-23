from tkinter import *
import random
from math import *
import winsound
class InitWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("DVD Bouncer")
        self.geometry("1000x1000+0+0")
        self.config(bg="#3C3744")
        self.iconbitmap("assets\\icons\\jack.ico")
        self.x,self.y,self.width,self.height,self.size,self.magnitude =0,0,1000,1000,50,10
        self.wall_hit= 'assets\\audio\\wall_hit.wav'
        self.colour_list=["cigar","cyan","grey","megapurple","pale","purple","sunflower","sunset","teal","tommy_rgb","turq","violet","yellow"]
        self.image_list=[]
        load_percent=0
        self.box=Canvas(self, width=self.width,height=self.height,bg="#121113")
        self.box.place(x=0,y=0)
        self.load_label=Label(self,text="Loading Assets... "+str(round(load_percent))+"%",font="Verdana",relief="groove")
        self.load_label.place(x=10,y=10)
        self.load_label.update_idletasks()
        self.jack=PhotoImage(file="assets\\dvd\\mald.png")
        load_percent+=100/(len(self.colour_list)+1)
        for colour in self.colour_list:
            path='assets\\dvd\\' + colour +'.png' 
            self.image_list.append(PhotoImage(file=path).subsample(10,10))
            load_percent+=100/(len(self.colour_list)+1)
            self.load_label['text'] = "Loading Assets... "+str(round(load_percent))+"%"
            self.load_label.update_idletasks()
        self.load_label.destroy()

        self.photo_image=random.choice(self.image_list)
        self.object=self.box.create_image(self.width/2,self.height/2,image=self.photo_image)
        self.MoveObject(sqrt(3),1,2)

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
        
    def Rotate(self,magnitude,x,y,mirrorX=False,mirrorY=False,side=""):
        hypotenuse=magnitude #this is the magnitude
        plus_angle=random.uniform(-15,15) #this is the number of degrees to add to angle
        initial_invert_x,initial_invert_y=False,False
        theta=degrees(asin(y/hypotenuse))
        print(theta,x,y,)
        print(side)
        if side=="side" and x<0:
            initial_invert_x=True
        if side=="bottom" and x<0:
            initial_invert_x=True
        if side=="bottom" and y<0:
            initial_invert_y=True
        if side=="bottom" and y<0 and x<0:
            print("hitting the top from right")
            initial_invert_x,initial_invert_y=True,False
        if side=="bottom" and y<0 and x>0:
            print("hitting the top from left")
            mirrorY=False
            
      #  if side=="bottom" and x<0:
       #     initial_invert_x=True


        x=magnitude*cos(radians(theta+plus_angle))
        y=magnitude*sin(radians(theta+plus_angle))
        if initial_invert_x==True:
            x=-x
        if initial_invert_y==True:
            y=-y
        if mirrorX==True:
            x=-x
        if mirrorY==True:
            y=-y
        print(theta,x,y)
        winsound.PlaySound(self.wall_hit,winsound.SND_ASYNC)
        return x,y

    
    def MoveObject(self,x,y,magnitude):
        current_coords=self.GetCoords(self.box.coords(self.object))
        if current_coords[2]>=self.width or current_coords[0]<=0:
            print("right or left")
            x,y=self.Rotate(magnitude,x,y,mirrorX=True,mirrorY=False,side="side")
            self.box.move(self.object, x, y)
            self.ChangeColour(self.box.coords(self.object))
            self.box.after(10, self.MoveObject,x,y,magnitude)
            #work out the y value using the opposite y adjacent x
        elif current_coords[3]>self.height or current_coords[1]<=0:
            print("bottom or top")
            x,y=self.Rotate(magnitude,x,y,mirrorX=False,mirrorY=True,side="bottom")
            self.box.move(self.object, x, y)
            self.ChangeColour(self.box.coords(self.object))
            self.box.after(10, self.MoveObject,x,y,magnitude)
            
        else:
            self.box.move(self.object, x, y)
            self.box.after(10, self.MoveObject,x,y,magnitude) #calls movement after 10 milliseconds              
            

window=InitWindow()
window.mainloop()
