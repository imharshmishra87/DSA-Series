from typing import List

"""Algorithm"""
"""Step1: We will first check if the matrix exist or not if not than return empty list
Step2: Now we will create a result list which will store the final output
Step3: Now we will create 4 variables top, left, bottom and right which will store the index of the matrix
Step4: Now we will run a while loop until top<=bottom and left<=right
Step5: Now we will run a for loop from left to right
Step6: Now we will run a for loop from top to bottom
Step7: Now we will check if top<=bottom than run a for loop from right to left
Step8: Now we will check if left<=right than run a for loop from bottom to top
Step9: Finally return the result list
Step10: Time complexity will be O(M*N) and space complexity will be O(1)
Step11: During each loop we will update the top, left, bottom and right variables to move towards the center of the matrix"""


def SpiralMatrix(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    result = []
    top = 0
    left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result


print(SpiralMatrix(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
