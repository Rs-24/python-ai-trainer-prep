# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/

from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Time: O(n + k log n), n = len(nums)
        # Space: O(n)
        h = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(h)
        for _ in range(k):
            num, idx = heapq.heappop(h)
            new = num * multiplier
            nums[idx] = new
            heapq.heappush(h, (new, idx))        
        return nums


