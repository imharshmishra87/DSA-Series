def partition(nums: list, low: int, high: int):
    i = low
    j = high
    pivot = nums[low]
    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] > pivot and j >= low:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick_sort(nums, low, high):
    if low < high:
        pindex = partition(nums, low, high)
        quick_sort(nums, low, pindex - 1)
        quick_sort(nums, pindex + 1, high)


arr = [98, 20, 0, 1, 6, 9, 7, 55]
low = 0
high = len(arr) - 1
quick_sort(arr, low, high)
print(arr)

"""Best case / Avg case o(nlogn) and worst case o(n**2)"""
