# TASK 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300
}

# Dictionary to store user portfolio
portfolio = {}

# Take input from user
n = int(input("Enter number of different stocks you want to add: "))

for i in range(n):
    stock = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
    quantity = int(input(f"Enter quantity of {stock}: "))
    
    if stock in stock_prices:
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    else:
        print(f"⚠️ Stock {stock} not found in price list!")

# Calculate total investment
total_value = 0
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_value += investment
    print(f"{stock}: {qty} × {price} = {investment}")

print("\nTotal Investment Value = ", total_value)

# Optional: Save to file
save = input("Do you want to save the result to file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} × {stock_prices[stock]} = {stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Investment Value = {total_value}")
    print("Portfolio saved to portfolio.txt ✅")
