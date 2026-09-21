"LeetCode 2149"

from typing import List

"""Time complexity and space complexity is O(N)"""


def RearrangeElements(nums: List[int]) -> List[int]:
    n = len(nums)
    arr = [0] * n
    pt_even = 0
    pt_odd = 1
    for num in nums:
        if num > 0:
            arr[pt_even] = num
            pt_even += 2
        else:
            arr[pt_odd] = num
            pt_odd += 2
    return arr


print(RearrangeElements(nums=[-1, 1]))
