from typing import List

"""leetcode 485"""

"""Approach -1"""


def maxConsecutive(nums: List[int]):
    n = len(nums)
    max_count = 0
    count = 0
    for i in range(n):
        if nums[i] == 1:
            count += 1
            if count >= max_count:
                max_count = count
        else:
            count = 0
    return max_count


"""Approach -2"""


def maxConsecutive(nums: List[int]):
    n = len(nums)
    max_count = 0
    count = 0
    for i in range(n):
        if nums[i] == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max_count


"""Time complexity is O(N) and space complexity is O(1)"""
print(maxConsecutive(nums=[1, 0, 0, 1, 1, 1, 1, 0, 1]))
