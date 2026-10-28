def generateCombination(nums: list[int], target: int) -> list[list[int]]:
    subset = []
    result = []

    def backtrack(index, subset, total):
        if total == target:
            result.append(subset.copy())
            return
        if total > target:
            return
        if index >= len(nums):
            return
        subset.append(nums[index])
        sum = total + nums[index]
        backtrack(index, subset, sum)
        e = subset.pop()
        sum = sum - e
        backtrack(index + 1, subset, sum)

    backtrack(0, subset, 0)
    return result


print(generateCombination(nums=[2, 3, 6, 7], target=7))
