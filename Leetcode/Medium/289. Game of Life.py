

class Solution:
    def gameOfLife(self, board: list[list]) -> None:
        # Time: O(n^2)
        # Space: O(1)
        m, n = len(board), len(board[0])
        d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for r in range(m):
            for c in range(n):
                t = 0
                for dr, dc in d:
                    t += (0 <= r + dr < m and 0 <= c + dc < n and board[r + dr][c + dc] in [1, 2])
                board[r][c] = 3 if board[r][c] == 0 and t == 3 else board[r][c]
                board[r][c] = 2 if board[r][c] == 1 and (t < 2 or t > 3) else board[r][c]
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                if board[r][c] == 3:
                    board[r][c] = 1


