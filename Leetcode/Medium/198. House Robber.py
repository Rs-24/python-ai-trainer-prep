

class Solution:
    def rob(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        a = b = 0
        for x in nums:
            t = max(b, a + x)
            b = a
            a = t
        return a


