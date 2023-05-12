import tkinter as tk
import tkinter.ttk
import numpy as np


def get_digit():
    digit = entry.get()
    label.config(text=digit)
    if digit.isdigit():
        print("The entered digit is:", digit)
    else:
        print("Please enter a valid digit.")


window = tk.Tk()  # implementacja okna
window.geometry("1200x600")  # ustawienie wielkości okna

# Parametry układu
R = 0
L = 0
J = 0
k = 0
KT = 0
zmienna = ''

rodzaj_pobudzenia = tk.IntVar()
rodzaj_pobudzenia.set(0)

tk.Radiobutton(window, state='normal', text='Prostokątny', variable=rodzaj_pobudzenia, value=0).pack(anchor='nw', padx=0, pady=2)
tk.Radiobutton(window, state='active', text='Trójkątny', variable=rodzaj_pobudzenia, value=1).pack(anchor='nw', padx=0, pady=4)
tk.Radiobutton(window, state='normal', text='Harmoniczny', variable=rodzaj_pobudzenia, value=2).pack(anchor='nw', padx=0, pady=6)

entry = tk.Entry(window)
entry.pack()

label = tk.Label(window, text='halo')

button = tk.Button(window, text="Get Digit", command=get_digit)

entry.pack()
button.pack()
label.pack()

window.mainloop()
