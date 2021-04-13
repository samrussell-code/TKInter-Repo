from tkinter import *
from functools import partial
import os
import pickle
import Time2
import random
import math
class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic Canvas")
        self.geometry("1280x1000+390+10")
        self.config(bg="#262322")

        info=[]
        self.info=info

        objCount="1"
        self.objCount=objCount
        
        mainFont=font=("Verdana",15)
        sizeButton=Button(self, text="Size",font=mainFont,command=self.openWindow)
        sizeButton.place(x=1000,y=500)

        clearButton=Button(self,text="Clear",font=mainFont,command=self.deleteCanvas)
        clearButton.place(x=1000,y=750)

        saveButton=Button(self,text="Save/Quit",font=mainFont,command=self.saveQuit)
        saveButton.place(x=1000,y=200)

        loadButton=Button(self,text="Load",font=mainFont,command=self.loadData)
        loadButton.place(x=1000,y=100)


        self.squareSize=50 #default square size value
        sizeLabel=Label(self, text="Current Size Is "+str(self.squareSize)+" Points",font=mainFont,relief="groove")
        sizeLabel.place(x=1000,y=250)
        self.sizeLabel=sizeLabel

        dynCanvas=Canvas(width=1900,height=1900, bg="#F1F5F2",scrollregion=(0,0,1900,1900),confine=True)
        dynCanvas.bind("<Button-1>",self.callCreate)
        dynCanvas.bind("<Button-3>",self.tryDelete)#new subroutine called trydelete

        #creating the canvas and scrollbars, for now it's copied and pasted, not sure how to make a subroutine when it needs to be in init
        hscroll,vscroll=Scrollbar(self,orient=HORIZONTAL,command=dynCanvas.xview),Scrollbar(self,orient=VERTICAL,command=dynCanvas.yview)
        dynCanvas.config(xscrollcommand=hscroll.set,yscrollcommand=vscroll.set)
        hscroll.pack(side=BOTTOM,fill=X);vscroll.pack(side=RIGHT,fill=Y)
        dynCanvas.place(x=25,y=25,height=950,width=950)
        self.dynCanvas,self.hscroll,self.vscroll=dynCanvas,hscroll,vscroll
        
        timer=Time2.Time2()
        timer.debug_mode=True
        timer.CountTime(1,self.randomnumbers) #just for debugging, times randomnumbers proc for 1 second.
        
    def randomnumbers(self):
        print(random.randint(0,9*pow(10,64)))
        
    def loadData(self):
        if os.path.isfile("savedata.txt"):
            with open("savedata.txt", "rb")as file:
                self.finalSave=pickle.loads(file.read())                           
                self.deleteCanvas()
           
                for item in self.finalSave:
                    x=item[0];y=item[1];self.squareSize=item[2]
                    self.info.insert(int(self.objCount), [x,y,self.squareSize])
                    Square(self.objCount,self.dynCanvas,x,y,self.squareSize)#this bit tries to save the square  
                    self.objCount=int(self.objCount);self.objCount+=1;self.objCount=str(self.objCount);size=self.squareSize
                    self.dynCanvas.create_rectangle(x-size,y-size,x+size,y+size,fill="#F49F0A")
                    self.changeSize(size)


    def getScrollValue(self,scrollbar,wSize,tSize):
        a,b=scrollbar.get()
        value=a+b-wSize/tSize
        return value

    def callCreate(self,event):
        relh=self.getScrollValue(self.hscroll,950,1900)
        relv=self.getScrollValue(self.vscroll,950,1900)
        x,y,size=event.x+(relh*950),event.y+(relv*950),self.squareSize

        self.info.insert(int(self.objCount), [x,y,size])
        Square(self.objCount,self.dynCanvas,x,y,size)#this bit tries to save the square  
        self.objCount=int(self.objCount);self.objCount+=1;self.objCount=str(self.objCount)
        self.dynCanvas.create_rectangle(x-size,y-size,x+size,y+size,fill="#F49F0A")

    def tryDelete(self,event):
        squareFound=False
        for ID in reversed(self.dynCanvas.find_all()):#searches the dictionary keys in reverse order (from newest to oldest)
            #since only one item can be deleted at a time and it is always the first item to be found this means the
            #newest items (the ones on top of the item stack) will be deleted instead of the item behind it when two squares overlap
            relh=self.getScrollValue(self.hscroll,950,1900)
            relv=self.getScrollValue(self.vscroll,950,1900)
            x,y=event.x+(relh*950),event.y+(relv*950)
            topx,topy,bottomx,bottomy=self.dynCanvas.coords(ID)
            if x>topx and x<bottomx and y>topy and y<bottomy:
                self.dynCanvas.delete(ID)
                toBeRemoved=ID;squareFound=True
                break
        if squareFound==True:
            print("Deleting",toBeRemoved,"...")
        
    def openWindow(self):
        window=SizeWindow(self)

    def changeSize(self,newSize):
        self.squareSize=int(newSize)
        self.sizeLabel['text'] = "Current Size Is "+str(self.squareSize)+" Points"

    def deleteCanvas(self):
        self.dynCanvas.delete("all");self.hscroll.destroy();self.vscroll.destroy()
        dynCanvas=Canvas(width=1920,height=1080, bg="#F1F5F2",scrollregion=(0,0,1900,1900))
        dynCanvas.config(xscrollcommand=self.hscroll.set,yscrollcommand=self.vscroll.set)
        dynCanvas.bind("<Button-1>",self.callCreate);dynCanvas.bind("<Button-3>",self.tryDelete)
        hscroll,vscroll=Scrollbar(self,orient=HORIZONTAL,command=dynCanvas.xview),Scrollbar(self,orient=VERTICAL,command=dynCanvas.yview)
        hscroll.pack(side=BOTTOM,fill=X);vscroll.pack(side=RIGHT,fill=Y)
        dynCanvas.config(xscrollcommand=hscroll.set,yscrollcommand=vscroll.set)
        dynCanvas.place(x=25,y=25,height=950,width=950)
        self.dynCanvas,self.hscroll,self.vscroll,self.objCount,self.info=dynCanvas,hscroll,vscroll,"0",[]

    def saveQuit(self):
        if len(self.dynCanvas.find_all())>0:
            with open("savedata.txt", "wb") as file:
                finalSave=[]
                for x in self.dynCanvas.find_all():
   
                    item=int(x)-1
                    finalSave.insert(item, self.info[item])
                pickle.dump(finalSave, file)
        else:
            try:
                os.remove("savedata.txt")
            except:
                print("Nothing to remove.")
        quit()

