import nltk

# get an array the amount of words for each title or text
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

#get an array of the amount of words for each text or title
def get_amount_words(data):
    result = []
    for text in data:
        amount = len(text.split())
        result.append(amount) #extend
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


"""
def get_average(amount_f, amount_r):
    average_f = get_average_word(amount_f)
    average_r = get_average_word(amount_r)
    return (average_r + average_f) / 2
"""
