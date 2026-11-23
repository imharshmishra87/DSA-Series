def nextGreaterElementII(arr: list[int]):
    n = len(arr)
    stack = []
    result = [-1] * n
    for i in range(2 * n - 1, -1, -1):
        while len(stack) != 0 and stack[-1] <= arr[i % n]:
            stack.pop()
        if i < n:
            if len(stack) != 0:
                result[i] = stack[-1]
        stack.append(arr[i % n])
    return result


print(nextGreaterElementII(arr=[1, 2, 3, 4, 3]))
