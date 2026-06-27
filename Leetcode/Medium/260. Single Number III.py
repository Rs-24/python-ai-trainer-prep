

class Solution:
    def singleNumber(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(1)
        t = 0
        for x in nums:
            t ^= x
        d = t & -t
        a = b = 0
        for x in nums:
            if x & d:
                a ^= x
            else:
                b ^= x
        return [a, b]


