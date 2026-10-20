from typing import List


class Linklist:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def rearrange(head):
    odd = head
    even = head.next
    even_head = even
    while even and even.next is not None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head


def traverse(head):
    while head is not None:
        print(head.val, end="")
        head = head.next


obj = Linklist(4)
obj.next = Linklist(5)
obj.next.next = Linklist(6)
head = rearrange(obj)
traverse(obj)
