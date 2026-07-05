# Simple Stock Tracker

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOG": 140
}
# Function to calculate total investment
def calculate_investment():
    total_value = 0
    investments = {}

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found in price list.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        investments[stock] = investments.get(stock, 0) + quantity
        total_value += stock_prices[stock] * quantity

    print("\n--- Investment Summary ---")
    for stock, qty in investments.items():
        print(f"{stock}: {qty} shares @ {stock_prices[stock]} = {qty * stock_prices[stock]}")
    print(f"\nTotal Investment Value: ${total_value}")

    # Optionally save to file
    save = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save == "yes":
        filename = input("Enter filename (e.g., result.txt or result.csv): ")
        with open(filename, "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty in investments.items():
                f.write(f"{stock},{qty},{stock_prices[stock]},{qty * stock_prices[stock]}\n")
            f.write(f"Total Investment,,,{total_value}\n")
        print(f"Results saved to {filename}")

# Run the program
calculate_investment()
