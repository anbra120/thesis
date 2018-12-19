from src import Get_path, Check, SVM
from src.Data import Data
from src.Punctuation import Punctuation
import glob
import errno
from numpy import array


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

    data = Data(data_r, data_f)

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

    data = Data(data_r, data_f)

    return data


def checking_adverb(data):
    Check.adverb(data)
    print()
    Check.adverb_rel(data)


def checking_word_count(data_text, data_title):
    Check.word_count_variance(data_text, data_title)
    print()
    Check.word_count(data_text, data_title)
    print()


data_text = get_data_text()
data_title = get_data_title()

# checking_adverb(data_text)
# checking_word_count(data_text, data_title)
# Check.nouns(data_text)
#Check.punctuation(data_text)


pr = Punctuation(data_text.text_r, data_text.amount_r)
pf = Punctuation(data_text.text_f, data_text.amount_f)

points = pr.point_rel + pf.point_rel
commas = pr.comma_rel + pf.comma_rel
data = list(zip(points, commas))


SVM.start(array(data), data_text.category, "Amount points", "Amount commas")









# adverbs = DataProcessing.count_adverbs_rel(data_text.text_r, data_text.amount_r)
# adverbs += DataProcessing.count_adverbs_rel(data_text.text_f, data_text.amount_f)

# nouns = DataProcessing.count_nouns(data_text.text_r, data_text.amount_r)
# nouns += DataProcessing.count_nouns(data_text.text_f, data_text.amount_f)
# amount = data_text.amount_r + data_text.amount_f

# data = list(zip(nouns, adverbs))
# data = list(zip(nouns, amount))
# test = array(data)

# SVM.start(test, data_text.category, "Amount nouns", "Amount adverbs")
# SVM.start(test, data_text.category, "Amount nouns", "Amount words")

