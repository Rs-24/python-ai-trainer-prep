

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time: O(log n)
        # Space: O(1)
        if n < 0:
            x = 1 / x
            n = -n
        r = 1
        while n:
            if n % 2 == 1:
                r *= x
            x *= x
            n //= 2
        return r


