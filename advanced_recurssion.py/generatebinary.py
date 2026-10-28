"""Generates all binary strings"""


def generateBinary(n: int) -> list[str]:
    numbers = ["0"] * n
    result = []

    def backtrack(index: int, numbers: list[str]):
        if index >= len(numbers):
            result.append("".join(numbers))
            return
        numbers[index] = "0"
        backtrack(index + 1, numbers)
        numbers[index] = "1"
        backtrack(index + 1, numbers)

    backtrack(index=0, numbers=numbers)
    return result


# print(generateBinary(n=3))


"""Generate binary strings such that it does not consist of adjacent ones"""


def generateBinary(n: int) -> list[str]:
    numbers = ["0"] * n
    result = []

    def backtrack(index: int, flag: bool, numbers: list[str]):
        if index >= len(numbers):
            result.append("".join(numbers))
            return
        numbers[index] = "0"
        backtrack(index + 1, flag=True, numbers=numbers)
        if flag == True:
            numbers[index] = "1"
            backtrack(index + 1, flag=False, numbers=numbers)
            numbers[index] = "0"

    backtrack(0, True, numbers)
    return result


print(generateBinary(n=3))
