
import csv
import os
from datetime import datetime

# Sample stock prices (demonstration only)
stock_prices = {
    "AAPL": 230.00,
    "MSFT": 510.00,
    "GOOGL": 250.00,
    "TSLA": 450.00,
    "AMZN": 220.00
}

portfolio = []

# Terminal colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def heading():
    print("\n" + "=" * 55)
    print("       STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 55)


def add_stock():
    print("\n--- ADD STOCK ---")
    print("Available stocks:", ", ".join(stock_prices))

    ticker = input("Enter stock symbol: ").strip().upper()

    if ticker not in stock_prices:
        print("Invalid stock symbol!")
        return

    try:
        buy_price = float(input("Enter purchase price: "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Price and quantity must be positive!")
            return

    except ValueError:
        print("Please enter valid numbers!")
        return

    current_price = stock_prices[ticker]

    investment = buy_price * quantity
    current_value = current_price * quantity
    profit_loss = current_value - investment
    percentage = (profit_loss / investment) * 100

    stock = {
        "Ticker": ticker,
        "Buy Price": buy_price,
        "Current Price": current_price,
        "Quantity": quantity,
        "Investment": investment,
        "Current Value": current_value,
        "Profit/Loss": profit_loss,
        "Return (%)": percentage
    }

    portfolio.append(stock)

    print(f"\n{GREEN}Stock added successfully!{RESET}")


def view_portfolio():
    if not portfolio:
        print("\nYour portfolio is empty!")
        return

    print("\n" + "=" * 105)
    print("                    YOUR STOCK PORTFOLIO")
    print("=" * 105)

    print(
        f"{'Stock':<10}{'Buy Price':>12}{'Current':>12}"
        f"{'Shares':>10}{'Investment':>15}{'Value':>15}"
        f"{'P/L':>15}"
    )

    print("-" * 105)

    for stock in portfolio:

        color = GREEN if stock["Profit/Loss"] >= 0 else RED

        print(
            f"{stock['Ticker']:<10}"
            f"{stock['Buy Price']:>12.2f}"
            f"{stock['Current Price']:>12.2f}"
            f"{stock['Quantity']:>10}"
            f"{stock['Investment']:>15.2f}"
            f"{stock['Current Value']:>15.2f}"
            f"{color}{stock['Profit/Loss']:>15.2f}{RESET}"
        )

    total_investment = sum(s["Investment"] for s in portfolio)
    total_value = sum(s["Current Value"] for s in portfolio)

    total_profit = total_value - total_investment
    total_return = (total_profit / total_investment) * 100

    color = GREEN if total_profit >= 0 else RED

    print("-" * 105)

    print(f"Total Investment : ₹{total_investment:,.2f}")
    print(f"Current Value    : ₹{total_value:,.2f}")

    print(
        f"Total Profit/Loss: "
        f"{color}₹{total_profit:,.2f}{RESET}"
    )

    print(f"Total Return     : {color}{total_return:.2f}%{RESET}")


def save_csv():
    if not portfolio:
        print("\nNo portfolio data to save!")
        return

    filename = "portfolio_summary.csv"

    file_exists = os.path.isfile(filename)

    fieldnames = [
        "Date",
        "Ticker",
        "Buy Price",
        "Current Price",
        "Quantity",
        "Investment",
        "Current Value",
        "Profit/Loss",
        "Return (%)"
    ]

    with open(filename, "a", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists or os.path.getsize(filename) == 0:
            writer.writeheader()

        for stock in portfolio:
            row = stock.copy()
            row["Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow(row)

    print(f"\n{GREEN}Portfolio saved to {filename}!{RESET}")


def main():

    while True:

        heading()

        print("\n1. Add Stock")
        print("2. View Portfolio")
        print("3. Save Portfolio to CSV")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            add_stock()

        elif choice == "2":
            view_portfolio()

        elif choice == "3":
            save_csv()

        elif choice == "4":
            print("\nThank you for using Stock Portfolio Tracker!")
            break

        else:
            print(f"\n{YELLOW}Invalid choice! Try again.{RESET}")


if __name__ == "__main__":
    main()
