

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list]) -> int:
        # Time: O(n), n = len(points)
        # Space: O(1)
        ans = -1
        best = float("inf")
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                mh = abs(a - x) + abs(b - y)
                if mh < best:
                    ans = i
                    best = mh
        return ans


