from typing import List


class Solution:
    def findfirst(self, nums: List[int], target: int):
        n = len(nums)
        left = 0
        right = n - 1
        lb = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                lb = mid
                right = mid - 1
            else:
                left = mid + 1
        return lb

    def findlast(self, nums: List[int], target: int):
        n = len(nums)
        left = 0
        right = n - 1
        ub = n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                ub = mid
                right = mid - 1
            else:
                left = mid + 1
        return ub

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = self.findfirst(nums, target)
        if lb == -1:
            return 0
        ub = self.findlast(nums, target)

        return ub - lb


obj = Solution()
print(obj.searchRange(nums=[1, 2, 3, 3, 3, 3, 3, 5, 6, 7, 8, 9, 9, 9, 9], target=38))
