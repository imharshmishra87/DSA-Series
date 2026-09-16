"""Time complexity is O(N) and space complexity is O(N)"""


def is_palindrome(value: str) -> bool:
    n = len(value) - 1
    data = ""

    while n >= 0:
        data += value[n]
        print(data)
        n -= 1
    if data == value:
        return True
    else:
        return False


value = "NITIN"
# print(is_palindrome(value=value))


"""Better Solution time complexity of O(n/2)~o(n) and space complexity is o(1)"""


def check_palindrome(value: str, left: int, right: int):
    data = "".join([i for i in value if i.isalpha()]).lower()
    while left <= right:
        if data[left] == data[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


print(check_palindrome(value=value, left=0, right=len(value) - 1))


"""Time complexity is O(N) and space complexity is O(N)"""


def check_plaindrome_recursion(value: str, left: int, right: int) -> bool:
    if right <= left:
        return True
    if value[left] != value[right]:
        return False
    return check_plaindrome_recursion(value=value, left=left + 1, right=right - 1)


# print(check_plaindrome_recursion(value=value, left=0, right=len(value) - 1))
