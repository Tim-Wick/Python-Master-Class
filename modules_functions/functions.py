def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(something):
    ### Converts something to a string so function can work on numbers ###
    something = str(something)
    left_margin = (80 - len(something)) // 2
    print(" " * left_margin, something)


center_text("Spam and eggs")
center_text("Spam spam spam and spam")
center_text(443)


def print_all(*args, sep=" ", end_char="\n", center_file=None, flush_me=False):
    arg = ""
    for i in args:
        arg += str(i) + sep
    print(arg, end=end_char, file=center_file, flush=flush_me)


with open("print_all", mode="w") as printed_file:
    print_all("Print", "this", "and", "also", "this", 77, sep=":", center_file=printed_file)


def print_all(*args):
    arg = ""
    for i in args:
        arg += str(i)
    return arg

print(print_all("Print", "this", "and", "also", "this", 77))

def print_all(*args):
    arg = ""
    for i in args:
        arg += str(i)
    return arg

s1 = print_all("Print", "this", "and", "also", "this", 77)
print(s1)


=============================================================================================

import tkinter


# Function to draw parabola
def parabola(x):
    y = x * x / 100
    return y


# Function to draw axis on a canvas in tkinter
def draw_axis(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, -y_origin, 0, y_origin, fill="black")


# Function to plot parabola
def plot(canvas, x, y):
    canvas.create_line(x, y, x+1, y+1, fill="red")


my_window = tkinter.Tk()

my_window.title("Parabola")
my_window.geometry("640x480")

my_canvas = tkinter.Canvas(my_window, width=320, height=480)
my_canvas.grid(row=0, column=0)

my_canvas2 = tkinter.Canvas(my_window, width=320, height=480, background="blue")
my_canvas2.grid(row=0, column=1)

print(repr(my_canvas), repr(my_canvas2))
draw_axis(my_canvas)
draw_axis(my_canvas2)

for q in range(-100, 101):
    z = parabola(q)
    plot(my_canvas, q, -z)


my_window.mainloop()

===============================================================================================================

import tkinter
import math


# Function to draw parabola
def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


# Function to draw circle
def circle(page, radius, g, h):
    for x in range(g * 100, (g + radius) * 100):
        x /= 100
        y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
        plot(page, x, y)
        plot(page, x, 2 * h - y)
        plot(page, 2 * g - x, y)
        plot(page, 2 * g - x, 2 * h - y)


# Function to draw axis on a canvas in tkinter
def draw_axis(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, -y_origin, 0, y_origin, fill="black")


# Function to plot parabola
def plot(canvas, x, y):
    canvas.create_line(x, -y, x+1, -y+1, fill="red")


my_window = tkinter.Tk()

my_window.title("Parabola")
my_window.geometry("640x480")

my_canvas = tkinter.Canvas(my_window, width=640, height=480)
my_canvas.grid(row=0, column=0)

draw_axis(my_canvas)

parabola(my_canvas, 100)
parabola(my_canvas, 200)
circle(my_canvas, 100, 0, 0)
circle(my_canvas, 100, 100, 0)
circle(my_canvas, 100, -100, 0)
circle(my_canvas, 100, -50, 50)
circle(my_canvas, 100, 50, 50)


my_window.mainloop()

=======================================================================================================

import tkinter
import math


# Function to draw parabola
def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


# Function to draw circle
def circle(page, radius, g, h, color="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)

    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


# Function to draw axis on a canvas in tkinter
def draw_axis(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, -y_origin, 0, y_origin, fill="black")


# Function to plot parabola
def plot(canvas, x, y):
    canvas.create_line(x, -y, x+1, -y+1, fill="red")


my_window = tkinter.Tk()

my_window.title("Parabola")
my_window.geometry("640x480")

my_canvas = tkinter.Canvas(my_window, width=640, height=480)
my_canvas.grid(row=0, column=0)

draw_axis(my_canvas)

circle(my_canvas, 100, -100, 0)
circle(my_canvas, 100, 100, 0, "blue")



my_window.mainloop()

