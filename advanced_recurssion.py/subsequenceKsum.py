"""Brute Force Solution"""


def backtrack(nums: list[int]) -> list[list[int]]:
    result = []
    subset = []
    n = len(nums)

    def func(index, subset):
        if index >= n:
            result.append(subset.copy())
            return
        subset.append(nums[index])
        func(index + 1, subset)
        subset.pop()
        func(index + 1, subset)

    func(index=0, subset=subset)
    return result


print(backtrack(nums=[5, 9, 3, 4, 1]))

"""Optimal SOlution"""


def subset(nums: list[int], target: int) -> list[int]:
    result = []
    subset = []

    def backtrack(index, subset, total):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        if index >= len(nums):
            return

        subset.append(nums[index])
        sum = total + nums[index]
        backtrack(index + 1, subset, sum)
        e = subset.pop()
        sum -= e
        backtrack(index + 1, subset, sum)

    backtrack(0, subset, 0)
    return result


# print(subset(nums=[5, 9, 3, 4, 1], target=9))
"""Time complexity is O(2**n) and space complexity is O(N)"""
