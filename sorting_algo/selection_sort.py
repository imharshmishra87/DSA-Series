def selection_sort_asc(nums: list) -> list:
    for i in range(len(nums) - 1):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums


print(selection_sort_asc([5, 7, 8, 4, 1, 6, 9, 2]))


def selection_sort_desc(nums: list) -> list:
    for i in range(len(nums) - 1):
        max = i
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[max]:
                max = j
        nums[i], nums[max] = nums[max], nums[i]
    return nums


print(selection_sort_desc([5, 7, 8, 4, 1, 6, 9, 2]))

"Time complexity is o(n**2)"
