

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        s = 0
        new = 0
        p = 0
        while n > 0:
            if n % 10 != 0:
                new += (n % 10) * (10 ** p)
                p += 1
            s += n % 10
            n //= 10
        return new * s


