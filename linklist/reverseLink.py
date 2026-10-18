class Linklist:
    def __init__(self, val: int):
        self.val = val
        self.next = None


"""Time Complexity is O(N) and Space Complexity is O(1)"""


def reverse(head):
    prev = None
    temp = head
    while temp is not None:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    return prev


def traverse(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next


obj = Linklist(4)
obj.next = Linklist(5)
obj.next.next = Linklist(6)
obj.next.next.next = Linklist(7)
obj.next.next.next.next = Linklist(8)
head = reverse(obj)
traverse(head)
