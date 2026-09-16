def insertion_sort(nums: list) -> list:
    for i in range(len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


print(insertion_sort([5, 7, 8, 4, 1, 6, 9, 2]))
"""Best case is o(n) and worst and avg case is o(n**2)"""
