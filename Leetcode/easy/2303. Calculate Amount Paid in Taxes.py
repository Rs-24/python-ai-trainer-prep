# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/calculate-amount-paid-in-taxes/description/

from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        # Time: O(n), n = len(brackets)
        # Space: O(1)
        total = 0
        prev_u = 0
        for u, p in brackets:
            if income <= prev_u:
                break
            total += min(u - prev_u, income - prev_u) * (p / 100)
            prev_u = u
        return total


