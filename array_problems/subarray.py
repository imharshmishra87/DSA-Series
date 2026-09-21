from typing import List

"""Brute force solution : Time complexity is O(N**2) and space complexity is O(1)"""


def Subarray(nums: List[int]) -> int:
    n = len(nums)
    total = 0
    high_score = float("-inf")
    for i in range(n):
        total = 0
        for j in range(i, n):
            total = total + nums[j]
            high_score = max(total, high_score)
    return high_score


"""Better Solution: Time complexity id O(N)"""


def BetterSubarray(nums: List[int]) -> int:
    n = len(nums)
    total = 0
    high_score = float("-inf")
    for i in range(n):
        total = total + nums[i]
        high_score = max(total, high_score)

        if total < 0:
            total = 0
    return high_score


print(BetterSubarray(nums=[5, 4, -1, 7, 8]))
