from random import randint
import tkinter as tk

def minus():
    global all_taken_candies
    minus_candies = number1.get()
    minus_candies = int(minus_candies)
    if (minus_candies > 0) & (minus_candies <= 28):
        all_taken_candies += minus_candies
        candies = 2021 - all_taken_candies
        label2['text'] = f"{candies}"
        label3['text'] = f"Player : -{minus_candies}"
        number1.delete(0,"end")
        if candies <=0:
            label3['text'] = f"Player : WIN"
            label4['text'] = f"Bot : LOSE"
    else:
        label3['text'] = f"Введите от 1 до 28"
        minus()
    #BOT
    minus_candies = randint(1,28)
    if (candies > 29) & (candies <58):
        minus_candies = all_taken_candies - 29
    if (candies <= 28):
        minus_candies = candies
    all_taken_candies += minus_candies
    candies = 2021 - all_taken_candies
    label2['text'] = f"{candies}"
    label4['text'] = f"Bot : -{minus_candies}"
    number1.delete(0,"end")
    if candies <=0:
        label3['text'] = f"Player : LOSE"
        label4['text'] = f"Bot : WIN"

all_taken_candies = 0 
window = tk.Tk() 
window.title(" Конфееееты!") 
window.geometry("500x500+500+200")
window.resizable(False, False)
photo = tk.PhotoImage(file='game-icon.png')
window.config(bg="#fff2e6")
window.iconphoto(False, photo)
label1 = tk.Label(window, text="Привет!\nЭто игра в Конфеты)",
                font=('Courier New', 20, 'bold'),
                fg="#ff9933",
                bg="#fff2e6")
label1.pack()
label2_1 = tk.Label(window, text="На столе лежит 2021 конфета.\nПервый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.\nПобеждает тот кто забрал последние конфеты.",
                font=('Courier New', 12, 'bold'),
                fg="#ff9933",
                bg="#fff2e6")
label2_1.pack()
label2 = tk.Label(window, text=f"2021",
                font=('Courier New', 32, 'bold'),
                fg="#ff9933",
                bg="#fff2e6")
label2.pack()
all_taken_candies = 0  
btn2 = tk.Button(window, text=f"Ввод",
                 font=('Courier New', 12, 'bold'),
                fg="#ff9933",
                bg="#ffe6cc",
                command=minus) 
number1 = tk.Entry(window)
number1.pack()
btn2.pack()   
label3 = tk.Label(window, text=f"",
                font=('Courier New', 32, 'bold'),
                fg="#ff9933",
                bg="#fff2e6")
label3.pack()
label4 = tk.Label(window, text=f"",
                font=('Courier New', 32, 'bold'),
                fg="#ff9933",
                bg="#fff2e6")
label4.pack()
btn2.pack()   

window.mainloop()