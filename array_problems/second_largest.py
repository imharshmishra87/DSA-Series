"""Brute Force: Time complexity is o(nlogn) and space comp is o(1)"""


def brute_force(nums: list) -> int:
    nums.sort()
    return nums[-2]


print(brute_force([88, 544, 4, 7, 988, 877]))


"""Better Solution time comp is o(m+n)~o(n) and space comp = o(1)"""


def second_largest(nums: list) -> int:
    largest_ele = float("-inf")
    second_largest_ele = 0
    for i in range(len(nums)):
        largest_ele = max(largest_ele, nums[i])

    for j in range(len(nums)):
        if nums[j] >= nums[second_largest_ele] and nums[j] != largest_ele:
            second_largest_ele = j
    return nums[second_largest_ele]


# print(second_largest([88, 54487, 4, 7, 988]))

"""Optimal Solution time comp is o(n) and space comp is o(1)"""


def optimal_sol(nums: list) -> int:
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        if nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]
    return second_largest


# print(optimal_sol([88, 544, 4, 7, 988, 877]))
