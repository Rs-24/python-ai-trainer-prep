

from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: list[list]) -> list:
        # Time: O(n log n)
        # Space: O(n)
        n = len(intervals)
        s = sorted((intervals[i][0], i) for i in range(n))
        t = [p for p, _ in s]
        o = [-1] * n
        for i, (a, b) in enumerate(intervals):
            p = bisect_left(t, b)
            if p < n:
                o[i] = s[p][1]
        return o


