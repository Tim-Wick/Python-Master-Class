# try:
import tkinter
# except ImportError: # python 2
#     import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("This is my test")
mainWindow.geometry("640x480-50-50")

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side="top")

leftFrame = tkinter.Frame(mainWindow, relief="raised", borderwidth=3)
leftFrame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=2)
canvas.pack(side="left", anchor="n")

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side="right", anchor="n", expand=True)

button1 = tkinter.Button(rightFrame, text="button 1")
button2 = tkinter.Button(rightFrame, text="button 2")
button3 = tkinter.Button(rightFrame, text="button 3")
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")
### pack>anchor. If button is packed to left, anchor can only effect vertical positioning.###



mainWindow.mainloop()

====================================================================================================

import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("This is my test")
mainWindow.geometry("640x480-50-50")

label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=2)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky="n")

button1 = tkinter.Button(rightFrame, text="button 1")
button2 = tkinter.Button(rightFrame, text="button 2")
button3 = tkinter.Button(rightFrame, text="button 3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
### pack>anchor. If button is packed to left, anchor can only effect vertical positioning.###


###Configure the columns###
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
###columnconfigure calls grid_columnconfigure. Both are valid, one uses less typing :)###
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief="sunken", borderwidth=1)
rightFrame.config(relief="sunken", borderwidth=1)
leftFrame.grid(sticky="ns")
rightFrame.grid(sticky="new")

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky="ew")

mainWindow.mainloop()
