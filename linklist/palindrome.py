class Linklist:
    def __init__(self, val):
        self.val = val
        self.next = None


def isPalindrome(head) -> bool:
    slow = head
    fast = head
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    prev = None
    temp = slow
    while temp is not None:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next

    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True


def traverse(head):
    while head is not None:
        print(head.val, end="")
        head = head.next


obj = Linklist(1)
obj.next = Linklist(2)
obj.next.next = Linklist(1)
print(isPalindrome(obj))
