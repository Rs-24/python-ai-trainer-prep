

from functools import cache

class Solution:
    def stoneGameII(self, piles: list) -> int:
        # Time: O(n^3)
        # Space: O(n^2)
        s = [0] * (len(piles) + 1)
        for i in range(len(piles) - 1, -1, -1):
            s[i] = piles[i] + s[i + 1]
        @cache
        def dp(i, M) -> int:
            if 2 * M >= len(piles) - i:
                return s[i]
            a = 0
            for X in range(1, 2 * M + 1):
                a = max(a, s[i] - dp(i + X, max(M, X)))
            return a
        return dp(0, 1)


