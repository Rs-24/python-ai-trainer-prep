

class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        # Time: O(n), n = len(points)
        # Space: O(1)
        total = 0
        for i in range(1, len(points)):
            a, b = points[i - 1]
            c, d = points[i]
            total += max(abs(c - a), abs(d - b))
        return total


