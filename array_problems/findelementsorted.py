from typing import List

"""If the array consist of duplicates than we will prefer this solution"""


def findElement(nums: List[int], target: int) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[left] == nums[mid] == nums[right]:
            left = left + 1
            right = right - 1
            continue
        if nums[mid] <= nums[right]:
            if not nums[mid] <= target <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if not nums[left] <= target <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return False


print(
    findElement(
        nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], target=2
    )
)


"""If the array does not consist of duplicates than we will prefer this solution"""


def findElement(nums: List[int], target: int) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[mid] <= nums[right]:
            if not nums[mid] <= target <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if not nums[left] <= target <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return False


# print(findElement(nums=[4,5,6,7,0,1,2],target=0))
