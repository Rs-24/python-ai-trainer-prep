

class Solution:
    def findMinDifference(self, timePoints: list) -> int:
        # Time: O(n log n)
        # Space: O(n)
        if len(timePoints) > 1440:
            return 0
        def m(s: str) -> int:
            h, m = s.split(":")
            return int(h) * 60 + int(m)
        t = sorted(m(p) for p in timePoints)
        a = float("inf")
        for i in range(1, len(t)):
            a = min(a, t[i] - t[i - 1])
        a = min(a, 1440 - (t[-1] - t[0]))
        return a


