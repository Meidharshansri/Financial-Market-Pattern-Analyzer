class Stock:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

    def get_name(self):
        return self.name

    def get_prices(self):
        return self.prices