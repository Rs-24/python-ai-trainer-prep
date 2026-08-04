

from collections import deque

class Solution:
    def shortestBridge(self, grid: list) -> int:
        # Time: O(n^2)
        # Space: O(n^2)
        n = len(grid)
        q = deque()
        s = set()
        def dfs(r: int, c: int) -> None:
            if (r < 0 or r >= n or c < 0 or c >= n or grid[r][c] == 0 or (r, c) in s):
                return
            s.add((r, c))
            q.append((r, c, 0))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    break
        while q:
            r, c, d = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= r + dr < n and 0 <= c + dc < n and (r + dr, c + dc) not in s:
                    if grid[r + dr][c + dc] == 1:
                        return d
                    s.add((r + dr, c + dc))
                    q.append((r + dr, c + dc, d + 1))
        return -1


