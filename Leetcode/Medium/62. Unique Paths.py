

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time: O(m * n)
        # Space: O(n)
        dp = [1] * n
        for _ in range(m):
            for j in range(n):
                dp[j] += dp[j - 1]
        return dp[-1]


