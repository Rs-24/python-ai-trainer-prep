# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/description/

from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Time: O(n), n = len(position)
        # Space: O(1)
        even = odd = 0
        for p in position:
            if p % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)


