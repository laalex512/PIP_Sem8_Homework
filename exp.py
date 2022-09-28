from imp import ImportCsv
import csv
import tkinter as tk
from keys import keys
from log import *


def ClickOutput():
    global inputFields, labels, window
    window = tk.Tk()
    window.title("Получить отфильтрованные сведения")
    inputFields = []
    labels = []
    for i in range(len(keys)):
        labels.append(tk.Label(window, text=keys[i], font="times 15"))
        labels[i].grid(row=2, column=i)
        inputFields.append(tk.Entry(window, validate="focusout"))
        inputFields[i].grid(row=3, column=i)
    butOutput = tk.Button(window, width=20, height=3,
                          text="Получить", command=lambda: ClickButtonOutput())
    butOutput.grid(row=4, column=1)


def ClickButtonOutput():
    dict = {}
    alreadyInput = False
    for i in range(len(keys)):
        dict[keys[i]] = inputFields[i].get()
        if dict[keys[i]] != "":
            OutputDataInCsv(keys[i], dict[keys[i]])
            LogOutput(keys[i], dict[keys[i]])
            label = tk.Label(window, foreground="green",
                             text="Сведения успешно добавлены", font="times 15")
            label.grid(row=5, column=1)
            alreadyInput = True
    if not alreadyInput:
        label = tk.Label(window, foreground="red",
                         text="Ни одно поле не введено!!!", font="times 15")
        label.grid(row=5, column=1)


def OutputDataInCsv(key, value, path="data.csv", outPath="output.csv"):
    data = ImportCsv(path)
    with open(outPath, 'w', encoding="UTF-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(
            data[0].keys()), delimiter=' ')
        writer.writeheader()
        count = 0
        for d in data:
            if d[key] == value:
                writer.writerow(d)
                count += 1
        if count == 0:
            f.write("No values for this key")
