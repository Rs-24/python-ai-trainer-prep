

import heapq

class Solution:
    def pickGifts(self, gifts: list, k: int) -> int:
        # Time: O(n + k log n)
        # Space: O(n)
        h = [-g for g in gifts]
        heapq.heapify(h)
        for _ in range(k):
            x = -heapq.heappop(h)
            heapq.heappush(h, -int(x ** 0.5))
        return -sum(h)
    

