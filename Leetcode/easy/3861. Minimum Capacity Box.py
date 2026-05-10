# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-capacity-box/description/

from typing import List

class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        # Time: O(n), n = len(capacity)
        # Space: O(1)
        best = -1
        for i, c in enumerate(capacity):
            if c >= itemSize:
                if best == -1 or c < capacity[best]:
                    best = i
        return best


