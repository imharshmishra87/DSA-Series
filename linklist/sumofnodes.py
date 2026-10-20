class Linklist:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def traverse(head):
    while head is not None:
        print(head.val, end="")
        head = head.next


obj = Linklist(2)
obj.next = Linklist(4)
obj.next.next = Linklist(3)

obj2 = Linklist(5)
obj2.next = Linklist(6)
obj2.next.next = Linklist(4)


def sumofNode(link1, link2):
    carry = 0
    dummy = Linklist(0)
    curr = dummy
    while link1 is not None or link2 is not None or carry != 0:
        val1 = link1.val if link1 else 0
        val2 = link2.val if link2 else 0
        nodesum = val1 + val2 + carry

        carry = nodesum // 10
        rem = nodesum % 10

        curr.next = Linklist(rem)
        curr = curr.next

        if link1:
            link1 = link1.next

        if link2:
            link2 = link2.next
    return dummy.next


head = sumofNode(obj, obj2)
traverse(head)
