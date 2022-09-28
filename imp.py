import csv
import tkinter as tk
from keys import keys
from log import *

def ClickImport():
    window = tk.Tk()
    window.title("Импорт из файла CSV")
    window.geometry("300x130")
    label = tk.Label(window, text="Path:", font="times 15")
    label.grid(row=0, column=1)
    global inputField
    inputField = tk.Entry(window, width=50, validate="focusout")
    inputField.grid(row=1, column=1)
    butImport = tk.Button(window, width=20, height=3,
                          text="Внести", command=lambda: ClickButtonImport())
    butImport.grid(row=2, column=1, pady=15)


def ClickButtonImport():
    path = str(inputField.get())
    WriteInCsv(ImportCsv(path))
    LogImport(path)


def ImportCsv(path):
    with open(path, encoding="UTF-8") as f:
        data = list(csv.DictReader(f, delimiter=" "))
    return data


def WriteInCsv(data, path="data.csv"):
    with open(path, 'a', encoding="UTF-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(
            data[0].keys()), delimiter=" ")
        try:
            if ImportCsv(path)[0] == 0:
                writer.writeheader()
        except:
            writer.writeheader()
        for d in OnlyNewInCsv(data):
            writer.writerow(d)


def OnlyNewInCsv(data, path="data.csv"):
    alreadyExist = ImportCsv(path)
    return [d for d in data if d not in alreadyExist]
