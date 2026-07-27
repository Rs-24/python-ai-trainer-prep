

class Solution:
    def minEatingSpeed(self, piles: list, h: int) -> int:
        # Time: O(n log n)
        # Space: O(1)
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            t = 0
            for p in piles:
                t += (p + m - 1) // m
            if t <= h:
                r = m
            else:
                l = m + 1
        return l


