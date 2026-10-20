def begincycle(head):
    slow = head
    fast = head
    has_cycle = False
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

        if not has_cycle:
            return None

    start = head
    while start != slow:
        start = start.next
        slow = slow.next
    return start
