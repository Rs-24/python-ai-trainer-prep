

class Solution:
    def smallestNumber(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        return (1 << n.bit_length()) - 1


