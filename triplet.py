from typing import List


def threeSum(nums_sorted: List[int]) -> List[List[int]]:
    nums_sorted.sort()
    triplets = []
    print(nums_sorted)

    for i in range(len(nums_sorted)):
        if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
            continue
        left = i + 1
        right = len(nums_sorted) - 1
        while left < right:
            final_sum = nums_sorted[left] + nums_sorted[right] + nums_sorted[i]
            if final_sum == 0:
                triplets.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                left += 1
                right -= 1
                while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                    left += 1
            elif final_sum > 0:
                right -= 1
            elif final_sum < 0:
                left += 1
    return triplets


print(threeSum([-1, 0, 1, 2, -1, -4]))
