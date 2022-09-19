import tkinter as tk
from random import randrange

win = tk.Tk()
canvas = tk.Canvas(win, height = 450, width = 600, bg= "black" )
canvas.pack()


voda = []
zem = []
mom_blue = True
pic_zem = tk.PhotoImage(file = "images\ostrov0.png")
pic_voda = tk.PhotoImage(file = "images\ostrov3.png")
b_kruh = tk.PhotoImage(file = "images\ostrov_kruh0.png")
h_kruh = tk.PhotoImage(file = "images\ostrov_kruh1.png")

def callback():
    print("yup")

def zmen_kruh():
    global kruh, mom_blue
    if mom_blue == True:
        kruh.config(image= h_kruh)
        mom_blue = False
    else:
        kruh.config(image=b_kruh)
        mom_blue = True

kruh = tk.Button(image=b_kruh, command=zmen_kruh, borderwidth=0)

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
    kruh.place(x=500, y=100)
canvas.bind("<Button-1>", callback())

make_a_scene()
win.mainloop()
