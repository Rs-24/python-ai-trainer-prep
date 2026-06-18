

class Solution:
    def singleNumber(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        o = t = 0
        for x in nums:
            o = (o ^ x) & ~t
            t = (t ^ x) & ~o
        return o


