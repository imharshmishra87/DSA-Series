def combinationSum(candidates: list[int], target: int) -> list[list]:
    candidates.sort()
    result = []
    subset = []

    def backtrack(index: int, total: int):
        if total == target:
            result.append(subset.copy())
            return

        elif total > target:
            return
        if index >= len(candidates):
            return

        subset.append(candidates[index])
        backtrack(index + 1, total + candidates[index])
        subset.pop()
        next_index = index + 1
        while (
            next_index < len(candidates) and candidates[next_index] == candidates[index]
        ):
            next_index += 1
        backtrack(next_index, total)

    backtrack(0, 0)
    return result


print(combinationSum(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
