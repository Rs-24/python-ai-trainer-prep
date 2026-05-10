

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Time: O(log n), n = max(x, y)
        # Space: O(log n)
        return (x ^ y).bit_count()


