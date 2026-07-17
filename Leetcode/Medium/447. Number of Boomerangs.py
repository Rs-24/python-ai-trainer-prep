

from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: list[list]) -> int:
        # Time: O(n^2)
        # Space: O(n)
        c = 0
        for i in range(len(points)):
            d = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                a = points[i][0] - points[j][0]
                b = points[i][1] - points[j][1]
                d[a * a + b * b] += 1
            for t in d.values():
                c += t * (t - 1)
        return c


