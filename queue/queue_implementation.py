class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data: int):
        self.items.append(data)

    # Time complexity of enqueue operation is O(1) as we are adding the element at the end of the list.

    def dequeue(self):
        if len(self.items) == 0:
            return "Queue is already empty"
        data = self.items.pop(0)
        return data

    # Time complexity of dequeue operation is O(n) as we are removing the first element of the list and shifting all other elements to the left.

    def front(self):
        if len(self.items) == 0:
            return "Cannot peek , queue is empty"
        return f"Front Element is : {self.items[0]}"

    # Time complexity of front operation is O(1) as we are accessing the first element of the list.

    def rear(self):
        if len(self.items) == 0:
            return "Cannot peek , queue is empty"
        return f"Rear Element is : {self.items[-1]}"

    # Time complexity of rear operation is O(1) as we are accessing the last element of the list.

    def size(self):
        return f"Size of the queue is : {len(self.items)}"

    # Time complexity of size operation is O(1) as we are accessing the length of the list. Don't confuse it with the size of the queue, which is O(n) as we are traversing the entire list to count the number of elements. The reason for the time complexity of size operation being O(1) is that we are using the built-in len() function, which is implemented in C and has a time complexity of O(1). it already keeps track of the size of the list and returns it in constant time.

    def traversequeue(self):
        for i in self.items:
            print(i, end="->")
        print(None)


obj = Queue()

obj.enqueue(56)
obj.enqueue(6)
obj.enqueue(67)
obj.enqueue(76)
obj.dequeue()
print(obj.front())
print(obj.size())
print(obj.rear())
obj.traversequeue()
