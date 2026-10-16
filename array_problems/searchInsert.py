from typing import List


def SearchInsert(nums: List[int], target: int) -> int:
    n = len(nums)
    lb = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb


print(SearchInsert(nums=[1, 3, 5, 6], target=5))
