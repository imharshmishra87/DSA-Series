def count_numbers(n: int) -> int:
    num = n
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    print(count)


count_numbers(n=9874566)

"""By using lograthmic function space complexity : o(log10(n), space comp: o(1))"""

from math import log10


def count_num(n: int) -> int:
    return int(log10(n) + 1)


print(count_num(9874566))
