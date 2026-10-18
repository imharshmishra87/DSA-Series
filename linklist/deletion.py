from typing import List


class Linklist:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def traverse(head):
    while head is not None:
        print(head.val, end="")
        print(" ")
        head = head.next


def atStart(head):
    if head is None:
        return None
    temp = head
    head = temp.next
    return head


def atEnd(head):
    if head is None:
        return None

    if head.next is None:
        return None
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head


"""delete by value"""


def deletebyValue(head, target: int):
    if head is None:
        return None

    if head.val == target:
        return head.next
    temp = head
    while temp.next is not None:
        if temp.next.val == target:
            temp.next = temp.next.next
            return head
        temp = temp.next


"""delete by index """


def atSpecificPosition(head, index: int):

    if head is None or index < 0:
        return head

    if index == 0:
        head = head.next
        return head

    else:
        temp = head
        for _ in range(index - 1):
            if temp is None:
                break
            temp = temp.next
        if temp.next is None:
            return head
        prevpos = temp.next.next
        temp.next = prevpos

        return head


obj = Linklist(4)
obj.next = Linklist(5)
obj.next.next = Linklist(6)
obj.next.next.next = Linklist(8)
obj.next.next.next.next = Linklist(9)

head = deletebyValue(obj, 9)
traverse(head)
