

class Solution:
    def numEnclaves(self, grid: list) -> int:
        # Time: O(m * n)
        # Space: O(m * n)
        m, n = len(grid), len(grid[0])
        def dfs(a: int, b: int) -> None:
            s = [(a, b)]
            grid[a][b] = 0
            while s:
                r, c = s.pop()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= r + dr < m and 0 <= c + dc < n and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 0
                        s.append((r + dr, c + dc))
        for r in range(m):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][n - 1] == 1:
                dfs(r, n - 1)
        for c in range(n):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[m - 1][c] == 1:
                dfs(m - 1, c)
        return sum(p for r in grid for p in r)


