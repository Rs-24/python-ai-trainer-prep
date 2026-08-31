

class Solution:
    def shipWithinDays(self, weights: list, days: int) -> int:
        # Time: O(n log sum(weights))
        # Space: O(1)
        def c(x: int) -> bool:
            a, t = 1, 0
            for w in weights:
                t = w if t + w > x else t + w              
                a += t + w > x
            return a <= days
        l, r = max(weights), sum(weights)
        while l < r:
            m = (l + r) // 2
            if c(m):
                r = m
            else:
                l = m + 1
        return l


