

class Solution:
    def longestSubsequence(self, arr: list, difference: int) -> int:
        # Time: O(n)
        # Space: O(n)
        dp = {}
        ans = 0
        for x in arr:
            dp[x] = dp.get(x - difference, 0) + 1
            ans = max(ans, dp[x])
        return ans


