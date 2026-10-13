"""leetcode 128"""

from typing import List

"""Naive Approach"""
"""Algorithm :
step1: Loop through each element in the array start with the first one
step2: Initialse a variable count and max_count
step3: Now run a while loop check if num+1 exists in the array nums
step4: if do exist than count+=1
step5: find out the max_element or count
step6: Return max_count"""
"""Time comp is o(n**2)"""


def LongestSequenceNaive(nums: List[int]) -> int:
    n = len(nums)
    max_count = 0
    for i in range(n):
        num = nums[i]
        count = 1
        while num + 1 in nums:
            count += 1
            num = num + 1
        max_count = max(max_count, count)
    return max_count


# print(LongestSequenceNaive(nums=[100, 4, 200, 1, 3, 2]))

"""Better Approach"""
"""Step1: We will first sort the array
Step2: Assign a variable as last_smaller, count, longest
Step3:Loop through each element and check if num-1 equal to las_smaller if yes than count+=1 and assign last_smaller equals to num.
Step4: If num is not equal to last smaller than assign last_smaller to num and reset count value to 1
Step5: Find out the longest element betweeen longest and count
Step6: Return the longest"""


def LongestSequenceBetter(nums: List[int]) -> int:
    n = len(nums)
    nums.sort()
    last_smaller = float("-inf")
    count = 0
    longest = 0
    for i in range(n):
        num = nums[i]
        if num - 1 == last_smaller:
            count += 1
            last_smaller = num
        elif num != last_smaller:
            last_smaller = num
            count = 1
        longest = max(longest, count)
    return longest


# print(LongestSequenceBetter(nums=[99, 98, 97, 96, 95, 87, 45]))


def LongestSequenceOptimal(nums: List[int]) -> int:
    n = len(nums)
    my_set = set()
    longest = 0
    for i in nums:
        my_set.add(i)

    for num in my_set:
        if num - 1 not in my_set:
            x = num
            count = 1
            while x + 1 in my_set:
                count += 1
                x += 1
            longest = max(longest, count)
    return longest


print(LongestSequenceOptimal(nums=[99, 98, 97, 96, 95, 87, 45]))
