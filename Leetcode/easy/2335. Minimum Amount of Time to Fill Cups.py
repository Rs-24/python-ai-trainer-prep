# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description/

from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # Time: O(1)
        # Space: O(1)
        return max(max(amount), (sum(amount) + 1) // 2)


