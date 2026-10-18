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


def atStart(head, val: int):
    new_val = Linklist(val)
    temp = head
    new_val.next = temp
    return new_val


def atEnd(head, val: int):
    new_val = Linklist(val)
    if head is None:
        return new_val
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = new_val
    return head


def atSpecificPosition(head, val: int, index: int):
    new_val = Linklist(val)
    if index == 0:
        new_val.next = head
        return new_val
    else:
        temp = head
        for _ in range(index - 1):
            if temp is None:
                break
            temp = temp.next
        prevpos = temp.next
        temp.next = new_val
        new_val.next = prevpos
        return head


obj = Linklist(4)
obj.next = Linklist(5)
obj.next.next = Linklist(6)
obj.next.next.next = Linklist(8)
obj.next.next.next.next = Linklist(9)

head = atSpecificPosition(obj, 7, 3)
traverse(head)
