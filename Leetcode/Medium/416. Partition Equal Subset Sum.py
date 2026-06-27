

class Solution:
    def canPartition(self, nums: list) -> bool:
        # Time: O(n^2)
        # Space: O(n)
        if sum(nums) % 2 != 0:
            return False
        t = sum(nums) // 2
        dp = [True] + [False] * t
        for x in nums:
            for i in range(t, x - 1, -1):
                dp[i] = dp[i] or dp[i - x]
        return dp[t]


