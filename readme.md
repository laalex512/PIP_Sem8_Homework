Модули inp, imp, exp, delModule - содержат функции для открытия отдельного окна интерфейса

Модуль inp.py также содержит функции для получения новых данных из окна 
интерфейса и записи их в csv файл

Модуль imp.py также содержит функции для импорта данных из CSV файла

Модуль exp.py также содержит функции для записи информации
с последующим хранением в csv файл

Модуль exp.py также содержит функции для вывода информации, отфильтрованной по ключу
и значению в csv файл. Работает только по одному ключу. Не стал усложнять и добавлять полноценный фильтр по нескольким ключам (чтобы Вам проверять полегче было, и так немало нагромождено))

Модуль log.py содержит функции для записи времени и действий в log.txt

keys.py содержит набор ключей, по которым хранится информация

controller.py сводит все функции всех модулей в один и создает главное окно интерфейса

main.py - выполнение функции controller

по умолчанию база данных хранится в data.csv, фильтр выкидывает в output.csv, импорт данных из input.csv