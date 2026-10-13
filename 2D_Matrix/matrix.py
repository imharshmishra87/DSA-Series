from typing import List


def UpperTriangle(arr: List[List[int]]):
    rows = len(arr)
    columns = len(arr[0])
    for i in range(rows):
        for j in range(columns):
            if j >= i:
                print(arr[i][j])
            else:
                print("*")
        print()


def LowerTriangle(arr: List[List[int]]) -> int:
    rows = len(arr)
    columns = len(arr[0])
    for i in range(rows):
        for j in range(columns):
            if i >= j:
                print(arr[i][j])
            else:
                print("*")
        print()


def Diagonal(arr: List[List[int]]) -> int:
    rows = len(arr)
    columns = len(arr[0])
    for i in range(rows):
        for j in range(columns):
            if i == j:
                print(arr[i][j])
            else:
                print("*")
        print()


def OppositeDiagonal(arr: List[List[int]]) -> int:
    rows = len(arr)
    columns = len(arr[0])
    for i in range(rows):
        for j in range(columns):
            if i + j == 2:
                print(arr[i][j])
            else:
                print("*")
        print()


def TransposeMatrix(arr: List[List[int]]) -> int:
    rows = len(arr)
    cols = len(arr[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = arr[i][j]
    return result


arr = [[4, 5], [9, 9], [7, 9]]
print(TransposeMatrix(arr))
# Diagonal(arr)
# UpperTriangle(arr)
# LowerTriangle(arr)
