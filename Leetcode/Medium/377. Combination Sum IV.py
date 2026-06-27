

class Solution:
    def combinationSum4(self, nums: list, target: int) -> int:
        # Time: O(target * len(nums))
        # Space: O(target)
        dp = [1] + [0] * target
        for s in range(1, target + 1):
            for x in nums:
                if s >= x:
                    dp[s] += dp[s - x]
        return dp[target]


