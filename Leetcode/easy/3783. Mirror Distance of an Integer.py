

class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        r = 0
        x = n
        while x > 0:
            r = r * 10 + x % 10
            x //= 10
        return abs(n - r)


