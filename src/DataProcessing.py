import nltk
import math

# get an array the amount of words for each title or text
def get_amount_words(data):
    result = []
    for text in data:
        amount = len(text.split())
        result.append(amount) #extend
    return result


#get an array of the amount of words for each text or title
def get_amount_words(data):
    result = []
    for text in data:
        amount = len(text.split())
        result.append(amount) #extend
    return result


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
    print(average + variance)
    print(average - variance)
    for x in amount:
        print(x)
        if x < average + variance and x > average - variance:
            sum += x
            count += 1
        count2 += 1
    print(count)
    print(count2)
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
            if "NN" in word or "NNP" in word or "NN" in word or "NNP" in word:
                amount += 1
        amount = count[i]/amount
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
            if "NN" in word or "NNP" in word or "NN" in word or "NNP" in word:
                amount += 1
        result.append(amount)
    return result
"""
def get_average(amount_f, amount_r):
    average_f = get_average_word(amount_f)
    average_r = get_average_word(amount_r)
    return (average_r + average_f) / 2
"""
