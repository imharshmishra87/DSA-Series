# Brute force solution : Time Complexity is O(N**2)
def nextGreater(arr: list[int]):
    result = [-1] * len(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break

    return result


# print(nextGreater(arr=[1, 2, 3, 5]))

# Optimal Soltuion


def nextGreaterOptimal(arr: list[int]):
    result = [-1] * len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while len(stack) != 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) != 0:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result


print(nextGreaterOptimal(arr=[1, 2, 3, 4, 3]))
