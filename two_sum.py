def get_sum(arr: list, target: int):
    seen = {}
    for i in arr:
        num = target - i
        if num in seen:
            return (i, num)
        else:
            seen[i] = num


print(get_sum(arr=[2, 7, 11, 15], target=13))
