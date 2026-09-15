from math import log10


def check_armstrong(n: int):
    num = n
    sum = 0
    count = int(log10(num) + 1)
    while num > 0:
        last_digit = (num % 10) ** count
        sum = sum + last_digit
        num = num // 10
    if sum == n:
        return f"It is an armstrong number"
    else:
        return f"It is not an armstrong number"


print(check_armstrong(n=163))
