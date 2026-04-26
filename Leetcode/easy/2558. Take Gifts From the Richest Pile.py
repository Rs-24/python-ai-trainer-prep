# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/

from typing import List
from math import sqrt
import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Time: O(n + k log n), n = len(gifts)
        # Space: O(n)
        h = [-g for g in gifts]
        heapq.heapify(h)
        for _ in range(k):
            x = -heapq.heappop(h)
            heapq.heappush(h, -int(sqrt(x)))
        return -sum(h)


