"""Leetcode 876 Problem Statement"""


class Linklist:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def traverse(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next


"""Brute Force Solution"""


def findMidBrute(head):
    count = 0
    temp = head
    while head is not None:
        count += 1
        head = head.next
    print(count)

    for _ in range(0, count // 2):
        temp = temp.next
    return temp


"""Time complexity is O(n+n//2) and space complexity is O(1)"""


"""Optimal Solution"""


def findMid(head):
    slow = head
    fast = head
    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


"""Time complexity is O(n) and space complexity is O(1)"""

obj = Linklist(4)
obj.next = Linklist(5)
obj.next.next = Linklist(6)
head = findMidBrute(obj)
traverse(head)
