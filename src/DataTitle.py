class DataTitle:
    def __init__(self, data_real,data_fake, amount_real,amount_fake, average_real, average_fake):
        self.data_f = data_fake
        self.data_r = data_real
        self.amount_r = amount_real
        self.amount_f = amount_fake
        self.amount = amount_fake + amount_real
        self.average_r = average_real
        self.average_f = average_fake
