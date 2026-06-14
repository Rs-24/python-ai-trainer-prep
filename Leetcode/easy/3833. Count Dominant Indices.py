

class Solution:
    def dominantIndices(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        c = 0
        r = sum(nums)
        for i in range(len(nums) - 1):
            r -= nums[i]
            c += nums[i] * (len(nums) - i - 1) > r
        return c


