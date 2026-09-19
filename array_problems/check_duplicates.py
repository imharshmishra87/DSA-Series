from typing import List


def hasDuplicate(nums: List[int]) -> bool:
    seen = {}
    for i in range(len(nums)):
        seen[nums[i]] = seen.get(nums[i], 0) + 1
    for j in range(len(nums)):
        if seen.get(nums[j]) != 1:
            return True
    return False


print(hasDuplicate([1, 2, 3, 7]))


"""Optimal approach"""


def hasDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True  # Early exit! We found a duplicate, stop searching immediately.
        seen.add(num)
    return False


print(hasDuplicate([1, 2, 3, 7]))
