

class Solution:
    def closedIsland(self, grid: list) -> int:
        # Time: O(m * n)
        # Space: O(1)
        def dfs(r: int, c: int) -> bool:
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return False
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1
            return dfs(r + 1, c) and dfs(r - 1, c) and dfs(r, c + 1) and dfs(r, c - 1)
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    ans += dfs(r, c)
        return ans


