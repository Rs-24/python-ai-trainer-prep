

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # Time: O(log n)
        # Space: O(1)
        s, p, x = 0, 1, n
        while x > 0:
            s += x % 10
            p *= x % 10
            x //= 10
        return n % (s + p) == 0


