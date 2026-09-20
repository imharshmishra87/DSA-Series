from typing import List

"""Using Gauss formula for expected sum"""


def MissingNumber(nums: List[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    diff = expected_sum - actual_sum
    return diff


"""Using bit manipulation"""


def MissingNumber(nums: List[int]) -> int:
    n = len(nums)
    res = n
    for i in range(n):
        res = res ^ i
        res = res ^ nums[i]
    return res


print(MissingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
