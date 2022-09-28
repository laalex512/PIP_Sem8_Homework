import tkinter as tk
from keys import keys
from inp import *
from imp import ClickImport
from exp import *
from delModule import *


def start():
    global window
    window = tk.Tk()
    window.geometry("800x150")
    but1 = tk.Button(window, width=20, height=5,
                     text="Импорт из файла CSV", command=lambda: ClickImport())
    but1.grid(row=1, column=1)
    but2 = tk.Button(window, width=30, height=5,
                     text="Внести нового человека", command=lambda: ClickInput())
    but2.grid(row=1, column=3)
    but3 = tk.Button(window, width=30, height=5,
                     text="Получить отфильтрованные сведения", command=lambda: ClickOutput())
    but3.grid(row=1, column=5)
    but4 = tk.Button(window, width=30, height=5,
                     text="Удалить одну запись", command=lambda: ClickDelete())
    but4.grid(row=1, column=7)
    window.mainloop()
