

class Solution:
    def solve(self, board: list[list]) -> None:
        # Time: O(m * n)
        # Space: O(1)
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != "O":
                return
            board[r][c] = "#"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        for r in range(m):
            for c in [0, n - 1]:
                if board[r][c] == "O":
                    dfs(r, c)
        for c in range(n):
            for r in [0, m - 1]:
                if board[r][c] == "O":
                    dfs(r, c)
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"


