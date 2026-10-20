"""Optimal Solution"""


def findlength(head):
    slow = head
    fast = head
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            temp = slow.next
            while slow != temp:
                count += 1
                temp = temp.next
            return count
    return 0


"""Brute Force"""


def findlength(head):
    my_dict = {}
    travel = 0
    temp = head
    while temp is not None:
        if temp in my_dict:
            return travel - my_dict[temp]
        my_dict[temp] = travel
        travel += 1
        temp = temp.next
    return 0
