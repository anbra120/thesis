import nltk
import math


#get an array of the amount of words for each text or title
def get_amount_words(data):
    result = []
    count = 0
    for text in data:
        amount = len(text.split())
        result.append(amount)
        count += 1
    return result, count


# get the average of a words
def get_average_word(data):
    sum = 0
    count = 0
    for amount in data:
        sum += amount
        count += 1
    return sum/count


def get_variance(average, amount):
    """
    :param average:
    :param amount:
    :return: variance
    variance^2 = Sum[ (amount - average)^2 ] / count
    """
    variance = 0
    count = 0
    for x in amount:
        variance += (x - average) * (x - average)
        count += 1
    return math.sqrt(variance/count)


def get_newAverage(variance, amount, average):
    sum = 0
    count= 0
    count2=0
    for x in amount:
        if x < average + variance and x > average - variance:
            sum += x
            count += 1
        count2 += 1
    return sum/count

#print("Check the amount of nouns in relation")
def count_nouns_rel(data, count):
    result = []
    i = 0
    for news in data:
        amount = 0
        tokens = nltk.word_tokenize(news)
        tagged = nltk.pos_tag(tokens)
        for word in tagged:
            if "NN" in word or "NNPS" in word or "NNS" in word or "NNP" in word:
                amount += 1
        amount = amount/count[i]
        result.append(amount)
        i += 1
    return result


def countNouns(data):
  #  print("Check the amount of nouns")
    result = []
    for news in data:
        amount = 0
        tokens = nltk.word_tokenize(news)
        tagged = nltk.pos_tag(tokens)
        for word in tagged:
            if "NN" in word or "NNPS" in word or "NNS" in word or "NNP" in word:
            #if "NN" in word or "NNS" in word:
                amount += 1
        result.append(amount)
    return result


def countNounsX(data):
    result = []
    for news in data:
        amount = 0
        tokens = nltk.word_tokenize(news)
        tagged = nltk.pos_tag(tokens)
        for word in tagged:
            if "NN" in word or "NNS" in word:
                amount += 1
        result.append(amount)
    return result


def count_nouns_relX(data, count):
    result = []
    i = 0
    for news in data:
        amount = 0
        tokens = nltk.word_tokenize(news)
        tagged = nltk.pos_tag(tokens)
        for word in tagged:
            if "NN" in word or "NNS" in word:
                amount += 1
        amount = count[i]/amount
        result.append(amount)
        i += 1
    return result

def count_adverbs_rel(data, count):
    result = []
    i = 0
    for news in data:
        amount = 0
        tokens = nltk.word_tokenize(news)
        tagged = nltk.pos_tag(tokens)
        for word in tagged:
            if "RB" in word or "RBR" in word or "RBS" in word:
                amount += 1
        amount = count[i]/amount
        result.append(amount)
        i += 1
    return result

#
def count_adverbs(data):
    result = []
    for news in data:
        amount = 0
        tokens = nltk.word_tokenize(news)
        tagged = nltk.pos_tag(tokens)
        for word in tagged:
            if "RB" in word or "RBR" in word or "RBS" in word:
                amount += 1
        result.append(amount)
    return result
