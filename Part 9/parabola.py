import math
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


# modify the circle function that it allows the color of the
# circle to be specified and defaulted to red if a color is not
# given. You want to review the previous lecture about named
# parameters and default values
def circle(page, radius, g, h, color='red'):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(canvas, x, y):
    canvas.create_line(x, -y, x + 1, -y + 1, fill="red")


parawindow = tkinter.Tk()

parawindow.title("Parabola")
parawindow.geometry("640x480")

canvasj = tkinter.Canvas(parawindow, width=640, height=480, background='brown')
canvasj.grid(row=0, column=0)

draw_axes(canvasj)

parabola(canvasj, 100)
parabola(canvasj, 200)
# circle(canvasj, 100, 100, 100, 'green')
# circle(canvasj, 100, 100, -100)
# circle(canvasj, 100, -100, 100)
# circle(canvasj, 100, -100, -100)
# circle(canvasj, 10, 30, 30)
# circle(canvasj, 10, 30, -30, 'magenta')
# circle(canvasj, 10, -30, 30, 'purple')
# circle(canvasj, 10, -30, -30, 'yellow')
# circle(canvasj, 30, 0, 0, 'blue')

parawindow.mainloop()
