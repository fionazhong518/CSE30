'''

'''
from tkinter import *

root = Tk()
#                          ,fg = (text color), bg = (background color)
e = Entry(root, width = 50,borderwidth=5) # entry wedge (text box)
e.pack()
e.insert(0, "Enter Your Name: ") # put default text inside the text box

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

#create button                             , padx = ,pady= (button size), command = (what would happen when clicked)
myButton = Button(root, text = "Enter Your Stock Quote", command=myClick, fg= "blue", bg = "#000000")
myButton.pack()
root.mainloop()
