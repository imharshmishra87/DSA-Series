from typing import List

"""Brute Force Solution with O(n**3) solution"""


def three_sumBrute(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    my_set = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    my_set.add(tuple(temp))
    return [list(ans) for ans in my_set]


# print(three_sumBrute(nums=[-1, 0, 1, 2, -1, -4]))

"""Better Solution: Time Complexity is O(n**2), space complexity is O(n)"""


def threesumBetter(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    my_result = set()
    for i in range(n):
        my_set = set()
        for j in range(i + 1, n):
            k = -(nums[i] + nums[j])
            if k not in my_set:
                my_set.add(nums[j])
            else:
                temp = [nums[i], nums[j], k]
                temp.sort()
                my_result.add(tuple(temp))
    return [list(ans) for ans in my_result]


# print(threesumBetter(nums=[-1, 0, 1, 2, -1, -4]))


"""Optimal SOlution"""


def threesumOptimal(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    result = []
    for i in range(n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            final_sum = nums[i] + nums[left] + nums[right]
            if final_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif final_sum > 0:
                right -= 1
            else:
                left += 1
    return result


print(threesumOptimal(nums=[-1, 0, 1, 2, -1, -4]))
