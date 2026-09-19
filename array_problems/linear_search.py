from typing import List


def LinearSearch(nums: List[int], k: int) -> str:
    for i, num in enumerate(nums):
        if nums[i] == k:
            return f"Element found at {i} index"
    return "Element does not exists"


print(LinearSearch(nums=[8, 9, 7, 5, 4, 2, 3], k=3))
