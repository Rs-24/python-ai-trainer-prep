

class Solution:
    def countServers(self, grid: list) -> int:
        # Time: O(m * n)
        # Space: O(m + n)
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n
        for r in range(m):
            for c in range(n):
                rows[r] += grid[r][c] == 1
                cols[c] += grid[r][c] == 1
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans += (rows[r] > 1 or cols[c] > 1)
        return ans


