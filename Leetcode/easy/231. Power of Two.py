
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        return n > 0 and (n & (n - 1) == 0)


