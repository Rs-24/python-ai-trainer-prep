

class Solution:
    def countCompleteDayPairs(self, hours: list) -> int:
        # Time: O(n)
        # Space: O(1)
        d = {}
        t = 0
        for h in hours:
            h %= 24
            if (24 - h) % 24 in d:
                t += d[(24 - h) % 24]
            d[h] = d.get(h, 0) + 1
        return t


