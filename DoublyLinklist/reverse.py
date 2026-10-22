class DoublyLinklist:
    def __init__(self, data: int):
        self.prev = None
        self.val = data
        self.next = None


obj = DoublyLinklist(2)
obj.next = DoublyLinklist(4)
obj.next.prev = obj
obj.next.next = DoublyLinklist(5)
obj.next.next.prev = obj.next

"""Better Solution"""


def reverselink(head):
    prev_pointer = None
    temp = head
    while temp is not None:
        next = temp.next
        temp.next = prev_pointer
        temp.prev = next
        prev_pointer = temp
        temp = next
    return prev_pointer


"""Pure Swap Logic"""


def reverselink(head):
    temp = head
    last = None
    while temp is not None:
        last = temp.prev
        temp.prev = temp.next
        temp.next = last
        temp = temp.prev
    return last.prev


def traverse(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next


head = reverselink(obj)
traverse(head)
