# 121. Best Time to Buy and Sell Stock


def maxProfit(prices: list[int]) -> int:
    min_price = prices[0]
    max_diff = 0
    for i in prices:
        min_price = min(min_price, i)
        profit = i - min_price

        max_diff = max(profit, max_diff)

    return max_diff


print(maxProfit([7, 6, 4, 3, 1, 5]))
