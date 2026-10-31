def SubsetSum(nums: list[int]) -> list[int]:
    result = []
    subset = []
    n = len(nums)

    def backtrack(index):
        if index >= n:
            result.append(sum(subset.copy()))
            return
        subset.append(nums[index])
        backtrack(index + 1)
        subset.pop()
        backtrack(index + 1)

    backtrack(0)
    return result


print(SubsetSum(nums=[2, 3]))
