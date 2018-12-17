from src import DataProcessing

class DataT:
    def __init__(self, data_real, data_fake):
        self.text_f = data_fake
        self.text_r = data_real
        self.amount_r = DataProcessing.get_amount_words(data_real)
        self.amount_f = DataProcessing.get_amount_words(data_fake)
        self.amount = self.amount_f + self.amount_r
        self.average_r = DataProcessing.get_average_word(self.amount_r)
        self.average_f = DataProcessing.get_average_word(self.amount_f)
        self.average = (self.average_f + self.average_r) / 2

