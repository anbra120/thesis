def fake_title(data, average):
    print("Testin fake titles....")
    correct = 0
    wrong = 0
    for value in data:
        if value < average:
            wrong += 1
        else:
            correct += 1
    print("For fake titles: " + str(correct) + " are correct and " + str(wrong) + " are wrong")
    return  wrong

def real_title(data, average):
    print("Testin real titles....")
    correct = 0
    wrong = 0
    for value in data:
        if value > average:
            wrong += 1
        else:
            correct += 1
    print("For fake titles: " + str(correct) + " are correct and " + str(wrong) + " are wrong")
    return  wrong
