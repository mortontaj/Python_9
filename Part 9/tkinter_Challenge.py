# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

interface = [[('C', 1), ('CE', 1)],
             [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
             [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
             [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
             [('0', 1), ('=', 2), ('/', 1)],
             ]

calcWindow = tkinter.Tk()
calcWindow.title("Calculator")
calcWindow.geometry('640x480-8+200')
calcWindow['padx'] = 10

answer = tkinter.Entry(calcWindow)
answer.grid(row=0, column=0, sticky='nsew')

keypad = tkinter.Frame(calcWindow)
keypad.grid(row=1, column=0, sticky='nsew')

x_row = 0

for keyRow in interface:
    y_col = 0
    for key in keyRow:
        tkinter.Button(keypad, text=key[0]).grid(row=x_row, column=y_col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        y_col += key[1]
    x_row += 1

calcWindow.update()
calcWindow.minsize(keypad.winfo_width() + 10, answer.winfo_height() + keypad.winfo_height())
calcWindow.maxsize(keypad.winfo_width() + 10, answer.winfo_height() + keypad.winfo_height())

calcWindow.mainloop()
