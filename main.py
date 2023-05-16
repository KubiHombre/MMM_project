import tkinter as tk
import tkinter.messagebox as messagebox
import numpy as np
import math
import matplotlib.pyplot as plt


def pobierz_amplitude():
    global amplituda
    digit = par_wej.get()
    if digit.isdigit():
        amplituda = float(digit)
        amp_t.configure(text=f'Amplituda={amplituda}')
    else:
        messagebox.showerror("Error", "Wpisz poprawną wartość!!!")


def pobierz_okres():
    global okres
    global skok
    digit = par_wej.get()
    if digit.isdigit():
        okres = float(digit)
        skok = float(okres) / 100
        okr_t.configure(text=f'Okres={okres}')
    else:
        messagebox.showerror("Error", "Wpisz poprawną wartość!!!")


def pobierz_liczba_okresow():
    global liczba_okresow
    digit = par_wej.get()
    if digit.isdigit():
        liczba_okresow = float(digit)
        l_o_t.configure(text=f'Liczba okresów={liczba_okresow}')
    else:
        messagebox.showerror("Error", "Wpisz poprawną wartość!!!")


def pobierz_r():
    global R
    digit = par_ukladu.get()
    if digit.isdigit():
        R = float(digit)
        r_t.configure(text=f'R={R}')
    else:
        messagebox.showerror("Error", "Wpisz poprawną wartość!!!")


def pobierz_l():
    global L
    digit = par_ukladu.get()
    if digit.isdigit():
        L = float(digit)
        l_t.configure(text=f'L={L}')
    else:
        messagebox.showerror("Error", "Wpisz poprawną wartość!!!")


def pobierz_j():
    global J
    digit = par_ukladu.get()
    if digit.isdigit():
        J = float(digit)
        j_t.configure(text=f'J={J}')
    else:
        messagebox.showerror("Error", "Wpisz poprawną wartość!!!")


def pobierz_k():
    global k
    digit = par_ukladu.get()
    if digit.isdigit():
        k = float(digit)
        k_t.configure(text=f'k={k}')
    else:
        messagebox.showerror("Error", "Wpisz poprawną wartość!!!")


def pobierz_kt():
    global KT
    digit = par_ukladu.get()
    if digit.isdigit():
        KT = float(digit)
        kt_t.configure(text=f'KT={KT}')
    else:
        messagebox.showerror("Error", "Wpisz poprawną wartość!!!")


def tworzenie_syg_wej():
    global syg_wej
    global czas
    global skok

    syg_wej = np.array([])

    czas = np.linspace(0, okres * liczba_okresow, int(okres * liczba_okresow * 1000))
    print(len(czas))

    if rodzaj_pobudzenia.get() == 2:
        for i in range(0, len(czas)):
            syg_wej = np.append(syg_wej, amplituda * math.sin(czas[i] / okres * 2 * math.pi))
    if rodzaj_pobudzenia.get() == 1:
        f1 = 0
        f2 = -1
        p1 = 1
        p2 = 0
        okr = int(1000 * okres)
        for i in range(0, len(czas)):
            syg_wej = np.append(syg_wej,
                                4 * f1 * amplituda - amplituda * f2 * 4 * czas[i - p2 * okr] / okres - amplituda)
            if i == p1 * okres * 500:
                p1 += 1
                if f1 == 0:
                    f1 = 1
                    f2 = 1
                else:
                    p2 += 1
                    f1 = 0
                    f2 = -1
    if rodzaj_pobudzenia.get() == 0:
        f = 1
        p = 1
        for i in range(0, len(czas)):
            syg_wej = np.append(syg_wej, amplituda * f)
            if i == 500 * p * okres:
                p += 1
                if f == 1:
                    f = -1
                else:
                    f = 1


def wykres():
    tworzenie_syg_wej()
    plt.plot(czas, syg_wej)
    plt.axis([0, czas[len(czas) - 1], -1.05 * amplituda, 1.05 * amplituda])
    plt.show()


window = tk.Tk(className=' ')  # implementacja okna
window.geometry("777x395")  # ustawienie wielkości okna

# Parametry układu
skok = 0.001
R = 0.0
L = 0.0
J = 0.0
k = 0.0
KT = 0.0
amplituda = 1.0
okres = 1.0
liczba_okresow: float = 2.0
rodzaj_pobudzenia = tk.IntVar()
rodzaj_pobudzenia.set(0)
czas = np.array([])
syg_wej = np.array([])

# wstawienie obrazu układu
image = tk.PhotoImage(file="bmp.png")
pic = tk.Label(window, image=image)
pic.place(x=430, y=0)

