def SolveSudoku(board: list[list[int]]):

    def isValid(r: int, c: int, board: list[list[int]], digit):
        """Checking duplicate in each row"""
        for i in range(9):
            if board[r][i] == digit:
                return False
        """Checking duplicate in each column"""
        for j in range(9):
            if board[j][c] == digit:
                return False

        """Checking value in a 3X3 Grid"""
        start_row = (r // 3) * 3
        start_col = (c // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == digit:
                    return False
        return True

    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for nums in range(1, 10):
                        digit = str(nums)
                        if isValid(row, col, board, digit):
                            board[row][col] = digit
                            if solve(board):
                                return True
                            board[row][col] = "."
                    return False
        return True

    solve(board)


"""Better Solution"""


class Solution:
    def isSafe(self, board, row, col, digit) -> bool:
        # Checking for each element in a single row (Horizontal)
        for i in range(9):
            if board[row][i] == digit:
                return False
        # Checking for each element in a single column (Vertical)
        for j in range(9):
            if board[j][col] == digit:
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == digit:
                    return False
        return True

    def helper(self, board: list[list[str]], row: int, col: int) -> bool:
        if row == 9:
            return True
        next_row, next_col = row, col + 1
        if next_col == 9:
            next_row += 1
            next_col = 0

        # Check if the place already consist of element or not
        if board[row][col] != ".":
            return self.helper(board, next_row, next_col)

        for num in range(1, 10):
            digit = str(num)
            if self.isSafe(board, row, col, digit):
                board[row][col] = digit
                if self.helper(board, next_row, next_col):
                    return True
            board[row][col] = "."
        return False

    def solveSudoku(self, board: list[list[str]]) -> None:
        self.helper(board, 0, 0)
        """
        Do not return anything, modify board in-place instead.
        """


"""Optimal Solution"""


class Solution:
    def isSafe(self, board, row, col, digit) -> bool:
        # Checking for each element in a single row (Horizontal)
        for i in range(9):
            if board[row][i] == digit:
                return False
        # Checking for each element in a single column (Vertical)
        for j in range(9):
            if board[j][col] == digit:
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == digit:
                    return False
        return True

    def helper(self, board: list[list[str]]) -> bool:
        best_candidates = None
        best_cell = None

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    candidates = []
                    for num in range(1, 10):
                        digit = str(num)
                        if self.isSafe(board, row, col, digit):
                            candidates.append(digit)
                    if not candidates:
                        return False
                    if best_candidates is None or len(candidates) < len(
                        best_candidates
                    ):
                        best_cell = row, col
                        best_candidates = candidates

        if best_cell is None:
            return True

        row, col = best_cell
        for digit in best_candidates:
            board[row][col] = digit
            if self.helper(board):
                return True
            board[row][col] = "."
        return False

    def solveSudoku(self, board: list[list[str]]) -> None:
        self.helper(board)
        """
        Do not return anything, modify board in-place instead.
        """


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
"""Time complexity is O(N**no of empty places) and space complexity is O(N**2) where N is the size of the board"""
# obj=Solution()
# obj.solveSudoku(board)
# print(board)
