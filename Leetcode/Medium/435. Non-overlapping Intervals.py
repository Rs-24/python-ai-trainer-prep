

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list]) -> int:
        # Time: O(n log n)
        # Space: O(1)
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        c = 0
        p = float("-inf")
        for a, b in intervals:
            if a >= p:
                c += 1
                p = b
        return len(intervals) - c


