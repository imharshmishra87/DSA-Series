def fibonnaci_series(n: int, memo: dict) -> int:
    if memo is None:
        memo = {}
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    answer = fibonnaci_series(n - 1, memo) + fibonnaci_series(n - 2, memo)
    memo[n] = answer
    return answer


print(fibonnaci_series(9, memo=None))

"""Space complexity is o(2**n) and Time Complexity is o(n)"""
