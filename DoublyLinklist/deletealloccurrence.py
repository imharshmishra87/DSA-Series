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


def delete_all_occurrence(head, x):
    if head is None:
        return None
    while head is not None and head.val == x:
        head = head.next
        if head is not None:
            head.prev = None
    if head is None:
        return None
    temp = head
    while temp is not None and temp.next is not None:
        if temp.next.val == x:
            node_to_delete = temp.next
            temp.next = node_to_delete.next
            if temp.next is not None:
                temp.next.prev = temp
        else:
            temp = temp.next
    return head


"""Algorithm:
Step1: We will check if head is none than return none
Step2: This is for the linklist that has continous elements 2->2->2->2->3->8->7->9 checks continously and update the value of head
Step3. Than the rest of the logic simply involves checking if temp and temp.next is not None and deleting the value"""


def traverse(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next
