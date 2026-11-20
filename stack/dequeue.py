from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, data: int):
        self.items.append(data)
        for _ in range(len(self.items) - 1):
            self.items.append(self.items.popleft())
        return self.items

    def pop(self):
        if len(self.items) == 0:
            return "Stack is empty"
        popped = self.items.popleft()
        return popped

    def top(self):
        if len(self.items) == 0:
            return "Stack is empty"
        return self.items[0]


obj = Stack()
print(obj.push(1))
print(obj.push(2))
print(obj.top())
print(obj.pop())
