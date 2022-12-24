
from tkinter import *
from PIL import ImageTk, Image # built-in image function

root = Tk()
root.title("radio buttons")
root.iconbitmap("gui/noodle.ico")

#r = IntVar()#interger, if want to call string, StringVal()
#r.set("2") # then 2 would be selected auto

TOPPING = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPING: #loop through TOPPING, take each text and topping(print out) variables
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W) #anchor(allign) to the West


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()
#                                                      pass in function using lambda, and pass variable 
#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda:clicked(r.get())).pack()

#myLabel = Label(root, text=r.get()) #set number and would sutomatically get 
#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

# by click it each time, it would print the passed-in value in clicked()
myButton = Button(root, text="click me!", command=lambda:clicked(pizza.get())) 
myButton.pack()

mainloop()
