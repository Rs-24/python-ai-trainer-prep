

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        c = 0
        while n:
            n //= 5
            c += n
        return c


