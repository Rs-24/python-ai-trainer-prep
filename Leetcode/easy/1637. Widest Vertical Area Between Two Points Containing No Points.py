

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list]) -> int:
        # Time: O(n log n), n = len(points)
        # Space: O(1)
        points.sort(key=lambda x: x[0])
        best = 0
        for i in range(1, len(points)):
            best = max(best, points[i][0] - points[i - 1][0])
        return best


