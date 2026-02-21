class Analyzer:

    def average(self, prices):
        return sum(prices) / len(prices)

    def trend(self, prices):
        if prices[-1] > prices[0]:
            return "UPWARD 📈"
        else:
            return "DOWNWARD 📉"

    def volatility(self, prices):
        return max(prices) - min(prices)

    def highest(self, prices):
        return max(prices)

    def lowest(self, prices):
        return min(prices)