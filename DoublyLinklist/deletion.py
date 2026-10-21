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
head.next.next.next = DoublyLinklist(6)
head.next.next.next.prev = head.next.next


def deletion_at_start(head):
    if head is None or head.next:
        return None
    head = head.next
    head.prev = None
    return head


def deletion_at_specific(head, index):
    if head is None or index < 0:
        return head
    if index == 0:
        return deletion_at_start(head)
    temp = head
    for _ in range(index - 1):
        if temp is None or temp.next is None:
            return head
        temp = temp.next

    if temp.next is not None:
        node_to_delete = temp.next
        temp.next = node_to_delete.next
        if node_to_delete.next is not None:
            node_to_delete.next.prev = temp
    return head


def deletion_by_value(head, val):
    if head is None:
        return None
    if head.val == val:
        return deletion_at_start(head)
    temp = head
    while temp.next is not None:
        if temp.next.val == val:
            node_to_delete = temp.next
            temp.next = node_to_delete.next
            if node_to_delete.next is not None:
                node_to_delete.next.prev = temp
            node_to_delete.next = None
            node_to_delete.prev = None
            return head
        else:
            temp = temp.next
    return head


def deletion_at_end(head):
    if head is None:
        return None
    if head.next is None:
        return None
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
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


# head = deletion_at_start(head)
# head = deletion_at_specific(head, 2)
# head = deletion_by_value(head, 4)
head = deletion_at_end(head)
# traverse(head)
reverse(head)
