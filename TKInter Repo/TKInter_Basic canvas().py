from tkinter import * #means import tkinter without having to call tkinter first to reach methods and variables stored under it
import os
window = Tk()
window.title("Canvas Test")
window.geometry("500x500+10+10")
window.config(bg= "#345")

canvas = Canvas(window, height=250, width=250, bg="#fff")
canvas.place(x=125,y=125) #new stuff to see if git saves it

#creating a rectangle in format topleftxcoord,topleftycoord,bottomrightxcoord,bottomrightycoord
canvas.create_rectangle(10,10,100,100,outline="Black",fill="Grey")


###creating an image
filepath=os.getcwd()
filepath=str(filepath)+"/image.png"
image=PhotoImage(file=filepath)
image=image.subsample(2,2) #divides image size by 2 in x and y axis - is limited to only integers so learn PIL for more detailed image modification
canvas.create_image(150,150,image=image)
###


###### importing in the button from the basic .place() script so that it can be drawn on top of the canvas
#button
def entry1IsPressed(): # a subroutine to be called when the button is pressed
    userinput=entry1.get()
    print(userinput)
button1 = Button(window, text = "Click me !", command=entry1IsPressed) #window to assign to, text inside of the button object
button1.place(x=275,y=140)
 
#entry
userinput=StringVar() #stringvar is a tkinter function that contains an entry in text format i think
entry1Font=("Comic Sans MS", 10) #defines the font to use inside of the entry
#order(master window, font, border size, background colour, foreground colour)
entry1=Entry(window, font=entry1Font, bd=2, bg="Dark Grey", fg="Dark Red")
entry1.place(x=150,y=320)



window.mainloop()
##
# IMPORTANT - save a file as .pyw instead of .py to prevent the command line from showing up when running in an executable