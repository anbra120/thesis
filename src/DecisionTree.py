class DecisionTree:

    def fake_title(self, data, average):
        print("Testin fake titles....")
        correct = 0
        wrong = 0
        for value in data:
            if value < average:
                wrong += 1
            else:
                correct += 1
        print("For fake titles: " + str(correct) + " are correct and " + str(wrong) + " are wrong")

    def real_title(self, data, average):
        print("Testin real titles....")
        correct = 0
        wrong = 0
        for value in data:
            if value > average:
                wrong += 1
            else:
                correct += 1
        print("For fake titles: " + str(correct) + " are correct and " + str(wrong) + " are wrong")
