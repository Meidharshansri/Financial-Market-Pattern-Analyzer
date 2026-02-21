import json
from models import Stock

class StockDatabase:
    def __init__(self, filename):
        self.filename = filename

    def save(self, stock):
        data = self.load_all()
        data.append({"name": stock.get_name(), "prices": stock.get_prices()})

        with open(self.filename, "w") as f:
            json.dump(data, f)

    def load_all(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except:
            return []

    def get_stocks(self):
        data = self.load_all()
        return [Stock(item["name"], item["prices"]) for item in data]