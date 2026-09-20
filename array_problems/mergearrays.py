from typing import List


def MergesortedArrays(arr1: List[int], arr2: List[int]) -> List[int]:
    n, m = len(arr1) - 1, len(arr2) - 1
    i, j = 0, 0
    nums = []
    while i <= n and j <= m:
        if arr1[i] <= arr2[j]:
            if len(nums) == 0 or nums[-1] != arr1[i]:
                nums.append(arr1[i])
            i += 1
        else:
            if len(nums) == 0 or nums[-1] != arr2[j]:
                nums.append(arr2[j])
            j += 1

    while i <= n:
        if len(nums) == 0 or nums[-1] != arr1[i]:
            nums.append(arr1[i])
        i += 1

    while j <= m:
        if len(nums) == 0 or nums[-1] != arr2[j]:
            nums.append(arr2[j])
        j += 1
    return nums


# print(MergesortedArrays([1, 2, 3, 4, 5, 66, 77], [2, 3, 5, 6, 8, 56, 98]))


"""Leetcode - 88"""

"""Time complexity is O(N) and space complexity is O(1)"""


def mergearrays(nums1: list[int], m: int, nums2: list[int], n: int):
    p1 = m - 1
    p2 = n - 1
    w = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[w] = nums1[p1]
            p1 -= 1
        else:
            nums1[w] = nums2[p2]
            p2 -= 1
        w -= 1
    while p2 >= 0:
        nums1[w] = nums2[p2]
        p2 -= 1
        w -= 1
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(mergearrays(nums1, m, nums2, n))
