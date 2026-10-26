def setMismatch(nums: list[int]) -> list[int, int]:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    unique_sum = sum(set(nums))

    duplicate_sum = actual_sum - unique_sum
    missing_num = expected_sum - unique_sum
    return [duplicate_sum, missing_num]
