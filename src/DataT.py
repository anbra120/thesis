from src import DataProcessing

class DataT:
    def __init__(self, data_real, data_fake):
        self.text_f = data_fake
        self.text_r = data_real

        self.amount_r, self.count_r = DataProcessing.get_amount_words(data_real)
        self.amount_f, self.count_f = DataProcessing.get_amount_words(data_fake)
        self.amount = self.amount_f + self.amount_r

        self.average_r = DataProcessing.get_average_word(self.amount_r)
        self.average_f = DataProcessing.get_average_word(self.amount_f)
        self.average = (self.average_f + self.average_r) / 2

        self.variance_r = DataProcessing.get_variance(self.average_r, self.amount_r)
        self.variance_f = DataProcessing.get_variance(self.average_f, self.amount_f)

        self.average_rV = DataProcessing.get_newAverage(self.variance_r, self.amount_r, self.average)
        self.average_fV = DataProcessing.get_newAverage(self.variance_f, self.amount_f, self.average)
        self.averageV = (self.average_fV + self.average_rV) / 2

        self.category = categorize(self.count_r, self.count_f)


# categorize the data for the SVM
def categorize(count_r, count_f):
    result = []
    i = 0
    categorization = 0  #the categorization of the data
    check = 1           #this is only for the if clause
    while i < count_r + count_f:
        if check == 1 and i >= count_r:
            categorization = 1
            check = -1
        result.append(categorization)
        i += 1
    return result
