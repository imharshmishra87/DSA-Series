def extract_digits(num: int) -> int:
    while num > 0:
        last_digit = num % 10
        print(last_digit)
        num = num // 10


extract_digits(num=5897)
