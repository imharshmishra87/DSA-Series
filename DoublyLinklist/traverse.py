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


def traverse(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next


def reverse(tail):
    temp = tail
    while temp is not None:
        print(temp.val)
        temp = temp.prev


reverse(obj.next.next)
