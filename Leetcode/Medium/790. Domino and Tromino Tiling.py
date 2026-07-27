

class Solution:
    def numTilings(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        dp = [1, 1, 2] + [0] * (n - 2)
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % (10**9 + 7)
        return dp[n]


