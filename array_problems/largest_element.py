def find_largest(nums: list) -> list:
    max = 0
    for i in range(len(nums)):
        if nums[i] > nums[max]:
            max = i
    return f"largest element is :{nums[max]}"


print(find_largest([-4, -8, -9, -5, -7, -78]))


def find_largest(nums: list) -> list:
    largest_ele = float("-inf")
    for i in range(len(nums)):
        largest_ele = max(largest_ele, nums[i])
    return f"largest element is :{largest_ele}"


print(find_largest([-4, -8, -9, -5, -7, -78]))
