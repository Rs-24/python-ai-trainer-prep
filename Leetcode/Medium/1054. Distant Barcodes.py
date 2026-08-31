

from collections import Counter
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: list) -> list:
        # Time: O(n log n)
        # Space: O(n)
        c = Counter(barcodes)
        h = [(-f, x) for x, f in c.items()]
        heapq.heapify(h)
        a = []
        pf, px = 0, None
        while h:
            f, x = heapq.heappop(h)
            a.append(x)
            f += 1
            if pf < 0:
                heapq.heappush(h, (pf, px))
            pf, px = f, x
        return a


