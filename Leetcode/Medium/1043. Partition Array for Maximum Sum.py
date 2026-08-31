

class Solution:
    def maxSumAfterPartitioning(self, arr: list, k: int) -> int:
        # Time: O(n * k)
        # Space: O(n)
        dp = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            t = 0
            for l in range(1, min(k, i) + 1):
                t = max(t, arr[i - l])
                dp[i] = max(dp[i], dp[i - l] + t * l)
        return dp[len(arr)]


