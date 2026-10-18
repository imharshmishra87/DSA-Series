from typing import List


class Solution:

    def findfirst(self, nums: List[int], target: int):
        n = len(nums)
        left = 0
        right = n - 1
        lb = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                lb = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return lb

    def findlast(self, nums: List[int], target: int):
        n = len(nums)
        left = 0
        right = n - 1
        ub = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ub = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ub

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = self.findfirst(nums, target)
        ub = self.findlast(nums, target)

        return [lb, ub]


obj = Solution()
print(obj.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
