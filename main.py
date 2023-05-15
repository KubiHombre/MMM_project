import tkinter as tk
import numpy as np
import math
import matplotlib.pyplot as plt


def pobierz_amplitude():
    global amplituda
    digit = entry.get()
    if digit.isdigit():
        print("Amplituda=", digit)
        amplituda = float(digit)
    else:
        print("Please enter a valid digit.")


def pobierz_okres():
    global okres
    global skok
    digit = entry.get()
    if digit.isdigit():
        print("Okres=", digit)
        okres = float(digit)
        skok = float(okres)/100
    else:
        print("Please enter a valid digit.")


def pobierz_liczba_okresow():
    global liczba_okresow
    digit = entry.get()
    if digit.isdigit():
        print("Liczba okresów=", digit)
        liczba_okresow = float(digit)
    else:
        print("Please enter a valid digit.")


def tworzenie_syg_wej():
    global syg_wej
    global czas

    syg_wej = np.array([])

    czas = np.linspace(0, okres*liczba_okresow, int(okres*liczba_okresow*1000))

    i = 0.0

    if rodzaj_pobudzenia.get() == 2:
        for i in range(0, len(czas)):
            syg_wej = np.append(syg_wej, amplituda * math.sin(czas[i]/okres * 2 * math.pi))
    if rodzaj_pobudzenia.get() == 1:
        while i < liczba_okresow:
            n = 0.0
            while n < okres:
                if n < (okres/2):
                    syg_wej = np.append(syg_wej, amplituda * 4 * n - amplituda)
                if n > (okres/2):
                    syg_wej = np.append(syg_wej, 4 * amplituda-amplituda * 4 * n - amplituda)
                n += skok
            i += 1
    if rodzaj_pobudzenia.get() == 0:
        while i < liczba_okresow:
            m = 0.0
            while m < okres:
                if m < okres/2:
                    syg_wej = np.append(syg_wej, amplituda)
                else:
                    syg_wej = np.append(syg_wej, -amplituda)
                m += skok
            i += 1


def wykres():
    tworzenie_syg_wej()
    plt.plot(czas, syg_wej)
    print(len(czas))
    plt.axis([0, czas[len(czas)-1], -1.05*amplituda, 1.05*amplituda])
    plt.show()


window = tk.Tk()  # implementacja okna
window.geometry("1200x600")  # ustawienie wielkości okna

# Parametry układu
skok = 0.001
R = 0
L = 0
J = 0
k = 0
KT = 0
amplituda = 1.0
okres = 1.0
liczba_okresow: float = 2.0
rodzaj_pobudzenia = tk.IntVar()
rodzaj_pobudzenia.set(0)
czas = np.array([])
syg_wej = np.array([])


tk.Radiobutton(window, state='normal', text='Prostokątny', variable=rodzaj_pobudzenia, value=0).place(x=0, y=0)
tk.Radiobutton(window, state='normal', text='Trójkątny', variable=rodzaj_pobudzenia, value=1).place(x=0, y=20)
tk.Radiobutton(window, state='normal', text='Harmoniczny', variable=rodzaj_pobudzenia, value=2).place(x=0, y=40)

entry = tk.Entry(window)

tk.Button(window, text="Amplituda", command=pobierz_amplitude, width=10, height=2).place(x=1, y=130)
tk.Button(window, text="Okres [s]", command=pobierz_amplitude, width=10, height=2).place(x=92, y=130)
tk.Button(window, text="Liczba okresów", command=pobierz_liczba_okresow, width=23, height=2).place(x=1, y=180)
tk.Button(window, text="wykres", command=wykres, width=23, height=2).place(x=500, y=500)

entry.place(x=0, y=100)

window.mainloop()
