# Stock prices over 7 days (example data)
prices = [120, 125, 123, 130, 128, 135, 140]

# 1. Display stock prices
print("Stock Prices:", prices)

# 2. Find highest and lowest price
max_price = max(prices)
min_price = min(prices)
print("Highest Price:", max_price)
print("Lowest Price:", min_price)

# 3. Calculate average price
average_price = sum(prices) / len(prices)
print("Average Price:", round(average_price, 2))

# 4. Calculate daily profit/loss (difference between consecutive days)
profit_loss = []
for i in range(1, len(prices)):
    profit_loss.append(prices[i] - prices[i-1])
print("Daily Profit/Loss:", profit_loss)

# 5. Find best day to buy and sell for maximum profit
min_price = prices[0]
max_profit = 0
buy_day = sell_day = 0

for i in range(1, len(prices)):
    if prices[i] - min_price > max_profit:
        max_profit = prices[i] - min_price
        sell_day = i
    if prices[i] < min_price:
        min_price = prices[i]
        buy_day = i

print("Best day to buy: Day", buy_day + 1)
print("Best day to sell: Day", sell_day + 1)
print("Maximum Profit:", max_profit)
