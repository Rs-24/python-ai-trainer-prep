

class Solution:
    def integerBreak(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if n == 2:
            return 1
        elif n == 3:
            return 2
        p = 1
        while n > 4:
            p *= 3
            n -= 3
        return p * n


