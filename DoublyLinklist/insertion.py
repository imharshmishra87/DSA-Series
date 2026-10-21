class DoublyLinklist:
    def __init__(self, data: int):
        self.prev = None
        self.val = data
        self.next = None


head = DoublyLinklist(2)
head.next = DoublyLinklist(4)
head.next.prev = head
head.next.next = DoublyLinklist(5)
head.next.next.prev = head.next


def insert_at_start(head, val):
    dummy = DoublyLinklist(val)
    dummy.next = head
    return dummy


def insert_at_specific(head, val, index):
    temp = head
    for _ in range(index - 1):
        temp = temp.next
    dummy = DoublyLinklist(val)
    next_pointer = temp.next
    temp.next = dummy
    dummy.next = next_pointer
    return head


def insert_at_end(head, val):
    dummy = DoublyLinklist(val)
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = dummy
    return head


def traverse(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next


# head = insert_at_start(head, 9)
# head = insert_at_end(head, 10)
# head = insert_at_specific(head, 75, 2)
traverse(head)
