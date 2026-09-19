from typing import List


def zeroesEnd(nums: List[int]) -> None:
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums


"""Time complexity is O(N) and space complexity is O(1)"""

print(zeroesEnd(nums=[1, 2, 3, 4]))
