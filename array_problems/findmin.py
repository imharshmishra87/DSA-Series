from typing import List


def Findmin(nums: List[int]) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    minimum_value = float("inf")
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= nums[right]:
            minimum_value = min(minimum_value, nums[mid])
            right = mid - 1
        else:
            minimum_value = min(minimum_value, nums[left])
            left = mid + 1
    return minimum_value


print(Findmin(nums=[4, 5, 6, 7, 0, 1, 2]))
