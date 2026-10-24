def singleNumber(nums: list[int]) -> int:
    my_hash = {}
    for i in range(len(nums)):
        my_hash[nums[i]] = my_hash.get(nums[i], 0) + 1
    for key in my_hash:
        if my_hash[key] != 3:
            return key


# print(singleNumber(nums=[0, 1, 0, 1, 0, 1, 99]))

"""Optimal Solution"""


def singleNumber(nums: list[int]) -> int:
    ones = 0
    twos = 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones


print(singleNumber(nums=[0, 1, 0, 1, 0, 1, 99]))
