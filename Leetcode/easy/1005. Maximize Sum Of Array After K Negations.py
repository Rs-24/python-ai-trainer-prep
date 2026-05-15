

import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        # Time: O(n + k log n), n = len(nums)
        # Space: O(n)
        heapq.heapify(nums)
        for _ in range(k):
            num = heapq.heappop(nums)
            heapq.heappush(nums, -num)
        return sum(nums)


