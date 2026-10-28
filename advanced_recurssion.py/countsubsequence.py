def countSubsequence(nums: list[int], target: int) -> int:
    count = 0

    def backtrack(index: int = 0, total: int = 0):
        if total == target:
            return 1
        elif total > target:
            return 0
        if index >= len(nums):
            return 0
        sum = total + nums[index]
        pick = backtrack(index + 1, sum)
        sum = total
        not_pick = backtrack(index + 1, sum)
        return pick + not_pick

    data = backtrack(0, 0)
    return data


print(countSubsequence(nums=[5, 9, 3, 4, 1], target=9))
