### My Solution ###

import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry("300x200+400+400")
mainWindow["padx"] = 8
mainWindow.update_idletasks()
height = mainWindow.winfo_height()
width = mainWindow.winfo_width()
mainWindow.minsize(height, width)

### Display Window ###
display = tkinter.Entry(mainWindow)
display.grid(row=0, column=0, columnspan=4, stick="ew")


### Buttons ###
button_list = ["C", "CE", 7, 8, 9, "+", 4, 5, 6, "-", 1, 2, 3, "*", 0, "=", "/", "", ""]
current_button = 0
for i in range(1, 6):
    for x in range(0, 4):
        if i == 1 and x == 2:
            continue
        elif i == 1 and x == 3:
            continue
        else:
            button = tkinter.Button(mainWindow, relief="raised", bd=2, width=5, height=2, text=button_list[current_button])
            button.grid(row=i, column=x, sticky="new")
            current_button += 1
        
mainWindow.mainloop()

=====================================================================================================

###Course Solution###

import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("300x200+400+400")
mainWindow["padx"] = 8
mainWindow.update_idletasks()
height = mainWindow.winfo_height()
width = mainWindow.winfo_width()
mainWindow.minsize(height, width)


keys = [[("C", 1), ("CE", 1)],
        [("7", 1), ("8", 1), ("9", 1), ("+", 1)],
        [("4", 1), ("5", 1), ("6", 1), ("-", 1)],
        [("1", 1), ("2", 1), ("3", 1), ("*", 1)],
        [("0", 1), ("=", 1), ("/", 1)]]

### Display Window ###
display = tkinter.Entry(mainWindow)
display.grid(row=0, column=0, columnspan=4, stick="ew")

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky="nsew")

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1



mainWindow.mainloop()
