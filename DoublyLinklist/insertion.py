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
    node_to_insert = DoublyLinklist(val)
    if head is None:
        head = node_to_insert
        return head
    node_to_insert.next = head
    head.prev = node_to_insert
    return node_to_insert


def insert_at_specific(head, val, index):
    node_to_insert = DoublyLinklist(val)
    if index < 0:
        return head
    if head is None:
        return node_to_insert if index == 0 else None
    if index == 0:
        return insert_at_start(head, val)

    temp = head
    for _ in range(index - 1):
        temp = temp.next

    if temp is None:
        return head

    node_to_insert.next = temp.next
    node_to_insert.prev = temp

    if node_to_insert.next is not None:
        node_to_insert.next.prev = node_to_insert
    temp.next = node_to_insert

    return head


def insert_at_end(head, val):
    node_to_insert = DoublyLinklist(val)
    if head is None:
        return node_to_insert

    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = node_to_insert
    node_to_insert.prev = temp
    return head


def traverse(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next


def reverse(head):
    temp = head
    while temp.next is not None:
        temp = temp.next
    tail = temp
    while tail is not None:
        print(tail.val)
        tail = tail.prev
    return head


# head = insert_at_start(head, 9)
# head = insert_at_end(head, 10)
# head = insert_at_specific(head, 75, 2)
# traverse(head)
reverse(head)
