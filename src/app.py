import glob
import errno
import csv
import src.DataTitle as myModule
from src import DecisionTree

from array import *
#from sklearn import svm


def writer(data):
    with open("C:/Users/Andreas/Desktop/Thesis/Features/Titels.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerows(line)


def get_path_real_title():
    return 'C:/Users/Andreas/Desktop/Thesis/Horne2017_FakeNewsData/Public Data/Buzzfeed Political News Dataset/Real_titles/*.txt'


def get_path_real_title_2():
    return 'C:/Users/Andreas/Desktop/Thesis/Horne2017_FakeNewsData/Public Data/Random Poltical News Dataset/Real_titles/*.txt'


def get_path_fake_title():
    return 'C:/Users/Andreas/Desktop/Thesis/Horne2017_FakeNewsData/Public Data/Buzzfeed Political News Dataset/Fake_titles/*.txt'


def get_path_fake_title_2():
    return 'C:/Users/Andreas/Desktop/Thesis/Horne2017_FakeNewsData/Public Data/Random Poltical News Dataset/Fake_titles/*.txt'


def get_average_word(data):
    sum = 0
    count = 0
    for amount in data:
        sum += data[amount]
        count += 1
    return sum/count


def get_text(path):
    data = []
    foo = ""
    fs = glob.glob(path)
    for name in fs:
        try:
            with open(name, encoding="utf8",errors='ignore') as f:
                foo = f.read()
                data.append(foo) #extend
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    return data


def get_amount_words(data):
    result = []
    for text in data:
        amount = len(text.split())
        result.append(amount) #extend
    return result


def get_average(amount_f, amount_r):
    average_f = get_average_word(amount_f)
    average_r = get_average_word(amount_r)
    return (average_r + average_f) / 2

def get_data():
    path = get_path_real_title()
    data_r = get_text(path)

    path = get_path_real_title_2()
    data_r += get_text(path)
    amount_r = get_amount_words(data_r)


    path = get_path_fake_title()
    data_f = get_text(path)

    path = get_path_fake_title_2()
    data_f += get_text(path)
    amount_f = get_amount_words(data_f)

    average = get_average(amount_f, amount_r)
    print("The average is: " + str(average))
    x= DecisionTree.fake_title(amount_f, average)
    y= DecisionTree.real_title(amount_r, average)
    #data = myModule.DataTitle(data_r, data_f, amount_r, amount_f, get_average_word(amount_r), get_average_word(amount_f))
    return


get_data()

"""
tree = myModule.DecisionTree()
tree.fake_title(data, average_word)
print()
tree.real_title(data2, average_word)

"""

