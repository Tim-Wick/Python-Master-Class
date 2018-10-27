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
