from random import randint
import tkinter as tk

def minus():
    btn1['text'] = 'Ввод'
    global count
    global count_person
    if count_person == 0:
        label2_2['text'] = f"Начинает игрок 1"
    elif count_person == 1:
        label2_2['text'] = "Начинает игрок 2"
    if count_person % 2 == 0:
        minus_mum = number1.get()
        minus_mum = int(minus_mum)
        if (minus_mum > 0) & (minus_mum <= 28):
            count += minus_mum
            perem = 2021 - count
            label2['text'] = f"{perem}"
            label3['text'] = f"Player 1 : -{minus_mum}"
            number1.delete(0,"end")
            label2_2['text'] = f""
            count_person += 1
            if perem <=0:
                label3['text'] = f"Player 1 : WIN"
                label4['text'] = f"Player 2 : LOSE"
        else:
            label3['text'] = f"Введите от 1 до 28"
            label2_2['text'] = f""
    else:
        minus_mum = number1.get()
        minus_mum = int(minus_mum)
        if (minus_mum > 0) & (minus_mum <= 28):
            count += minus_mum
            perem = 2021 - count
            label2['text'] = f"{perem}"
            label4['text'] = f"Player 2 : -{minus_mum}"
            number1.delete(0,"end")
            label2_2['text'] = f""
            count_person += 1
            if perem <=0:
                label3['text'] = f"Player 1 : LOSE"
                label4['text'] = f"Player 2 : WIN"
        else:
            label4['text'] = f"Введите от 1 до 28"
            label2_2['text'] = f""


count_person = randint(0,1)
count = 0
window = tk.Tk() 
window.title(" Конфееееты!") 
window.geometry("600x500+500+200")
window.resizable(False, False)
photo = tk.PhotoImage(file='game-icon.png')
window.config(bg="#fff2e6")
window.iconphoto(False, photo)
label1 = tk.Label(window, text="Привет!\nЭто игра в Конфеты)",
                font=('Courier New', 20, 'bold'),
                fg="#ff9966",
                bg="#fff2e6")
label1.pack()
label2_1 = tk.Label(window, text="На столе лежит 2021 конфета.\nПервый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.\nПобеждает тот, кто забрал последние конфеты.",
                font=('Courier New', 12, 'bold'),
                fg="#ff9933",
                bg="#fff2e6")
label2_1.pack()
label2_2 = tk.Label(window, text="",
                font=('Courier New', 16, 'bold'),
                fg="#ff9933",
                bg="#fff2e6")
label2_2.pack()
label2 = tk.Label(window, text=f"2021",
                font=('Courier New', 32, 'bold'),
                fg="#ff9966",
                bg="#fff2e6")
label2.pack()

count = 0  
btn1 = tk.Button(window, text=f"Start",
                 font=('Courier New', 12, 'bold'),
                fg="#ff9933",
                bg="#ffe6cc",
                height=1,
                width=8,
                command=minus) 
number1 = tk.Entry(window,width = 40)
number1.pack()
btn1.pack()   
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
btn1.pack()   


window.mainloop()