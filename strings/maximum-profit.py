# Find the maximum single sell profit

def maximum_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]           # assuming first price to be minimum price
    max_profit = 0                  # assuming max profit to be 0 initially

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

stock_prices = [7, 1, 5, 3, 6, 4]
max_profit = maximum_profit(stock_prices)
print(max_profit)