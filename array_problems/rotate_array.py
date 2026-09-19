from typing import List


def RotateRight(nums: List[int]) -> List[int]:
    n = len(nums)
    key = nums[n - 1]
    for i in range(n - 2, -1, -1):
        nums[i + 1] = nums[i]
    nums[0] = key
    return nums


# print(RotateRight(nums=[89, 78, 4, 5, 6, 1, 2, 7]))

"""Brute Force Solution may cause recurssion overflow error"""


def RotateRightK(nums: List[int], k: int) -> List[int]:
    if k == 0:
        return nums
    n = len(nums)
    key = nums[n - 1]
    for i in range(n - 2, -1, -1):
        nums[i + 1] = nums[i]
    nums[0] = key
    return RotateRightK(nums, k - 1)


# print(RotateRightK([89, 78, 4, 5, 6, 1, 2, 7], k=11))


"""Better solution"""


def RotateRightBetter(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if n == 0:
        return nums
    k = k % n

    def ReversedArray(left: int, right: int) -> List[int]:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

    ReversedArray(0, n - 1)
    ReversedArray(0, k - 1)
    ReversedArray(k, n - 1)
    return nums


print(RotateRightBetter([1, 2, 3, 4, 5, 6, 7], k=3))
