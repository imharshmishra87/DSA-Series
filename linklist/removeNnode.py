from typing import List


class Linklist:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


"""2 Pass Solution"""


def removeNthnode(head, n):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    actual_index = count - n

    point = head
    for _ in range(actual_index - 1):
        point = point.next
    point.next = point.next.next

    return head


"""Optimal Solution"""


def removeNthnode(head, n):
    dummy = Linklist(0, head)
    slow = dummy
    fast = dummy
    for _ in range(n):
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    slow.next == slow.next.next
    return dummy.next


def traverse(head):
    while head is not None:
        print(head.val, end="")
        head = head.next


obj = Linklist(4)
obj.next = Linklist(5)
obj.next.next = Linklist(6)
obj.next.next.next = Linklist(7)
head = removeNthnode(obj, 2)
traverse(head)
