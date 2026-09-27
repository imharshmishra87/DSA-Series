from typing import List

"Algorithm"
"""
1. Initialise 3 variables max_pd,min_pd,result
2.Loop through each elements starting from 1,n
3.Create a temp_max variable which picks the max value b/w num, max_pd*num, min_pd*num
4. Similarly pick the min value
5. Update max_pd with temp_max
6. Update the result
"""

"""Time complexity is O(N) and Space complexity is O(1)"""


def generate_product(nums: List[int]) -> int:
    n = len(nums)
    max_pd = nums[0]
    min_pd = nums[0]
    result = nums[0]
    for i in range(1, n):
        num = nums[i]
        temp_max = max(num, max_pd * num, min_pd * num)
        min_pd = min(num, max_pd * num, min_pd * num)
        max_pd = temp_max
        result = max(max_pd, result)
    return result


print(generate_product(nums=[2, -5, -2, 8, -4, -6, 3]))
