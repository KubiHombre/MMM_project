import tkinter as tk
import tkinter.ttk
import numpy as np


def pobierz_amplitude():
    global amplituda
    digit = entry.get()
    if digit.isdigit():
        print("Amplituda=", digit)
        amplituda = digit
    else:
        print("Please enter a valid digit.")


def pobierz_okres():
    global okres
    digit = entry.get()
    if digit.isdigit():
        print("Okres=", digit)
        okres = digit
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
amplituda = 0
okres = 0
zmienna = ''

rodzaj_pobudzenia = tk.IntVar()
rodzaj_pobudzenia.set(0)

tk.Radiobutton(window, state='normal', text='Prostokątny', variable=rodzaj_pobudzenia, value=0).place(x=0, y=0)
tk.Radiobutton(window, state='active', text='Trójkątny', variable=rodzaj_pobudzenia, value=1).place(x=0, y=20)
tk.Radiobutton(window, state='normal', text='Harmoniczny', variable=rodzaj_pobudzenia, value=2).place(x=0, y=40)

entry = tk.Entry(window)

tk.Button(window, text="Amplituda", command=pobierz_amplitude, width=10, height=2).place(x=0, y=130)
tk.Button(window, text="Okres [rad]", command=pobierz_amplitude, width=10, height=2).place(x=90, y=130)

entry.place(x=0, y=100)

window.mainloop()
