

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return n if n % 2 == 0 else 2 * n


