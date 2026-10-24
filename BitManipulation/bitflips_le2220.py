def bitflips(start: int, goal: int) -> int:
    result = start ^ goal
    binary = ""
    count = 0
    while result != 0:
        remainder = result % 2
        binary += str(remainder)
        result = result // 2
    for i in binary:
        if int(i) == 1:
            count += 1
    return count


print(bitflips(start=10, goal=7))


"""Optimization 2: Brian Kernighan’s Algorithm ($O(\text{set bits})$ Time)"""


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = start ^ goal
        count = 0
        while result > 0:
            result &= result - 1
            count += 1
        return count
