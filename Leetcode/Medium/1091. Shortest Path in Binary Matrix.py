

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list) -> int:
        # Time: O(n^2)
        # Space: O(n^2)
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        q = deque([(0, 0, 1)])
        grid[0][0] = 1
        while q:
            r, c, d = q.popleft()
            if r == n - 1 and c == n - 1:
                return d
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                if 0 <= r + dr < n and 0 <= c + dc < n and grid[r + dr][c + dc] == 0:
                    grid[r + dr][c + dc] = 1
                    q.append((r + dr, c + dc, d + 1))
        return -1


