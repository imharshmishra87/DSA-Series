def generate_factors(n: int) -> list:
    num = n
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


"""Time complexity is o(n) and space complexity is o(n)"""
# print(generate_factors(n=258978))

"""Better solution"""


def generate_factors_b(n: int) -> list:
    num = n
    factors = []
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            factors.append(i)
    factors.append(num)
    return factors


"""Time complexity is o(n/2) and space complexity is o(n/2)"""
# print(generate_factors_b(n=258978))


def sqrt_generate_factors(n: int) -> list:
    num = n
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if num // i != i:
                factors.append(num // i)
    return factors


"""Time complexity is o(sqrt(n)), space complexity is o(k)"""
print(sqrt_generate_factors(n=16))
