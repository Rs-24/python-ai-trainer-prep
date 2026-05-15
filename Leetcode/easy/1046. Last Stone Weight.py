

import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Time: O(n log n), n = len(stones)
        # Space: O(n)
        s = [-stone for stone in stones]
        heapq.heapify(s)
        while len(s) > 1:
            a = heapq.heappop(s)
            b = heapq.heappop(s)
            if a != b:
                heapq.heappush(s, a - b)
        return -s[0] if s else 0


