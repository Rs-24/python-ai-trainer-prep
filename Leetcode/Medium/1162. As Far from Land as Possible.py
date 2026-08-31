

from collections import deque

class Solution:
    def maxDistance(self, grid: list) -> int:
        # Time: O(n^2)
        # Space: O(n^2)
        n = len(grid)
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
        if not q or len(q) == n * n:
            return -1
        a = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if 0 <= r + dr < n and 0 <= c + dc < n and grid[r + dr][c + dc] == 0:
                        grid[r + dr][c + dc] = 1
                        q.append((r + dr, c + dc))
            a += 1
        return a


