

class Solution:
    def numTrees(self, n: int) -> int:
        # Time: O(n^2)
        # Space: O(n)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for r in range(1, i + 1):
                dp[i] += dp[r - 1] * dp[i - r]
        return dp[n]


