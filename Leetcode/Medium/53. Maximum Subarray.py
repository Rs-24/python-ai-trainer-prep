

class Solution:
    def maxSubArray(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        c, m = 0, float("-inf")
        for n in nums:
            c = max(n, c + n)
            m = max(m, c)
        return m


