

import heapq

class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        # Time: O(n log n)
        # Space: O(n)
        h = []
        for x in nums:
            heapq.heappush(h, x)
            if len(h) > k:
                heapq.heappop(h)
        return h[0]


