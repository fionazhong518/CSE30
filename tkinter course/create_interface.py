'''
Name: Tkinter course
author: Fiona Zhong
date created: 2022-02-04
'''
from tkinter import *

root  = Tk() # have to present before everything

# creating a Label Widget
myLabel1 = Label(root, text = "Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text = 'My name is ...').grid(row=1, column=5)
myLabel3 = Label(root, text = '0o0').grid(row=1, column=1)

'''
# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)
'''
#myLabel.pack()


root.mainloop() # create grahpic interface