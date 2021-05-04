from tkinter import *
from functools import partial
class NodeStackCheck(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("640x600+480+30")
        self.config(bg="#BFD7EA")
        self.title("Node Stack Experiment")
        self.iconbitmap("assets\\icons\\undo.ico")
        self.mainFont="Verdana",30
        self.stackDisplay=Label(self,text="Top of the stack:Empty",font=("Verdana",20),fg="#FEFFFE",bg="#0B3954",relief="raised")
        self.stackDisplay.place(x=10,y=10)
        self.undoButton=Button(self,text="Undo from stack",font=self.mainFont,command=self.UndoStack,fg="#FEFFFE",bg="#0B3954")
        self.undoButton.place(x=10,y=60)
        self.stack,nodeList=[],["Mondeo","Golf","Fiesta","Punto","Civic","Porsche"]
        for node in nodeList:
            Button(self,text=node,font=self.mainFont,fg="#FEFFFE",bg="#0B3954",command=partial(self.AddStack,node)).place(x=410,y=(nodeList.index(node))*100+10)      
        listboxScroll=Scrollbar(self)  
        self.stackList=Listbox(self,font=("Verdana",20),yscrollcommand=listboxScroll.set,height=13,bg="#FEFFFE",fg="#0B3954")
        self.stackList.place(x=10,y=160)    
        listboxScroll.pack(side = RIGHT, fill = Y);listboxScroll.config(command = self.stackList.yview) 
    def UndoStack(self):
        if len(self.stack)>0:
            del self.stack[0]
            self.stackList.delete(0) #END returns the most recent in the list, ACTIVE is the first in the list (oldest)
        if len(self.stack)==0:
            node="Empty"
        else:
            node=self.stack[0]
        self.UpdateLabel(node)            
    def AddStack(self,node):
       self.stack.insert(0,node)
       self.stackList.insert(0, node) 
       self.UpdateLabel(node)
    def UpdateLabel(self,node):
        text=str("Top of the stack:")+str(node)
        self.stackDisplay.config(text=text)        
window=NodeStackCheck();window.mainloop()
