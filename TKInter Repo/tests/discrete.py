from tkinter import *
import random
from math import *
import time
class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        point_list=[]
        WIDTH,HEIGHT=1000,1000
        self.POSITION_NUMBER=250
        self.geometry("1200x1000+10+10")
        self.title("Graphs")
        self.config(bg="Black")
        self.main_font=("Verdana",20)
        self.main_canvas=Canvas(width=WIDTH,height=HEIGHT,bg="#1C1C1C")
        self.main_canvas.place(x=0,y=0)
        self.ResetButton=Button(text="Reset",font=self.main_font,command=self.Reset)
        self.ResetButton.place(x=1025,y=500)
        for x in range(0,self.POSITION_NUMBER):
            self.RandomPoint(self.main_canvas,point_list,WIDTH,HEIGHT)
        self.CalculatePositions(self.main_canvas,point_list)

    def CalculatePositions(self,canvas,pos_list):
        for x in canvas.find_all():
            pos_list.append([canvas.coords(x)[0],canvas.coords(x)[1]])
        pos_list.sort()
        self.distance_table=self.GetDistanceTable(pos_list,canvas)
        lines=self.MainPrimming(self.distance_table)
        self.DrawLines(lines,pos_list,canvas)

    def DrawLines(self,line_list,pos,canvas):
        for a,b in line_list:
            canvas.create_line(pos[a][0],pos[a][1],pos[b][0],pos[b][1],fill="#FDFFFC")
    
    def GetDistanceTable(self,pos_list,canvas):
        distance_table=[]
        for x,y in pos_list:
            current_distance_list=[]
            for a,b in pos_list:                
                height,width=abs(y-b),abs(x-a)
                distance=sqrt((height**2)+(width**2))
                distance=696969 if distance==0 else distance
                current_distance_list.append(distance)
            distance_table.append(current_distance_list)
        return distance_table

    def MainPrimming(self,distance_table):
        lines_to_draw=[]
        reformatting=[]
        for list in distance_table:
            for item in list:
                reformatting.append(item)
        distance_table=reformatting
        checklist=[]
        for x in range(len(distance_table)):
            checklist.append(696969)
        checklist[0:self.POSITION_NUMBER]=distance_table[0:self.POSITION_NUMBER]
        for x in range(0,self.POSITION_NUMBER-1):
            smallest_num=min(checklist) #finds smallest out of used nodes
            row=checklist.index(smallest_num) 
            column=row//self.POSITION_NUMBER
            row=row-column*self.POSITION_NUMBER
            #print("ROW",row,"COLUMN",column,"smallest_num",round(smallest_num))
            distance_table[row*self.POSITION_NUMBER+column]=696969
            for x in range(0,len(distance_table)//self.POSITION_NUMBER):
                if row==0:
                    distance_table[column]=696969
                else:
                    distance_table[x*self.POSITION_NUMBER+row]=696969
            for x in range(0,len(checklist)//self.POSITION_NUMBER):
                if row==0:
                    checklist[x]=696969
                else:
                    checklist[x*self.POSITION_NUMBER+row]=696969
            lines_to_draw.append([row,column])
            for item in distance_table[self.POSITION_NUMBER:2*self.POSITION_NUMBER]:
                checklist[row*self.POSITION_NUMBER:(row+1)*self.POSITION_NUMBER]=distance_table[row*self.POSITION_NUMBER:(row+1)*self.POSITION_NUMBER]
       # print(lines_to_draw)
        return lines_to_draw
    
    def EqualChecker(self,list_to_check):
        result=all(element==list_to_check[0] for element in list_to_check)
        if(result):
            return True
        else:
            return False

    def Reset(self):
       self.destroy()
       self.__init__()

    def BoggedClosest(self,pos_list,canvas):
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

