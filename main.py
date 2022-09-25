import tkinter as tk
from random import randrange

win = tk.Tk()
canvas = tk.Canvas(win, height = 450, width = 600, bg= "black" )
canvas.place(x=500, y=100)


voda = []
zem = []
most_v = []
most_z = []
mom_blue = True
pic_zem = tk.PhotoImage(file = "images\ostrov0.png")
pic_voda = tk.PhotoImage(file = "images\ostrov3.png")
b_kruh = tk.PhotoImage(file = "images\ostrov_kruh0.png")
h_kruh = tk.PhotoImage(file = "images\ostrov_kruh1.png")
v_most = tk.PhotoImage(file = "images\ostrov1.png")
z_most = tk.PhotoImage(file = "images\ostrov2.png")

penaze = 150

def klik(e):
    global penaze,money
    idecko = canvas.find_withtag("current")[0]
    x, y = canvas.coords(idecko)[0], canvas.coords(idecko)[1]
    if idecko in voda:
        canvas.delete(idecko)
        voda.remove(idecko)
        if mom_blue == True:
            temp = canvas.create_image(x, y, anchor="nw", image=v_most)
            most_v.append(temp)
            penaze -= 10
        else:
            temp = canvas.create_image(x, y, anchor="nw", image=pic_zem)
            zem.append(temp)
            penaze -= 50
    elif idecko in most_v and mom_blue == True:
        canvas.delete(idecko)
        most_v.remove(idecko)
        temp = canvas.create_image(x, y, anchor="nw", image=z_most)
        most_z.append(temp)
    elif idecko in most_z and mom_blue == True:
        canvas.delete(idecko)
        most_z.remove(idecko)
        temp = canvas.create_image(x, y, anchor="nw", image=v_most)
        most_v.append(temp)
    canvas.itemconfig(money,text=f"{penaze}")
    canvas.update()

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
    global penaze, money
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
    money = canvas.create_text(550, 50, text=f"{penaze}", fill="white", font=('Comicsans 20 bold'), anchor="ne")

win.bind("<Button-1>", klik)
make_a_scene()

canvas.pack()
win.mainloop()
