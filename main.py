# - All trades and prices are manually entered
# - Portfolio metrics are calculated by the system
def add_trade():
    date = input("Date")
    asset = input("Asset")
    quantity = input("Quantity")
    price = input("Price")
    note = input("Note")
    with open("trade.csv", "a") as f:
        f.write(f"{date}, {asset}, {quantity}, {price}, {note}\n")

def update_price():
    asset = input("Asset")
    current_price = input("Current Price")
    updated_at = input("Updated At")
    with open("price.csv", "a") as f:
        f.write(f"{asset}, {current_price}, {updated_at}\n")

def calculate_portfolio(price, quantity, current_price):    
    invest_value = price * quantity
    current_value = current_price * quantity
    change_percent = (current_value - invest_value) / invest_value
    return change_percent, invest_value, current_value
    
def calculate_full_portfolio():
    portfolio = {}
    with open("trade.csv", "r") as f:
        for line in f:
            data, asset, quantity, price, note = line.strip().split(", ")
            quantity = float(quantity)
            price = float(price)
            if asset not in portfolio:
                portfolio[asset] = {"quantity": quantity, "price": price}
            else:
                portfolio[asset]["quantity"] += quantity
                portfolio[asset]["price"] = price
                with open("price.csv", "r") as pf:
                    for pline in pf:
                        p_asset, current_price, updated_at = pline.strip().split(", ")
                        if p_asset == asset:
                            current_price = float(current_price)
                            change_percent, invest_value, current_value = calculate_portfolio(price, quantity, current_price)
                            print(f"Asset: {asset}, Quantity: {quantity}, Invest Value: {invest_value}, Current Value: {current_value}, Change Percent: {change_percent:.2%}")

def view_history():
    with open("trade.csv", "r") as f:
        for line in f:
            print(line.strip())

def main():
    while True:
        choice = input("Enter 'add' to add a trade, 'history' to view trade history, 'update' to update the price, 'portfolio' to view portfolio,'quit' to exit:")
        if choice == 'add':
            add_trade()
        elif choice == 'history':
            view_history()
        elif choice == 'update':
            update_price()
        elif choice == 'portfolio':
            calculate_full_portfolio()    
        elif choice == 'quit':
            break
        else:
            print("Invalid choice. Please try again.")        

if __name__ == "__main__":
    main()