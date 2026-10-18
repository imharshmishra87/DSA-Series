def get_sum(nums: list, target: int):
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index


print(get_sum(nums=[2, 7, 11, 15], target=13))
