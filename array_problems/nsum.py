from typing import List


def nSum(nums: list[int], target: int, N: int) -> list[list[int]]:
    nums.sort()  # Sort first so both pointers and duplicate checks work!
    return nSumTarget(nums, target, N, 0)


def nSumTarget(nums: List[int], target: int, N: int, start: int) -> List[List[int]]:
    n = len(nums)
    result = []
    if N == 2:
        left = start
        right = n - 1
        while left < right:
            final_sum = nums[left] + nums[right]
            if final_sum == target:
                result.append([nums[left], nums[right]])
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
    for i in range(start, n - N + 1):
        if i != start and nums[i] == nums[i - 1]:
            continue
        sub_result = nSumTarget(nums, target=target - nums[i], N=N - 1, start=i + 1)
        for sub in sub_result:
            result.append([nums[i]] + sub)
    return result


print(nSumTarget(nums=[1, 2, 1, 0, 3], target=3, N=3, start=0))
