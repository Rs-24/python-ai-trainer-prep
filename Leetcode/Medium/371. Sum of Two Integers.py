

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Time: O(1)
        # Space: O(1)
        t = 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & t, ((a & b) << 1) & t
        return a if a <= 0x7FFFFFFF else ~(a ^ t)


