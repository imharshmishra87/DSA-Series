"""In order to swap 2 numbers we will be using the XOR logic : XOR states that if number of 1's are odd than 1 else even or when 2 bits are same than 0 else 1"""


def swapnumber(a: int, b: int) -> tuple[int, int]:
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


# print(swapnumber(a=15, b=10))


def check_ith_bit(a: int, i: int) -> bool:
    """Right SHift Approach"""
    # if (1 >> i) & a == 1:
    #     return True
    # else:
    #     return False

    """Left Shift Approach"""
    if (1 << i) & a != 1:
        return True
    else:
        return False


# print(check_ith_bit(a=13, i=3))


def set_ith_bit(a: int, i: int):
    result = (1 << i) | a
    binary = ""
    while result != 0:
        remainder = result % 2
        binary += str(remainder)
        result = result // 2
    return binary[::-1]


# print(set_ith_bit(a=9, i=2))


def clear_ith_bit(a: int, i: int):
    result = ~(1 << i) & a
    binary = ""
    while result != 0:
        remainder = result % 2
        binary += str(remainder)
        result = result // 2
    return binary[::-1]


# print(clear_ith_bit(a=13, i=3))


def toggle_ith_bit(a: int, i: int):
    result = (1 << i) ^ a
    binary = ""
    while result != 0:
        remainder = result % 2
        binary += str(remainder)
        result = result // 2
    return binary[::-1]


# print(toggle_ith_bit(a=13, i=3))


def power_of_two(a: int):
    """for right shift do (a & (a-1))"""
    if (a & (a - 1)) == 0:
        return True
    else:
        return False


print(power_of_two(a=13))
