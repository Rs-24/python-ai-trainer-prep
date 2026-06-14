

import heapq

class Solution:
    def getFinalState(self, nums: list, k: int, multiplier: int) -> list:
        # Time: O(n + k log n)
        # Space: O(n)
        h = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(h)
        for _ in range(k):
            num, i = heapq.heappop(h)
            num *= multiplier
            nums[i] = num
            heapq.heappush(h, (num, i))
        return nums


