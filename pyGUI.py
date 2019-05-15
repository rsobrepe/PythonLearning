import tkinter

from tkinter import Tk
from tkinter import ttk
from tkinter import *

root = Tk()


'''
root.title("First GUI using python")
ttk.Button(root, text="Hello World").grid()
root.mainloop()


frame = Frame(root)
labelText = StringVar()

label = Label(frame, textvariable= labelText)
button = Button(frame, text="I am a button")

labelText.set("Hey! Whatsup")

label.pack()
button.pack()
frame.pack()

root.mainloop()


frame=Frame(root)
Label(frame, text="hi").pack()
Button(frame, text="b1").pack(side=LEFT, fill=Y)
Button(frame, text="b2").pack(side=RIGHT, fill=X)
Button(frame, text="b3").pack(side=TOP, fill=Y)
Button(frame, text="b4").pack(side=LEFT, fill=X)
Button(frame, text="b5").pack(side=RIGHT, fill=Y)

frame.pack()
root.mainloop()

'''

Label(root, text="Name").grid(row=0, column=0, sticky=N)
Entry(root, width=50).grid(row=0, column=1)
Button(root, text="submit").grid(row=0, column=5)

root.mainloop()

