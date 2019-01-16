from src import DecisionTree, Data, DataProcessing, Punctuation
from src.Punctuation import Punctuation


# start checking word count with variance and without variance
def word_count(data_text, data_title):
    word_count_variance(data_text, data_title)
    print()
    word_count_total(data_text, data_title)
    print()


# check the word count with variance
def word_count_variance(data_text, data_title):
    print("Check word count text with variance...")
    DecisionTree.above_average(data_text.amount_r, data_text.averageV)
    DecisionTree.under_average(data_text.amount_f, data_text.averageV)
    print()
    print("Check word count title with variance...")
    DecisionTree.under_average(data_title.amount_r, data_title.averageV)
    DecisionTree.above_average(data_title.amount_f, data_title.averageV)


# check the word count without variance
def word_count_total(data_text, data_title):
    print("Check word count text...")
    DecisionTree.above_average(data_text.amount_r, data_text.average)
    DecisionTree.under_average(data_text.amount_f, data_text.average)
    print()
    print("Check word count title...")
    DecisionTree.under_average(data_title.amount_r, data_title.average)
    DecisionTree.above_average(data_title.amount_f, data_title.average)


# start checking amount of adverbs. One in relation and one absolute
def adverb(data):
    adverb_absolute(data)
    print()
    adverb_rel(data)


# check the adverb in relation
def adverb_rel(data):
    print("Check adverb with relation...")
    adverb_r = DataProcessing.count_adverbs_rel(data.text_r, data.amount_r)
    adverb_f = DataProcessing.count_adverbs_rel(data.text_f, data.amount_f)

    average = DataProcessing.get_average(adverb_r, adverb_f)

    DecisionTree.under_average(adverb_r, average)
    DecisionTree.above_average(adverb_f, average)


# check the adverb
def adverb_absolute(data):
    print("Check adverb without relation...")
    adverb_r = DataProcessing.count_adverbs(data.text_r)
    adverb_f = DataProcessing.count_adverbs(data.text_f)

    average = DataProcessing.get_average(adverb_r, adverb_f)

    DecisionTree.under_average(adverb_r, average)
    DecisionTree.above_average(adverb_f, average)


# check all variants of nouns
def nouns(data):
    print("Check nouns with all benefits")
    nouns_r = DataProcessing.count_nouns(data.text_r, data.amount_r)
    nouns_f = DataProcessing.count_nouns(data.text_f, data.amount_f)

    average_r = DataProcessing.get_average_word(nouns_r)
    average_f = DataProcessing.get_average_word(nouns_f)

    average = (average_r + average_f) / 2

    DecisionTree.above_average(nouns_r, average)
    DecisionTree.under_average(nouns_f, average)

    print()
    print("Check for only nouns")

    nouns_r = DataProcessing.count_nouns_x(data.text_r, data.amount_r)
    nouns_f = DataProcessing.count_nouns_x(data.text_f, data.amount_f)

    average_r = DataProcessing.get_average_word(nouns_r)
    average_f = DataProcessing.get_average_word(nouns_f)

    average = (average_r + average_f) / 2

    DecisionTree.above_average(nouns_r, average)
    DecisionTree.under_average(nouns_f, average)


# check the punctuation
def punctuation(data):
    pr = Punctuation(data.text_r, data.amount_r)
    pf = Punctuation(data.text_f, data.amount_f)

    result_punctuation(" points: real = above, false = under ", pr.point_rel,  pf.point_rel)
    result_punctuation(" comma: real = above, false = under ", pr.comma_rel,  pf.comma_rel)
    result_punctuation(" question: real = above, false = under ", pr.q_mark_rel,  pf.q_mark_rel)
    result_punctuation(" exclamation: real = above, false = under ", pr.ex_mark_rel,  pf.ex_mark_rel)
    result_punctuation(" quotes in relation: real = above, false = under ", pr.quotes_rel,  pf.quotes_rel)
    result_punctuation(" quotes: real = above, false = under ", pr.quotes,  pf.quotes)


def result_punctuation(string, data_r, data_f):
    text = "Check " + string
    print(text)
    average = DataProcessing.get_average(data_r, data_f)
    DecisionTree.above_average(data_r, average)
    DecisionTree.under_average(data_f, average)
    print()


def do_decision_tree(data, average):
    print("")
