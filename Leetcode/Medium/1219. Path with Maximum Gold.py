

class Solution:
    def getMaximumGold(self, grid: list) -> int:
        # Time: O(m * n * (3 ^ (m * n)))
        # Space: O(m * n)
        m, n = len(grid), len(grid[0])
        def dfs(r: int, c: int) -> int:
            if not (0 <= r < m and 0 <= c < n and grid[r][c] != 0):
                return 0
            gold = grid[r][c]
            grid[r][c] = 0
            nxt = 0
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nxt = max(nxt, dfs(r + dr, c + dc))
            grid[r][c] = gold
            return gold + nxt
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    ans = max(ans, dfs(r, c))
        return ans


