from typing import List


class Linklist:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def traverse(head):
    while head is not None:
        print(head.val, end="")
        head = head.next


obj = Linklist(4)
obj.next = Linklist(5)
obj.next.next = Linklist(6)
traverse(obj)
