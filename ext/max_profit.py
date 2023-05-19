"""
leet code : Best Time to Buy and Sell Stock
"""


def max_profit(prices: list):
    temp = prices[0]
    result = 0
    for price in prices:
        if price - temp > 0:
            result = max(price - temp, result)
        else:
            temp = price
    return result


print(max_profit([7, 1, 5, 3, 6, 4]))
