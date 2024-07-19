prices = [10,8,7,5,2]
"""
brute force
def maxProfit(prices):
    res = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            res = max(res, prices[j] - prices[i])
    return res
"""
def maxProfit(prices):
    profit = 0
    lowest = prices[0]

    for price in prices:
        if price < lowest:
            lowest = price
        profit = max(profit, price - lowest)
        
    return profit





print(maxProfit(prices))