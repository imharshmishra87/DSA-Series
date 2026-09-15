def check_palindrome(num: int) -> bool:
    number = num
    new_num = 0
    while number > 0:

        last_digit = number % 10
        new_num = new_num * 10 + last_digit
        number = number // 10

    if num == new_num:
        return True
    else:
        return False


print(check_palindrome(num=989))
"""Time complexity will be O(log10(n)), space complexity=o(1)"""
