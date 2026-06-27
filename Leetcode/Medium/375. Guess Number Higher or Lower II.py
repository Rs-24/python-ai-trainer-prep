

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # Time: O(n^3)
        # Space: O(n^2)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for d in range(2, n + 1):
            for l in range(1, n - d + 2):
                r = l + d - 1
                dp[l][r] = float("inf")
                for x in range(l, r + 1):
                    dp[l][r] = min(dp[l][r], x + max(dp[l][x - 1], dp[x + 1][r]))
        return dp[1][n]


