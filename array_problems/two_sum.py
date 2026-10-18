from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    left = 0
    right = n - 1
    result = []

    while left < right:
        if nums[left] + nums[right] == target:
            result.append([nums[left], nums[right]])
            left += 1
            right -= 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1
    return result


print(two_sum(nums=[1, 2, 3, 4, 5, 6], target=6))
