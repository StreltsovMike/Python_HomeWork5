import random, time
from tkinter import *

def push(x):
    global turn
    global game
    global game_left
    game[x] = 'x'
    buttons[x].config(text='x', state="disabled")
    game_left.remove(x)
    if x == 4 and turn == 0: 
        t = random.choice(game_left)
    elif x != 4 and turn == 0:
        t = 4
    if turn > 0:
        t = 8 - x
        if game[t] != None:
            t = random.choice(game_left)
        if (game[0] == game[2] != None) and (game[1] == None) :
            t = 1
        if (game[2] == game[8] != None) and (game[5] == None) :
            t = 5
        if (game[8] == game[6] != None) and (game[7] == None) :
            t = 7
        if (game[6] == game[0] != None) and (game[3] == None) :
            t = 3
    game[t] = 'o'
    time.sleep(0.3)
    buttons[t].config(text='o', state="disabled")
    game_left.remove(t)
    turn += 1

    if game[0] == game[1] == game[2] != None:
        Label(text=f'Победа {game[0]}', font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=3)
    if game[3] == game[4] == game[5] != None:
        Label(text=f'Победа {game[3]}', font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=3)
    if game[6] == game[7] == game[8] != None:
        Label(text=f'Победа {game[6]}', font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=3)
    if game[0] == game[4] == game[8] != None:
        Label(text=f'Победа {game[0]}', font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=3)
    if game[2] == game[4] == game[6] != None:
        Label(text=f'Победа {game[2]}', font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=3)
    if game[0] == game[3] == game[6] != None:
        Label(text=f'Победа {game[0]}', font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=3)
    if game[1] == game[4] == game[7] != None:
        Label(text=f'Победа {game[1]}', font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=3)
    if game[2] == game[5] == game[8] != None:
        Label(text=f'Победа {game[2]}', font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=3)

game = [None] * 9
game_left = list(range(9))
turn = 0
win = Tk()
win.title("X with O") 
win.geometry("285x293+500+200")
win.resizable(False, False)
win.config(bg="#fff2e6")
label1 = Label(text='', font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=3)

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