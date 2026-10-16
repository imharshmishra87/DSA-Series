from typing import List


def LowerBounds(nums: List[int], target: int) -> int:
    n = len(nums)
    low = 0
    high = n - 1
    minlowerbound = n
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            minlowerbound = mid
            high = mid - 1

        else:
            low = mid + 1
    return minlowerbound


print(LowerBounds(nums=[100, 200, 300, 400, 500, 600, 700, 800, 900], target=400))


def UpperBounds(nums: List[int], target: int) -> int:
    n = len(nums)
    low = 0
    high = n - 1
    upperbound = n
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            upperbound = mid
            high = mid - 1

        else:
            low = mid + 1
    return upperbound


print(UpperBounds(nums=[100, 200, 300, 400, 500, 600, 700, 800, 900], target=400))
