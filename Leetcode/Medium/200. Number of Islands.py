

class Solution:
    def numIslands(self, grid: list[list]) -> int:
        # Time: O(n^2)
        # Space: O(1)
        m, n = len(grid), len(grid[0])
        def dfs(r: int, c: int):
            if (r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        t = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    t += 1
                    dfs(r, c)
        return t


