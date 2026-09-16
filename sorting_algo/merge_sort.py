def merge_arr(left: list, right: list) -> list:
    sorted_arr = []
    l, r = 0, 0
    n, m = len(left) - 1, len(right) - 1

    while l <= n and r <= m:
        if left[l] <= right[r]:
            sorted_arr.append(left[l])
            l += 1
        else:
            sorted_arr.append(right[r])
            r += 1
    if l <= n:
        while l <= n:
            sorted_arr.append(left[l])
            l += 1
    if r <= m:
        while r <= m:
            sorted_arr.append(right[r])
            r += 1
    return sorted_arr


def merge_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    left_arr = merge_sort(left)
    right_arr = merge_sort(right)
    data = merge_arr(left=left_arr, right=right_arr)
    return data


print(merge_sort(nums=[1, 5, 4, 5, 4, 7]))

# print(merge_arr(left=[5], right=[4, 5]))

"""best case / avg case/worst case o(nlogn)"""
