

class Solution:
    def findMinArrowShots(self, points: list[list]) -> int:
        # Time: O(n log n)
        # Space: O(1)
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        c, p = 0, float("-inf")
        for a, b in points:
            if a > p:
                c += 1
                p = b
        return c


