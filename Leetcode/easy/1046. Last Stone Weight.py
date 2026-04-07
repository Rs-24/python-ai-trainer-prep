# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/last-stone-weight/description/

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time: O(n log n)
        # Space: O(n)
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, -abs(a - b))
        return -stones[0] if stones else 0


