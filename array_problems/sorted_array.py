def isSorted(nums: list) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


print(isSorted([1, 4, 5, 6, 9]))
"""Time complexity is O(N) and Space complexity is O(1)"""
