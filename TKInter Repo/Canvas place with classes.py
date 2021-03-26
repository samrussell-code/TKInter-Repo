from tkinter import *
from functools import partial

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic Canvas")
        self.geometry("1280x1000+10+10")
        self.config(bg="#424B54")
        
        mainFont=font=("Comic Sans MS",15)
        sizeButton=Button(self, text="Size",font=mainFont,command=self.openWindow)
        sizeButton.place(x=1000,y=500)

        clearButton=Button(self,text="Clear",font=mainFont,command=self.deleteCanvas)
        clearButton.place(x=1000,y=750)

        self.squareSize=50
        sizeLabel=Label(self, text="Current Size Is "+str(self.squareSize)+" Points",font=mainFont,relief="groove")
        sizeLabel.place(x=1000,y=250)
        self.sizeLabel=sizeLabel

        dynCanvas=Canvas(width=950,height=950, bg="#FAFDF6")
        dynCanvas.bind("<Button-1>",self.createSquare)
        dynCanvas.place(x=25,y=25)
        self.dynCanvas=dynCanvas



    def getCanvas(self):
        return self.dynCanvas

    def createSquare(self,event):
        self.dynCanvas.create_rectangle(event.x-self.squareSize,event.y-self.squareSize,event.x+self.squareSize,event.y+self.squareSize,fill="#3993DD")

    def openWindow(self):
        window=SizeWindow(self)
        window.grab_set()

    def changeSize(self,newSize):
        self.squareSize=newSize
        self.sizeLabel['text'] = "Current Size Is "+str(self.squareSize)+" Points"

    def deleteCanvas(self):
        self.dynCanvas.delete("all")


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