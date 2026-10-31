"""Brute Force solution , Time Complexity is O(N!*N) and space complexity is O(N**2 + N where N is stack space)"""


def NQueen(n: int) -> list[list[str]]:
    ans = []
    board = ["." * n for _ in range(n)]

    def issafe(row, col, board, n):
        duprow = row
        dupcol = col

        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row = duprow
        col = dupcol

        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1

        row = duprow
        col = dupcol

        while row < n and col >= 0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1
        return True

    def solve(col: int, board: list[str], ans: list[str], n: int):
        if col == n:
            ans.append(list(board))
            return

        for row in range(n):
            if issafe(row, col, board, n):
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                solve(col + 1, board, ans, n)
                board[row] = board[row][:col] + "." + board[row][col + 1 :]

    solve(0, board, ans, n)
    return ans


# print(NQueen(n=3))


"""Optimal Solution"""


def NQueen(n: int):
    ans = []
    board = ["." * n for _ in range(n)]
    horizontal = [0] * n
    lower_diagonals = [0] * (2 * n - 1)
    upper_diagonals = [0] * (2 * n - 1)

    """For lower diagonal we will use the formula of r+c"""
    """For Upper diagonal we will use the formula (n-1)+(col-row)"""

    def solve(
        col: int,
        board: list[str],
        ans: list[str],
        n: int,
        lower_diagonals: list[int],
        upper_diagonals: list[int],
        horizontal: list[int],
    ):
        if col == n:
            ans.append(list(board))
            return

        for row in range(n):
            if (
                horizontal[row] == 0
                and lower_diagonals[row + col] == 0
                and upper_diagonals[(n - 1) + (col - row)] == 0
            ):
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                horizontal[row] = 1
                lower_diagonals[row + col] = 1
                upper_diagonals[(n - 1) + (col - row)] = 1

                solve(
                    col + 1, board, ans, n, lower_diagonals, upper_diagonals, horizontal
                )

                board[row] = board[row][:col] + "." + board[row][col + 1 :]
                horizontal[row] = 0
                lower_diagonals[row + col] = 0
                upper_diagonals[(n - 1) + (col - row)] = 0

    solve(0, board, ans, n, lower_diagonals, upper_diagonals, horizontal)
    return ans


print(NQueen(n=4))
