

class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        # Time: O(log n)
        # Space: O(1)
        f = False
        while n > 0:
            if n & 3 == 3:
                if f:
                    return False
                f = True
            n >>= 1
        return f


