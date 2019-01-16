from src import Get_path, Check, SVM, DataProcessing, Filehandler
from src.Data import Data
from numpy import array

def get_data_title():
    path = Get_path.real_title()
    data_r = Filehandler.get_text(path)

    path = Get_path.real_title_2()
    data_r += Filehandler.get_text(path)

    path = Get_path.fake_title()
    data_f = Filehandler.get_text(path)

    path = Get_path.fake_title_2()
    data_f += Filehandler.get_text(path)

    data = Data(data_r, data_f)

    return data


def get_data_text():
    path = Get_path.real_text()
    data_r = Filehandler.get_text(path)

    path = Get_path.real_text_2()
    data_r += Filehandler.get_text(path)

    path = Get_path.fake_text()
    data_f = Filehandler.get_text(path)

    path = Get_path.fake_text_2()
    data_f += Filehandler.get_text(path)

    data = Data(data_r, data_f)

    return data


def get_data_hyp():
    path = Get_path.hyp()
    data_A, data_B = Filehandler.text_hyp(path)
    return data_A, data_B


#data1, data2 = Filehandler.text_hyp(Get_path.hyp())
#Filehandler.writer(data1)
data = Filehandler.reader("part.txt")
print(data)
"""

# data = list(zip(nouns, amount))
# test = array(data)
# SVM.start(test, data_text.category, "Amount nouns", "Amount adverbs")
"""
