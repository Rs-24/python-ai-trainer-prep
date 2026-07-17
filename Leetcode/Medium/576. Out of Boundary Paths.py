

from functools import lru_cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Time: O(m * n * maxMove)
        # Space: O(m * n * maxMove)
        @lru_cache(None)
        def dp(r, c, t):
            if not (0 <= r < m and 0 <= c < n):
                return 1
            if t == 0:
                return 0
            a = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                a += dp(r + dr, c + dc, t - 1)
            return a % (10 ** 9 + 7)
        return dp(startRow, startColumn, maxMove)


