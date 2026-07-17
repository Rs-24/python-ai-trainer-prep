

class Solution:
    def findMaxForm(self, strs: list, m: int, n: int) -> int:
        # Time: O(m * n)
        # Space: O(m * n)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            for i in range(m, s.count("0") - 1, -1):
                for j in range(n, s.count("1") - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - s.count("0")][j - s.count("1")] + 1)
        return dp[m][n]


