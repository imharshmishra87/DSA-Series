"""Time complexity is O(2**n) and space complexity is O(2*n)"""


def generate_parenthesis(n: int) -> list[str]:
    numbers = [""] * n * 2
    result = []

    def backtrack(index: int, numbers: list[str], total):

        if index >= len(numbers):
            if total == 0:
                result.append("".join(numbers))
            return
        if total > len(numbers) // 2:
            return
        if total < 0:
            return
        numbers[index] = "("
        sum = total + 1
        backtrack(index + 1, numbers, total=sum)
        numbers[index] = ")"
        sum = total - 1
        backtrack(index + 1, numbers, total=sum)

    backtrack(0, numbers, total=0)
    return result


print(generate_parenthesis(n=3))
