# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-cost-to-reach-every-position/description/

from typing import List

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        # Time: O(n), n = len(cost)
        # Aux space: O(1)
        out = []
        min_so_far = float("inf")
        for c in cost:
            min_so_far = min(min_so_far, c)
            out.append(min_so_far)
        return out


