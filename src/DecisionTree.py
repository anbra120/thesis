#check the amount of word in a title or text
def under_average(data, average):
    correct = 0
    wrong = 0
    for value in data:
        if value < average:
            correct += 1
        else:
            wrong += 1
    print("For under average: " + str(correct) +
          " are correct and " + str(wrong) + " are wrong")


def above_average(data, average):
    correct = 0
    wrong = 0
    for value in data:
        if value > average:
            correct += 1
        else:
            wrong += 1
    print("For above average : " + str(correct) +
          " are correct and " + str(wrong) + " are wrong")






""" TESTING, TESTING , TESTING 

def writer(data):
    with open("G:/Thesis/Features/Titels.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerows(line)



"""