# Ramki ozdobne
tk.LabelFrame(window, text="Wartości parametrów", width=430, height=80, bg='white').place(x=0, y=315)
tk.LabelFrame(window, text="Sygnał wejściowy", width=215, height=315, bg='white').place(x=0, y=0)
tk.LabelFrame(window, text="Parametry układu", width=215, height=315, bg='white').place(x=215, y=0)
tk.LabelFrame(window, text="Symulacja", width=347, height=135, bg='white').place(x=430, y=260)

# Przyciski do wyboru pobudzenia
tk.Radiobutton(window, state='normal', text='Prostokątny', variable=rodzaj_pobudzenia, bg='white', value=0) \
    .place(x=10, y=20)
tk.Radiobutton(window, state='normal', text='Trójkątny', variable=rodzaj_pobudzenia, bg='white', value=1) \
    .place(x=10, y=40)
tk.Radiobutton(window, state='normal', text='Harmoniczny', variable=rodzaj_pobudzenia, bg='white', value=2) \
    .place(x=10, y=60)

# okna wejściowe
par_wej = tk.Entry(window, bd=5, bg='#D3D3D3', width=30)
par_ukladu = tk.Entry(window, bd=5, bg='#D3D3D3', width=30)
par_wej.place(x=10, y=102)
par_ukladu.place(x=230, y=40)

# napisy
tk.Label(window, bg='white', text='Tu wpisz wartość:') \
    .place(x=3, y=80)
tk.Label(window, bg='white', text='Wybierz jaki parametr chcesz zmienić:') \
    .place(x=3, y=130)
tk.Label(window, bg='white', text='Wciśnij żeby narysować wykres:') \
    .place(x=3, y=250)
tk.Label(window, bg='white', text='Tu wpisz wartość:') \
    .place(x=218, y=15)
tk.Label(window, bg='white', text='Wybierz jaki parametr chcesz zmienić:') \
    .place(x=218, y=70)

# przyciski do ustawiania parametrów wejściowych
tk.Button(window, bg='#D3D3D3', text="Amplituda", command=pobierz_amplitude, width=13, height=2) \
    .place(x=3, y=150)
tk.Button(window, bg='#D3D3D3', text="Okres [s]", command=pobierz_okres, width=13, height=2) \
    .place(x=107, y=150)
tk.Button(window, bg='#D3D3D3', text="Liczba okresów", command=pobierz_liczba_okresow, width=28, height=2) \
    .place(x=3, y=195)
tk.Button(window, bg='#D3D3D3', text="Wykres sygnału wejściowego.", command=wykres, width=28, height=2) \
    .place(x=3, y=270)

# przyciski do ustawiania parametrów układu
tk.Button(window, bg='#D3D3D3', text="R", command=pobierz_r, width=28, height=2) \
    .place(x=220, y=270)
tk.Button(window, bg='#D3D3D3', text="L", command=pobierz_l, width=28, height=2) \
    .place(x=220, y=180)
tk.Button(window, bg='#D3D3D3', text="J", command=pobierz_j, width=28, height=2) \
    .place(x=220, y=90)
tk.Button(window, bg='#D3D3D3', text="k", command=pobierz_k, width=28, height=2) \
    .place(x=220, y=135)
tk.Button(window, bg='#D3D3D3', text="KT", command=pobierz_kt, width=28, height=2) \
    .place(x=220, y=225)

# Pokazywanie parametrów
r_t = tk.Label(window, text=f'R={R}', bg='white')
r_t.place(x=10, y=340)
l_t = tk.Label(window, text=f'L={L}', bg='white')
l_t.place(x=105, y=340)
j_t = tk.Label(window, text=f'J={J}', bg='white')
j_t.place(x=200, y=340)
k_t = tk.Label(window, text=f'k={k}', bg='white')
k_t.place(x=287, y=340)
kt_t = tk.Label(window, text=f'KT={KT}', bg='white')
kt_t.place(x=375, y=340)
okr_t = tk.Label(window, text=f'Okres={okres}', bg='white')
okr_t.place(x=10, y=360)
amp_t = tk.Label(window, text=f'Amplituda={amplituda}', bg='white')
amp_t.place(x=150, y=360)
l_o_t = tk.Label(window, text=f'Liczba okresów={liczba_okresow}', bg='white')
l_o_t.place(x=310, y=360)

# przyciski symulacja
tk.Button(window, bg='#D3D3D3', text="Wykres prądu płynącego w obwodzie.", width=47, height=3) \
    .place(x=434, y=276)
tk.Button(window, bg='#D3D3D3', text="Wykres prędkości kątowej wału.", width=47, height=3) \
    .place(x=434, y=335)


# główna pętla programu
window.mainloop()
