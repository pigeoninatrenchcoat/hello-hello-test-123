import tkinter as tk
from random import randrange

win = tk.Tk()
canvas = tk.Canvas(win, height = 450, width = 600, bg= "black" )
canvas.place(x=500, y=100)
canvas.pack()


voda = []
zem = []
mom_blue = True
pic_zem = tk.PhotoImage(file = "images\ostrov0.png")
pic_voda = tk.PhotoImage(file = "images\ostrov3.png")
b_kruh = tk.PhotoImage(file = "images\ostrov_kruh0.png")
h_kruh = tk.PhotoImage(file = "images\ostrov_kruh1.png")

def klik(e):
    print("klik klik")
    idecko = canvas.find_withtag("current")[0]
    if canvas.itemcget(idecko,"tag") == "voda":
        canvas.delete(idecko)
    print(idecko)

def dze_si(e):
    print("tu som",e.x, e.y)


def zmen_kruh():
    global kruh, mom_blue
    if mom_blue == True:
        kruh.config(image= h_kruh)
        mom_blue = False
    else:
        kruh.config(image=b_kruh)
        mom_blue = True

kruh = tk.Button(image=b_kruh, command=zmen_kruh, borderwidth=0)

#tag_binfd a also tagy existuju

def make_a_scene():
    global zem
    m = randrange(4,7)
    n = randrange(3,10)
    for stlp in range(n):
        for riadok in range(m):
            if randrange(5) == 2:
                temp = canvas.create_image(50 * riadok, 50*stlp, anchor= "nw", image = pic_zem,tag = "zem_zase")
                zem.append(temp)
            else:
                temp = canvas.create_image(50 * riadok, 50*stlp, anchor= "nw", image = pic_voda, tag = "voda")
                voda.append(temp)
    kruh.place(x=500, y=100)

make_a_scene()

win.bind("<Button-1>", klik)
win.bind("<Motion>", dze_si)

win.mainloop()

#hello
