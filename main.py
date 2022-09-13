import tkinter as tk
from random import randrange

win = tk.Tk()
canvas = tk.Canvas(win, height = 450, width = 600, bg= "black" )
canvas.pack()

voda = []
zem = []

pic_zem = tk.PhotoImage(file = "images\ostrov0.png")
pic_voda = tk.PhotoImage(file = "images\ostrov3.png")


def make_a_scene():
    global zem
    m = randrange(4,7)
    n = randrange(3,10)
    for stlp in range(0,n+1):
        for riadok in range(0, m+1):
            if randrange(5) == 2:
                temp = canvas.create_image(50 * riadok, 50*stlp, anchor= "nw", image = pic_zem)
                zem.append(temp)
            else:
                temp = canvas.create_image(50 * riadok, 50*stlp, anchor= "nw", image = pic_voda)
                voda.append(temp)
make_a_scene()
win.mainloop()
