class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data: int):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(data)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.stack1

    def dequeue(self):
        return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]


obj = QueueUsingStack()
print(obj.enqueue(5))
print(obj.enqueue(6))
print(obj.enqueue(7))
print(obj.peek())
print(obj.dequeue())
