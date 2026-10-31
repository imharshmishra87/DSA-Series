def letterCombination(digits: str):
    my_hash = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    result = []
    subset = []

    def backtrack(index: int):

        if index == len(digits):
            result.append("".join(subset.copy()))
            return
        digits_now = digits[index]
        char_now = my_hash[digits_now]
        for char in char_now:
            subset.append(char)
            backtrack(index + 1)
            subset.pop()

    backtrack(0)
    return result


print(letterCombination(digits="23"))
