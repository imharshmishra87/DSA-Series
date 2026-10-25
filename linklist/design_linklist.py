class ListNode:
    def __init__(self, data: int = 0, next=None):
        self.data = data
        self.next = next


"""Don't copy the above ListNode Class while submitting to leetcode"""


class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode(-1)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        temp = self.dummy_head.next
        for _ in range(index):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(index=0, val=val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        pred = self.dummy_head
        for _ in range(index):
            pred = pred.next

        node_to_insert = ListNode(val)
        if pred.next is not None:
            node_to_insert.next = pred.next
        pred.next = node_to_insert
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        temp = self.dummy_head
        for _ in range(index):
            temp = temp.next
        temp.next = temp.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
