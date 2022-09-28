import datetime as dt


def LogInput(data):
    with open("log.txt", "a", encoding="utf-8") as f:
        result = str(dt.datetime.now()) + f":\ninput employee: {data}\n"
        f.write(result)


def LogImport(path):
    with open("log.txt", "a", encoding="utf-8") as f:
        result = str(dt.datetime.now()) + f":\nimport from: {path}\n"
        f.write(result)


def LogOutput(key, value):
    with open("log.txt", "a", encoding="utf-8") as f:
        result = str(dt.datetime.now()) + \
            f":\nfind people: key: {key}, value: {value}\n"
        f.write(result)


def LogDelete(data):
    with open("log.txt", "a", encoding="utf-8") as f:
        result = str(dt.datetime.now()) + f":\ndelete employee: {data}\n"
        f.write(result)
