
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 330}

print("=== STOCK PORTFOLIO TRACKER ===")
print("Available stocks:")
for name, price in stock_prices.items():
    print(name, ":", "$" + str(price))
print("Type 'done' when finished.\n")

portfolio = {}      # user ke stocks aur quantity
total = 0

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Choose from the list.\n")
        continue

    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity

print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total += value
    print(stock, ":", quantity, "x", stock_prices[stock], "=", value)

print("TOTAL INVESTMENT: $" + str(total))

with open("portfolio.txt", "w") as file:
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(stock + ": " + str(quantity) + " x " + str(stock_prices[stock]) + " = " + str(value) + "\n")
    file.write("TOTAL INVESTMENT: $" + str(total))

print("Result saved in portfolio.txt")