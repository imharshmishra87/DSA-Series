from typing import List


def sumCounts(nums: List[int]) -> int:

    grand_total = 0
    n = len(nums)
    for i in range(n):
        my_set = set()
        for j in range(i, n):
            my_set.add(nums[j])
            grand_total = grand_total + len(my_set) ** 2
    return grand_total


"""Algorithm
Step1: Set a variable grand_total=0
Step2: Loop through each element 
Step3: Define a set called my_set
Step4: Now from i to n run anonther loop 
Step5: Add nums[j] to the my_set
Step6: Calculate grand_total, grand_total = grand_total + len(my_set) ** 2
Step7: Return grand_total"""
print(sumCounts(nums=[1, 2, 1]))
