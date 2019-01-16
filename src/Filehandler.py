import glob
import errno
from pathlib import Path


def get_text(path):
    data = []
    fs = glob.glob(path)

    for name in fs:
        try:
            with open(name, encoding="utf8", errors='ignore') as f:
                foo = f.read()
                data.append(foo)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    return data


def text_hyp(path):
    fs = glob.glob(path)
    for name in fs:
        try:
            with open(name, encoding="utf8", errors='ignore') as f:
                data = f.read()
                data_A, data_B = split(data)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    return data_A, data_B


# Quelle https://stackoverflow.com/questions/752308/split-list-into-smaller-lists
def split(data):
    half = len(data)//2
    return data[:half], data[half:]


def writer(data):
    f = open("part.txt", "w", errors='ignore')
    f.write(data)

def reader(name):
    f = open(name, "r")
    return f.read()
