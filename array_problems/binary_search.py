from typing import List

"""Iterative Approach for finding Element"""


def binarySearch(nums: List[int], target: int) -> str:
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return f"Value found at index {mid}"
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return "Value does not exist"


# print(binarySearch(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=8))

"""Recurssive Approach for finding Element"""


def binnarySearchRecursive(nums: List[int], low: int, high: int, target: int):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return f"Value found at index {mid}"
    elif nums[mid] > target:
        return binnarySearchRecursive(nums, low, mid - 1, target)
    else:
        return binnarySearchRecursive(nums, mid + 1, high, target)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 0
high = len(nums) - 1
target = 2
print(binnarySearchRecursive(nums, low, high, target))

"""Time complexity is O(log2N), space complexity is O(1) in recurssive it is O(N)"""
