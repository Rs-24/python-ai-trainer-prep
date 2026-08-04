

import heapq

class Solution:
    def kClosest(self, points: list, k: int) -> list:
        # Time: O(n log n)
        # Space: O(n)
        h = []
        for x, y in points:
            heapq.heappush(h, (x * x + y * y, [x, y]))
        return [heapq.heappop(h)[1] for _ in range(k)]


