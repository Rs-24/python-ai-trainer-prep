

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        x = (n >> 1) ^ n
        return x & (x + 1) == 0


