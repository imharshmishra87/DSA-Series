"""leetcode:121"""

from typing import List

"""Brute force solution"""


def Stocks(nums: List[int]) -> int:
    n = len(nums)
    profit = 0

    max_profit = float("-inf")
    for i in range(n):
        buy = nums[i]
        for j in range(i, n):
            profit = nums[j] - buy
            max_profit = max(profit, max_profit)
    return max_profit


# print(Stocks(nums=[7, 1, 5, 3, 6, 4]))

"""Optimal solution"""


def OptimalStocks(nums: List[int]) -> int:
    n = len(nums)
    max_profit = 0
    lowest_price = float("inf")
    for price in range(n):
        if nums[price] < lowest_price:
            lowest_price = nums[price]
        else:
            profit = nums[price] - lowest_price
            max_profit = max(profit, max_profit)
    return max_profit


print(OptimalStocks(nums=[7, 1, 5, 3, 6, 4]))
