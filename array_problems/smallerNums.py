def smallerNums(nums: list[int]) -> list[int]:
    result = []
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] > nums[j]:
                count += 1
        result.append(count)
    return result


# print(smallerNums(nums=[8, 1, 2, 2, 3]))

"""Smaller Nums : Optimal Approach"""


def smallerNums(nums: list[int]) -> list[int]:
    sorted_nums = sorted(nums)
    my_hash = {}
    for index, val in enumerate(sorted_nums):
        if val not in my_hash:
            my_hash[val] = index
    return [my_hash[num] for num in nums]


print(smallerNums(nums=[8, 1, 2, 2, 3]))
