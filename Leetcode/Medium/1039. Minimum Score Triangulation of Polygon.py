

from functools import lru_cache

class Solution:
    def minScoreTriangulation(self, values: list) -> int:
        # Time: O(n^3)
        # Space: O(n^2)
        @lru_cache(None)
        def dp(i: int, k: int) -> int:
            if k - i < 2:
                return 0
            a = float("inf")
            for j in range(i + 1, k):
                a = min(a, dp(i, j) + dp(j, k) + values[i] * values[j] * values[k])
            return a
        return dp(0, len(values) - 1)


