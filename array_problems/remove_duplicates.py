def RemoveDuplicates(nums: list) -> list:
    if len(nums) == 1:
        return nums[:1]
    l, r = 1, 1
    while r <= len(nums) - 1:
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            r += 1
            l += 1
        else:
            r += 1
    return nums[:l]


"""Time complexity is O(N) and space complexity is O(1)"""
print(RemoveDuplicates([1, 2, 2, 2, 2, 2, 5, 4, 4, 7, 8]))