class Square():
    def __init__(self,ID,canvas,x,y,size):
        self.ID,self.pos,self.size,self.canvas=ID,(x,y),size,canvas


class SizeWindow(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Modify Size")
        self.geometry("130x260+200+20")
        self.config(bg="#262322")

        #partial is useful for calling a method and its arguments in one pair of brackets
        #(e.g. instead of setSize(10) it becomes setSize,10)
        #this means Button's arg 'command' will accept it as a single callable method
        self.buttonFont=("Verdana",10)
        slider=Scale(self, orient="horizontal", resolution=1, from_=1, to=100, command=partial(self.sliderChange,parent))
        slider.set(parent.squareSize)
        #slider.config(command=partial(parent.changeSize,slider.get()))
        slider.place(x=10,y=210)

        setupList=[["10",10,10,10],["25",25,10,50],["50",50,10,90],["75",75,10,130],["100",100,10,170]]
        for x in setupList:
            self.ButtonSetup(parent,x[0],x[1],x[2],x[3])
    def ButtonSetup(self,parent,text,size,xpos,ypos):
        Button(self,font=self.buttonFont,text=text,command=partial(parent.changeSize,size)).place(x=xpos,y=ypos)

    def sliderChange(self,parent,event):
        parent.changeSize(event)


mainWindow=MainWindow()
mainWindow.mainloop()