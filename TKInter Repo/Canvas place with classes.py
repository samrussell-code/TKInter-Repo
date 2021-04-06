from tkinter import *
from functools import partial
import os
import pickle


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic Canvas")
        self.geometry("1280x1000+390+10")
        self.config(bg="#424B54")

        saveData={}
        info=[]
        self.info=info

        objCount="0"
        self.objCount=objCount
        
        mainFont=font=("Comic Sans MS",15)
        sizeButton=Button(self, text="Size",font=mainFont,command=self.openWindow)
        sizeButton.place(x=1000,y=500)

        clearButton=Button(self,text="Clear",font=mainFont,command=self.deleteCanvas)
        clearButton.place(x=1000,y=750)

        saveButton=Button(self,text="Save/Quit",font=mainFont,command=self.saveQuit)
        saveButton.place(x=1000,y=200)

        loadButton=Button(self,text="Load",font=mainFont,command=self.loadData)
        loadButton.place(x=1000,y=100)

        self.squareSize=50
        sizeLabel=Label(self, text="Current Size Is "+str(self.squareSize)+" Points",font=mainFont,relief="groove")
        sizeLabel.place(x=1000,y=250)
        self.sizeLabel=sizeLabel

        dynCanvas=Canvas(width=950,height=950, bg="#FAFDF6")
        dynCanvas.bind("<Button-1>",self.callCreate)
        dynCanvas.bind("<Button-3>",self.tryDelete)#new subroutine called trydelete
        dynCanvas.place(x=25,y=25)
        self.dynCanvas=dynCanvas
        
        self.saveData=saveData

    def loadData(self):
        if os.path.isfile("savedata.txt"):
            with open("savedata.txt", "rb")as file:
                self.finalSave=pickle.loads(file.read())
                self.deleteCanvas()
                for item in self.finalSave:
                    x=item[0];y=item[1];self.squareSize=item[2]
                    self.info.insert(int(self.objCount), [x,y,self.squareSize])
                    self.objCount=int(self.objCount);self.objCount+=1;self.objCount=str(self.objCount)

                    self.saveData[self.objCount]=Square(self.objCount,self.dynCanvas,x,y,self.squareSize)#this bit tries to save the square  
                    size=self.squareSize
                    self.dynCanvas.create_rectangle(x-size,y-size,x+size,y+size,fill="#444554")

    def callCreate(self,event):
        self.info.insert(int(self.objCount), [event.x,event.y,self.squareSize])
        self.objCount=int(self.objCount);self.objCount+=1;self.objCount=str(self.objCount)
        self.saveData[self.objCount]=Square(self.objCount,self.dynCanvas,event.x,event.y,self.squareSize)#this bit tries to save the square  
        x=event.x;y=event.y;size=self.squareSize
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
        
    def openWindow(self):
        window=SizeWindow(self)
        window.grab_set()

    def changeSize(self,newSize):
        self.squareSize=newSize
        self.sizeLabel['text'] = "Current Size Is "+str(self.squareSize)+" Points"

    def deleteCanvas(self):
        self.dynCanvas.delete("all")
        self.saveData={}
        self.objCount="0"
        self.info=[]

    def saveQuit(self):
        if len(self.saveData)>0:
            with open("savedata.txt", "wb") as file:
                finalSave=[]
                for x in self.saveData.keys():
                    item=int(x)-1
                    finalSave.insert(item, self.info[item])
                pickle.dump(finalSave, file)
        else:
            os.remove("savedata.txt")
        quit()

class Square():
    def __init__(self,ID,canvas,x,y,size):
        self.ID=ID
        self.pos=x,y
        self.size=size
        self.canvas=canvas


class SizeWindow(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Modify Size")
        self.geometry("20x210+200+20")
        self.config(bg="#424B54")

        #partial is useful for calling a method and its arguments in one pair of brackets
        #(e.g. instead of setSize(10) it becomes setSize,10)
        #this means Button's arg 'command' will accept it as a single callable method
        buttonFont=("Comic Sans MS",10)
        Button(self,font=buttonFont, text="10", command=partial(parent.changeSize,10)).place(x=10,y=10)
        Button(self,font=buttonFont, text="25", command=partial(parent.changeSize,25)).place(x=10,y=50)
        Button(self,font=buttonFont, text="50", command=partial(parent.changeSize,50)).place(x=10,y=90)
        Button(self,font=buttonFont, text="75", command=partial(parent.changeSize,75)).place(x=10,y=130)
        Button(self,font=buttonFont, text="100", command=partial(parent.changeSize,100)).place(x=10,y=170)


mainWindow=MainWindow()
mainWindow.mainloop()