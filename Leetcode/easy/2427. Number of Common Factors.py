

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(1 for x in range(1, min(a, b) + 1) if a % x == b % x == 0)


