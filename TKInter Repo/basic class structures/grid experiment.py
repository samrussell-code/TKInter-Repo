from tkinter import *
from functools import partial
class Window3x3(Tk):
    def __init__(self):
        super().__init__()
        #self.geometry("250x250+10+10")
        self.title("3x3 Grid")
        self.verdana = ("Verdana", 40, "bold")
        self.config(bg="#001524")
        self.words = ['A8', 'B8', 'C8','D8', 'E8', 'F8','G8', 'H8', 'A7', 'B7', 'C7','D7','E7','F7','G7','H7','A6', 'B6', 'C6','D6','E6','F6','G6','H6','A5', 'B5', 'C5','D5','E5','F5','G5','H5','A4', 'B4', 'C4','D4','E4','F4','G4','H4','A3', 'B3', 'C3','D3','E3','F3','G3','H3','A2', 'B2', 'C2','D2','E2','F2','G2','H2','A1', 'B1', 'C1','D1','E1','F1','G1','H1']
        self.label_list={}
        COLUMNLENGTH,rownumber,columnnumber=8,0,0
        colourFlip=True
        for x in self.words:
            if self.words.index(x)%COLUMNLENGTH==0:
                colourFlip=True if colourFlip==False else False
            colour="#937B63" if colourFlip==False else "#EEE3D2"
            colourFlip=True if colourFlip==False else False

            self.label_list[len(self.label_list)]=Label(self, text=x,font=self.verdana, bg=colour, fg="#FFFFFF")
            
        for pos in self.label_list:
            if pos%(COLUMNLENGTH)==0:
                columnnumber=0
                rownumber+=1
            self.label_list.get(pos).bind("<Button-1>",partial(self.OnPress,self.label_list.get(pos).cget("text")))
            self.label_list.get(pos).grid(row=rownumber, column=columnnumber,padx=2,pady=2)
            columnnumber+=1

    def OnPress(self,pos,event):
        print("pressing",pos)
        
window=Window3x3()
window.mainloop()
