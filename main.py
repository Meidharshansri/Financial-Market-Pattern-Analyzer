from database import StockDatabase
from models import Stock
from analyzer import Analyzer
from utils import print_menu

db = StockDatabase("stock_data.json")
analyzer = Analyzer()

while True:
    print_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Stock Name: ")
        prices = list(map(float, input("Enter prices separated by space: ").split()))
        stock = Stock(name, prices)
        db.save(stock)
        print("Stock data saved!")

    elif choice == "2":
        stocks = db.get_stocks()

        if not stocks:
            print("No data available")
            continue

        for i, s in enumerate(stocks):
            print(i + 1, s.get_name())

        idx = int(input("Choose stock: ")) - 1
        prices = stocks[idx].get_prices()

        print("Average:", analyzer.average(prices))
        print("Trend:", analyzer.trend(prices))
        print("Volatility:", analyzer.volatility(prices))
        print("Highest:", analyzer.highest(prices))
        print("Lowest:", analyzer.lowest(prices))

    elif choice == "3":
        break

    else:
        print("Invalid choice")