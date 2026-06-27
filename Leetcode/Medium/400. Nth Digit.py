

class Solution:
    def findNthDigit(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        d, c, s = 1, 9, 1
        while n > d * c:
            n -= d * c
            d += 1
            c *= 10
            s *= 10
        x = s + (n - 1) // d
        return int(str(x)[(n - 1) % d])


