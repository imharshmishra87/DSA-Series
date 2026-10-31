def combinationSumIII(k: int, n: int):
    result = []
    subset = []

    def backtrack(index: int, total: int):
        if total == 0 and len(subset) == k:
            result.append(subset.copy())
            return
        if total < 0 or len(subset) >= k:
            return

        for i in range(index, 10):
            subset.append(i)
            backtrack(i + 1, total - i)
            subset.pop()

    backtrack(1, n)
    return result


print(combinationSumIII(k=3, n=7))
