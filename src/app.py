import glob
import errno
import nltk

from src import DecisionTree, Get_path, DataProcessing
from src.DataT import DataT


from array import *
#from sklearn import svm


def get_text(path):
    data = []
    foo = ""
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


def get_data_title():
    path = Get_path.real_title()
    data_r = get_text(path)

    path = Get_path.real_title_2()
    data_r += get_text(path)

    path = Get_path.fake_title()
    data_f = get_text(path)

    path = Get_path.fake_title_2()
    data_f += get_text(path)

    data = DataT(data_r, data_f )

    return data

def get_data_text():
    path = Get_path.real_text()
    data_r = get_text(path)

    path = Get_path.real_text_2()
    data_r += get_text(path)

    path = Get_path.fake_text()
    data_f = get_text(path)

    path = Get_path.fake_text_2()
    data_f += get_text(path)

    data = DataT(data_r, data_f )

    return data

def tree(average, amount_f, amount_r):
    print("The average is: " + str(average))
    DecisionTree.fake_title(amount_f, average)
    DecisionTree.real_title(amount_r, average)


data_title = get_data_title()

nouns_f =DataProcessing.countNouns(data_title.text_f)
nouns_f2 =DataProcessing.count_nouns_rel(data_title.text_f, data_title.amount_f)

nouns_r =DataProcessing.countNouns(data_title.text_r)
nouns_r2 =DataProcessing.count_nouns_rel(data_title.text_f, data_title.amount_r)

f_average = DataProcessing.get_average_word(nouns_f)
r_average = DataProcessing.get_average_word(nouns_r)

f2_average = DataProcessing.get_average_word(nouns_f2)
r2_average = DataProcessing.get_average_word(nouns_r2)

"""
print(f_average)
print(r_average)

print(f2_average)
print(r2_average)
"""

#tree(data_title.average, data_title.amount_f, data_title.amount_r)
data_text = get_data_text()
print(data_text.amount_r)
print(data_text.amount_f)




""" TESTING, TESTING , TESTING 

def writer(data):
    with open("G:/Thesis/Features/Titels.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerows(line)

"""

"""
def test(data):

"""
