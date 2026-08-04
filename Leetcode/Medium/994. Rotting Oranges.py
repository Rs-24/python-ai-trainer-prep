

from collections import deque

class Solution:
    def orangesRotting(self, grid: list) -> int:
        # Time: O(m * n)
        # Space: O(m * n)
        m, n = len(grid), len(grid[0])
        q = deque()
        f = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                f += grid[r][c] == 1
        if f == 0:
            return 0
        a = 0
        while q and f > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= r + dr < m and 0 <= c + dc < n and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        f -= 1
                        q.append((r + dr, c + dc))
            a += 1
        return a if f == 0 else -1


