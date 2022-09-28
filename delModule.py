from imp import WriteInCsv, OnlyNewInCsv, ImportCsv
from keys import keys
from log import *
import tkinter as tk
import csv


def ClickDelete():
    global inputFields, labels, window
    window = tk.Tk()
    window.title("Удалить сотрудника")
    inputFields = []
    labels = []
    for i in range(len(keys)):
        labels.append(tk.Label(window, text=keys[i], font="times 15"))
        labels[i].grid(row=2, column=i)
        inputFields.append(tk.Entry(window, validate="focusout"))
        inputFields[i].grid(row=3, column=i)
    butInput = tk.Button(window, width=20, height=3,
                         text="Удалить", command=lambda: ClickButtonDelete())
    butInput.grid(row=4, column=1)


def ClickButtonDelete():
    data = []
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = inputFields[i].get()
    if "" not in dict.values():
        data.append(dict)
        DeleteFromCsv(dict)
    else:
        label = tk.Label(window, foreground="red",
                         text="Не все поля введены!!!", font="times 15")
        label.grid(row=5, column=1)


def DeleteFromCsv(dictForDelete, path="data.csv"):
    if dictForDelete in ImportCsv(path):
        data = list(filter(lambda x: x != dictForDelete, ImportCsv(path)))
        with open(path, 'w', encoding="UTF-8") as f:
            f.truncate()
        WriteInCsv(data)
        LogDelete(dictForDelete)
        label = tk.Label(window, foreground="green",
                         text="Сотрудник успешно удален", font="times 15")
        label.grid(row=5, column=1)
    else:
        label = tk.Label(window, foreground="red",
                         text="Такого сотрудника нет", font="times 15")
        label.grid(row=5, column=1)
