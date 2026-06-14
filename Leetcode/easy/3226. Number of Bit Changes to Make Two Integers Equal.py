

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if (n & k) != k:
            return -1
        return (n ^ k).bit_count()


