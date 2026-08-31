

from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: list) -> int:
        # Time: O(n^2)
        # Space: O(n^2)
        dp = [defaultdict(int) for _ in range(len(nums))]
        a = 2
        for j in range(len(nums)):
            for i in range(j):
                dp[j][nums[j] - nums[i]] = dp[i].get(nums[j] - nums[i], 1) + 1
                a = max(a, dp[j][nums[j] - nums[i]])
        return a


