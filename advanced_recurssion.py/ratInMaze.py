def RatInMaze(maze: list[list[int]]):
    n = len(maze[0])
    DIRECTIONS = [["D", +1, 0], ["L", 0, -1], ["R", 0, +1], ["U", -1, 0]]
    visited = [[0] * n for _ in range(len(maze))]
    result = []
    current_path = ""

    def solve(
        row: int,
        col: int,
        maze: list[list[int]],
        visited: list[list[int]],
        result: list[list[str]],
        n: int,
        current_path: str,
    ):
        if row == n - 1 and col == n - 1:
            result.append(current_path)
            return

        if maze[row][col] == 0 or maze[n - 1][n - 1] == 0:
            return

        visited[row][col] = 1

        for move, dr, dc in DIRECTIONS:
            next_r = row + dr
            next_c = col + dc
            if (
                0 <= next_r < n
                and 0 <= next_c < n
                and maze[next_r][next_c] == 1
                and visited[next_r][next_c] == 0
            ):
                solve(next_r, next_c, maze, visited, result, n, current_path + move)
        visited[row][col] = 0

    solve(0, 0, maze, visited, result, n, current_path)
    return result


print(RatInMaze(maze=[[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]))
