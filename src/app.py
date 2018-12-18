from src import DecisionTree, DataProcessing, Get_path, Check, SVM
from src.DataT import DataT
import glob
import errno
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


def check_nouns(data):
    nouns_f = DataProcessing.countNouns(data.text_f)
    nouns_f2 = DataProcessing.count_nouns_rel(data.text_f, data.amount_f)

    nouns_r = DataProcessing.countNouns(data.text_r)
    nouns_r2 = DataProcessing.count_nouns_rel(data.text_r, data.amount_r)


    a = DataProcessing.get_average_word(nouns_r)
    b = DataProcessing.get_average_word(nouns_r2)


    x = DataProcessing.get_average_word(nouns_f)
    y = DataProcessing.get_average_word(nouns_f2)

    i = (x + a) / 2
    j = (b + y) / 2

    DecisionTree.above_average(nouns_r, i)
    DecisionTree.above_average(nouns_r, j)

    DecisionTree.above_average(nouns_r2, i)
    DecisionTree.above_average(nouns_r2, j)

    print("-----------------------")

    DecisionTree.under_average(nouns_f, i)
    DecisionTree.under_average(nouns_f, j)

    DecisionTree.under_average(nouns_f2, i)
    DecisionTree.under_average(nouns_f2, j)

    print("*****************")

    nouns_f =DataProcessing.countNounsX(data.text_f)
    nouns_f2 =DataProcessing.count_nouns_relX(data.text_f, data.amount_f)

    nouns_r =DataProcessing.countNounsX(data.text_r)
    nouns_r2 =DataProcessing.count_nouns_relX(data.text_r, data.amount_r)


    a = DataProcessing.get_average_word(nouns_r)
    b = DataProcessing.get_average_word(nouns_r2)


    x = DataProcessing.get_average_word(nouns_f)
    y = DataProcessing.get_average_word(nouns_f2)

    i = (x + a) / 2
    j = (b + y) / 2

    DecisionTree.above_average(nouns_r, i)
    DecisionTree.above_average(nouns_r, j)

    DecisionTree.above_average(nouns_r2, i)
    DecisionTree.above_average(nouns_r2, j)


    print("-----------------------")

    DecisionTree.under_average(nouns_f, i)
    DecisionTree.under_average(nouns_f, j)

    DecisionTree.under_average(nouns_f2, i)
    DecisionTree.under_average(nouns_f2, j)


data_text = get_data_text()
data_title = get_data_title()

#Check.word_count_variance(data_text, data_title)
#print()
#Check.word_count(data_text, data_title)

#checkNouns(data_text)
#Check.adverb(data_text)

adverbs = DataProcessing.count_adverbs_rel(data_text.text_r, data_text.amount_r)
adverbs += DataProcessing.count_adverbs_rel(data_text.text_f, data_text.amount_f)

nouns = DataProcessing.count_nouns_rel(data_text.text_r, data_text.amount_r)
nouns += DataProcessing.count_nouns_rel(data_text.text_f, data_text.amount_f)

print(nouns)
print()
print(adverbs)
data = list(zip(nouns, adverbs))
print(data)
SVM.start(data, data_text.category)
