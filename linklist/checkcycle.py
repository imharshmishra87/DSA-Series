"""Leetcode 141 Problem Statement"""


class Linklist:
    def __init__(self, val: int):
        self.val = val
        self.next = None


"""Extreme Brute Force"""


def checkcycle(head):
    my_hash = {}
    temp = head
    while temp is not None:
        if temp.next in my_hash:
            return True
        else:
            my_hash[temp.next] = temp.val
            temp = temp.next
    return False


"""Brute Force"""


def checkcycle(head):
    my_set = set()
    temp = head
    while temp is not None:
        if temp in my_set:
            return True
        my_set.add(temp)
        temp = temp.next
    return False


"""Optimal Solution"""


def checkcycle(head):
    slow = head
    fast = head
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


def traverse(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next


obj = Linklist(4)
obj.next = Linklist(5)
obj.next.next = Linklist(6)
obj.next.next.next = Linklist(7)
obj.next.next.next.next = Linklist(8)
