

from collections import defaultdict

class Solution:
    def leastBricks(self, wall: list[list]) -> int:
        # Time: O(n^2)
        # Space: O(n)
        d = defaultdict(int)
        for p in wall:
            t = 0
            for i in range(len(p) - 1):
                t += wall[i]
                d[t] += 1
        t = max(d.values(), default=0)
        return len(wall) - t


