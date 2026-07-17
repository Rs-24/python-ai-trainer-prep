

from bisect import bisect_left

class Solution:
    def findRadius(self, houses: list, heaters: list) -> int:
        # Time: O(n log n)
        # Space: O(1)
        heaters.sort()
        a = 0
        for h in houses:
            i = bisect_left(heaters, h)
            l = float("inf") if i == 0 else h - heaters[i - 1]
            r = float("inf") if i == len(heaters) else heaters[i] - h
            a = max(a, min(l, r))
        return a


