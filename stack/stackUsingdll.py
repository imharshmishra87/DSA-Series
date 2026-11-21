class DoublyLinklist:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


class StackUsingDll:
    def __init__(self):
        pass

    def push(self, head, data: int):
        data = DoublyLinklist(data)
        if head is None:
            return data
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = data
        data.prev = temp
        return head

    def pop(self, head):
        tail = head
        while tail.next.next is not None:
            tail = tail.next
        val = tail.next.val
        tail.next.prev = None
        tail.next = None

        return val

    def peek(self, head):
        tail = head
        while tail.next is not None:
            tail = tail.next

        return f"The peek element of the stack is : {tail.val}"

    def size(self, head):
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        return f"The size of the stack is : {count}"

    def traverse(self, head):
        temp = head
        while temp is not None:
            print(temp.val)
            temp = temp.next


# Initialise the doubly linklist first
obj = StackUsingDll()
h1 = obj.push(None, 89)
h2 = obj.push(h1, 97)
h3 = obj.push(h2, 56)
h4 = obj.push(h3, 78)

# print(obj.pop(h4))
# print(obj.pop(h4))
print(obj.peek(h4))
print(obj.size(h4))
obj.traverse(h4)
