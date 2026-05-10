

class Solution:
    def reverseBits(self, n: int) -> int:
        # Time: O(1)
        # Space: O(1)
        rev = 0
        for _ in range(32):
            rev = (rev << 1) | (n & 1)
            n >>= 1
        return rev


