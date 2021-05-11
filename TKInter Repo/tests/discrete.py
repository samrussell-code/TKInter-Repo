from tkinter import *
import random
class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        point_list=[]
        WIDTH,HEIGHT=1000,1000
        
        self.geometry("1200x1000+10+10")
        self.title("Graphs")
        self.config(bg="Black")
        self.main_font=("Verdana",20)
        self.main_canvas=Canvas(width=WIDTH,height=HEIGHT,bg="White")
        self.main_canvas.place(x=0,y=0)
        self.ResetButton=Button(text="Reset",font=self.main_font,command=self.Reset)
        self.ResetButton.place(x=1025,y=500)
        for x in range(0,30):
            self.RandomPoint(self.main_canvas,point_list,WIDTH,HEIGHT)
        self.CalculateLengths(self.main_canvas,point_list)

    def CalculateLengths(self,canvas,pos_list):
        for x in canvas.find_all():
            pos_list.append([canvas.coords(x)[0],canvas.coords(x)[1]])
        pos_list.sort()
        #self.BunchOfLines(pos_list,canvas)
        self.BoggedClosest(pos_list,canvas)
        
    def Reset(self):
       self.destroy()
       self.__init__()

    def BoggedClosest(self,pos_list,canvas): #i think find_closest doesnt work properly. Might be smarter to just do a dictionary with distances in it
        for x,y in pos_list:
            a,b=canvas.coords(canvas.find_closest(x,y,halo=1000))[0],canvas.coords(canvas.find_closest(x,y,halo=1000))[1]
            print(a,b,x,y)
            canvas.create_line(x,y,a,b)

    def BunchOfLines(self,pos_list,canvas):
        for x,y in pos_list:
            for a,b in pos_list:
                canvas.create_line(x,y,a,b)

    def RandomPoint(self,canvas,point_list,width,height):
        generated_point=random.randint(0,width),random.randint(0,height)
        canvas.create_line(generated_point[0],generated_point[1],generated_point[0]+1,generated_point[1]+1)
window=MainWindow()
window.mainloop()


#find_closest(x,y,halo=5)
