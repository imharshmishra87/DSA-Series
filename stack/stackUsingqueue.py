class Stack:
    def __init__(self):
        self.items = []

    def push(self, data: int):
        def reverse(left: int, right: int, nums: list[int]) -> list[int]:
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums

        self.items.append(data)
        n = len(self.items)
        k = n - 1
        arr = reverse(0, n - 1, self.items)
        final_arr = reverse(n - k, n - 1, arr)
        return final_arr

    def pop(self):
        if len(self.items) == 0:
            return "Stack is empty"
        popped = self.items.pop(0)
        return popped


obj = Stack()
print(obj.push(8))
print(obj.push(9))
print(obj.push(10))
print(obj.push(11))
print(obj.push(12))
print(obj.pop())
