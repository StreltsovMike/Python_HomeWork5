
from cgitb import text
from random import randint
from tkinter import *

def push(x):
    global count

    if count % 2 == 0:
        buttons[x].config(text="X", bg = '#e6f0ff', state='disabled')
        count += 1
        game[x] = 'x'
    else:
        buttons[x].config(text="0", bg = '#e6f0ff', state='disabled')
        count += 1 
        game[x] = 'o'
    if game[0] == game[1] == game[2] != None:
        Label(text=f'Победа {game[0]}', font=('Arial', 14, 'bold'), bg="#3399ff").grid(row=0, column=0, columnspan=3)
    if game[3] == game[4] == game[5] != None:
        Label(text=f'Победа {game[3]}', font=('Arial', 14, 'bold'), bg="#3399ff").grid(row=0, column=0, columnspan=3)
    if game[6] == game[7] == game[8] != None:
        Label(text=f'Победа {game[6]}', font=('Arial', 14, 'bold'), bg="#3399ff").grid(row=0, column=0, columnspan=3)
    if game[0] == game[4] == game[8] != None:
        Label(text=f'Победа {game[0]}', font=('Arial', 14, 'bold'), bg="#3399ff").grid(row=0, column=0, columnspan=3)
    if game[2] == game[4] == game[6] != None:
        Label(text=f'Победа {game[2]}', font=('Arial', 14, 'bold'), bg="#3399ff").grid(row=0, column=0, columnspan=3)
    if game[0] == game[3] == game[6] != None:
        Label(text=f'Победа {game[0]}', font=('Arial', 14, 'bold'), bg="#3399ff").grid(row=0, column=0, columnspan=3)
    if game[1] == game[4] == game[7] != None:
        Label(text=f'Победа {game[1]}', font=('Arial', 14, 'bold'), bg="#3399ff").grid(row=0, column=0, columnspan=3)
    if game[2] == game[5] == game[8] != None:
        Label(text=f'Победа {game[2]}', font=('Arial', 14, 'bold'), bg="#3399ff").grid(row=0, column=0, columnspan=3)


game = [None] * 9
count = 0
win = Tk()
win.title("X vs O") 
win.geometry("285x293+500+200")
win.resizable(False, False)
win.config(bg="#3399ff")
Label(text='', font=('Arial', 14, 'bold'), bg="#3399ff").grid(row=0, column=0, columnspan=3)

buttons = [Button(width=5, height=2, font=('Arial', 20, 'bold'), bg = '#cce0ff', command=lambda x=i: push(x)) for i in range(9)]

r = 1
c=0
for i in range(9):
    buttons[i].grid(row=r, column=c)
    c +=1
    if c == 3:
        r += 1
        c = 0

win.mainloop()