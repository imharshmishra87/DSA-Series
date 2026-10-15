from typing import List


def Foursum(nums: List[List[int]], target: int) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    result = []
    for i in range(n):
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                final_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if final_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif final_sum > target:
                    right -= 1
                else:
                    left += 1
    return result


print(Foursum(nums=[2, 2, 2, 2, 2], target=8))
