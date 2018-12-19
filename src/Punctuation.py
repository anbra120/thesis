from src import DataProcessing
import re

class Punctuation:
    def __init__(self, data, amount):
        self.point, self.comma, self.q_mark, self.ex_mark= count(data)
        self.point_rel, self.comma_rel, self.q_mark_rel, self.ex_mark_rel = count_rel(data, amount)
        self.quotes, self.quotes_rel= get_quotes(data, amount)

    def print_p(self):
        print("Point:")
        print(self.point)
        print()
        print("Comma:")
        print(self.comma)
        print()
        print("Question Mark:")
        print(self.q_mark)
        print()
        print("Exclamation mark:")
        print(self.ex_mark)

    def print_rel(self):
        print("Point:")
        print(self.point_rel)
        print()
        print("Comma:")
        print(self.comma_rel)
        print()
        print("Question Mark:")
        print(self.q_mark_rel)
        print()
        print("Exclamation mark:")
        print(self.ex_mark_rel)


def count(data):
    point = []
    comma = []
    q_mark = []
    ex_mark = []

    for article in data:
        point.append(article.count("."))
        comma.append(article.count(","))
        q_mark.append(article.count("?"))
        ex_mark.append(article.count("!"))
    
    return point, comma, q_mark, ex_mark


def count_rel(data, amount):
    point = []
    comma = []
    q_mark = []
    ex_mark = []

    i = 0
    for article in data:
        point.append(article.count(".") * 50 / amount[i])
        comma.append(article.count(",") * 50 / amount[i])
        q_mark.append(article.count("?") * 50 / amount[i])
        ex_mark.append(article.count("!") * 50 / amount[i])
        i += 1

    return point, comma, q_mark, ex_mark


# Quelle: https://stackoverflow.com/questions/9519734/python-regex-to-find-a-string-in-double-quotes-within-a-string/9519934
def get_quotes(data, amount):
    result = []
    result_rel = []
    i = 0
    for text in data:
        foo = len(re.findall(r'\"(.+?)\"',text))
        result.append(foo)
        result_rel.append(foo/amount[i])
        i += 1
    return result, result_rel
