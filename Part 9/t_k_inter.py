try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hell0 World")
mainWindow.geometry('640x480+8-200')

label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column= 0)

leftframe =tkinter.Frame(mainWindow)
leftframe.grid(row= 1, column=1)

canvas = tkinter.Canvas(leftframe, relief= "raised", borderwidth=1)
canvas.grid(row=1, column=0)

rightframe = tkinter.Frame(mainWindow)
rightframe.grid(row=1,column=2, sticky="n")

button1 = tkinter.Button(rightframe, text="button1")
button2 = tkinter.Button(rightframe, text="button2")
button3 = tkinter.Button(rightframe, text="button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# Configure columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftframe.config(relief='sunken', borderwidth=1)
rightframe.config(relief='sunken', borderwidth=1)
leftframe.grid(sticky='ns')
rightframe.grid(sticky='new')

rightframe.columnconfigure(0, weight=1)
button2.grid(sticky="new")
mainWindow.mainloop()
