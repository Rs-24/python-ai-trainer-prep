

from collections import defaultdict
from math import hypot

class Solution:
    def minAreaFreeRect(self, points: list) -> float:
        # Time: O(n^2)
        # Space: O(n)
        n = len(points)
        p = defaultdict(list)
        for i in range(n):
            a, b = points[i]
            for j in range(i + 1, n):
                c, d = points[j]
                p[(a + c, b + d, (a - c) ** 2 + (b - d) ** 2)].append((i, j))
        t = float("inf")
        for e in p.values():
            for i in range(len(e)):
                for j in range(i + 1, len(e)):
                    a, b = e[i]
                    c, d = e[j]
                    x1, y1 = points[a]
                    x2, y2 = points[c]
                    x3, y3 = points[d]
                    f = hypot(x1 - x2, y1 - y2) * hypot(x1 - x3, y1 - y3)
                    if f > 0:
                        t = min(t, f)
        return 0 if t == float("inf") else t


        