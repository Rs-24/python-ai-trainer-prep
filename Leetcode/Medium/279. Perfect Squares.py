

class Solution:
    def numSquares(self, n: int) -> int:
        # Time: O(n^2)
        # Space: O(n)
        t = [x * x for x in range(1, int(n ** 0.5) + 1)]
        dp = [0] + [float("inf")] * n
        for x in range(1, n + 1):
            for p in t:
                if p > x:
                    break
                dp[x] = min(dp[x], dp[x - p] + 1)
        return dp[n]


