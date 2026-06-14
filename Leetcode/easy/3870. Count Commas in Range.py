

class Solution:
    def countCommas(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        c = 0
        p = 1000
        while p <= n:
            c += n - p + 1
            p *= 1000
        return c


