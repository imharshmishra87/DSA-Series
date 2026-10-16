from typing import List

"""floor means the largest number which is smaller than or equal to the target 
ciel means the smallest number which is greater than or equal to the target
step1: find the mid of the array
step2: if mid is equal to the target return the target as floor and ciel
step3: if mid is greater than the target then update ciel to mid and move the right pointer to mid-1
step4: if mid is smaller than the target then update floor to mid and move the left pointer to mid+1
step5: return floor and ciel"""


def Floor_Ciel(nums: List[int], target: int) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    floor = -1
    ciel = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return [target, target]
        elif nums[mid] >= target:
            ciel = nums[mid]
            right = mid - 1
        else:
            floor = nums[mid]
            left = mid + 1
    return [floor, ciel]


print(Floor_Ciel(nums=[3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15], target=11))
