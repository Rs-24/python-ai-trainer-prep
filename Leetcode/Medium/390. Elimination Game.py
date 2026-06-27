

class Solution:
    def lastRemaining(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        a = 1
        d = 1
        lr = True
        while n > 1:
            if lr or n % 2 == 1:
                a += d
            n //= 2
            d *= 2
            lr = not lr
        return a


