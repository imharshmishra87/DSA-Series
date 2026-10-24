def decimal_to_binary(val: int) -> str:
    binary = ""
    while val != 0:
        remainder = val % 2
        binary += str(remainder)
        val = val // 2
    return binary[::-1]


"""Time complexity is O(log2N) and Space Complexity is O(log2N)"""

# print(decimal_to_binary(val=13))


def binary_to_decimal(val: str) -> int:
    n = len(val) - 1
    result = 0
    for i in range(len(val) - 1, -1, -1):
        result += int(val[i]) * 2 ** (n - i)
    return result


"""Time complexity is O(n) and space complexity is O(1)"""
print(binary_to_decimal(val="1101"))
