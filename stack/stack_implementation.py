class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    """TC:O(1)"""

    def push(self, items: int):
        self.data.append(items)
        """TC:O(1)"""

    def pop(self):
        if len(self.data) == 0:
            return "Stack is already empty"
        x = self.data.pop(-1)
        return x

    """TC:O(1)"""

    def top(self):
        if len(self.data) == 0:
            return "Stack is already empty"
        return self.data[-1]

    """TC:O(1)"""

    def size(self):
        return len(self.data)


obj = Stack()
obj.push(9)
obj.push(8)
obj.push(7)
obj.push(6)
obj.push(5)

print(obj.pop())
print(obj.pop())

print(obj.top())
print(obj.size)
