

class Solution:
    def findTargetSumWays(self, nums: list, target: int) -> int:
        # Time: O(n^2)
        # Space: O(n)
        if abs(target) > sum(nums):
            return 0
        if (sum(nums) + target) % 2:
            return 0
        t = (sum(nums) + target) // 2
        dp = [1] + [0] * t
        for x in nums:
            for i in range(t, x - 1, -1):
                dp[i] += dp[i - x]
        return dp[t]


