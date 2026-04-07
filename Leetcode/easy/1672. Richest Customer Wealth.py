# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/richest-customer-wealth/description/

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Time: O(m * n), m = len(accounts), n = len(accounts[0])
        # Space: O(1)
        return max(sum(row) for row in accounts)


