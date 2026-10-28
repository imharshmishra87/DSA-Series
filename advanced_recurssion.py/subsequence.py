"""Time complexity is O(2**n) and space complexity is O(N)"""


def subsets(nums: list[int]) -> list[list[int]]:
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


print(subsets(nums=[1, 2, 3]))
