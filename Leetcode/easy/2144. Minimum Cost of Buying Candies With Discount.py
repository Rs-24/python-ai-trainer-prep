# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/

from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Time; O(n log n), n = len(cost)
        # Space: O(n)
        total = 0
        cost.sort(reverse = True)
        for i, c in enumerate(cost):
            if (i + 1) % 3 != 0:
                total += c
        return total


