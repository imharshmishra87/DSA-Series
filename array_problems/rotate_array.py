from typing import List

"""Algorithm:"""
"""Rotate array by left & right both have the same code structure it simply depends upon the reversal of the array
    IN CASE OF LEFT ARRAY ROTATION:
    1. first calculate k=k%n
    2. reverse the k elements eg [1,2,3,4,5],k=2 --> [2,1,3,4,5] (0,k-1)
    3. reverse the remaining elements eg:[2,1,3,4,5]-->[2,1,5,4,3] (k,n-1)
    4. finally reverse the entire array eg: [2,1,5,4,3]-->[3,4,5,1,2] (0,n-1)

    IN CASE OF RIGHT ARRAY ROTATION:
    1. first calculate k=k%n
    2. Completely reverse the entire array eg:[1,2,3,4,5]-->[5,4,3,2,1] (0,n-1)
    3. Only reverse the k elements eg:[5,4,3,2,1]-->[4,5,3,2,1] (0,k-1)
    4. Reverse the remaining array eg:[4,5,3,2,1]-->[4,5,1,2,3] (k, n-1)
"""


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
