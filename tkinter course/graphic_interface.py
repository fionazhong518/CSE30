from tkinter import *
from PIL import ImageTk, Image # built-in image function

root = Tk()
root.title('graphic interface')
#root.iconbitmap('CS 30/tkinter course/noodle.ico') #why it doesnt work?

# using images
my_img = ImageTk.PhotoImage(Image.open("gui/bg_1.png")) # why it doesnt work ?
my_label = Label(image= my_img)
my_label.pack()

button_quit = Button(root, text = 'Exit Program', command = root.quit)
button_quit.pack()

root.mainloop()