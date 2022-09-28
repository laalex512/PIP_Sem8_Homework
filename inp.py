from imp import WriteInCsv, OnlyNewInCsv, ImportCsv
from keys import keys
from log import *
import tkinter as tk


# когда из главного окна нажимаем кнопку Внести вызывается эта функция
# создает новое окно с полями ввода (что мы хотим добавить) и своей кнопкой "Внести"
def ClickInput():
    global inputFields, labels, window
    window = tk.Tk()
    window.title("Внести нового человека")
    inputFields = []
    labels = []
    for i in range(len(keys)):
        labels.append(tk.Label(window, text=keys[i], font="times 15"))
        labels[i].grid(row=2, column=i)
        inputFields.append(tk.Entry(window, validate="focusout"))
        inputFields[i].grid(row=3, column=i)
    butInput = tk.Button(window, width=20, height=3,
                         text="Внести", command=lambda: ClickButtonInput())
    butInput.grid(row=4, column=1)


# Вызывается при нажатии "Внести". проверяет, чтобы все поля были введены
# и добавляет сотрудника. Если все поля совпадают с уже существующим в базе,
# все-равно выведет "успешно добавлен", но в базе ничего не поменяется  
# и вносим в лог)
def ClickButtonInput():
    data = []
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = inputFields[i].get()
    if "" not in dict.values():
        data.append(dict)
        WriteInCsv(data)
        LogInput(data)
        label = tk.Label(window, foreground="green",
                         text="Сотрудник успешно добавлен", font="times 15")
        label.grid(row=5, column=1)
    else:
        label = tk.Label(window, foreground="red",
                         text="Не все поля введены!!!", font="times 15")
        label.grid(row=5, column=1)
