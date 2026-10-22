class DoublyLinklist:
    def __init__(self, data: int):
        self.prev = None
        self.val = data
        self.next = None


obj = DoublyLinklist(1)
obj.next = DoublyLinklist(1)
obj.next.prev = obj
obj.next.next = DoublyLinklist(3)
obj.next.next.prev = obj.next
obj.next.next.next = DoublyLinklist(4)
obj.next.next.next.prev = obj.next.next
obj.next.next.next.next = DoublyLinklist(4)
obj.next.next.next.next.prev = obj.next.next.next


def traverse(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next


def removeduplicates(head):
    if head is None:
        return None
    if head.next is not None and head.val == head.next.val:
        head = head.next
        if head is not None:
            head.prev = None

    if head is None:
        return None
    """The above part will handle consecutive numbers which are duplicate from the start"""
    temp = head
    while temp is not None and temp.next is not None:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
            if temp.next is not None:
                temp.next.prev = temp
        else:
            temp = temp.next
    return head


head = removeduplicates(obj)
traverse(head)
