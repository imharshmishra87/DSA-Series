"""Time complexity is O(2**n) and space complexity is O(N)"""


def issubsequence(nums: list[int], target: int) -> bool:

    def backtrack(index, total):
        if total == target:
            return True
        elif total > target:
            return False
        if index >= len(nums):
            return False

        sum = total + nums[index]
        pick = backtrack(index + 1, sum)
        if pick == True:
            return True
        sum = total
        not_pick = backtrack(index + 1, sum)
        return not_pick

    result = backtrack(0, 0)

    if result:
        return True
    return False


# print(issubsequence(nums=[5, 9, 3, 4, 1], target=98))


"""Return the first occurrence of the element that satisfy the given sum"""


def Returnsubsequence(nums: list[int], target: int) -> bool:
    result = []
    subset = []

    def backtrack(index, total):
        if total == target:
            result.append(subset.copy())
            return True
        elif total > target:
            return False
        if index >= len(nums):
            return False

        subset.append(nums[index])
        sum = total + nums[index]
        pick = backtrack(index + 1, sum)
        if pick == True:
            return True
        subset.pop()
        sum = total
        not_pick = backtrack(index + 1, sum)
        return not_pick

    backtrack(0, 0)
    return result


print(Returnsubsequence(nums=[5, 9, 3, 4, 1], target=9))
