class DoublyLinklist:
    def __init__(self, data: int):
        self.prev = None
        self.val = data
        self.next = None


obj = DoublyLinklist(1)
obj.next = DoublyLinklist(2)
obj.next.prev = obj
obj.next.next = DoublyLinklist(3)
obj.next.next.prev = obj.next
obj.next.next.next = DoublyLinklist(4)
obj.next.next.next.prev = obj.next.next
obj.next.next.next.next = DoublyLinklist(5)
obj.next.next.next.next.prev = obj.next.next.next


def twosum(head, target: int):
    temp = head
    while temp.next is not None:
        temp = temp.next
    right = temp
    left = head
    result = []
    while left != right and left.prev != right:
        final_sum = left.val + right.val
        if final_sum == target:
            result.append([left.val, right.val])
            left = left.next
            right = right.prev
        elif final_sum > target:
            right = right.prev
        else:
            left = left.next
    return result


print(twosum(obj, target=5))
