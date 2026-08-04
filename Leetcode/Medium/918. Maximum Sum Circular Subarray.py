

class Solution:
    def maxSubarraySumCircular(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        cma = ma = cmi = mi = nums[0]
        for i in range(1, len(nums)):
            cma = max(nums[i], cma + nums[i])
            ma = max(ma, cma)
            cmi = min(nums[i], cmi + nums[i])
            mi = min(mi, cmi)
        if ma < 0:
            return ma
        return max(ma, sum(nums) - mi)


