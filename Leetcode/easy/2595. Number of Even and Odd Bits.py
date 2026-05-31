

class Solution:
    def evenOddBit(self, n: int) -> list:
        # Time: O(log n)
        # Space: O(1)
        e = o = i = 0
        while n > 0:
            if i % 2 == 0:
                e += n & 1
            else:
                o += n & 1
            i += 1
            n >>= 1
        return [e, o]


