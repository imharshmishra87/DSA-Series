"""Optimal Solution"""


def singleNumber(nums: list[int]) -> int:
    a = 0
    for i in nums:
        a = i ^ a
    print(a)


print(singleNumber(nums=[4, 1, 2, 1, 2]))


"""Brute Force"""


def singleNumber(nums: list[int]) -> int:
    my_hash = {}
    for i in range(len(nums)):
        my_hash[nums[i]] = my_hash.get(nums[i], 0) + 1
    for key in my_hash.items():
        if my_hash[key] == 1:
            return key


print(singleNumber(nums=[4, 1, 2, 1, 2]))
