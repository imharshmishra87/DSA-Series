from typing import List

"""Space Complexity is o(n**2) and time complexity is o(n**2)
Step1: Create an extra space of result named varable.
Step2: Now do this result[j][(rows - 1) - i] = arr[i][j] (Usually done by understanding the pattern)"""


def transposeMatrices(arr: List[List[int]]) -> List[List[int]]:
    rows = len(arr)
    cols = len(arr[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    print(result)
    for i in range(rows):
        for j in range(cols):
            result[j][(rows - 1) - i] = arr[i][j]
    return result


# print(transposeMatrices(arr=[[2, 1, 3], [4, 2, 8], [9, 4, 5]]))


"""Optimal SOlution"""

"""Space complexity is O(1) and time complexity is O(n**2)
Step1: Convert the matrices into transpose
Step2: Reverse each array of the matrices
Step3 Return the arr"""


def transposeMatricesOptimal(arr: List[List[int]]) -> List[List[int]]:
    rows = len(arr)
    cols = len(arr[0])
    for i in range(rows - 1):
        for j in range(i + 1, rows):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(0, rows):
        arr[i].reverse()
    return arr


print(transposeMatricesOptimal(arr=[[2, 1, 3], [4, 2, 8], [9, 4, 5]]))
