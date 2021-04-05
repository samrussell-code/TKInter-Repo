from tkinter import *
import os, pickle
#created a prototype for unlimited square deletion (it works!)
#next I need to work on saving this information so I can load it into a text file...
class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Test Canvas")
        self.geometry("1000x1000+480+10")
        self.config(bg="#172121")

        saveData={}
        if os.path.isfile("constant.txt"):
            with open("constant.txt", "rb")as file:
                self.saveData=pickle.loads(file.read())
        else:
            self.saveData=saveData
        objCount="0"
        self.objCount=objCount

        dynCanvas=Canvas(width=950,height=950, bg="#E5D0CC")
        dynCanvas.bind("<Button-1>",self.callCreate)
        dynCanvas.bind("<Button-3>",self.tryDelete)#new subroutine called trydelete
        dynCanvas.place(x=25,y=25)
        self.dynCanvas=dynCanvas

    def callCreate(self,event):
        self.objCount=int(self.objCount);self.objCount+=1;self.objCount=str(self.objCount)
        self.saveData[self.objCount]=Square(self.objCount,self.dynCanvas,event.x,event.y,50)#this bit tries to save the square  
        x=event.x;y=event.y;size=50
        self.dynCanvas.create_rectangle(x-size,y-size,x+size,y+size,fill="#444554")

    def tryDelete(self,event):
        squareFound=False
        for ID in reversed(self.saveData.keys()):#searches the dictionary keys in reverse order (from newest to oldest)
            #since only one item can be deleted at a time and it is always the first item to be found this means the
            #newest items (the ones on top of the item stack) will be deleted instead of the item behind it when two squares overlap
            topx,topy,bottomx,bottomy=self.dynCanvas.coords(self.saveData[ID].ID)
            if event.x>topx and event.x<bottomx and event.y>topy and event.y<bottomy:
                self.dynCanvas.delete(self.saveData[ID].ID)
                toBeRemoved=ID;squareFound=True
                break
        if squareFound==True:
            print("Deleting",toBeRemoved,"...")
            del self.saveData[toBeRemoved]

class Square():
    def __init__(self,ID,canvas,x,y,size):
        self.ID=ID
        self.pos=x,y
        self.size=size
        self.canvas=canvas


mainWindow=Window();mainWindow.mainloop()