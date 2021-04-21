from tkinter import *
import os

class InitWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("DVD Bouncer")
        self.geometry("800x800+560+140")
        self.config(bg="#3C3744")
        self.x,self.y,self.width,self.height,self.size,self.magnitude =0,0,800,800,50,10

        self.box=Canvas(self, width=self.width,height=self.height,bg="#FBFFF1")
        filepath=os.getcwd()
        filepath=str(filepath)+"/image.png"
        self.box.place(x=0,y=0)
        img=PhotoImage(file=filepath)
        self.box.create_image(50,50, image=img,state=NORMAL,anchor=CENTER)

        
window=InitWindow()
window.mainloop()