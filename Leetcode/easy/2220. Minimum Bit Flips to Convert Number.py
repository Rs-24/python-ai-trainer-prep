

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        return (start ^ goal).bit_count()


