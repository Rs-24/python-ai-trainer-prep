

class Solution:
    def removeCoveredIntervals(self, intervals: list) -> int:
        # Time: O(n log n)
        # Space: O(1)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = max_right = 0
        for l, r in intervals:
            if r > max_right:
                ans += 1
                max_right = r
        return ans


