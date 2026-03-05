# Phase 0 Web Version
# - All trades and prices are manually entered
# - Portfolio metrics are calculated by the system

import csv
import os
from decimal import Decimal, ROUND_HALF_UP
from collections import defaultdict

TRADE_FILE = "trade.csv"
PRICE_FILE = "price.csv"

# =========================
# Utility
# =========================

def to_decimal(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


# =========================
# Initialize / Repair Files
# =========================

def ensure_file(file_path, headers):
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
        return

    # Verify header integrity
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        first_row = next(reader, None)

    if first_row != headers:
        print(f"{file_path} header corrupted. Rebuilding file.")
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)


def initialize_files():
    ensure_file(TRADE_FILE, ["date", "asset", "quantity", "price", "note"])
    ensure_file(PRICE_FILE, ["asset", "current_price", "updated_at"])


# =========================
# Load Prices
# =========================

def load_prices():
    prices = {}
    try:
        with open(PRICE_FILE, "r") as pf:
            reader = csv.DictReader(pf)

            if "asset" not in reader.fieldnames:
                raise ValueError("price.csv header invalid")

            for row in reader:
                asset = row["asset"].strip()
                prices[asset] = to_decimal(row["current_price"])
    except Exception as e:
        print("Error loading prices:", e)

    return prices


# =========================
# Add Trade
# =========================

def add_trade(date, asset, quantity, price, note):
    try:
        asset = asset.strip().upper()
        quantity = to_decimal(quantity)
        price = to_decimal(price)

        with open(TRADE_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date, asset, quantity, price, note])

    except Exception as e:
        print("Error adding trade:", e)


# =========================
# Update Price
# =========================

def update_price(asset, current_price, updated_at):
    try:
        asset = asset.strip().upper()
        current_price = to_decimal(current_price)

        prices = load_prices()
        prices[asset] = current_price

        with open(PRICE_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["asset", "current_price", "updated_at"])
            for a, p in prices.items():
                writer.writerow([a, p, updated_at])

    except Exception as e:
        print("Error updating price:", e)


# =========================
# Portfolio Calculation
# =========================

def get_portfolio_summary():
    portfolio = {}

    try:
        with open(TRADE_FILE, "r") as f:
            reader = csv.DictReader(f)

            if "asset" not in reader.fieldnames:
                raise ValueError("trade.csv header invalid")

            for row in reader:
                asset = row["asset"].strip()
                quantity = to_decimal(row["quantity"])
                price = to_decimal(row["price"])

                if asset not in portfolio:
                    portfolio[asset] = {
                        "total_quantity": Decimal("0"),
                        "total_cost": Decimal("0")
                    }

                portfolio[asset]["total_quantity"] += quantity
                portfolio[asset]["total_cost"] += quantity * price

    except Exception as e:
        print("Error reading trades:", e)
        return {}

    prices = load_prices()

    total_invested = Decimal("0")
    total_current_value = Decimal("0")
    asset_breakdown = []

    for asset, data in portfolio.items():
        total_quantity = data["total_quantity"]
        total_cost = data["total_cost"]

        current_price = prices.get(asset)
        if current_price is None:
            current_price = total_cost / total_quantity
        current_value = total_quantity * current_price

        total_invested += total_cost
        total_current_value += current_value

        asset_breakdown.append({
            "asset": asset,
            "quantity": float(total_quantity),
            "invested": float(total_cost),
            "current_value": float(current_value)
        })

    if total_invested > 0:
        total_return = (total_current_value - total_invested) / total_invested
    else:
        total_return = Decimal("0")

    return {
        "total_invested": float(total_invested),
        "current_value": float(total_current_value),
        "return": float(total_return),
        "asset_breakdown": asset_breakdown
    }


# =========================
# Trade History
# =========================

def get_trade_history():
    trades = []
    try:
        with open(TRADE_FILE, "r") as f:
            reader = csv.DictReader(f)
            trades = list(reader)
    except Exception as e:
        print("Error loading trade history:", e)

    return trades


# =========================
# Portfolio History
# =========================

def get_portfolio_history():
    trades = get_trade_history()
    trades_sorted = sorted(trades, key=lambda x: x["date"])
    
    # 按日期收集价格更新
    price_updates = defaultdict(dict)
    try:
        with open("price.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                date = row["updated_at"]
                asset = row["asset"].strip()
                price = Decimal(str(row["current_price"]))
                price_updates[date][asset] = price
    except Exception as e:
        print("Error loading price updates:", e)
    
    # 按日期收集交易
    trades_by_date = defaultdict(list)
    for trade in trades_sorted:
        trades_by_date[trade["date"]].append(trade)
    
    all_dates = sorted(set(list(trades_by_date.keys()) + list(price_updates.keys())))
    
    holdings = defaultdict(Decimal)
    last_price_per_asset = {}
    history = []
    
    for date in all_dates:
        # 先处理当天交易
        for trade in trades_by_date.get(date, []):
            asset = trade["asset"].strip()
            qty = Decimal(str(trade["quantity"]))
            trade_price = Decimal(str(trade["price"]))
            
            holdings[asset] += qty
            # 如果当天没有 price 更新，就用交易价格
            if asset not in price_updates.get(date, {}):
                last_price_per_asset[asset] = trade_price
        
        # 再处理当天 price.csv 更新
        for asset, price in price_updates.get(date, {}).items():
            last_price_per_asset[asset] = price
        
        # 计算当天组合总价值
        total_value = sum(holdings[a] * last_price_per_asset.get(a, Decimal("0")) for a in holdings)
        history.append({"date": date, "value": float(total_value)})
    
    return history