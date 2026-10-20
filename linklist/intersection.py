class Linklist:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def traverse(head):
    while head is not None:
        print(head.val, end="")
        head = head.next


"""Time complexity is O(m+n) and space complexity is O(N)"""


def getIntersectionNode(head1, head2):
    my_set = set()
    temp1 = head1
    while temp1 is not None:
        my_set.add(temp1)
        temp1 = temp1.next
    temp2 = head2
    while temp2 is not None:
        if temp2 in my_set:
            return temp2
        temp2 = temp2.next
    return None


def getIntersectionNode(head1, head2):
    if head1 is None or head2 is None:
        return None
    Pa = head1
    Pb = head2
    while Pa != Pb:
        Pa = Pa.next if Pa else head2
        Pb = Pb.next if Pb else head1
    return Pa


obj = Linklist(5)
obj.next = Linklist(6)
obj.next.next = Linklist(1)
obj.next.next.next = Linklist(8)
obj.next.next.next.next = Linklist(4)
obj.next.next.next.next.next = Linklist(5)


obj2 = Linklist(4)
obj2.next = Linklist(2)
obj2.next.next = Linklist(8)
obj2.next.next.next = Linklist(4)
obj2.next.next.next.next = Linklist(5)


print(getIntersectionNode(obj, obj2))
