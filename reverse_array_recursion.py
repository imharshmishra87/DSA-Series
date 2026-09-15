def traverse_array(n, list: list) -> None:
    if n > len(list) - 1:
        return
    print(list[n])
    n += 1
    traverse_array(n, list=list)


# traverse_array(0, list=[5, 8, 7, 9, 4])

"""Revrese Array using head recursion Time complexity is o(n), space complexity is o(n/2)==o(n) """


def reverse_array(n, arr: list) -> None:
    if n > len(arr) - 1:
        return

    reverse_array(n + 1, arr=arr)
    print(arr[n])


# reverse_array(0, arr=[5, 8, 7, 9, 4])

"""Reverse array using pointers method Time complexity is o(n) precise is o(n/2) and space complexity is o(n/2)==o(n)"""


def reverse_array_pointer(left, right, arr: list) -> list:
    if right <= left:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array_pointer(left + 1, right - 1, arr)


arr = [5, 8, 7, 9, 4, 2, 4, 1, 7, 6, 9, 5]
left = 0
right = len(arr) - 1
print(reverse_array_pointer(left=left, right=right, arr=arr))
print(arr)

"""Reverse array using while loop"""


def reverse_while_loop(arr: list, left: int, right: int) -> list:
    while right <= left:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


print(reverse_while_loop(arr=arr, left=left, right=len(arr) - 1))
