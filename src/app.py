import glob
import errno
import csv
import src.DataTitle as myModule
import src.DecisionTree as myModule

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
    print(count)
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
    print(get_average_word(result))
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

    print()

    path = get_path_fake_title()
    data_f = get_text(path)

    path = get_path_fake_title_2()
    data_f += get_text(path)
    amount_f = get_amount_words(data_f)

    print()

    average = get_average(amount_f, amount_r)
    print("The average is: " + str(average))
    tree = myModule.DecisionTree()
    tree.fake_title(amount_f, average)
    print()
    tree.real_title(amount_r, average)
 #   data = myModule.DataTitle(data_r, data_f, amount_r, amount_f, get_average_word(amount_r), get_average_word(amount_f))
    return


get_data()

"""
tree = myModule.DecisionTree()
tree.fake_title(data, average_word)
print()
tree.real_title(data2, average_word)

"""

"""
def get_text(path):
    data = []
    fs = glob.glob(path)
    for name in fs:
        try:
            with open(name, encoding="utf8",errors='ignore') as f:
                amount = len(f.read().split())
                data.append(amount) #extend
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    return data
    """

""""   path = get_path_real_title_2()
    data, amount += get_text(path)

    path = get_path_fake_title()
    data_F = get_text(path)

    path = get_path_fake_title_2()
    data_F += get_text(path)
    d = myModule.DataTitle(data, data_F, amount, amount_F)
    average_word = get_average_word(data) + get_average_word(data2)
    return average_word/2, data, data_F


    average_word, data,data2 = get_data()
"""

