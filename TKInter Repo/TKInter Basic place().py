#imports all methods and variables used from tkinter
from tkinter import *
# creating Tk window
window1 = Tk()
 
#title
window1.title("My Window 1") #defines the name of the window to create

#button
def entry1IsPressed(): # a subroutine to be called when the button is pressed
    userinput=entry1.get()
    print(userinput)
button1 = Button(window1, text = "Click me !", command=entry1IsPressed) #window to assign to, text inside of the button object
button1.place(x=75,y=20)
 
#entry
userinput=StringVar() #stringvar is a tkinter function that contains an entry in text format i think
entry1Font=("Comic Sans MS", 15) #defines the font to use inside of the entry
#order(master window, font, border size, background colour, foreground colour)
entry1=Entry(window1, font=entry1Font, bd=5, bg="Dark Grey", fg="Dark Red")
entry1.place(x=75,y=50)

# label
label1 = Label(window1, text = "I'm a Label", relief="groove") #relief types flat,solid,raised,sunken,ridge,groove
label1.place(x=10,y=25)
  

# setting geometry of tk window
window1.geometry("400x100+10+10")#defines window as 225x200 with a distance from top left of 10,10
  
#run the tkinter window
mainloop()