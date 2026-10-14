from typing import List

"""Brute Force Solution"""
"""Step1: Scan the 2d Matrix 
Step2: Convert all the elements of rows and columns containing 0 to float("inf").
Step3: Once this is done simply iterate through each element and convert the float inf back to 0
"""

"""Time complexity will be O((M*N)*(M+N)+O(M*N)"""


def SetMatrixZeroBrute(arr: List[List[int]]) -> List[List[int]]:

    def setinfinity(matrix: List[List[int]], row: int, col: int) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0, r):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")
        for j in range(0, c):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")
        return matrix

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                setinfinity(arr, row=i, col=j)

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == float("inf"):
                arr[i][j] = 0
    return arr


# print(SetMatrixZeroBrute(arr=[[0, 1], [1, 1]]))

"""Algorithm"""
"""Step1: We will take 2 list one called track_rows and other called track_cols which will be same as the length of rows and columns
Step2: Now we will check through each element if it is 0 than change it's corresponding index (i,j) to -1
Step3: Finally again loop through each element and check if track_rows or track_cols is -1 at index (i or j) than simply replace that element with 0"""


def SetMatrixZeroOptimal(arr: List[List[int]]) -> List[List[int]]:
    rows = len(arr)
    cols = len(arr[0])
    track_rows = [0] * rows
    track_cols = [0] * cols
    for i in range(0, rows):
        for j in range(0, cols):
            if arr[i][j] == 0:
                track_rows[i] = -1
                track_cols[j] = -1

    for i in range(0, rows):
        for j in range(0, cols):
            if track_rows[i] == -1 or track_cols[j] == -1:
                arr[i][j] = 0
    return arr


print(SetMatrixZeroOptimal(arr=[[0, 1], [1, 1]]))
